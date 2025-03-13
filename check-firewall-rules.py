import subprocess

def check_firewall_rules(required_rules):
    result = subprocess.getoutput("iptables -L")
    for rule in required_rules:
        if rule not in result:
            print(f"Warning: Firewall rule '{rule}' is missing.")
        else:
            print(f"Firewall rule '{rule}' is present.")
if __name__ == "__main__":
    rules = ["ACCEPT tcp -- anywhere anywhere tcp dpt:ssh", 
             "ACCEPT udp -- anywhere anywhere udp dpt:53"]
    check_firewall_rules(rules)
