# Lab 01 — Cloud Secure Server (AWS + Linux + Security)

Este laboratório tem como objetivo criar um servidor seguro na AWS, configurá-lo via SSH, aplicar hardening inicial e documentar todo o processo.

---

## 🧱 Objetivos do Lab
- Criar uma instância EC2 t2.micro (Free Tier)
- Criar e gerir pares de chaves SSH
- Configurar Security Groups (firewall AWS)
- Aceder via SSH ao servidor
- Instalar Nginx
- Criar utilizador próprio (sem ser root)
- Fazer hardening básico do sistema
- Documentar comandos e procedimentos

---

## 🛠️ Passos (visão geral)
1. Criar instância EC2 na AWS
2. Criar par de chaves (Key Pair)
3. Configurar o Security Group (22 + 80)
4. Aceder via SSH
5. Instalar Nginx
6. Criar utilizador e permissões
7. Hardening básico
8. Testes e validação
9. Documentação final

---

## 📦 Arquitetura Simples
EC2 Instance (t2.micro)
└── Linux + SSH + Nginx
└── Security Group (22/80)
└── Key Pair (SSH)

---

## 📝 Notas importantes
- No final, terminar sempre a instância para evitar custos. Nunca deixar instâncias EC2 ligadas sem necessidade.
- Manter sempre as chaves SSH num local seguro. Não partilhar chaves SSH com ninguém.
- Este lab prepara as bases para Docker, Kubernetes e Terraform.
- Apagar instâncias, volumes e IPs elásticos quando terminar.

---

## ✔ Checklist
- [✔] Instância criada
- [✔] Key Pair criado
- [✔] Security Group configurado
- [✔] SSH validado
- [✔] Nginx instalado
- [✔] Hardening feito
- [✔] Documentação concluída

###### Dia 16/11/2025 ######

# Lab 01 — Cloud Secure Server (AWS EC2 + Ubuntu + Nginx)

Este laboratório tem como objetivo criar e configurar o primeiro servidor seguro na cloud, utilizando AWS EC2, Ubuntu Server e Nginx.
Este exercício faz parte do meu roadmap DevSecOps, focando em cloud, infraestrutura e segurança.

---

## 🧩 Objetivos do Lab
- Criar uma instância EC2 na AWS (Free Tier)
- Aceder ao servidor através de SSH de forma segura
- Instalar e configurar um servidor web Nginx
- Implementar boas práticas de segurança iniciais
- Documentar o processo seguindo abordagem DevSecOps

---

## 🔧 Tecnologias e Serviços Utilizados
- **AWS EC2** (Elastic Compute Cloud)
- **Ubuntu Server 24.04 LTS**
- **Nginx Web Server**
- **Security Groups (firewall AWS)**
- **SSH com chave privada (.pem)**
- **Terminal (PowerShell / Git Bash / SSH)**

---

## ☁️ Criação da Instância EC2
**Configurações escolhidas:**

- **Região:** Europe (Ireland) — `eu-west-1`
- **AMI:** Ubuntu Server 24.04 LTS (HVM), SSD — *Free Tier Eligible*
- **Tipo de instância:** `t3.micro` — *Free Tier*
- **Armazenamento:** 8 GiB gp3
- **Key Pair:**
  - Nome: `lab01-key`
  - Tipo: RSA
  - Formato: `.pem`

### 🔐 Security Group
Regras configuradas:

| Tipo | Porta | Origem | Descrição |
|------|-------|---------|-----------|
| SSH  | 22 | My IP | Acesso seguro apenas a partir da minha rede |
| HTTP | 80 | 0.0.0.0/0 | Permitir acesso ao servidor web |

---

## 🔑 Acesso via SSH
Comando utilizado para aceder:

#bash#

ssh -i lab01-key.pem ubuntu@IP_PUBLICO
# Após a instância ser parada e iniciada novamente, o IP público muda.

# Instalação Nginx - Comandos Executados
- sudo apt update
- sudo apt upgrade -y
- sudo apt install -y nginx
- sudo systemctl status nginx

Verificação no browser:
http://IP-PUBLICO

Página "Welcome to Nginx" confirmada com sucesso.

###### Dia 17/11/2025 ######

- Custom HTML page created
- Reviewed Nginx logs (access.log and error.log)
- Created a simple sysinfo automation script

