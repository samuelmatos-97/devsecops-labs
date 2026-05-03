# Lab 06 – Terraform Infrastructure as Code Documentation

---

## Introduction

This document provides a detailed explanation of the steps followed in **Lab 06 – Terraform IaC**, including setup, execution, and troubleshooting.

The goal of this lab is to provision and manage AWS infrastructure using Terraform.

---

## Environment Setup

### 1. AWS CLI Installation

The AWS CLI was installed and verified using:

```id="cmd1"
aws --version
```

---

### 2. IAM User Creation

An IAM user named:

```id="cmd2"
terraform-user
```

was created with the following configuration:

* Programmatic access enabled via **Access Keys**
* Permission policy: `AdministratorAccess`

---

### 3. AWS CLI Configuration

The CLI was configured using:

```id="cmd3"
aws configure
```

Inputs:

* AWS Access Key ID
* AWS Secret Access Key
* Region: `eu-west-1`
* Output format: `json`

---

### 4. Verification

The configuration was validated with:

```id="cmd4"
aws sts get-caller-identity
```

This confirmed successful authentication with AWS.

---

## Terraform Setup

### 1. Installation

Terraform was installed using:

```id="cmd5"
winget install Hashicorp.Terraform
```

---

### 2. Verification

```id="cmd6"
terraform -version
```

---

## Project Configuration

The Terraform configuration file:

```id="cmd7"
main.tf
```

contains:

* AWS provider configuration
* EC2 instance resource definition

---

## Execution Steps

### 1. Initialize Terraform

```id="cmd8"
terraform init
```

This downloads the required AWS provider and initializes the working directory.

---

### 2. Generate Execution Plan

```id="cmd9"
terraform plan
```

Terraform displays the resources that will be created:

```id="cmd10"
Plan: 1 to add, 0 to change, 0 to destroy.
```

---

### 3. Apply Configuration

```id="cmd11"
terraform apply
```

Confirmation required:

```id="cmd12"
yes
```

Terraform creates the EC2 instance.

---

### 4. Validate Resource Creation

The instance was verified in:

* AWS Console → EC2 → Instances

Status:

```id="cmd13"
Running
```

---

### 5. Destroy Infrastructure

```id="cmd14"
terraform destroy
```

Confirmation:

```id="cmd15"
yes
```

Result:

```id="cmd16"
Destroy complete! Resources: 1 destroyed.
```

---

## Troubleshooting

### Terraform not recognized

**Error:**

```id="err1"
terraform is not recognized
```

**Cause:**
Terraform not installed or not in PATH.

**Solution:**

* Install using `winget` or manually
* Restart terminal after installation

---

### AWS CLI not recognized

**Error:**

```id="err2"
aws is not recognized
```

**Cause:**
AWS CLI not installed or PATH not configured.

**Solution:**

* Install AWS CLI
* Restart terminal

---

### Invalid AMI ID

**Error:**

```id="err3"
InvalidAMIID.NotFound
```

**Cause:**
AMI not available in selected region.

**Solution:**

* Use a valid AMI for `eu-west-1`
* Example:

```id="cmd17"
ami = "ami-08f9a9c699d2ab3f9"
```

---

### Permission Issues

**Error:**

```id="err4"
UnauthorizedOperation
```

**Cause:**
IAM user lacks permissions.

**Solution:**

* Attach `AdministratorAccess` policy

---

### Forgot to destroy resources

**Impact:**

* AWS costs may be incurred

**Solution:**

```id="cmd18"
terraform destroy
```

---

## Key Learnings

* Infrastructure as Code (IaC) fundamentals
* Terraform lifecycle management
* AWS IAM and access control
* Resource provisioning and cleanup
* Importance of avoiding manual changes outside Terraform

---

## Conclusion

This lab successfully demonstrated how to automate cloud infrastructure provisioning using Terraform.

It highlights best practices such as:

* Using IAM users instead of root
* Managing infrastructure through code
* Cleaning up resources to prevent costs
