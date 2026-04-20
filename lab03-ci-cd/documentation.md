# Lab 03 — CI/CD Pipeline and Security Scanning Documentation

This document explains the design, logic, and reasoning behind the CI/CD pipeline implemented using GitHub Actions.

---

# Objective

The goal of this lab is to automate the execution and validation of a Python script using a CI pipeline, while integrating basic security scanning.

This simulates a real workflow where code is automatically tested and analyzed on every change.

---

# Key Concepts

## Continuous Integration (CI)

Continuous Integration is the practice of automatically testing and validating code whenever changes are pushed to a repository.

In this lab, CI is implemented using GitHub Actions.

---

## DevSecOps

DevSecOps extends DevOps by integrating security checks into the development pipeline.

In this lab, security is introduced through static code analysis using Bandit.

---

# Pipeline Overview

The pipeline is defined in:

    .github/workflows/python-ci.yml

It is triggered when:

- Code is pushed to the repository
- A pull request is created or updated

---

# Pipeline Execution Flow

The pipeline executes the following steps:

1. Checkout repository
2. Set up Python environment
3. Install security tools
4. Run security scan (Bandit)
5. Execute Python script
6. Validate output
7. Upload artifacts

---

# Step-by-Step Explanation

## 1. Checkout Repository

The pipeline downloads the repository into the runner environment.

This is required so the workflow can access the project files.

---

## 2. Set Up Python

Python is installed using a predefined GitHub Action.

This ensures a consistent runtime environment for the script.

---

## 3. Install Bandit

Bandit is installed using pip:

    pip install bandit

Bandit is a static analysis tool that detects common security issues in Python code.

---

## 4. Run Bandit Security Scan

Bandit scans the Python source code:

    bandit -r lab02-python-automation/src -f json -o security-reports/bandit-report.json

This step:

- analyzes all Python files recursively
- generates a JSON report
- stores the report for later use

---

## 5. Execute Python Script

The pipeline runs the log analyzer:

    python lab02-python-automation/src/log_analyzer.py

This step validates that the script runs successfully in a clean environment.

---

## 6. Validate Output

The pipeline checks if the expected JSON file exists:

    lab02-python-automation/reports/log_summary.json

If the file is missing, the pipeline fails.

This ensures that the script not only runs but also produces the expected output.

---

## 7. Upload Artifacts

Two artifacts are uploaded:

### Log Analysis Report

    lab02-log-summary

Contains the JSON output from the script.

---

### Bandit Security Report

    bandit-security-report

Contains the results of the security scan.

---

# Artifacts and Their Importance

Artifacts allow storing results generated during the pipeline execution.

They are useful for:

- debugging
- auditing
- sharing results
- integrating with other tools

---

# Security Integration

Security scanning is implemented using Bandit.

This allows early detection of:

- insecure function usage
- potential vulnerabilities
- risky coding patterns

Integrating security into CI is a key principle of DevSecOps.

---

# Design Decisions

## Why GitHub Actions?

- Native integration with GitHub
- Easy to configure
- Widely used in real-world environments

---

## Why use a CI pipeline?

- Automates validation
- Reduces manual errors
- Ensures consistency
- Provides fast feedback

---

## Why validate output?

Running a script is not enough.

The pipeline must ensure that the expected result is produced.

---

## Why store artifacts?

Artifacts provide visibility into pipeline results and allow further processing.

---

## Why Bandit?

- Lightweight
- Easy to integrate
- Focused on Python security

---

# Real-World Relevance

This pipeline represents a simplified version of:

- CI/CD pipelines in production environments
- automated testing systems
- security validation workflows
- DevSecOps practices

---

# What I Learned

- How to build a CI pipeline using GitHub Actions
- How to automate code execution
- How to validate outputs in CI
- How to integrate security scanning
- How pipelines simulate real-world environments
- How DevSecOps practices are applied
