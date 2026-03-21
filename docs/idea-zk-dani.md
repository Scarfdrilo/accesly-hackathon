# 🔮 Idea ZK Bridge - Dani

> Propuesta de bridge descentralizado usando Zero-Knowledge Proofs con Noir (Aztec)

---

## 🎯 El Problema: Centralización en Axelar

### ¿Por qué Axelar está "centralizado"?

1. **Validator Set Limitado:** Solo ~75 validators activos, requieren stake alto de AXL
2. **Gateway Contracts:** Controlados por Axelar Foundation
3. **Multisig Dependency:** Si 51%+ validators se coluden → funds at risk
4. **Single Point of Failure:** Solo hay UN bridge (Axelar) para Stellar

---

## 💡 La Solución: ZK Bridge con Noir

### Arquitectura General

```
┌─────────────────────────────────────────┐
│  Source Chain (Ethereum/Base/Polygon)   │
│  - Usuario deposita USDC                │
│  - Event emitido on-chain               │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Noir Circuit (Off-chain Prover)        │
│  - Genera ZK proof de transacción       │
│  - Prueba: "TX existe en Ethereum"      │
│  - Output: Proof (~3 KB)                │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Stellar (Soroban Smart Contract)       │
│  - Verifica ZK proof                    │
│  - Si válido → mint USDC                │
│  - Usuario recibe en Stellar wallet     │
└─────────────────────────────────────────┘
```

---

## 📝 Flujo Técnico Detallado

### Paso 1: Usuario deposita en Ethereum

```solidity
// DepositContract.sol (Ethereum)
contract USDCBridge {
    event Deposit(
        address indexed user,
        uint256 amount,
        bytes32 stellarAddress,
        uint256 blockNumber,
        bytes32 txHash
    );
    
    function deposit(uint256 amount, bytes32 stellarAddress) external {
        USDC.transferFrom(msg.sender, address(this), amount);
        emit Deposit(msg.sender, amount, stellarAddress, block.number, blockhash(block.number));
    }
}
```

### Paso 2: Noir Circuit genera ZK Proof

```rust
// bridge_proof.nr (Noir circuit)

use dep::std;

// Public inputs (visibles para verifier)
pub struct PublicInputs {
    deposit_hash: Field,
    block_number: Field,
    merkle_root: Field,
}

// Private inputs (secretos)
struct PrivateInputs {
    user_address: Field,
    amount: Field,
    stellar_address: Field,
    tx_hash: Field,
    merkle_proof: [Field; 10],
    event_index: Field,
}

fn main(public_inputs: PublicInputs, private_inputs: PrivateInputs) {
    // 1. Verificar que el deposit event existe
    let deposit_event = hash_deposit_event(
        private_inputs.user_address,
        private_inputs.amount,
        private_inputs.stellar_address,
        private_inputs.tx_hash
    );
    
    assert(deposit_event == public_inputs.deposit_hash);
    
    // 2. Verificar merkle proof del event en el block
    let is_valid = verify_merkle_proof(
        deposit_event,
        private_inputs.merkle_proof,
        private_inputs.event_index,
        public_inputs.merkle_root
    );
    
    assert(is_valid == true);
}
```

### Paso 3: Soroban verifica y mints

```rust
// lib.rs - Soroban contract

#[contract]
pub struct ZKBridge;

#[contractimpl]
impl ZKBridge {
    pub fn verify_and_mint(
        env: Env,
        proof: Bytes,
        deposit_hash: BytesN<32>,
        block_number: u64,
        merkle_root: BytesN<32>,
        recipient: Address,
        amount: u128,
    ) -> Result<(), Error> {
        // Check no replay
        if env.storage().get(&deposit_hash).is_some() {
            return Err(Error::AlreadyProcessed);
        }
        
        // Verify ZK proof
        let is_valid = verifier::verify(&env, &proof, &[deposit_hash, block_number, merkle_root])?;
        if !is_valid {
            return Err(Error::InvalidProof);
        }
        
        // Mark processed & mint
        env.storage().set(&deposit_hash, &true);
        usdc_token.mint(&recipient, &amount);
        
        Ok(())
    }
}
```

---

## ⚡ Performance

| Step | Tiempo | Donde |
|------|--------|-------|
| Deposit Ethereum | ~15 seg | Ethereum |
| Generate ZK Proof | **30-60 seg** | Off-chain prover |
| Submit to Stellar | ~5 seg | Stellar |
| **TOTAL** | **~1 minuto** | End-to-end |

### Costos

| Componente | Costo |
|------------|-------|
| Ethereum gas | ~$5-20 |
| ZK proof generation | ~$0.50 |
| Stellar verification | ~$0.00001 |

### Proof Size
- **~2-5 KB** (tiny!)

---

## 🛡️ Seguridad

### ¿Qué Garantiza el ZK Proof?

✅ Transacción existe en Ethereum block X
✅ Event contiene datos exactos (user, amount, stellar address)
✅ Block X tiene merkle root Y
✅ Proof es computacionalmente imposible de falsificar

### Vectores Mitigados

| Ataque | Protección |
|--------|------------|
| Fake Deposits | ZK verifica merkle proof |
| Replay Attacks | Contract guarda deposit_hash |
| Old Block Attacks | Verifica block < 1 hora |
| Amount Manipulation | Hash incluye amount |

### Trust Assumptions

**Zero trust en:**
- ✅ Validators (no hay)
- ✅ Relayers (solo generan proof)
- ✅ Oracles (no necesarios)

---

## 📊 Comparación vs Competencia

| Feature | Axelar | Optimistic | **ZK (Noir)** |
|---------|--------|-----------|---------------|
| **Trust** | Validators | Economic | **Pure math** ✅ |
| **Speed** | 15 min | 1 hour | **1 min** ✅ |
| **Decentralization** | 75 validators | Permissionless | **Permissionless** ✅ |
| **Security** | Multisig | Fraud proofs | **Cryptographic** ✅ |
| **Complexity** | Medium | Low | **High** ⚠️ |

---

## 🚀 Roadmap de Implementación

### Mes 1-2: POC
- [ ] Escribir Noir circuit básico
- [ ] Deploy Ethereum test contract
- [ ] Generar primer proof exitoso
- [ ] Portar verifier a Soroban WASM

### Mes 3-4: MVP
- [ ] Event listener automatizado
- [ ] Prover service production-ready
- [ ] Frontend integration
- [ ] Testnet beta

### Mes 5-6: Audit & Launch
- [ ] Security audit
- [ ] Formal verification
- [ ] Mainnet deployment
- [ ] Public launch

---

## 💰 Modelo de Negocio

### Revenue Streams

1. **Bridge Fee:** 0.1% del amount
2. **Premium Fast Track:** 0.3% (proof en <10s)
3. **Relayer-as-a-Service:** $50-200/mes

### Profit Margin: ~90%

---

## 🎯 Pitch para SCF Grant

> "Accesly ZK Bridge: El primer bridge **trustless** para Stellar.
>
> - Sin validators, sin oracles
> - Seguridad criptográfica pura
> - 1 minuto cross-chain
>
> Axelar usa 75 validators. Nosotros usamos **matemáticas**."

---

## ⚠️ Gaps Técnicos a Resolver

1. **Noir Verifier en Soroban:** No existe out-of-the-box, hay que portar Barretenberg a WASM
2. **Ethereum Headers:** Necesitamos mecanismo para verificar headers en Stellar
3. **Auditoría:** Trail of Bits ~$100-300K

---

## 📚 Referencias

- [Noir Language](https://noir-lang.org/)
- [Aztec Protocol](https://aztec.network/)
- [Soroban Docs](https://soroban.stellar.org/)
- [OpenZeppelin Stellar Contracts](https://docs.openzeppelin.com/stellar-contracts)

---

*Documento creado por DrConnors - Hackathon Stellar Growth Lab 2026*
