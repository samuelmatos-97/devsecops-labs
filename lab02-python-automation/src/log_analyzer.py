# pathlib is used to work with files and folders in a clean way
from pathlib import Path
# defaultdict is a special type of dictionary
# It automatically creates a default value when a key does not exist yet
# Useful for counters
from collections import defaultdict
# json is used to export the final analysis into a JSON file
import json

# BASE_DIR represents the root folder of this lab
# __file__ is the current Python file
# .resolve() gets the full path
# .parent gets the folder of this file (src/)
# .parent.parent goes deeper (lab02-python-automation/)
BASE_DIR = Path(__file__).resolve().parent.parent
# Define path to input log file
LOG_FILE = BASE_DIR / "data" / "sample_nginx.log"
# Define output directory and report file
REPORTS_DIR = BASE_DIR / "reports"
REPORT_FILE = REPORTS_DIR / "log_summary.json"


def main():
    print(f"[INFO] Using log file: {LOG_FILE}")

    # Check if log file exists before proceeding
    if not LOG_FILE.exists():
        print("[ERROR] Log file not found.")
        return

    # Ensure reports directory exists (create if missing)
    REPORTS_DIR.mkdir(exist_ok=True)

    # Total number of log entries
    total_lines = 0
    # Count how many times each HTTP status appears
    status_codes = defaultdict(int)
    # Count status codes per IP
    ip_status_counts = defaultdict(lambda: defaultdict(int))
    # Count how many times each endpoint is accessed
    endpoint_counts = defaultdict(int)
    # Track endpoints accessed by IPs that trigger 404s
    suspicious_activity = defaultdict(list)

    # Open and read the log file line by line
    with LOG_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip() # Remove whitespaces/newlines
            if not line:
                continue # Skip empty lines

            total_lines += 1
            # Split log line into components
            parts = line.split()

            try:
                # Extract relevant fields based on log format
                ip_address = parts[0] # Client IP
                endpoint = parts[6] # Requested path (/admin, /login, etc.)
                status_code = parts[8] # HTTP response code

                # Update global counters
                status_codes[status_code] += 1
                endpoint_counts[endpoint] += 1
                # Update per IP tracking
                ip_status_counts[ip_address][status_code] += 1

                # Track suspicious behavior (404 responses)
                if status_code == "404":
                    suspicious_activity[ip_address].append(endpoint)

            except IndexError:
                # Handle malformed log lines
                print(f"[WARNING] Failed to parse line: {line}")

    # Detect suspicious IPs based on rule: 3 or more 404 responses
    suspicious_ips = []

    for ip, codes in ip_status_counts.items():
        if codes["404"] >= 3:
            suspicious_ips.append(
                {
                    "ip_address": ip,
                    "404_count": codes["404"],
                    "targeted_endpoints": sorted(set(suspicious_activity[ip])),
                }
            )

    # Prepare structured report data
    report_data = {
        "total_requests": total_lines,
        "status_codes": dict(status_codes),
        "top_endpoints": dict(sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True)),
        "suspicious_ips": suspicious_ips,
    }

    print("\nLog Summary:")
    print(f"Total requests: {total_lines}\n")

    for code, count in sorted(status_codes.items()):
        print(f"Status {code}: {count} requests")

    print("\nTop Endpoints:")
    for endpoint, count in sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{endpoint}: {count} requests")

    print("\nSuspicious IPs (3 or more 404 responses):")
    if suspicious_ips:
        for item in suspicious_ips:
            print(f"- {item['ip_address']} -> {item['404_count']} x 404 responses")
            print(f"  Targeted endpoints: {', '.join(item['targeted_endpoints'])}")
    else:
        print("No suspicious IPs detected.")

    # Wirte JSON report to file
    with REPORT_FILE.open("w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)

    print(f"\n[INFO] JSON report generated: {REPORT_FILE}")

# Entry point of the script
if __name__ == "__main__":
    main()
