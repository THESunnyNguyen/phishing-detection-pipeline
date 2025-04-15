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
