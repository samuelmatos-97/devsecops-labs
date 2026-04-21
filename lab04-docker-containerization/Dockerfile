# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy script and data from Lab 02
COPY ../lab02-python-automation/src ./src
COPY ../lab02-python-automation/data ./data

# Create reports directory
RUN mkdir -p reports

# Run the script
CMD ["python", "src/log_analyzer.py"]
