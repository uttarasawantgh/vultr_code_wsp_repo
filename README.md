# VultrGuard AI: Edge-to-Cloud Governance & Weight-Space Programming (WSP)

> **Autonomous hybrid edge-to-cloud security and network optimization framework featuring Vultr Serverless Inference, NVIDIA DGX Spark edge infrastructure, and Gemini-powered multi-agent diagnostics.**

---

## 🚀 Overview

**VultrGuard AI** is an advanced hybrid framework engineered to solve critical challenges in data sovereignty, network egress costs, and real-time operational safety for mission-critical deployments. By leveraging a tiered architecture, the system combines **Vultr Serverless (Llama 3.3 70B)** in the cloud as an intelligent advisory oracle with local edge compute running on high-performance infrastructure like **NVIDIA DGX Spark**. 

The core innovation centers on **Weight-Space Programming (WSP)**, enabling secure local model weight mutations and optimizations based on cloud-prescribed guidance without exposing proprietary telemetry or sensitive data to external servers.

---

## 🏗️ Architecture & Key Features

* **Hybrid Edge-to-Cloud Tiering**: Offloads heavy advisory intelligence to Vultr Serverless while maintaining localized, air-gapped execution on DGX Spark bare-metal hardware.
* **Weight-Space Programming (WSP)**: Executes precise, secure model weight adjustments for network optimization and resource governance.
* **Gemini Multi-Agent Diagnostics**: Integrates advanced language models for autonomous anomaly detection, diagnostic reasoning, and structured verification.
* **Human-in-the-Loop (HITL) Safety Governance**: Incorporates automated safety gates, L2 norm shift calculations, and timestamped local `.pt` snapshot artifacts.
* **Verifiable Audit Proofs**: Generates immutable audit logs and compliance artifacts for enterprise traceability.

---

## 🧪 Validation & Test Cases

### Test Case 1: Simple Routine Use Case (Local Model 0.5B)
> *"For my first test case, I run a routine local evaluation. As you can see, the request is processed entirely on my local 0.5B micro-edge tier in sub-second time, requiring zero cloud tokens, zero data egress, and incurring zero cost while ensuring total privacy."*

* **Tier**: Local 0.5B Micro-Edge
* **Execution Time**: Sub-second
* **Cloud Cost**: $0.00 (Zero tokens, zero egress)
* **Privacy**: Air-gapped / Total local isolation

### Test Case 2: Cloud Invocation & Weight-Space Programming (WSP)
> *"For my second test case, I trigger a cloud escalation where Vultr's Serverless Llama 3.3 70B acts as an advisory oracle. The cloud model generates a secure JSON weight prescription, which my DGX Spark executes locally via Weight-Space Programming—calculating the precise L2 norm shift and minting a verified, timestamped local snapshot artifact without leaking sensitive weights."*

* **Oracle Tier**: Vultr Serverless (Llama 3.3 70B)
* **Execution Engine**: Weight-Space Programming (WSP) on DGX Spark
* **Artifacts Generated**: Precise L2 norm shift calculation and timestamped local `.pt` weight snapshot
* **Cloud Cost**: $0.01

---

## 🎥 Project Walkthrough & Video Demonstration

Watch the complete demonstration and technical walkthrough on YouTube:
👉 **[VultrGuard AI Video Demonstration](https://youtu.be/cnlkjWkp3u4)**

---

## 🔗 Baseline Reference Repository

This project builds upon and extends concepts from the foundational architecture established in:
* **Baseline Repo**: [uttarasawantgh/nebius_nemo_auto_code_repo](https://github.com/uttarasawantgh/nebius_nemo_auto_code_repo)

---

## 🛠️ Technical Stack & Toolchain

* **Cloud Infrastructure**: Vultr Serverless Inference (Llama 3.3 70B)
* **Edge Infrastructure**: NVIDIA DGX Spark (Grace Blackwell GB10 Superchip, 128GB unified memory)
* **AI & Multi-Agent Frameworks**: Gemini, PyTorch, vLLM, Hugging Face Transformers
* **Language & Runtime**: Python, C++, Docker, Git

---

## 📂 Repository Structure

```text
├── src/
│   ├── core/               # Core WSP engine and weight mutation logic
│   ├── serverless/         # Vultr Serverless API connectors and wrappers
│   ├── edge/               # DGX Spark local execution & safety governance
│   └── agents/             # Gemini-powered diagnostic multi-agent loops
├── checkpoints/            # Local model snapshots (.pt) and audit artifacts
├── README.md               # Project documentation
├── LICENSE                 # Open-source license
└── requirements.txt        # Python dependencies
