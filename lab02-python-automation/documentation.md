# Lab 02 — Python Log Analysis Documentation

This document explains the reasoning, structure, and logic behind the Python script developed in this lab.

---

# Objective

The goal of this lab is to simulate a real-world task:

- Analyze log files
- Extract useful information
- Detect suspicious behavior
- Generate structured reports

---

# Overview

The script (`log_analyzer.py`) reads an Nginx-style log file and processes it to produce meaningful insights.

Instead of just displaying raw logs, the script transforms them into structured and actionable data.

---

# Input Data

The script reads a log file located at:

    data/sample_nginx.log

Each line represents a request and contains:

- IP address
- Timestamp
- HTTP method (GET, POST)
- Endpoint (e.g., /admin)
- HTTP status code (200, 404, 500)

---

# How the Script Works

The script follows a simple pipeline:

## 1. Read the Log File

- The file is read line by line
- This approach is scalable and memory-efficient

---

## 2. Parse Each Line

Each log entry is split into parts to extract:

- IP address → identifies the client
- Endpoint → requested resource
- Status code → response result

---

## 3. Aggregate Data

The script collects:

### HTTP Status Codes

Counts how many times each code appears:

- 200 → successful requests
- 404 → resource not found
- 500 → server error

---

### Endpoints

Tracks how often each endpoint is accessed.

This helps identify:

- popular endpoints
- potentially targeted endpoints

---

### IP Behavior

Tracks how each IP behaves individually.

This enables detecting unusual or suspicious patterns.

---

# Suspicious Activity Detection

The script applies a simple rule:

> Any IP with 3 or more 404 responses is considered suspicious

---

## Why this rule?

Repeated 404 responses may indicate:

- directory scanning
- brute-force attempts
- probing for hidden endpoints

---

## Example

An IP repeatedly requesting `/admin` and receiving 404 responses may be trying to discover an admin panel.

---

# Output

The script generates two types of output:

## 1. Terminal Output

Displays:

- total number of requests
- status code distribution
- most accessed endpoints
- suspicious IPs

---

## 2. JSON Report

File generated:

    reports/log_summary.json

Contains structured data:

- total requests
- status codes
- endpoints
- suspicious IPs

---

# Design Decisions

## Why Python?

- Simple and readable
- Ideal for scripting and automation

---

## Why Dictionaries?

- Efficient for counting and grouping
- Flexible for dynamic keys (IPs, endpoints)

---

## Why JSON?

- Standard format for data exchange
- Easily used by other tools and systems
- Human-readable and machine-readable

---

## Why This Structure?

The project is organized as:

- `src/` → code
- `data/` → input logs
- `reports/` → generated output
- `evidence/` → screenshots

This reflects real-world project organization.

---

# Real-World Relevance

This script simulates a simplified version of:

- log analysis systems
- SIEM tools
- security monitoring pipelines
- automated detection systems

---

# What I Learned

- How to parse and analyze logs
- How to extract meaningful data
- How to detect suspicious behavior
- How to automate analysis with Python
- How to generate structured reports
- How to organize a project

