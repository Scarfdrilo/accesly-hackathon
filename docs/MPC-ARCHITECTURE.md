# 🔐 Accesly MPC Non-Custodial Architecture

## Resumen

Arquitectura de wallets **non-custodial** usando MPC (Multi-Party Computation) con esquema **2-of-3 Threshold** donde **Accesly nunca puede firmar transacciones sin la participación del usuario**.

---

## 🔑 Distribución de Llaves (2-of-3 Threshold)

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
│      LocalStorage         Servidor             Cifrado con     │
│      / Secure             Accesly              EMAIL + OTP     │
│      Enclave              (plain)              del usuario     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔐 Combinaciones de Firma

| Combinación | ¿Puede firmar? | Caso de uso |
|-------------|----------------|-------------|
| **Share 1 + Share 2** | ✅ SÍ (sin OTP) | Operación normal |
| **Share 1 + Share 3** | ✅ SÍ (con OTP) | Recovery si servidor cae |
| **Share 2 + Share 3** | ❌ NO | Accesly no puede firmar solo |

---

## 🛡️ Por Qué Es Non-Custodial

### La Regla Clave

> **Share 2 (servidor) + Share 3 (recovery) NO pueden firmar juntos**
> 
> Aunque Accesly tiene Share 2 y almacena Share 3, **Share 3 está cifrado con el email del usuario y requiere OTP para descifrarse**.
> 
> Esto significa: **Accesly NUNCA puede actuar sin la participación del usuario.**

### Implicaciones Legales

| Modelo | ¿Accesly tiene control? | Regulación |
|--------|------------------------|------------|
| **Custodial** (antes) | ✅ Sí, tiene las llaves | Requiere licencias, KYC/AML |
| **Non-Custodial** (ahora) | ❌ No, necesita al usuario | Sin requisitos custodiales |

> **Resultado:** Accesly es un **proveedor de infraestructura**, no un custodio. Esto elimina barreras regulatorias.

---

## 🔄 Flujo de Firma Normal (Sin OTP)

```
┌──────────────────────────────────────────────────────────────────┐
│ FIRMA NORMAL: Share 1 (dispositivo) + Share 2 (servidor)        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Usuario abre la app y está logueado                         │
│  2. Usuario inicia transacción (ej: enviar 100 USDC)            │
│  3. App envía request al servidor Accesly                       │
│  4. MPC signing combina Share 1 + Share 2                       │
│  5. TX firmada se envía a Stellar                               │
│                                                                  │
│  ⚡ Flujo rápido, sin fricción, sin OTP                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Flujo de Recovery (Con OTP)

```
┌──────────────────────────────────────────────────────────────────┐
│ RECOVERY: Share 1 (nuevo dispositivo) + Share 3 (recovery)      │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Escenario: Usuario perdió su dispositivo o quiere migrar       │
│                                                                  │
│  1. Usuario hace login con Google en nuevo dispositivo          │
│  2. Sistema detecta que no hay Share 1 local                    │
│  3. Usuario solicita recovery                                   │
│  4. Sistema envía OTP al email del usuario                      │
│  5. Usuario ingresa OTP                                         │
│  6. Share 3 se descifra usando email + OTP                      │
│  7. Se genera nuevo Share 1 para el dispositivo                 │
│  8. Usuario puede operar normalmente                            │
│                                                                  │
│  🔐 OTP requerido porque Share 3 está cifrado con el email     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

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
│  Share 2 ──► Almacenado en servidor Accesly (plain)             │
│  Share 3 ──► Cifrado con email, almacenado en servidor/backup   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│ 3. FIRMAR TRANSACCIÓN (Operación Normal)                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Usuario quiere enviar 100 USDC                                  │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ a) App genera TX unsigned                                   │ │
│  │ b) App envía request con Share 1 al servidor                │ │
│  │ c) Servidor usa Share 2 para completar firma MPC            │ │
│  │ d) TX firmada se envía a Stellar                            │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ⚡ Sin OTP - flujo rápido y sin fricción                       │
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

## 📋 Deliverables para Instaward (10 días)

| Día | Deliverable | Descripción | Evidencia |
|-----|-------------|-------------|-----------|
| 1-4 | **MPC Key Generation** | Biblioteca 2-of-3: Share 1+2 firman, Share 2+3 no | Repo + docs |
| 5-8 | **Firma en Testnet** | TX firmada con Share 1 + Share 2 en Stellar testnet | TX hash |
| 9-10 | **Demo + Docs** | Video corto + documentación técnica | Video 2 min |

### Out of Scope (Instaward 1)
- Smart Contract Soroban complejo
- Recovery flow completo con OTP
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
