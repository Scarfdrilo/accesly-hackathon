# 📋 SCF Instaward - Statement of Work

## 1. Project & Team Information

| Campo | Valor |
|-------|-------|
| **Project Name** | Accesly |
| **Builder / Team Name** | Accesly Team |
| **Primary Contact** | Vianey - *(email pendiente)* |
| **Ambassador Chapter** | *(pendiente - México?)* |
| **Ambassador Chapter Lead** | *(pendiente)* |
| **Date Submitted** | *(pendiente)* |
| **Suggested Sprint Start Date** | *(pendiente)* |

---

## 2. Instawards Overview & Intent

*(Sección informativa - no requiere llenar)*

---

## 3. Problem Statement & Objective

### Problem Being Addressed

Los SDKs de wallets actuales en Stellar (incluyendo versiones anteriores de Accesly) son **custodiales**: el proveedor del servicio tiene control sobre las llaves privadas de los usuarios. Esto implica:

- **Obligaciones regulatorias costosas** (licencias de custodia, KYC/AML obligatorio)
- **Riesgo de seguridad centralizado** (si el servidor se compromete, todos los fondos están en riesgo)
- **Barrera para escalar** (cada jurisdicción tiene diferentes requisitos)

### Objective of This Instaward

> Al final de **10 días**, Accesly tendrá un **prototipo funcional de MPC 2-of-3 non-custodial** que demuestre:
> 1. Generación de 3 shares (dispositivo, servidor, recovery)
> 2. **Share 1 + Share 2** firman transacciones sin OTP (operación normal)
> 3. **Share 3** cifrado con email del usuario (para recovery, requiere OTP)
> 4. **Share 2 + Share 3 NO pueden firmar juntos** → Accesly nunca puede actuar solo

Esto elimina la clasificación de custodio y las barreras regulatorias asociadas.

---

## 4. Scope of Work (30-Day Deliverables)

### 4.1 In-Scope Deliverables

| # | Deliverable | Descripción | Por qué importa |
|---|-------------|-------------|-----------------|
| 1 | **MPC Key Generation 2-of-3** | Biblioteca que genera 3 shares con esquema 2-of-3. Share 1+2 firman sin OTP. Share 3 cifrado con email. Share 2+3 NO pueden firmar juntos | Accesly nunca puede actuar sin el usuario = non-custodial |
| 2 | **Firma funcional en Testnet** | Share 1 + Share 2 firman transacción real en Stellar testnet | Prueba técnica de que la arquitectura funciona |
| 3 | **Demo + Documentación** | Video corto del flujo + documentación técnica del sistema | Evidencia visual verificable del concepto |

### Out of Scope (Explícitamente NO incluido)

- ❌ Bridge EVM↔Stellar (fase posterior)
- ❌ Fee Abstraction (USDC para fees)
- ❌ UI de producción / diseño final
- ❌ Mobile app
- ❌ Marketing o promoción
- ❌ Integración con partners externos

### 4.2 Deliverable-Aligned Budget Request

| Monto Solicitado | Justificación |
|------------------|---------------|
| **$2,000 USD** | ~40 horas de desarrollo técnico distribuidas en: |
| | • Research + setup MPC library (~10 hrs) |
| | • Implementación key generation (~12 hrs) |
| | • Integración firma + testnet (~12 hrs) |
| | • Testing, demo y documentación (~6 hrs) |

---

## 5. 10-Day Execution Plan & Timeline

| Día | Trabajo Planeado | Output Esperado |
|-----|------------------|-----------------|
| **1-2** | Setup proyecto, research MPC libraries (lit-protocol, @aspect-fi) | Repo configurado, library seleccionada |
| **3-4** | Implementar MPC key generation 3 shares | Código generando shares correctamente |
| **5-6** | Integrar firma con Share 1 + Share 2 | Firma MPC funcionando en local |
| **7-8** | Conectar a Stellar testnet, testing | TX firmada en testnet |
| **9-10** | Grabar demo, escribir documentación | Video demo + docs técnicos listos |

---

## 6. Evidence of Completion

### 6.1 Planned Evidence to Be Submitted

| Deliverable | Tipo de Evidencia | Descripción |
|-------------|-------------------|-------------|
| MPC Key Generation | **Repo + Docs** | Link a GitHub con código y README explicando el esquema 2-of-3 |
| Firma en Testnet | **TX Hash** | Hash de transacción firmada con MPC en Stellar testnet |
| Demo + Docs | **Video 2 min + MD** | Video corto del flujo + documentación técnica |

---

## 7. Next-Step Alignment

Después de este Instaward, el siguiente paso más probable es:

- ☐ Apply to SCF Build Award ← **Objetivo principal**
- ☐ Apply for follow-on Instaward (Fee Abstraction)
- ☐ Continue development independently

**Roadmap:**
1. **Instaward 1** (este): MPC Non-Custodial MVP
2. **Instaward 2**: Fee Abstraction (usuarios pagan fees en USDC)
3. **Build Award**: Bridge EVM↔Stellar + Mainnet deployment

---

## 8. Instawards Constraints Acknowledgement

- ☐ Este scope se completará en **10 días**
- ☐ Instawards apoyan **ejecución**, no exploración abierta
- ☐ Un proyecto puede recibir máximo **2 follow-on Instawards**
- ☐ Cada Instaward está limitado a **$5,000**
- ☐ El funding total de Instawards no puede exceder **$15,000**

---

## 9. Submission Confirmation

Una vez finalizado, este Statement of Work será enviado por el Ambassador Chapter Lead vía el formulario de Airtable para revisión y aprobación.

---

## 📚 Documentación Relacionada

- [MPC Architecture Details](./MPC-ARCHITECTURE.md)
- [Pivot Brief](./PIVOT-BRIEF.md)
- [Idea ZK Bridge](./idea-zk-dani.md)

---

*Documento preparado para SCF Instaward Application - Marzo 2026*
