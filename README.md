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

                
2) App Deployment

Step 1: Pushing the application to the github repository.

Step 2: Creating the Docker image
        Choose the base image: python:3.9.
        Choosing the work directory where the source code is going to be saved.
        Installing necessary packages for running the app.
        Copying all the files necessary files.
        Installing all the dependencies from the requirements.txt file (requirements.txt stores all the python depencies like kivy).
        Writing the command to start the application.
        Pushing the docker image to to the github repository.

Step 3: Cloning the repository on our EC2 instance using git clone.
        run the command "docker build -t app ." to build the docker container.
        run the container using "docker run -p 8000:8000 app" [8000:8000 for port mapping]

Step 3.1: Adding the inbound traffic rules in our security group of our EC2 instance to allow port 8000.
        Edit inbound rules
        Type : Custom TCP
        Port range: 8000
        CIDR : 0.0.0.0/0


3) CI/CD Pipeline

Step 1: Installing Jenkins using :
        sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
                  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
        echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
                https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
                /etc/apt/sources.list.d/jenkins.list > /dev/null
        sudo apt-get update
        sudo apt-get install jenkins
        Environment="JENKINS_PORT=8081"

Step 2: Installing Java (Since, Jenkins is a Java application):
        sudo apt update
        sudo apt install fontconfig openjdk-17-jre
        java -version
        openjdk version "17.0.13" 2024-10-15
        build 17.0.13+11-Debian-2, mixed mode, sharing

Step 3: Open Jenkins on the IP adress of EC2 instance
        using "sudo cat /var/lib/jenkins/secrets/initialAdminPassword" to get the initial password
        Install Suggested Packages
        Create a new Pipeline Project
        Definition : Pipeline script for SCM
        SCM : Git
        Repository URL : 
        Branch Specifier : */main
        Script Path : 
