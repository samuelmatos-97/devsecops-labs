# Lab 04 — Docker Containerization Documentation

This document explains the design, concepts, and reasoning behind containerizing the Python log analyzer using Docker.

---

# Objective

The goal of this lab is to package an existing Python application into a Docker container to ensure consistent and reproducible execution across different environments.

---

# Key Concepts

## Containerization

Containerization allows applications to run in isolated environments that include all required dependencies.

This ensures that the application behaves the same regardless of the system where it is executed.

---

## Docker

Docker is a platform that enables building, running, and managing containers.

It uses images as templates to create containers.

---

## Docker Image

A Docker image is a blueprint that defines:

- the base operating system
- installed dependencies
- application code
- execution instructions

---

## Docker Container

A container is a running instance of an image.

It is lightweight and isolated from the host system.

---

## Build Context

The build context defines the set of files that Docker can access during the build process.

When running:

    docker build .

Docker can only access files inside the current directory.

Attempting to copy files outside this context will result in an error.

---

## Common Issue — Docker Build Context

During the build process, an error occurred when attempting to copy files from outside the build context:

    COPY ../lab02-python-automation/src ./src

This resulted in a failure because Docker cannot access files outside the build context.

### Solution

The build was executed from the repository root using:

    docker build -t log-analyzer -f lab04-docker-containerization/Dockerfile .

This allowed Docker to access all required files.

### Key Takeaway

Docker can only access files within the build context.
Understanding this is critical when structuring projects.

---

# Dockerfile Explanation

The Dockerfile defines how the image is built.

---

## Base Image

    FROM python:3.11-slim

This specifies the base environment.

- Python 3.11 is used for compatibility
- The "slim" variant reduces image size

---

## Working Directory

    WORKDIR /app

Sets the working directory inside the container.

All subsequent commands are executed relative to this path.

---

## Copy Application Files

    COPY ./lab02-python-automation/src ./src
    COPY ./lab02-python-automation/data ./data

Copies source code and data into the container.

These paths are valid because the build is executed from the repository root.

---

## Create Reports Directory

    RUN mkdir -p reports

Creates a directory where output files will be stored.

---

## Execution Command

    CMD ["python", "src/log_analyzer.py"]

Defines the default command executed when the container starts.

---

# Execution Flow

1. Build the image
2. Start a container
3. Execute the Python script
4. Process log data
5. Generate a JSON report

---

# Container Behavior

Containers are ephemeral by default.

This means:

- data created inside the container is not persisted
- once the container stops, the data is lost

---

# Data Persistence with Volumes

To persist data, Docker volumes are used.

Example:

    docker run -v <host_path>:/app/reports log-analyzer

This maps a directory from the host machine to the container.

---

## How It Works

| Host System | Container |
|------------|----------|
| reports/   | /app/reports |

The container writes output directly to the host.

---

# Why Volumes Are Important

- preserve data after container stops
- allow data sharing between host and container
- enable debugging and inspection
- support real-world workflows

---

# Design Decisions

## Why Docker?

- ensures environment consistency
- simplifies deployment
- reduces dependency issues

---

## Why use a slim image?

- smaller size
- faster builds
- reduced attack surface

---

## Why run from repository root?

To ensure Docker has access to all required files within the build context.

---

## Why not copy files manually?

Manual copying breaks scalability and automation.

Using proper build context ensures reproducibility.

---

# Real-World Relevance

This lab simulates real-world scenarios where applications are containerized before deployment.

It prepares for:

- container orchestration (Kubernetes)
- CI/CD integration
- scalable deployments

---

# What I Learned

- how Docker images are built
- how containers execute applications
- the importance of build context
- how to persist data using volumes
- how containerization improves consistency
