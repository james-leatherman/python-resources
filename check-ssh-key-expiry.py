import os
from datetime import datetime, timedelta

def check_ssh_key_expiry(ssh_key_path, alert_days=30):
    if os.path.exists(ssh_key_path):
        expiry_date_str = os.popen(f"ssh-keygen -L -f {ssh_key_path} | grep 'Valid:'").read()
        expiry_date_str = expiry_date_str.split("to")[-1].strip()
        expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y")
        days_to_expiry = (expiry_date - datetime.now()).days
        
        if days_to_expiry < alert_days:
            print(f"Warning: SSH key at {ssh_key_path} expires in {days_to_expiry} days.")
        else:
            print(f"SSH key at {ssh_key_path} is valid for {days_to_expiry} more days.")
    else:
        print(f"SSH key at {ssh_key_path} not found.")
if __name__ == "__main__":
    check_ssh_key_expiry("/path/to/your/ssh_key.pub")
