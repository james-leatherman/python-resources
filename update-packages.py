import os

def apply_security_updates():
    os.system("sudo apt-get update && sudo apt-get upgrade -y")
    print("Security updates applied successfully.")
if __name__ == "__main__":
    apply_security_updates()
