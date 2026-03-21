# 🔐 Accesly MPC Non-Custodial Architecture

## Resumen

Arquitectura de wallets **non-custodial** usando MPC (Multi-Party Computation) donde **ninguna parte puede firmar transacciones sola**.

---

## 🔑 Distribución de Llaves (3-of-3 Threshold)

```
┌─────────────────────────────────────────────────────────────────┐
│                    MPC KEY GENERATION                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │    SHARE 1      │  │    SHARE 2      │  │    SHARE 3      │ │
│  │   Dispositivo   │  │    Servidor     │  │    Recovery     │ │
│  │    Usuario      │  │    Accesly      │  │   (Encriptado)  │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘ │
│           │                    │                    │          │
│           │                    │                    │          │
│      LocalStorage         Cifrado con           Backup         │
│      / Secure             EMAIL + OTP           Offline        │
│      Enclave              del usuario           Multi-región   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Por Qué Es Non-Custodial

### Share 2 (Servidor Accesly) - El Detalle Clave

| Aspecto | Implementación |
|---------|----------------|
| **Cifrado** | La llave del servidor está cifrada con el **email del usuario** |
| **Acceso** | Solo se puede descifrar cuando el usuario confirma **OTP** |
| **Control** | Accesly **NO puede usar** esta llave sin la participación activa del usuario |

### Flujo de Firma

```
1. Usuario inicia transacción en su dispositivo
2. App solicita OTP al email del usuario
3. Usuario ingresa OTP
4. Servidor descifra Share 2 usando email + OTP validado
5. Se genera firma MPC combinando Share 1 + Share 2
6. Transacción firmada se envía a Stellar
```

### Implicaciones Legales

| Modelo | ¿Accesly tiene control? | Regulación |
|--------|------------------------|------------|
| **Custodial** (antes) | ✅ Sí, tiene las llaves | Requiere licencias, KYC/AML |
| **Non-Custodial** (ahora) | ❌ No, necesita OTP del usuario | Sin requisitos custodiales |

> **Resultado:** Accesly es un **proveedor de infraestructura**, no un custodio. Esto elimina barreras regulatorias.

---

## 🔄 Flujo Completo: Login → Wallet → TX

```
┌──────────────────────────────────────────────────────────────────┐
│ 1. LOGIN                                                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Usuario ──► Google OAuth ──► Email verificado                  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│ 2. KEY GENERATION (Primera vez)                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MPC Protocol genera 3 shares:                                   │
│                                                                  │
│  Share 1 ──► Almacenado en dispositivo (localStorage/enclave)   │
│  Share 2 ──► Cifrado con email, almacenado en servidor Accesly  │
│  Share 3 ──► Cifrado, backup en storage distribuido             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│ 3. FIRMAR TRANSACCIÓN                                            │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Usuario quiere enviar 100 USDC                                  │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ a) App genera TX unsigned                                   │ │
│  │ b) Servidor envía OTP al email del usuario                  │ │
│  │ c) Usuario ingresa OTP en la app                            │ │
│  │ d) Servidor valida OTP y descifra Share 2                   │ │
│  │ e) MPC signing: Share 1 (device) + Share 2 (server)         │ │
│  │ f) TX firmada se envía a Stellar                            │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ⚠️  En ningún momento se reconstruye la llave completa         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Stack Técnico Propuesto

| Componente | Tecnología | Notas |
|------------|------------|-------|
| MPC Library | `@aspect-fi/mpc-sdk` o `lit-protocol` | TSS (Threshold Signature Scheme) |
| Key Storage (device) | Web Crypto API + localStorage | O secure enclave en mobile |
| Key Storage (server) | AES-256-GCM cifrado con email | Descifrado solo con OTP válido |
| OTP | TOTP (Time-based) o Email Magic Link | 6 dígitos, 5 min expiry |
| Recovery | Shamir Secret Sharing | Multi-región backup |

---

## 📋 Deliverables para Instaward (30 días)

| # | Deliverable | Descripción | Evidencia |
|---|-------------|-------------|-----------|
| 1 | **MPC Key Generation** | Sistema 3-of-3 con Share 2 cifrado por email+OTP | Repo + documentación técnica |
| 2 | **Smart Account (Soroban)** | Contrato testnet que valida firmas MPC | Contract address + TX hash |
| 3 | **Demo E2E** | Video: Google login → OTP → TX firmada | Video 3 min + link testnet |

### Out of Scope (Instaward 1)
- Bridge EVM↔Stellar
- Fee Abstraction
- UI de producción
- Mobile app
- Marketing

---

## 🔮 Roadmap Post-Instaward

| Fase | Objetivo | Instaward |
|------|----------|-----------|
| **Instaward 1** | MPC Non-Custodial MVP | Este documento |
| **Instaward 2** | Fee Abstraction (pagar fees en USDC) | Futuro |
| **Build Award** | Bridge EVM↔Stellar + Mainnet | Post-Instawards |

---

## 📚 Referencias

- [Lit Protocol MPC](https://developer.litprotocol.com/)
- [Fireblocks MPC Architecture](https://www.fireblocks.com/what-is-mpc/)
- [SEP-30 Account Recovery](https://stellar.org/protocol/sep-30)
- [Soroban Smart Contracts](https://soroban.stellar.org/)

---

*Última actualización: Marzo 2026 - SCF Instaward Application*
