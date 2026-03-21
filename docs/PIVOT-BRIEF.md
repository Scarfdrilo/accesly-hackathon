# 🚀 Accesly Pivot Brief

## Sprint Actual: Non-Custodial Wallets + Multichain Bridge EVM ↔ Stellar

---

## 📋 Resumen Ejecutivo

**Accesly** es infraestructura de wallets para Stellar que resuelve dos problemas fundamentales:

1. **Onboarding sin fricción** → Login con Google, sin seed phrases
2. **Liquidez cross-chain** → Bridge descentralizado EVM ↔ Stellar

### Este Sprint (Hackathon Stellar Growth Lab)

| Componente | Estado | Descripción |
|------------|--------|-------------|
| SDK Wallets | ✅ MVP | Google login → Stellar wallet |
| Non-Custodial | 🔄 En desarrollo | MPC + threshold signatures |
| Bridge EVM→Stellar | 🔄 Research | ZK/Optimistic bridge |

### Futuro (Q3-Q4 2026)

**Accesly for Agents** → SDK para que AI Agents tengan wallets propias y operen autónomamente en Stellar.

---

## 🎯 El Problema

### 1. Onboarding Complejo
- Los usuarios necesitan entender seed phrases, gas fees, trustlines
- Stellar tiene ~10M wallets vs Ethereum ~300M
- Barrera de entrada demasiado alta

### 2. Falta de Liquidez en Stellar
- La mayoría de liquidez está en EVM chains (Ethereum, Base, Polygon)
- **Ningún bridge descentralizado** conecta EVM ↔ Stellar
- Axelar existe pero es **centralizado** (75 validators permissioned)

### 3. Custodia Regulatoria
- SDKs actuales (incluyendo nuestra versión anterior) son **custodiales**
- Esto implica licencias, KYC/AML, regulaciones costosas
- Necesitamos arquitectura **non-custodial** para escalar

---

## 💡 La Solución: Accesly 2.0

### Capa 1: Wallets Non-Custodial

```
┌─────────────────────────────────────────┐
│  Usuario hace login con Google          │
│                                         │
│  ┌─────────────────────────────────────┐│
│  │  MPC Key Generation                 ││
│  │  - Share 1: Dispositivo usuario     ││
│  │  - Share 2: Servidor Accesly        ││
│  │  - Share 3: Recovery (encriptado)   ││
│  └─────────────────────────────────────┘│
│                                         │
│  Ninguna parte puede firmar SOLA        │
│  = Non-Custodial = Sin regulaciones     │
└─────────────────────────────────────────┘
```

**Stack Técnico:**
- OpenZeppelin Smart Accounts (Soroban)
- Fee Abstraction (usuarios pagan en USDC, no XLM)
- SEP-30 Recovery multi-región

### Capa 2: Bridge Descentralizado EVM ↔ Stellar

**Opción A: Optimistic Bridge (MVP - 2-3 meses)**
```
1. Usuario deposita USDC en Ethereum
2. Relayer (permissionless) propone bridge + pone bond
3. 1 hora dispute period
4. Si no hay disputa → Stellar mints USDC
5. Si hay fraude → relayer pierde bond
```

**Opción B: ZK Bridge (Roadmap - 6 meses)**
```
1. Usuario deposita USDC en Ethereum
2. Prover genera ZK proof (30-60 seg)
3. Proof verifica criptográficamente que TX existe
4. Stellar verifica proof y mints USDC
5. Zero validators, zero trust, pure math
```

---

## 🆚 Diferenciación vs Competencia

| Feature | Pollar | Axelar | **Accesly** |
|---------|--------|--------|-------------|
| Wallets frictionless | ✅ | ❌ | ✅ |
| Non-custodial | ✅ | N/A | ✅ (MPC) |
| Bridge EVM↔Stellar | ❌ | ✅ | ✅ |
| Descentralizado | N/A | ❌ (75 validators) | ✅ (ZK/Optimistic) |
| Fee Abstraction | ✅ | ❌ | ✅ |
| AI Agents Ready | ❌ | ❌ | 🔜 Roadmap |

---

## 📊 Tracción Actual

| Métrica | Valor |
|---------|-------|
| Wallets creadas | 88 |
| API Keys activas | 30 |
| Integraciones cerradas | 7 equipos |
| NPM Downloads | ~400 |

---

## 🛣️ Roadmap

### Q1 2026 (Ahora - Hackathon)
- [x] SDK de wallets MVP
- [x] 7 integraciones con equipos Stellar
- [ ] Arquitectura non-custodial definida
- [ ] Propuesta de bridge documentada

### Q2 2026 (Post-Hackathon)
- [ ] Implementar MPC non-custodial
- [ ] Optimistic Bridge MVP (testnet)
- [ ] Fee Abstraction con OpenZeppelin
- [ ] Aplicar a SCF Grant

### Q3 2026
- [ ] Bridge mainnet
- [ ] ZK verification para montos grandes
- [ ] Auditoría de seguridad

### Q4 2026
- [ ] **Accesly for Agents** 🤖
- [ ] SDK para AI Agents autónomos
- [ ] Wallets que los agentes controlan
- [ ] Integración con frameworks de agentes

---

## 🤖 Futuro: Accesly for Agents

**Visión:** Los AI Agents necesitarán wallets propias para operar autónomamente en blockchain.

**Casos de uso:**
- Agente de trading que ejecuta órdenes
- Agente de pagos que procesa facturas
- Agente de rewards que distribuye tokens
- Agente de treasury que maneja fondos

**Por qué Stellar:**
- Transacciones rápidas (~5 seg)
- Fees bajísimos (~$0.00001)
- USDC nativo
- Soroban smart contracts

**Por qué Accesly:**
- Ya tenemos el SDK de wallets
- Non-custodial = agentes tienen control real
- Bridge = agentes pueden operar cross-chain

---

## 💰 Modelo de Negocio

### Revenue Streams

| Stream | Pricing | Target |
|--------|---------|--------|
| Wallet SDK | Free tier + $49-199/mes | Devs |
| Bridge fees | 0.1% del volumen | Usuarios |
| Enterprise | Custom | Fintechs |
| Agent SDK | TBD | AI Companies |

### Go-to-Market

1. **Hackathon** → Cerrar integraciones con equipos Stellar
2. **SCF Grant** → Financiar desarrollo del bridge
3. **Enterprise** → Fintechs Latam (Vianey tiene conexiones)
4. **AI Market** → Cuando Agents explotan, estamos listos

---

## 👥 Equipo

| Rol | Persona | Responsabilidad |
|-----|---------|-----------------|
| Business Lead | Vianey | Partnerships, pitch, GTM |
| Tech Lead | Scarf | Arquitectura, código, integrations |
| Security Lead | Daniel | Infraestructura, contratos, ZK research |

---

## 📚 Documentación Relacionada

- [Idea ZK Bridge (Dani)](./idea-zk-dani.md)
- [Arquitectura](./architecture-diagram.md)
- [Estrategia Hackathon](./estrategia.md)
- [Competencia](./competencia.md)

---

## 🎯 Pitch de 30 Segundos

> "**Accesly** es el Privy de Stellar + el primer bridge descentralizado EVM↔Stellar.
>
> Login con Google, wallet non-custodial, trae tu liquidez de Ethereum en 1 minuto.
>
> 88 wallets, 7 integraciones, y un roadmap hacia AI Agents.
>
> Axelar usa 75 validators. Nosotros usamos matemáticas."

---

*Última actualización: Marzo 2026 - Hackathon Stellar Growth Lab*
