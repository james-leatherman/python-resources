import re

def analyze_logs(log_file, keywords):
    with open(log_file, "r") as file:
        for line in file:
            for keyword in keywords:
                if re.search(keyword, line):
                    print(f"Security alert: {line.strip()}")
if __name__ == "__main__":
    log_file = "/var/log/syslog"
    security_keywords = ["failed password", "unauthorized access", "error"]
    analyze_logs(log_file, security_keywords)
