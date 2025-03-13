import os

def run_vulnerability_scan(target_ip, report_path):
    command = f"openvas-cli scan --target {target_ip} --output {report_path}"
    os.system(command)
    print(f"Vulnerability scan completed. Report saved to {report_path}")
if __name__ == "__main__":
    target_ip = "192.168.1.1"
    report_path = "/path/to/vulnerability_report.xml"
    run_vulnerability_scan(target_ip, report_path)
