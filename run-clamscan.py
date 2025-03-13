import os

def run_malware_scan(target_path):
    os.system(f"clamscan -r {target_path}")
    print("Malware scan completed.")
if __name__ == "__main__":
    run_malware_scan("/path/to/scan")
