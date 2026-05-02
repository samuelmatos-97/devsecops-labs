# Lab 05 — Kubernetes Documentation

This document provides a detailed explanation of the concepts, decisions, and troubleshooting steps involved in running the log analyzer application in Kubernetes.

---

## What is Kubernetes?

Kubernetes is a container orchestration platform used to automate the deployment, scaling, and management of containerized applications.

It allows applications to run reliably across different environments.

---

## Key Concepts

### Pod

A Pod is the smallest deployable unit in Kubernetes.

- It represents a running instance of a container
- It can contain one or more containers
- It shares networking and storage

---

### Container

A container is a lightweight, portable unit that packages an application and its dependencies.

In this lab, the container runs the Python log analyzer.

---

### Job

A Job is a Kubernetes resource used to run **batch processes**.

- It runs a task until completion
- It ensures the task successfully finishes
- It does not restart indefinitely like Deployments

This makes it ideal for scripts or data processing tasks.

---

## Why a Job Instead of a Deployment?

Initially, a Deployment was used to run the application.

However, this caused issues because:

- The application executes and exits
- Deployments expect containers to run continuously

This mismatch caused a:

    CrashLoopBackOff

error.

---

## Problem Encountered

### CrashLoopBackOff

When using a Deployment, the pod entered a CrashLoopBackOff state.

This happens when:

- a container starts
- finishes execution
- Kubernetes restarts it repeatedly

---

## Root Cause

The log analyzer is a **batch application**, not a long-running service.

Kubernetes Deployments are designed for:

- APIs
- web applications
- services that run continuously

---

## Solution

The Deployment was replaced with a Kubernetes Job.

This change:

- allows the container to run once
- stops after completion
- prevents restart loops

---

## Execution Flow

1. Docker image is built (Lab 04)
2. Image is pushed to Docker Hub
3. Kubernetes pulls the image
4. Job creates a Pod
5. Pod runs the Python script
6. Script processes log file
7. Output is generated
8. Pod completes successfully

---

## Output

The application generates a JSON report:

    /app/reports/log_summary.json

It also prints a summary including:

- total requests
- HTTP status distribution
- top endpoints
- suspicious IPs

---

## Verification

The following commands were used:

### Check cluster

    kubectl get nodes

---

### Check job

    kubectl get jobs

---

### Check pods

    kubectl get pods

---

### View logs

    kubectl logs job/log-analyzer-job

---

## Evidences

Screenshots are stored in:

    lab05-kubernetes-basics/evidences/

They demonstrate:

- Kubernetes cluster readiness
- Job execution
- Pod completion
- Application logs
- Troubleshooting (CrashLoopBackOff)

---

## Key Learnings

- Understanding Kubernetes architecture
- Difference between Pods, Jobs, and Deployments
- Handling batch workloads correctly
- Debugging using logs and pod states
- Managing container execution lifecycle

---

## Conclusion

This lab demonstrates how to correctly run a batch application in Kubernetes using a Job.

It highlights the importance of choosing the correct Kubernetes resource based on application behavior.

The transition from Deployment to Job was key to achieving a successful execution.
