# Lab 07 — DevSecOps Pipeline Documentation

---

## Introduction

This document explains the implementation and architecture of the DevSecOps pipeline created in Lab 07.

The pipeline integrates automation, security scanning, container validation, and artifact management using GitHub Actions.

---

## Purpose of the Pipeline

The main objective of this pipeline is to automate security and validation tasks during the software development lifecycle.

The workflow ensures that:

- Python code is validated automatically
- Security scanning is executed
- Docker builds are tested
- Reports are generated and stored

---

## Technologies Used

- GitHub Actions
- Python 3.13
- Bandit
- Docker
- GitHub Artifacts

---

## DevSecOps Concepts

### CI/CD

CI/CD stands for:

- Continuous Integration
- Continuous Delivery / Deployment

The pipeline automatically validates code changes whenever code is pushed to the repository.

---

### DevSecOps

DevSecOps integrates security into the DevOps lifecycle.

Instead of performing security checks manually at the end of development, security validation becomes part of the automated pipeline.

---

### SAST (Static Application Security Testing)

Bandit performs static security analysis on Python code.

It scans source files looking for:

- insecure functions
- hardcoded credentials
- weak cryptography
- unsafe patterns

---

## Workflow Structure

The workflow file:

    .github/workflows/devsecops-pipeline.yml

contains:

- workflow triggers
- jobs
- execution steps

---

## Workflow Triggers

The pipeline executes automatically on:

    push
    pull_request

for changes related to:

- Lab 02
- Lab 04
- workflow configuration

This avoids unnecessary executions when unrelated files change.

---

## Pipeline Stages

### 1. Repository Checkout

    uses: actions/checkout@v6

This downloads the repository into the GitHub Actions runner.

---

### 2. Python Setup

    uses: actions/setup-python@v6

Installs Python 3.13 inside the runner environment.

---

### 3. Install Bandit

    pip install bandit

Installs the Bandit security scanner.

---

### 4. Security Scan

    bandit -r lab02-python-automation/src

Scans all Python source files recursively.

The generated report is stored as JSON.

---

### 5. Execute Python Application

    python lab02-python-automation/src/log_analyzer.py

Runs the log analyzer application.

---

### 6. Validate JSON Output

The workflow checks whether:

    log_summary.json

was successfully generated.

If the file is missing, the pipeline fails.

---

### 7. Docker Build Validation

    docker build -t log-analyzer:ci -f lab04-docker-containerization/Dockerfile .

This validates that the Docker image can be successfully built during CI execution.

---

### 8. Artifact Upload

The workflow uploads:

- JSON log analysis report
- Bandit security report

These artifacts can be downloaded directly from GitHub Actions.

---

## Generated Artifacts

### Log Analysis Report

Artifact:

    lab07-log-summary

Contains:

- request statistics
- endpoint analysis
- suspicious IP detection

---

### Security Report

Artifact:

    lab07-bandit-security-report

Contains:

- Bandit findings
- severity levels
- security recommendations

---

## Pipeline Validation

The workflow was validated successfully with:

- successful GitHub Actions execution
- successful Docker build
- generated artifacts
- completed security scan

---

## Troubleshooting

### YAML Validation Errors

Issue:
VS Code displayed schema validation errors.

Cause:
GitHub Actions schema was not automatically detected.

Solution:
Add schema definition:

    # yaml-language-server: $schema=https://json.schemastore.org/github-workflow.json

---

### Missing JSON Report

Issue:
Pipeline failed because the JSON report did not exist.

Solution:
A validation step was added to ensure the report is generated correctly.

---

### Docker Build Failures

Possible causes:

- incorrect Dockerfile path
- missing build context
- missing source files

Solution:
Use:

    docker build -t log-analyzer:ci -f lab04-docker-containerization/Dockerfile .

from the repository root.

---

## Key Learnings

- GitHub Actions workflow design
- CI/CD automation
- DevSecOps principles
- Security scanning integration
- Docker validation in pipelines
- Artifact generation and storage
- YAML workflow structure

---

## Conclusion

This lab demonstrates how DevSecOps practices can be integrated into an automated CI/CD workflow.

The pipeline combines:

- automation
- security
- validation
- containerization
- reporting

into a single reproducible process.

This approach improves software quality, consistency, and security throughout the development lifecycle.
