# 🛡️ Phishing Detection & Response Pipeline (KubeSecOps Edition)

A full-stack cybersecurity project that simulates phishing attacks and builds an automated detection and response system using a modern DevSecOps toolchain. Designed to showcase skills in **Kubernetes, Docker, Jenkins, SALT, AWS, MySQL/Cassandra, and Python-based security tooling**.

---

## 📌 Project Goals

- Simulate phishing emails and track user interaction.
- Detect suspicious email content using a lightweight detection API.
- Log and analyze phishing attempts using MySQL or Cassandra.
- Deploy microservices via Kubernetes with CI/CD pipelines.
- Provision infrastructure using SALT and optionally deploy to AWS.

---

## 🚀 Tech Stack

| Category         | Tools Used                                                |
|------------------|-----------------------------------------------------------|
| Containerization | Docker                                                    |
| Orchestration    | Kubernetes (Minikube or AWS EKS)                          |
| CI/CD            | Jenkins                                                   |
| Infra Automation | SALT                                                      |
| Cloud            | AWS (EC2, EKS, S3, CloudWatch – optional)                 |
| Backend          | Python (Flask), Bash                                      |
| Database         | MySQL (default), Cassandra (optional)                     |
| OS/Platform      | Linux (Ubuntu/Debian-based distros)                       |

---

## 🏗️ Architecture Overview

```text
[Phishing Simulator] ---> [User Click Tracker]
       |                       |
       v                       v
 [Detection API] ----> [MySQL/Cassandra Logging]
       |
       v
[Dashboard / Alerts / CI/CD Auto Response]

All services run in containers, orchestrated via Kubernetes, built and deployed via Jenkins.

---

## 🔧 Setup Instructions
### 1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/phishing-detection-pipeline.git
cd phishing-detection-pipeline
### 2. Start Local Services (Dev Mode)
bash
Copy
Edit
docker-compose up -d
### 3. Build and Deploy to Minikube
bash
Copy
Edit
eval $(minikube docker-env)
docker build -t phishing-simulator ./simulator
docker build -t phishing-detector ./detector
kubectl apply -f k8s/
### 4. Jenkins CI/CD
Install Jenkins locally or run jenkins/jenkins-compose.yml

Import the provided Jenkinsfile

Configure Docker/K8s credentials inside Jenkins

### 5. SALT Provisioning (Optional)
bash
Copy
Edit
sudo salt-call --local state.apply
### 📊 Features
🧪 Simulated phishing emails with clickable payloads

🔍 Lightweight phishing content scanner

📉 Click logging and threat response audit trail

🛠️ Fully containerized microservices

⚙️ CI/CD via Jenkins Pipelines

☁️ Cloud-ready (EKS/EC2/S3 support)

📦 SALT for repeatable, scalable VM config

### ✅ To-Do / Stretch Goals
 Add real-time alerting via Slack or MS Teams

 Visual dashboard for phishing analytics

 Integrate Suricata or Zeek for network-based detection

 Deploy to AWS using Terraform or CloudFormation

 Implement role-based access controls for simulation portal

### 🧠 Inspiration
This project is inspired by real-world blue team ops and red team simulation frameworks like GoPhish, PhishTool, and MITRE ATT&CK tactics.

### 👨‍💻 Author
Sunny Nguyen

