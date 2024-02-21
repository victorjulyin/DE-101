# First touch of AWS and Azure

## EC2 (Virtual Machine) instance creation

### It works according to this model
What we have:
  * VPC (virtual private cloud) - virtual network, dedicated to the AWS account.
    * Subnets - a range of IP addresses in your VPC
      * Public Subnet - connecting to the internet
      * Private Subnet - we can connect to it from the Public Subnet
    * Availability Zone - it is a place where servers actually located
    * Internet Gateway - just an internet connection
    * Route Tables - traffic rules
    * CIDR - it is used when we want to use a range of IP's (ours is "/16") 
  * SSH - secure shell protocol
<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_model1.png"></p>



### First of all we need to make sure that we have a VPC.

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_vpc1.png"></p>

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_vpc2.png"></p>



### Launching process

1) *Application and OS Images (Amazon Machine Image)* - choose an OS
2) *Instance type* - instance's performance
3) *Network settings* - choose a VPC, change Subnet, security settings
4) *Advanced details* - IAM (access roles) and different settings (SSH)
5) *Key pair* - very important. Access key to connect to the VM by SSH. 

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_ec2_1.png"></p>


### Now we can try to connect to our VM

#### Try
via command (for Mac):
  ssh -i /path/to/private-key root@<ec2-public-dns-address>

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_t1.png"></p>


#### Doesn't work:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_t2.png"></p>


#### We must protect the public key:
  chmod 600 vjulyin.pem

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2%20Introduction%20to%20cloud%20computing/pics/5.2_t3.png"></p>





## Azure Virtual Machine

  * Details:
    * Subscirptions - payment account that you can add to your resources
    * Resource Group - just grupped resources

