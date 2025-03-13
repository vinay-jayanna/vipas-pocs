# 🚀 Vipas.AI Serverless Agents & Secure AI Model Deployment

## Overview
This repository contains foundational components that power **Vipas.AI’s** **serverless AI agents, secure model execution, and enterprise-grade AI deployment workflows**. The architecture integrates **Knative, Kubernetes, Streamlit, Jenkins CI/CD, and Python security best practices**, ensuring scalable and secure AI applications.

### 🔥 Key Features:
- **Serverless AI Agents** – Dynamic, event-driven **agent execution** using **Knative & Kubernetes**.
- **Secure AI Model Deployment** – Enforce **isolated, secure launch environments** for AI models.
- **Python Static Security Checks** – Automated **Bandit-based security analysis** during CI/CD.
- **Jenkins CI/CD for Security Testing** – Triggers **automated security & compliance checks** during onboarding.
- **Streamlit UI for Agent Management** – Easily manage AI agents and configurations.
- **DevPI Private Python Package Repository** – Secure **package distribution and versioning** for enterprise AI models.

---

## 📌 Architecture & Components
### **1️⃣ Serverless AI Agents (Knative + Kubernetes)**
- Uses **Knative for event-driven execution** of AI models.
- Supports **secure execution** of models in **ephemeral, containerized environments**.
- Integrated with **AWS EKS** for **scalable AI workloads**.

### **2️⃣ Secure Model Execution & AI Launch Mechanism**
- **App proxy configurations** (`app_proxy_flower_class.yaml`) ensure **model security**.
- **Transformer pipelines** (`transform_flower_class.py`) enhance inference **efficiency**.
- **Kubernetes service isolation** prevents unauthorized model access.

### **3️⃣ Security & Compliance Checks (CI/CD + Static Analysis)**
- **Jenkins CI/CD pipeline** triggers **security scans** & **static code analysis**.
- **Bandit Python Security Tests** (`bandit/`) detect vulnerabilities in AI models.
- **Python CI Pipeline** runs **automated unit tests** (`Jenkins_python_CI/tests`).

### **4️⃣ Streamlit UI for AI Agent Management**
- **Streamlit-based dashboards** for managing AI agent configurations (`streamlit.base/`).
- **Dockerized application** (`Dockerfile`) for streamlined **deployment & scaling**.

### **5️⃣ DevPI Private Python Package Repository**
- **Enterprise-grade Python package management** using `devpi/`.
- Supports **secure Python dependency distribution** within AI deployments.

---

## 🚀 Quick Start Guide
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/vinay-jayanna/vipas-serverless-agents.git
cd vipas-serverless-agents
```

### **2️⃣ Deploy Serverless AI Agents**
```sh
kubectl apply -f serverless_agents/deploy_manager.yaml
kubectl apply -f serverless_agents/app_flower_class.yaml
```

### **3️⃣ Run Python Security Analysis (Bandit)**
```sh
bandit -r bandit/
```

### **4️⃣ Deploy Streamlit UI**
```sh
docker build -t vipas-streamlit-ui -f streamlit.base/Dockerfile .
docker run -p 8501:8501 vipas-streamlit-ui
```

### **5️⃣ Setup Jenkins CI/CD Pipeline**
```sh
kubectl apply -f Jenkins_python_CI/Jenkinsfile
```

---

## 🔥 Why Use This?
🔹 **Enterprise-Grade AI Deployment** – Secure, scalable, serverless AI model execution.  
🔹 **CI/CD Security Compliance** – Enforces security standards for AI models at every stage.  
🔹 **Fully Serverless** – AI agents scale dynamically, reducing costs & improving efficiency.  
🔹 **Streamlit UI Management** – Simplified AI model & agent tracking.  
🔹 **Private Python Package Repository** – Secure, internal Python dependency management.  

---

## 📚 Additional Resources
- **📖 Serverless Deployment Steps:** [`serverless_agents/deploy_manager.yaml`](serverless_agents/deploy_manager.yaml)
- **🔒 Bandit Security Tests:** [`bandit/`](bandit/)
- **⚡ Python CI/CD Pipeline:** [`Jenkins_python_CI/`](Jenkins_python_CI/)
- **📦 DevPI Private Repo Setup:** [`devpi/`](devpi/)


