# Lab 06 – Terraform Infrastructure as Code (IaC)

## Overview

This lab demonstrates how to provision cloud infrastructure using **Terraform** on **AWS**.

The goal is to create, manage, and destroy infrastructure using code, following Infrastructure as Code (IaC) principles.

In this lab, an **EC2 instance** is created and later destroyed using Terraform.

---

## Objectives

* Configure AWS CLI with IAM user credentials
* Install and configure Terraform
* Create infrastructure using Terraform
* Validate infrastructure using AWS Console
* Destroy infrastructure to avoid unnecessary costs

---

## Project Structure

```
devsecops-labs/
│
├── lab02-python-automation/
├── lab04-docker-containerization/
├── lab05-kubernetes-basics/
├── lab06-terraform-iac/
│   ├── main.tf
│   ├── README.md
│   ├── documentation.md
│   └── evidences/
```

---

## Technologies Used

* **Terraform**
* **AWS (EC2)**
* **AWS CLI**
* **IAM (Identity and Access Management)**

---

## Terraform Configuration

### Provider Configuration

```
provider "aws" {
  region = "eu-west-1"
}
```

### EC2 Instance Resource

```
resource "aws_instance" "lab06_instance" {
  ami           = "ami-08f9a9c699d2ab3f9"
  instance_type = "t2.micro"

  tags = {
    Name = "lab06-terraform-instance"
  }
}
```

---

## Execution Steps

### 1. Initialize Terraform

```
terraform init
```

---

### 2. Review Execution Plan

```
terraform plan
```

Expected output:

```
Plan: 1 to add, 0 to change, 0 to destroy.
```

---

### 3. Apply Configuration (Create Infrastructure)

```
terraform apply
```

Confirm with:

```
yes
```

Expected result:

```
Apply complete! Resources: 1 added
```

---

### 4. Validate in AWS

* Go to **AWS Console → EC2 → Instances**
* Confirm instance:

  * Name: `lab06-terraform-instance`
  * State: `Running`

---

### 5. Destroy Infrastructure

```
terraform destroy
```

Confirm with:

```
yes
```

Expected result:

```
Destroy complete! Resources: 1 destroyed.
```

---

## Important Notes

* Always destroy resources after testing to avoid AWS charges
* Do not delete resources manually from AWS when using Terraform
* Terraform maintains state and must control the lifecycle

---

## Key Concepts Learned

* Infrastructure as Code (IaC)
* Terraform workflow (`init`, `plan`, `apply`, `destroy`)
* AWS resource provisioning
* IAM user and access keys
* State management and lifecycle control

---

## Related Labs

* Lab 02 – Python Automation
* Lab 04 – Docker Containerization
* Lab 05 – Kubernetes Basics

---

## Evidences

Screenshots are available in the `evidences/` directory, including:

* Terraform initialization
* Terraform plan
* Terraform apply
* Terraform destroy
* AWS EC2 instance (running and terminated)

---

## Conclusion

This lab successfully demonstrates how to manage cloud infrastructure using Terraform.

It highlights the power of automation, reproducibility, and proper lifecycle management in modern DevSecOps workflows.
