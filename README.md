# 🚀 Accesly - Hackathon Stellar Growth Lab

**Fecha:** 19-23 Marzo 2026  
**Track:** Scale  
**Equipo:** Vianey, Daniel, José Román (Scarf)

---

## 🎯 Este Sprint: Non-Custodial + Multichain Bridge

### El Pivot

| Antes | Ahora | Futuro |
|-------|-------|--------|
| Wallets custodiales | **Non-Custodial + Bridge EVM↔Stellar** | Accesly for Agents |
| Solo onboarding | Onboarding + Liquidez cross-chain | SDK para AI Agents |

### ¿Por qué el cambio?

1. **Feedback de mentores:** "Wallets custodiales = regulaciones costosas"
2. **Diferenciación vs Pollar:** Ellos no tienen bridge, nosotros sí
3. **Oportunidad:** **Ningún bridge descentralizado** conecta EVM con Stellar

---

## 📂 Documentación

### 🆕 Nuevo (Pivot)

| Doc | Descripción |
|-----|-------------|
| [📋 **PIVOT BRIEF**](./docs/PIVOT-BRIEF.md) | Resumen ejecutivo del pivot |
| [🔮 Idea ZK Bridge](./docs/idea-zk-dani.md) | Propuesta técnica de bridge ZK (Dani) |
| [🏗️ Arquitectura](./docs/architecture-diagram.md) | Diagrama de arquitectura |

### Estrategia

| Doc | Descripción |
|-----|-------------|
| [📊 Estrategia](./docs/estrategia.md) | Plan del hackathon |
| [📅 Cronograma](./docs/cronograma.md) | Agenda día por día |
| [👥 Roles](./docs/roles.md) | Quién hace qué |

### Business

| Doc | Descripción |
|-----|-------------|
| [💼 Business](./docs/business.md) | Modelo de negocio |
| [🔍 Competencia](./docs/competencia.md) | vs Pollar, Axelar, Privy |
| [🎤 Pitch](./docs/pitch.md) | Script del pitch |

---

## 💡 La Propuesta de Valor

```
┌─────────────────────────────────────────────────────────────┐
│  ACCESLY = Privy de Stellar + Bridge Descentralizado        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ONBOARDING SIN FRICCIÓN                                 │
│     Google login → Stellar wallet en 3 segundos             │
│     Sin seed phrases, sin gas fees, non-custodial           │
│                                                             │
│  2. LIQUIDEZ CROSS-CHAIN                                    │
│     Bridge EVM → Stellar descentralizado                    │
│     Axelar usa 75 validators. Nosotros usamos matemáticas.  │
│                                                             │
│  3. FUTURO: AI AGENTS                                       │
│     SDK para que agentes tengan wallets propias             │
│     Operación autónoma en Stellar                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🆚 Competencia

| Feature | Pollar | Axelar | **Accesly** |
|---------|--------|--------|-------------|
| Wallets frictionless | ✅ | ❌ | ✅ |
| Non-custodial | ✅ | N/A | ✅ (MPC) |
| Bridge EVM↔Stellar | ❌ | ✅ | ✅ |
| **Descentralizado** | N/A | ❌ | ✅ |
| Fee Abstraction | ✅ | ❌ | ✅ |
| AI Agents | ❌ | ❌ | 🔜 |

---

## 📊 Tracción

| Métrica | Valor |
|---------|-------|
| Wallets creadas | 88 |
| API Keys | 30 |
| Integraciones | 7 equipos |
| NPM Downloads | ~400 |

---

## 🛣️ Roadmap

```
Q1 2026 (Hackathon)     Q2 2026              Q3 2026           Q4 2026
     │                      │                    │                 │
     ▼                      ▼                    ▼                 ▼
┌─────────┐          ┌─────────────┐      ┌───────────┐    ┌──────────────┐
│ SDK MVP │ ──────►  │ Non-Custodial│ ───►│ Bridge    │───►│ ACCESLY FOR  │
│ 7 integ │          │ Optimistic   │      │ Mainnet   │    │   AGENTS 🤖  │
│ Pitch   │          │ Bridge MVP   │      │ ZK Verify │    │              │
└─────────┘          └─────────────┘      └───────────┘    └──────────────┘
                            │
                            ▼
                      SCF Grant Q2
```

---

## 🔗 Links

| Recurso | Link |
|---------|------|
| Landing | https://accesly.vercel.app |
| Pitch Deck | https://pitch-vercel.vercel.app |
| SDK Code | https://github.com/daniellagart4-sys/Accesly |
| npm | https://www.npmjs.com/package/accesly |

---

## 👥 Equipo

| Persona | Rol | Focus |
|---------|-----|-------|
| **Vianey** | Business Lead | Partnerships, pitch, GTM |
| **Daniel** | Security Lead | Infra, contratos, ZK research |
| **Scarf** | Tech Lead | Arquitectura, código, integraciones |

---

## 🎯 Objetivos Hackathon

- [x] 7+ integraciones con equipos Stellar
- [x] Tracción demostrable (88 wallets, 30 API keys)
- [ ] Arquitectura non-custodial definida
- [ ] Propuesta de bridge documentada
- [ ] Pitch listo para SCF Grant

---

## 📝 Changelog

### 2026-03-21
- **PIVOT:** Non-custodial + Multichain Bridge
- Agregado `PIVOT-BRIEF.md` con resumen ejecutivo
- Agregado `idea-zk-dani.md` con propuesta ZK Bridge
- Reorganizado README para reflejar nuevo enfoque

### 2026-03-20
- Pitch Deck v2 interactivo
- 7 integraciones cerradas
- Feedback de mentores sobre custodia

---

**¡Vamos Accesly!** 🚀🐊
