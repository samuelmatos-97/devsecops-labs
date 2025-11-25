# Lab 01 — Cloud Secure Server (AWS + Linux + Security)

This lab aims to create a secure server on AWS, configure it via SSH, apply initial hardening, and document the entire process.

---

## 🧱 Lab Objectives
- Create an EC2 t3.micro instance (Free Tier)
- Create and manage SSH key pairs
- Configure Security Groups (AWS firewall)
- Access the server via SSH
- Install Nginx
- Create my own user (not root)
- Perform basic system hardening
- Document commands and procedures

---

## 🛠️ Steps (overview)
1. Create an EC2 instance on AWS
2. Create a key pair
3. Configure the Security Group (22 + 80)
4. Access via SSH
5. Install Nginx
6. Create user and permissions
7. Basic hardening
8. Testing and validation
9. Final documentation

---

## 📦 Simple Architecture
EC2 Instance (t3.micro)

└── Linux + SSH + Nginx

└── Security Group (22/80)

└── Key Pair (SSH)

---

## 📝 Important notes
- At the end, always terminate the instance to avoid costs. Never leave EC2 instances running unnecessarily.
- Always keep SSH keys in a safe place. Do not share SSH keys with anyone.
- This lab lays the groundwork for Docker, Kubernetes, and Terraform.
- Delete instances, volumes, and elastic IPs when finished.

---

## ✔ Checklist
- [✔] Instance created
- [✔] Key Pair created
- [✔] Security Group configured
- [✔] SSH validated
- [✔] Nginx installed
- [✔] Hardening done
- [✔] Documentation completed

# Lab 01 — Cloud Secure Server (AWS EC2 + Ubuntu + Nginx)

This lab aims to create and configure the first secure server in the cloud, using AWS EC2, Ubuntu Server, and Nginx.
This exercise is part of my DevSecOps roadmap, focusing on cloud, infrastructure, and security.

---

## 🧩 Lab Objectives
- Create an EC2 instance on AWS (Free Tier)
- Securely access the server via SSH
- Install and configure an Nginx web server
- Implement initial security best practices
- Document the process following the DevSecOps approach

---

## 🔧 Technologies and Services Used
- **AWS EC2** (Elastic Compute Cloud)
- **Ubuntu Server 24.04 LTS**
- **Nginx Web Server**
- **Security Groups (AWS firewall)**
- **SSH with private key (.pem)**
- **Terminal (PowerShell / Git Bash / SSH)**

---

## ☁️ Creating the EC2 Instance
**Configurations chosen:**

- **Region:** Europe (Ireland) — `eu-west-1`
- **AMI:** Ubuntu Server 24.04 LTS (HVM), SSD — *Free Tier Eligible*
- **Instance type:** `t3.micro` — *Free Tier*
- **Storage:** 8 GiB gp3
- **Key Pair:**
  - Name: `lab01-key`
  - Type: RSA
  - Format: `.pem`

### 🔐 Security Group
Configured rules:

| Type | Port | Source | Description |
|------|-------|---------|-----------|
| SSH  | 22 | My IP | Secure access only from my network |
| HTTP | 80 | 0.0.0.0/0 | Allow access to the web server |

---

## 🔑 Access via SSH
Command used to access:

#bash#

ssh -i lab01-key.pem ubuntu@PUBLIC_IP
# After the instance is stopped and restarted, the public IP changes.

# Nginx Installation - Commands Executed
- sudo apt update
- sudo apt upgrade -y
- sudo apt install -y nginx
- sudo systemctl status nginx

Verification in the browser:
http://PUBLIC_IP

“Welcome to Nginx” page successfully confirmed.

- Custom HTML page created
- Reviewed Nginx logs (access.log and error.log)
- Created a simple sysinfo automation script

