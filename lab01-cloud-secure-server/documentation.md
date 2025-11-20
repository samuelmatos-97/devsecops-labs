# Lab 01 — Cloud Secure Server (AWS EC2 + Linux + Security)

This lab focuses on creating, configuring, and securing a cloud server on AWS using EC2, Ubuntu, Nginx, and essential DevSecOps practices.
The main goal is to understand how to deploy a real cloud instance, access it securely, harden it, and document the entire process.

---

# 🎯 1. Lab Objectives

- Deploy an EC2 instance using AWS Free Tier
- Access the instance securely via SSH and key-based authentication
- Configure AWS Security Groups (cloud-level firewall)
- Install and configure the Nginx web server
- Create a dedicated non-root user with sudo privileges
- Configure UFW firewall on Ubuntu
- Apply basic system hardening
- Create a custom HTML page hosted on Nginx
- Inspect server logs and create a simple automation script
- Document the entire process following DevSecOps standards

---

# ☁️ 2. Key Concepts Explained

### **AWS EC2**
A service that provides virtual machines in the cloud.

Allows choosing OS, hardware size, network rules, and access policies.

### **AMI**
Amazon Machine Image — a template used to create the server.

I used **Ubuntu Server 24.04 LTS**.

### **Instance Type: t3.micro**
Free Tier–eligible instance with:
- 1 vCPU
- 1 GB RAM

Perfect for testing, learning, and small workloads.

### **Key Pair (.pem)**
A private SSH key used instead of a password.

Provides more secure authentication.

### **Security Groups**
AWS-level firewall that controls inbound/outbound traffic.

Configured rules:

| Rule | Port | Source | Reason |
|------|------|--------|--------|
| SSH | 22 | My IP | Secure access |
| HTTP | 80 | Anywhere | Allow public web access |

### **SSH**
Encrypted protocol used to access the server remotely.

### **Nginx**
A high-performance web server used widely in DevOps, reverse proxies, APIs, etc.

### **UFW**
Ubuntu’s built-in firewall (Uncomplicated Firewall).

### **Hardening**
The practice of securing a system by reducing attack surfaces.

---

# 🛠️ 3. Steps Performed in the Lab

## 3.1 Deploy EC2 Instance
Configuration used:
- **Region:** eu-west-1 (Ireland)
- **AMI:** Ubuntu Server 24.04 LTS
- **Instance Type:** `t3.micro` (Free Tier)
- **Storage:** 8 GiB gp3
- **Key Pair:** `lab01-key.pem`

---

## 3.2 Connect via SSH

Initial access:

#bash#

`ssh -i lab01-key.pem ubuntu@PUBLIC_IP`

Explanation:
  - `ssh` - opens a secure terminal connection to a remote server.
  - `-i lab01-key.pem` - specifies the private key for authentication.
  - `ubuntu` - username used in Ubuntu AMIs on AWS.
  - `@PUBLIC_IP` - the public IP address of the EC2 instance.

SSH checks the .pem key - verifies the user - opens a secure session.

## 3.3 Create a Dedicated User (devops)

`sudo adduser devops`

Explanation:
  - `sudo` - runs the command with administrator/root privileges.
  - `adduser` - creates a new user on the system.
  - `devops` - the username being created.

This creates:
  - `/home/devops/`
  - user password
  - basic configuration files

`sudo usermod -aG sudo devops`

Explanation:
  - `usermod` - modifies an existing user.
  - `-aG sudo` - add the user to the sudo group (admin privileges).
  - `devops` - the user to modify.

This allows devops to run commands like:

`sudo apt update`

# 🔐 Copy SSH Key to New User

Command:

`sudo mkdir /home/devops/.ssh`

Explanation:

- Creates a .ssh directory, which stores SSH keys.
- Must exist for key-based login.

Command:

`sudo cp ~/.ssh/authorized_keys /home/devops/.ssh/`

Explanation:

- Copies the file containing my public SSH key.
- This allows the same key to authenticate as the devops user.

Command:

`sudo chown -R devops:devops /home/devops/.ssh`

Explanation:

- `chown` - change owner.
- Ensures the devops user owns the .ssh directory.
- Required for SSH to accept the key.

Command:

`sudo chmod 700 /home/devops/.ssh`

Explanation:

- `chmod 700` - only the user can read/write/enter the directory.
- SSH rejects directories with weaker permissions.

Command:

`sudo chmod 600 /home/devops/.ssh/authorized_keys`

Explanation:

- Only the owner can read/write the file.
- Prevents other users from reading my authorized SSH keys.

Command (login as devops):

`ssh -i lab01-key.pem devops@PUBLIC_IP`

Same as before but using the new user.

## 3.4 Install Nginx

Command:

`sudo apt update`

Explanation:

- Downloads the list of available package updates from Ubuntu repositories.
- Does NOT install updates - just refreshes info.

Command:

`sudo apt upgrade -y`

Explanation:

- Installs all available package updates.
- `-y` - automatically answers "yes" to prompts.
- Ensures the server is up to date and secure.

Command:

`sudo apt install -y nginx`

Explanation:

- Installs the Nginx web server.
- Ubuntu automatically:
  - downloads Nginx
  - installs it
  - starts the Nginx service
  - enables it on boot

Command:

`sudo systemctl status nginx`

Explanation:

- Shows current service status.
- Returns things like:
  - active (running)
  - PID
  - logs
- Useful to confirm the server is running.

## 3.5 Configure UFW Firewall

Command:

`sudo ufw allow 80/tcp`

Explanation:

- Allows inbound HTTP traffic for Nginx.

Command:

`sudo ufw enable`

Explanation:

- Activates the firewall.
- Prompts:

`Proceed with operation (y|n)?`

Command:

`sudo ufw status verbose`

Explanation:

- Shows active firewall rules and default policies.

## 3.6 SSH Hardening

Command (edit SSH config):

`sudo nano /etc/ssh/sshd_config`

Explanation:

- Opens the SSH server configuration file.
- I modify authentication rules here.


Settings:

- `PermitRootLogin no` - Disables root login (recommended).
- `PasswordAuthentication no` - Disables password logins, only SSH keys allowed.
- `PubkeyAuthentication yes` - Enables key-based access.

Command:

`sudo systemctl restart ssh`

Explanation:

- Restarts SSH service to apply the new configuration.
- Does NOT close current SSH sessions.

## 3.7 Automatic updates

Command:

`sudo apt install -y unattended-upgrades`

Explanation:

- Installs a system package that automatically handles:
  - security patches
  - kernel updates
  - package fixes

Command:

`sudo dpkg-reconfigure --priority=low unattended-upgrades`

Explanation:

- Shows a configuration screen where I choose:

`Enable automatic updates? Yes`

Command:

`sudo systemctl status unattended-upgrades`

Explanation:

- Confirms that the automatic upgrade service is running.

## 3.8 Custom HTML Page

Command:

`echo "<h1>Lab 01 - Cloud Secure Server</h1><p>Created by Samuel</p>" | sudo tee /var/www/html/index.html`

Explanation:

- `echo` - outputs the HTML content.
- `| sudo tee` - writes the content into a file with root permissions.
- File path is the default Nginx web directory.

This generates my custom website homepage.

Command:

`sudo rm /var/www/html/index.nginx-debian.html`

Explanation:

- Removes the default Nginx welcome page so my page becomes the default.

## 3.9 View Logs

Command:

`sudo tail -n 20 /var/log/nginx/access.log`

Explanation:

- `tail -n 20` - shows the last 20 lines.
- `access.log` - contains all HTTP requests to the server.

Great for:
- troubleshooting
- understanding traffic
- security investigations

Command:

`sudo tail -n 20 /var/log/nginx/error.log`

Explanation:

- Shows the last 20 error logs.
- Useful for debugging Nginx issues.

## 3.10 Automation Script

Command:

`sudo nano /usr/local/bin/sysinfo.sh`

Explanation:

- Creates a new script file in /usr/local/bin, which is:
  - reserved for custom executables
  - automatically included in PATH


Script content explanation:


- `#!/bin/bash` - tells the OS to run the script using Bash.
- `echo "=== SYSTEM INFORMATION ==="` - prints a header.
- `echo "Hostname: $(hostname)"` - prints machine hostname.
- `echo "Date: $(date)"` - shows current date/time.
- `echo "Uptime: $(uptime -p)"` - shows how long the system has been running.
- `df -h /` - prints disk usage of the root filesystem.

Command:

`sudo chmod +x /usr/local/bin/sysinfo.sh`

Explanation:

- Makes the script executable.

Command:

`sysinfo.sh`

Explanation:

- Executes the script because /usr/local/bin is in the PATH.

