import ssl
import socket

from datetime import datetime
def check_ssl_certificate_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as conn:
        with context.wrap_socket(conn, server_hostname=domain) as sock:
            cert = sock.getpeercert()
            expiry_date = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y GMT")
            days_to_expiry = (expiry_date - datetime.now()).days
            if days_to_expiry < 30:
                print(f"Warning: SSL certificate for {domain} expires in {days_to_expiry} days.")
            else:
                print(f"SSL certificate for {domain} is valid for {days_to_expiry} more days.")
if __name__ == "__main__":
    check_ssl_certificate_expiry("website.com")
