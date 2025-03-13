import re

def monitor_login_attempts(auth_log):
    with open(auth_log, "r") as file:
        for line in file:
            if "Failed password" in line or "Invalid user" in line:
                print(f"Suspicious login attempt: {line.strip()}")
if __name__ == "__main__":
    monitor_login_attempts("/var/log/auth.log")
