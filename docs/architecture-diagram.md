# Accesly - Diagrama de Arquitectura

> **Estado:** Arquitectura objetivo. Actualmente solo tenemos KMS para cifrar llaves.
> 
> **Pendientes:** Integración USDC, EURC, y Trustlines.

---

## 📊 Vista General

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ACCESLY COMPLETE ARCHITECTURE                            │
│         SDK Distribution + AWS Infrastructure + Stellar Integration         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1: Developer Experience & SDK Distribution

### Developer's Application

```
┌────────────────────────────────────────────────────────────────┐
│  DEVELOPER'S APPLICATION                                       │
│                                                                │
│  👨‍💻 Developer  ──────►  npm install @accesly/sdk               │
│                                                                │
│  // Developer's App Code                                       │
│  import { Accesly } from '@accesly/sdk';                       │
│                                                                │
│  const accesly = new Accesly({                                 │
│    apiKey: 'sk_live_abc123'                                    │
│  });                                                           │
│                                                                │
│  const wallet = await accesly.createWallet();                  │
└────────────────────────────────────────────────────────────────┘
```

### NPM Registry & GitHub

| Componente | URL | Detalles |
|------------|-----|----------|
| 📦 NPM Registry | npmjs.com/package/accesly | Version: 1.0.3, Downloads: 380/week |
| 📂 GitHub | github.com/accesly/sdk | ⭐ Stars: 245, Open Source |

### Developer Portal

```
┌────────────────────────────────────────────────────────────────┐
│  DEVELOPER PORTAL                                              │
│                                                                │
│  🌐 portal.accesly.com (S3 + CloudFront)                       │
│                                                                │
│  Dashboard Features:                                           │
│  ✓ Sign Up / Login                                             │
│  ✓ Generate API Keys                                           │
│  ✓ View Usage Metrics                                          │
│  ✓ Billing Dashboard                                           │
│  ✓ Documentation                                               │
│  ✓ Code Examples                                               │
│                                                                │
│  Your API Key: sk_live_abc123xyz...                            │
└────────────────────────────────────────────────────────────────┘
```

---

## Section 2: Public API Gateway (api.accesly.com)

### REST Endpoints

```
POST /v1/wallets
POST /v1/auth/sep10/challenge
POST /v1/auth/sep10/verify
POST /v1/recovery/start
POST /v1/recovery/verify
POST /v1/transactions/sign
GET  /v1/wallets/:address
GET  /v1/balances/:address
```

### API Flow

```
┌──────────────┐    ┌─────────────────┐    ┌──────────────┐    ┌──────────────┐
│ API Gateway  │───►│ Lambda          │───►│ Rate Limiter │───►│ Usage        │
│ api.accesly  │    │ Authorizer      │    │ 100 req/min  │    │ Tracker      │
│ .com         │    │ (API Key Valid) │    │ (Free Tier)  │    │ DynamoDB     │
└──────────────┘    └─────────────────┘    └──────────────┘    └──────────────┘
       │
       │            ┌─────────────────┐    ┌──────────────┐
       └───────────►│ AWS WAF         │───►│ CloudWatch   │
                    │ • SQL Injection │    │ Logs         │
                    │ • XSS Protection│    └──────────────┘
                    │ • Bot Detection │
                    └─────────────────┘
```

### 💰 Pricing Tiers

| Tier | Wallets/mes | Precio |
|------|-------------|--------|
| Free | 1K | $0 |
| Pro | 10K | $99/mes |
| Enterprise | Custom | Contactar |

---

## Section 3: Authentication (SEP-10 + Google OAuth)

```
┌─────────────────────────────────────────────────────────────────┐
│  AUTHENTICATION LAYER                                           │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │ Amazon       │◄──►│ Google OAuth │    │ SEP-10 Handler   │  │
│  │ Cognito      │    │ 2.0 Identity │    │ Challenge-       │  │
│  │ User Pools   │    │ Provider     │    │ Response         │  │
│  └──────────────┘    └──────────────┘    └────────┬─────────┘  │
│         │                  │                       │            │
│         │      Federated   │                       ▼            │
│         └──────────────────┘              ┌──────────────────┐  │
│                                           │ JWT Generator    │  │
│                                           │ Session Tokens   │  │
│                                           └──────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Section 4: Workflow Orchestration

```
┌─────────────────────────────────────────────────────────────────┐
│  WORKFLOW ORCHESTRATION                                         │
│                                                                 │
│  ┌──────────────────┐    ┌────────────────┐    ┌────────────┐  │
│  │ Step Functions   │───►│ Workflows:     │───►│ EventBridge│  │
│  │ State Machine    │    │ 1. Create      │    │ Event Bus  │  │
│  │                  │    │    Wallet      │    └─────┬──────┘  │
│  │                  │    │ 2. SEP-30      │          │         │
│  │                  │    │    Recovery    │          ▼         │
│  │                  │    │ 3. Sign TX     │    ┌────────────┐  │
│  │                  │    │ 4. Update      │    │ SQS        │  │
│  │                  │    │    Owner       │    │ Async Queue│  │
│  └──────────────────┘    └────────────────┘    └────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Section 5: Business Logic (Lambda Functions)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAMBDA FUNCTIONS                                                           │
│                                                                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ Key     │ │ XDR     │ │ SEP-10  │ │ SEP-30  │ │ Stellar │ │Contract │  │
│  │ Manage- │ │ Signing │ │ Handler │ │ Recovery│ │ Handler │ │ Deployer│  │
│  │ ment    │ │         │ │         │ │         │ │         │ │         │  │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘  │
│                                                                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐             │
│  │ Wallet  │ │ Balance │ │ Email   │ │ Webhook │ │ Analytics│             │
│  │ Query   │ │ Checker │ │ Sender  │ │ Notifier│ │ Aggregat.│             │
│  │         │ │         │ │ (SES)   │ │         │ │          │             │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └──────────┘             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Section 6: Data & Key Management (Multi-Region para SEP-30)

### AWS KMS (Multi-Region) - SEP-30: 2-of-3 Threshold

```
┌─────────────────────────────────────────────────────────────────┐
│  AWS KMS (Multi-Region)                                         │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ 🇺🇸 KMS          │  │ 🇪🇺 KMS          │  │ 🇸🇬 KMS          │ │
│  │ us-east-1       │  │ eu-west-1       │  │ ap-southeast-1  │ │
│  │ Recovery Key 1  │  │ Recovery Key 2  │  │ Recovery Key 3  │ │
│  │ Weight: 10      │  │ Weight: 10      │  │ Weight: 10      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│              ⚡ SEP-30: 2-of-3 Threshold Recovery               │
└─────────────────────────────────────────────────────────────────┘
```

### DynamoDB Global Tables

| Tabla | Descripción |
|-------|-------------|
| `users` | userId, address |
| `api_keys` | keyId, limits |
| `usage_metrics` | logs |
| `recovery_state` | SEP-30 state |
| `transactions` | history |

> **Replicación:** 3 regiones

### Servicios Adicionales

```
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ S3         │ │ Secrets    │ │ Parameter  │ │ ElastiCache│
│ Backups    │ │ Manager    │ │ Store      │ │ Redis      │
└────────────┘ └────────────┘ └────────────┘ └────────────┘

┌────────────┐ ┌────────────┐ ┌────────────┐
│ Timestream │ │ SNS        │ │ SES        │
│ Time Series│ │ Notificati.│ │ Email (OTP)│
└────────────┘ └────────────┘ └────────────┘
```

---

## Section 7: Stellar Blockchain Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STELLAR BLOCKCHAIN INTEGRATION                                             │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  ┌────────────┐  │
│  │ Horizon API  │  │ Soroban RPC  │  │ Accesly Contract │  │ Stellar    │  │
│  │ REST         │  │ Smart        │  │ (Soroban/Rust)   │  │ Network    │  │
│  │ Interface    │  │ Contracts    │  │                  │  │            │  │
│  │              │  │              │  │ Functions:       │  │ Testnet:   │  │
│  │ • Accounts   │  │ • Invoke     │  │ • init()         │  │ horizon-   │  │
│  │ • Transact.  │  │   Contract   │  │ • __check_auth() │  │ testnet.   │  │
│  │ • Operations │  │ • Deploy     │  │ • update_owner() │  │ stellar.org│  │
│  │ • Effects    │  │   Contract   │  │ • get_nonce()    │  │            │  │
│  │              │  │ • Query      │  │                  │  │ Mainnet:   │  │
│  │              │  │   State      │  │                  │  │ horizon.   │  │
│  │              │  │ • Simulate   │  │                  │  │ stellar.org│  │
│  │              │  │   TX         │  │                  │  │            │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  └────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 🔍 Stellar Expert - stellarexpert.io - Block Explorer               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Section 8: Monitoring, Logging & Observability

```
┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌──────────────┐
│ CloudWatch     │  │ X-Ray          │  │ GuardDuty      │  │ Alarms       │
│ Logs + Metrics │  │ Tracing        │  │ Threat         │  │ Automated    │
│                │  │                │  │ Detection      │  │ Alerts       │
└────────────────┘  └────────────────┘  └────────────────┘  └──────────────┘
```

---

## 🔄 Complete Flow Example: Create Wallet

```
Step 1: Developer code
        const wallet = await accesly.createWallet();

Step 2: SDK
        POST https://api.accesly.com/v1/wallets (with API key)

Step 3: API Gateway
        Validates API key, rate limits, logs usage

Step 4: Cognito
        Authenticates user with Google OAuth

Step 5: Step Functions - Orchestrates workflow:
        • Lambda: Generate keypair (KMS secp256k1)
        • Lambda: Deploy Soroban contract on Stellar
        • Lambda: Store recovery keys in 3 KMS regions
                  (us-east-1, eu-west-1, ap-southeast-1)
        • Lambda: Save metadata in DynamoDB

Step 6: Stellar Network
        Smart contract deployed, address generated (GABC123...)

Step 7: Response
        { address: 'GABC123...', status: 'created', recovery_servers: 3 }

Step 8: SDK returns wallet object to developer's app

Step 9: Developer displays wallet address in UI
        User sees their new wallet!
```

---

## 💡 Key Differentiators vs Ethereum AA

| Feature | Accesly (Stellar) | Ethereum AA |
|---------|-------------------|-------------|
| Bundler | ❌ No necesario (Stellar no tiene mempool) | ✅ Requerido |
| Gas Manager | ❌ No necesario (fees fijos ~$0.00001) | ✅ Requerido |
| Auth Standard | SEP-10 + SEP-30 (nativos Stellar) | EIP-4337 |
| Signing | XDR | EIP-191 |
| Finality | ⚡ 5 segundos | ⏳ 12+ segundos |

---

## 📋 Pendientes por Implementar

- [ ] Integración USDC
- [ ] Integración EURC
- [ ] Trustlines management

---

## 🔗 Referencias

- [Stellar SEP-10](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0010.md)
- [Stellar SEP-30](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0030.md)
- [Soroban Documentation](https://soroban.stellar.org/)
