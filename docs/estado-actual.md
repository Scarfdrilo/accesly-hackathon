# 📍 Estado Actual - Accesly

**Actualizado:** 2026-03-21 (Día 2 del Hackathon)

---

## 🎯 Ethos

> **"Focus on value. We handle the friction."**

Tu enfócate en lo que genera valor. Nosotros armamos la experiencia frictionless para tus usuarios.

---

## 🛤️ Roadmap

### Sprint Hackathon (ahora)
- Demo sólida del flow actual

### 30 días
- ✅ Full non-custodial wallet infrastructure
- ✅ x402 pay-as-you-use en testnet

### 60 días
- Mainnet launch
- x402 en mainnet

### 90 días
- Etherfuse on/off ramp (México)
- Bridge EVM → Stellar

---

## 💰 Modelo de Negocio

### Revenue Streams

1. **x402 Pay-as-you-use**
   - Developers pagan por uso
   - Pricing por wallet creada / transacción

2. **Yield Share (Etherfuse)**
   - Usuarios tienen CETES en su wallet Accesly
   - Etherfuse genera rendimiento
   - Accesly se queda con % del yield
   - Usuario ve balance en la moneda que quiera
   - ⚠️ Solo México inicialmente

---

## 🎤 Narrativa de Venta

**Para developers/empresas:**
> "Accesly es la solución que ayuda a tu dApp a ser frictionless con tus usuarios. Ofrecemos onboarding non-custodial con social login y pay-as-you-use para negocios. Tú te enfocas en tu core business, nosotros resolvemos wallets y pagos."

**Taglines:**
- "Build value, not wallets."
- "Your app. Your users. Zero friction."
- "Focus on value. We handle the friction."

---

## 🏗️ Arquitectura

### Capa 1 (Global)
- Non-custodial social login
- x402 payments standard
- TEE + Shamir key sharding

### Capa 2 (México)
- Etherfuse integration
- CETES yield para usuarios
- On/off ramp en pesos

---

## 📋 Consideraciones

### Regulación
- Yield en México puede requerir registro CNBV
- Verificar que Etherfuse tenga esto resuelto

### Non-custodial + Yield
- Asegurar que el mensaje sea consistente
- ¿Quién tiene custody cuando está en CETES?

### Escalabilidad
- Core funciona global
- Etherfuse es feature regional (pitch a SCF)

---

## 🔗 Links

- **Landing:** https://accesly.vercel.app
- **GitHub:** https://github.com/daniellagart4-sys/Accesly
- **npm:** https://www.npmjs.com/package/accesly

---

*Documentado por Scarfdrilo 🐊*
