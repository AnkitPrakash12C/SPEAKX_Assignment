# SPEAKX_Assignment
An assignment which covers the use of various devops tools for deploying the application.

1) Provisioning the Infrastructure as Code (IaC) using AWS management console:

Step 1: Creating an IAM (Identity and Access Management) user SPEAKX. 
        Provide it full access to resources like EC2 (Elastic Compute Cloud), S3 (Simple Storage Service) and VPC (Virtual Private Cloud).

Step 2: Signing-in as the IAM User SPEAKX just created.

Step 3: Creating VPC with name tag SPEAKX.
        IPV4 CIDR : 10.0.0.0/16 (It provisions 65,536 IPs)
        VPC ID : vpc-0f50ecb973c0fd3c5

Step 4: Creating Subnets
        Public Subnet : SPEAKX_Public
        VPC ID : vpc-0f50ecb973c0fd3c5
        Availability Zone (AZ) : Asia Pacific (Mumbai) / ap-south-1a
        IPv4 subnet CIDR block : 10.0.1.0/24
        Subnet ID : subnet-0179dc4bc7ede3154
        Route table ID : rtb-0e49681446eaa7eb3

Step 5: Creating Internet Gateways
        Name : SPEAKX_Public_IG
        Internet gateway ID : igw-077189c15339b984a
        Attach to VPC : vpc-0f50ecb973c0fd3c5
        
![image alt](https://github.com/AnkitPrakash12C/SPEAKX_Assignment/blob/5ff5d659c9490a1ac2413482ac80046e0a32fff5/VPC_Map.PNG)

Step 6: Creating Route Table
        Name : SPEAKX_Public_RT
        VPC : vpc-0f50ecb973c0fd3c5
        Associate Subnets : SPEAKX_Public

Step 7: Creating NAT Gateways
        Name : SPEAKX_NG
        Subnet : SPEAKX_Public
        Allocate Elastic IP
        NAT gateway ID : nat-035476974c69dbb2e

Step 8: Creating EC2 instances
        Name : SPEAKX_EC2
        Amazon Machine Image (AMI) : Ubuntu
        Instance type : t2.micro
        Create new key pair : SPEAKX_Public_Secret, 
        type : RSA, 
        Private key file format : .pem
        Network Settings :
                VPC : SPEAKX
                Subnet : SPEAKX_Public
                Auto-assign public IP : Enable
                Security Group Name : SPEAKX_Public_SG
                Inbound Security Group Rules : 
                        Add HTTP : 0.0.0.0/0 (CIDR)
                        Add HTTPs : 0.0.0.0/0 (CIDR)
                        
        Instance ID : i-0e55e7d177cf12420
        Public IPv4 address : 13.233.112.240

Step 9: Edit routes in the route table
        Add route : 0.0.0.0/0 (Destination), 
        Internet Gateway : igw-077189c15339b984a (Target)

Step 10 : Connecting to Public EC2 instance
          Connect to instance
          Run : chmod 400 "SPEAKX_Public_Secret.pem"
          Run : ssh -i "SPEAKX_Public_Secret.pem" ubuntu@13.233.112.240

                

        
        
        

        
