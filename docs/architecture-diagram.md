# Accesly: 3-Fragment Distributed Key Architecture

> **Non-Custodial Wallet:** Fragment 1 (Device) + Fragment 2 (Server) + Fragment 3 (Email-Encrypted)

---

## 🔐 NON-CUSTODIAL

**User controls Fragment 1 (device). Accesly CANNOT access funds without user device.**

### XOR Splitting

```
Master key split into 3 fragments. Any 2 fragments can reconstruct the key.

• Normal Use:  Fragment 1 (device) + Fragment 2 (server)
• Recovery:    Fragment 2 (server) + Fragment 3 (email OTP required)
```

---

## Fragment 1: DEVICE - Hardware Protected

```
┌─────────────────────────────────────────────────────────────────┐
│  📱 User Device (Browser / Mobile App)                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🔐 WebAuthn / FIDO2                                      │   │
│  │                                                         │   │
│  │ Biometric Authentication                                │   │
│  │ FaceID / TouchID / YubiKey                              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🔒 Hardware Security (TPM / Secure Enclave)              │   │
│  │                                                         │   │
│  │ Stores Fragment 1                                       │   │
│  │ Encrypted with AES-256                                  │   │
│  │                                                         │   │
│  │ Access: Biometric only                                  │   │
│  │ Cannot be exported                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 🔑 FRAGMENT 1/3

| Property | Value |
|----------|-------|
| **Location** | Device TPM/Secure Enclave |
| **Encryption** | AES-256-GCM |
| **Access** | Biometric authentication |

**Properties:**
- ❌ NEVER leaves device
- ❌ NEVER sent to server
- 🔒 Hardware-bound
- 🚫 Cannot be extracted

**Usage:**
- Unlocked with biometric
- Combined with Fragment 2
- Used for transaction signing

**Security:**
- ⚠️ Fragment 1 alone is USELESS
- ⚠️ Requires Fragment 2 to work
- ⚠️ If device lost: Use recovery flow

### 💳 Wallet Interface

```
Address: CABC...XYZ

Balances:
• 1,234.50 USDC
• 567.89 EURC
• 25.00 XLM

Actions:
✓ Send / Receive
✓ Sign Transactions
✓ Bridge from Ethereum
✓ Connect to dApps
```

---

## Fragment 2: SERVER - Always Available

```
┌─────────────────────────────────────────────────────────────────┐
│  🌐 API Gateway                                                 │
│                                                                 │
│  Endpoint: GET /api/fragment2                                   │
│  Authentication: JWT Token                                      │
│  Rate Limit: 100 requests/min                                   │
│                                                                 │
│  ┌───────────────────────┐    ┌───────────────────────────┐    │
│  │ 💾 DynamoDB           │    │ 🔐 AWS KMS                │    │
│  │                       │    │                           │    │
│  │ Table: user_fragments │    │ Customer Master Key       │    │
│  │ Region: us-east-1     │    │ Type: AES-256             │    │
│  │                       │    │                           │    │
│  │ Data:                 │    │ Operations:               │    │
│  │ • Fragment 2 (enc)    │    │ • Encrypt Fragment 2      │    │
│  │ • User ID mapping     │    │ • Decrypt on request      │    │
│  │ • Timestamps          │    │                           │    │
│  │                       │    │ Security:                 │    │
│  │ Features:             │    │ • CloudHSM backed         │    │
│  │ • Multi-region repl.  │    │ • Annual rotation         │    │
│  │ • Point-in-time rec.  │    │ • Audit logs              │    │
│  │ • Encrypted at rest   │    │                           │    │
│  └───────────────────────┘    └───────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### 🔑 FRAGMENT 2/3

| Property | Value |
|----------|-------|
| **Location** | DynamoDB (AWS) |
| **Encryption** | AWS KMS (AES-256) |
| **Regions** | us-east-1, eu-west-1, ap-southeast-1 |

**Properties:**
- ✅ Always available
- 🌍 Multi-region replication
- 🔒 Encrypted at rest
- 📡 Sent via HTTPS to client

**Usage:**
1. Client requests with JWT
2. Server validates token
3. KMS decrypts fragment
4. Returns to client securely

**Security:**
- ⚠️ Fragment 2 alone is USELESS
- ⚠️ Requires Fragment 1 to work
- ⚠️ All access logged (CloudTrail)

### 🌍 Multi-Region Setup

| Region | Location | Purpose |
|--------|----------|---------|
| **Primary** | us-east-1 | Main |
| **Replica** | eu-west-1 | Europe |
| **Replica** | ap-southeast-1 | Asia |

**Benefits:**
- Low latency worldwide
- High availability
- Disaster recovery
- Replication: under 1 second

---

## Fragment 3: EMAIL-ENCRYPTED - Recovery Only

### 🔑 FRAGMENT 3/3

| Property | Value |
|----------|-------|
| **Location** | DynamoDB (eu-west-1) |
| **Encryption** | PBKDF2 + AES-256-GCM |
| **Key Derivation** | User email + salt |

**Properties:**
- 📧 Email-based encryption
- 🚫 No KMS needed
- 🔐 OTP required to access
- 🆘 Only for recovery

**Generation:**
1. Derives key from email
2. Encrypts Fragment 3
3. Stores encrypted in DB

**Access Restrictions:**
- ⚠️ Requires email OTP verification
- ⏰ 5-minute expiry
- 🔢 3 attempts maximum
- ⏳ 1-hour cooldown after failures

**Usage:**
- **ONLY when device is lost**
- Normal: Fragment 1 + Fragment 2
- Recovery: Fragment 2 + Fragment 3

### 📧 Email OTP System

| Setting | Value |
|---------|-------|
| **Service** | AWS SES |
| **Code** | 6-digit number |
| **Delivery** | Under 5 seconds |
| **Expiry** | 5 minutes |
| **Storage** | Redis Cache |

**Security:**
- Rate limiting
- Attempt tracking
- Cooldown enforcement
- All attempts logged

### 🔐 PBKDF2 Security

**Purpose:** Slow key derivation - Makes brute-force attacks infeasible

**Configuration:**
- 100,000 iterations
- SHA-256 hash
- 32-byte salt (random)

**Why It Works:**
Even if database is leaked, Fragment 3 cannot be decrypted without knowing the email.

---

## User Flows

### 🎯 NORMAL USE (Fragment 1 + Fragment 2)

```
1. User wants to send 100 USDC
2. Biometric prompt (FaceID/TouchID)
3. User authenticates
4. Device unlocks Fragment 1
5. App fetches Fragment 2 from server
6. Combines: F1 XOR F2 = Master Key
7. Signs transaction with master key
8. Submits via OpenZeppelin Relayer
9. Clears all keys from memory
10. Transaction confirmed ✅

Time: ~5 seconds
```

**Security:**
- Fragment 1 never leaves device
- Master key exists in memory briefly
- All keys cleared after use
- No persistence of sensitive data

### 🔄 RECOVERY (Fragment 2 + Fragment 3)

```
Device Lost - Fragment 1 Gone

1. User goes to recovery page
2. Enters email address
3. Receives 6-digit OTP code
4. Enters OTP within 5 minutes
5. OTP validated by backend
6. Fragment 3 decrypted with email
7. Fetches Fragment 2 from server
8. Combines: F2 XOR F3 = Master Key
9. Master key restored on new device
10. Creates NEW Fragment 1 on new device
11. Updates Fragment 3 in database
12. Old Fragment 1 invalidated
13. User regains access ✅

Time: ~1 minute
```

**Security:**
- Requires email ownership (OTP)
- Old device access revoked
- New Fragment 1 for new device

### 🔢 XOR FRAGMENT SYSTEM

**How It Works:**

**Wallet Creation:**
1. Generate master key (random)
2. Generate Fragment 1 (random)
3. Generate Fragment 2 (random)
4. Calculate: `F3 = Master XOR F1 XOR F2`

**Normal Use:**
- Combine: `F1 XOR F2 = Master Key`

**Recovery:**
- Combine: `F2 XOR F3 = Master Key`

**Properties:**
- ✓ Any 2 fragments reconstruct key
- ✓ Simple XOR operation (fast)
- ✓ Cryptographically secure
- ✓ No complex math needed

**Security:**
- ⚠️ Each fragment alone = USELESS
- ⚠️ Need exactly 2 fragments minimum
- ⚠️ All 3 fragments also work

---

## ⚠️ Attack Resistance

| Scenario | Attack Vector | Result |
|----------|---------------|--------|
| **Steal Database** | Fragment 2: KMS encrypted, Fragment 3: PBKDF2 encrypted | ✅ SAFE |
| **Steal Device** | Fragment 1: Requires biometric | ✅ SAFE |
| **Compromise Server** | Fragment 2 alone is useless, Still needs Fragment 1 (device) | ✅ SAFE |
| **Intercept Email** | OTP expires in 5 minutes, Still needs Fragment 2 | ✅ SAFE |
| **Insider Attack** | Accesly cannot access Fragment 1, User controls device | ✅ NON-CUSTODIAL |

---

## Stellar Blockchain Integration

### 📜 Stellar Smart Contract

| Property | Value |
|----------|-------|
| **Platform** | Soroban |
| **Address** | CABC...XYZ |
| **Owner** | Master public key (derived from master key) |

**Features:**
- Authentication verification
- Owner updates
- Multi-sig capable
- Nonce tracking

### 💰 USDC + EURC Trustlines

Auto-created on wallet setup.

| Token | Issuer | Example Balance |
|-------|--------|-----------------|
| USDC | Circle | 1,234.50 |
| EURC | Circle | 567.89 |

Native Stellar stablecoins - no wrapping needed.

### 💎 Native XLM

```
Balance: 25.00 XLM

Purpose:
• Base reserve (2 XLM minimum)
• Gas fees (paid by relayer)

User Experience:
User never needs to buy XLM
All gas paid by OpenZeppelin Relayer
```

### 🚀 OpenZeppelin Relayer

**Gasless Transactions:**
- User pays: 0.1% in USDC
- Relayer pays: XLM gas

**Example (Send 100 USDC):**
- User total: 100.1 USDC
- Recipient gets: 100 USDC
- Relayer fee: 0.1 USDC
- Gas cost: $0.00001 XLM

**No XLM needed by user!**

### 🌐 Stellar Network

| Metric | Value |
|--------|-------|
| **Finality** | 5 seconds |
| **TPS** | ~3,000 |
| **Cost** | $0.00001 per transaction |

**Features:**
- Native USDC/EURC
- Soroban smart contracts
- Horizon API
- Soroban RPC

### 🎮 dApp Integration

Compatible with:
- Soroswap (DEX)
- Blend (Lending)
- Aqua (Liquidity)
- Any Stellar dApp

Wallet Kit: Seamless connection to entire Stellar ecosystem.

---

## ZK Bridge - Ethereum ↔ Stellar (Trustless Cross-Chain)

### ⟁ Ethereum Side

**Bridge Deposit Contract**

| Action | Details |
|--------|---------|
| **User Actions** | Deposit USDC, Specify Stellar recipient, Pay gas (~$10-15) |
| **Event Emitted** | Deposit details, Amount, Recipient address, Transaction hash |
| **Time** | ~15 seconds |
| **Security** | Ethereum L1 |

### 👂 Event Listener

Monitors Ethereum for:
- Deposit events
- Block confirmations
- Merkle tree updates

**Triggers:** Proof generation when deposit is confirmed
**Latency:** Real-time

### 🔐 Noir ZK Prover

**Technology:** Aztec Noir

**Generates Zero-Knowledge Proof:**
- Proves deposit occurred
- Proves amount is correct
- Proves Merkle inclusion
- Does NOT reveal transaction details

| Metric | Value |
|--------|-------|
| **Proof Size** | ~3 KB |
| **Generation Time** | 30-60 seconds |
| **Compute Cost** | ~$0.50 |

**Why ZK:**
- Privacy-preserving
- Trustless verification
- No reliance on validators
- Pure cryptography

### 📦 Proof Components

**Public Inputs:**
- Deposit hash
- Block number
- Merkle root

**Private Inputs (hidden):**
- User address
- Amount
- Stellar recipient
- Merkle proof path

**Output:** ZK Proof (verifiable on Stellar)

### ✨ Stellar Bridge Contract

**Platform:** Soroban

**Verifies ZK Proof:**
1. Validates proof cryptographically
2. Checks block age (under 1 hour)
3. Prevents double-spending
4. Marks deposit as processed

**On Success:**
- Mints USDC to recipient
- Emits confirmation event
- Updates processed deposits

| Metric | Value |
|--------|-------|
| **Verification Time** | ~5 milliseconds |
| **Gas Cost** | ~0.00001 XLM |

**Security:** Zero-trust - pure math verification

### Bridge Flow

```
Ethereum ──[Deposit Event]──► Noir ZK Prover ──[ZK Proof ~3KB]──► Stellar Bridge Contract
```

### ✅ ZK Bridge Benefits

**Trustless:**
- No validators needed
- No centralized control
- Pure cryptography

**Security:**
- Mathematically proven
- Cannot be compromised
- No single point of failure

**Performance:**
- Total time: 1-2 minutes
- Proof size: ~3 KB
- Verification: ~5ms

**Cost:**
- Ethereum deposit: $10-15
- Proof generation: $0.50
- Stellar verification: $0.00001

**Privacy:**
- ZK proof hides details
- Only proves validity

### ⚔️ vs Centralized Bridges

| Feature | Axelar/Wormhole | Accesly ZK Bridge |
|---------|-----------------|-------------------|
| Validators | ~75 validators (centralized) | Zero validators needed |
| Control | Foundation controls contracts | Trustless (pure math) |
| Failure | Single point of failure | No central authority |
| Trust | Trust required | Cryptographically secure |

### 📊 Example Bridge Flow

```
User wants to bridge 1,000 USDC from Ethereum to Stellar:

Step 1: Deposit on Ethereum (~15 seconds, ~$12 gas)
Step 2: Event Listener detects deposit (real-time)
Step 3: Noir generates ZK proof (30-60 seconds, ~$0.50)
Step 4: Submit proof to Stellar Bridge Contract
Step 5: Contract verifies proof (~5ms)
Step 6: Mints 1,000 USDC to Stellar wallet
Step 7: User receives USDC on Stellar ✅

Total Time: ~1-2 minutes
Total Cost: ~$12.50
Security: Trustless (zero-knowledge cryptography)
```

---

## 📊 Infrastructure

**AWS Services:**
- DynamoDB (multi-region)
- KMS (encryption)
- SES (email)
- CloudWatch (monitoring)
- CloudTrail (audit)
- Lambda (compute)
- API Gateway (endpoints)

---

## 🔒 Security Architecture Summary

- 3-fragment distributed key
- Fragment 1: Device TPM (biometric)
- Fragment 2: AWS KMS encrypted
- Fragment 3: Email encrypted (PBKDF2)
- OTP recovery (5 min expiry)
- Multi-region redundancy
- CloudTrail audit logs
- Rate limiting
- Non-custodial design

---

## ✅ Key Innovations

| Innovation | Description |
|------------|-------------|
| **Non-Custodial** | User controls Fragment 1 in device hardware. Accesly cannot access funds without user device. |
| **No Seed Phrases** | Hardware-protected fragments instead of 12/24-word phrases that can be lost or stolen. |
| **Biometric Security** | Fragment 1 unlocked with FaceID/TouchID, stored in TPM/Secure Enclave. |
| **Email Recovery** | Lost device? Recover using email OTP + Fragment 2 + Fragment 3. |
| **Gasless UX** | OpenZeppelin Relayer pays XLM gas fees, user pays 0.1% in USDC. |
| **Native Stablecoins** | USDC/EURC trustlines auto-created, no wrapping needed. |
| **Multi-Region** | Fragment 2 replicated across 3 AWS regions for high availability. |
| **XOR Splitting** | Simple, fast, cryptographically secure. Any 2 fragments reconstruct master key. |
| **Attack Resistant** | Database leak, device theft, server compromise, email interception - all scenarios protected. |
| **Stellar Native** | 5-second finality, $0.00001 transactions, Soroban smart contracts. |
| **ZK Bridge** | Trustless Ethereum to Stellar bridge using Noir zero-knowledge proofs. No validators, pure cryptography. |
| **Multichain Liquidity** | Bridge assets from Ethereum, access Stellar DeFi, all in one wallet. |

---

## ⚠️ Consideraciones Pendientes

### 🔄 Problema de Doble KYC

**Issue:** Riesgo de requerir doble autenticación KYC:
1. **Offramp** - KYC para convertir crypto → fiat
2. **CETES (Etherfuse)** - KYC separado para inversión en bonos mexicanos

**Impacto:** Mala UX, fricción para el usuario, posible abandono.

**A resolver:**
- [ ] Investigar si Etherfuse acepta KYC delegado
- [ ] Evaluar proveedores de offramp que compartan KYC con Etherfuse
- [ ] Considerar KYC unificado (un solo proceso, múltiples servicios)
- [ ] Revisar requisitos regulatorios de cada servicio

**Prioridad:** Alta - Afecta directamente la experiencia del usuario.
