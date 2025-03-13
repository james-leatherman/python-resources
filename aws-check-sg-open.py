import boto3

def check_security_group_rules():
    ec2 = boto3.client("ec2")
    security_groups = ec2.describe_security_groups()["SecurityGroups"]
    
    for sg in security_groups:
        for permission in sg["IpPermissions"]:
            for ip_range in permission.get("IpRanges", []):
                if ip_range["CidrIp"] == "0.0.0.0/0":
                    print(f"Warning: Security group {sg['GroupName']} has an open rule.")
                    
if __name__ == "__main__":
    check_security_group_rules()
