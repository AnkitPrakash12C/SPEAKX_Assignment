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
        
[image](https://github.com/user-attachments/assets/109eab15-c401-4e73-9d3b-579594f9e393)

        
