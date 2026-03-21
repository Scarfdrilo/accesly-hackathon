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

> Al final de 30 días, Accesly tendrá una **arquitectura non-custodial funcional usando MPC (Multi-Party Computation)** donde:
> 1. Las llaves se dividen en 3 shares
> 2. El share del servidor está **cifrado con el email del usuario**
> 3. Solo se puede usar cuando el usuario **confirma un OTP**
> 4. **Ninguna parte puede firmar transacciones sola**

Esto elimina la clasificación de custodio y las barreras regulatorias asociadas.

---

## 4. Scope of Work (30-Day Deliverables)

### 4.1 In-Scope Deliverables

| # | Deliverable | Descripción | Por qué importa |
|---|-------------|-------------|-----------------|
| 1 | **MPC Key Generation con cifrado por email** | Sistema donde el key se divide en 3 shares. Share 2 (servidor) está cifrado con el email del usuario y solo se descifra al confirmar OTP | Ninguna parte puede firmar sola = non-custodial. Accesly no puede acceder a fondos sin participación activa del usuario |
| 2 | **Smart Account en Soroban (Testnet)** | Contrato inteligente en Stellar testnet que valida firmas generadas por MPC | Prueba técnica on-chain de que la arquitectura funciona |
| 3 | **Demo End-to-End con Video** | Flujo completo: Google login → OTP al email → TX firmada en testnet | Evidencia visual verificable del concepto funcionando |

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
| **$5,000 USD** | ~120 horas de desarrollo técnico distribuidas en: |
| | • Investigación e implementación MPC (~50 hrs) |
| | • Smart Contract Soroban (~30 hrs) |
| | • Integración OTP + cifrado por email (~25 hrs) |
| | • Testing, documentación y demo (~15 hrs) |
| | • Infraestructura testnet |

---

## 5. 30-Day Execution Plan & Timeline

| Semana | Trabajo Planeado | Output Esperado |
|--------|------------------|-----------------|
| **Week 1** | Investigación MPC libraries, setup proyecto, definir esquema de cifrado | Documento técnico de arquitectura, repo configurado |
| **Week 2** | Implementar MPC key generation, cifrado Share 2 con email | Código funcionando en local, tests unitarios |
| **Week 3** | Smart Contract Soroban, integración OTP, conexión frontend | Contrato desplegado en testnet, flujo E2E funcionando |
| **Week 4** | Testing completo, fix bugs, grabar demo, documentación | Video demo, documentación final, evidencia lista |

---

## 6. Evidence of Completion

### 6.1 Planned Evidence to Be Submitted

| Deliverable | Tipo de Evidencia | Descripción |
|-------------|-------------------|-------------|
| MPC Key Generation | **Repo + Docs** | Link a GitHub con código y README explicando el flujo de cifrado |
| Smart Account Soroban | **Contract + TX Hash** | Link al contrato en testnet + hash de transacción de ejemplo |
| Demo E2E | **Video 3 min** | Walkthrough completo: login → OTP → firma → TX confirmada |

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

- ☐ Este scope se completará en **30 días o menos**
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
