# EC2 in VPC (public and private)

#### The plan

  * [Introduction](#introduction)
  * [Solution](#solution)
    * [VPC creation](#step-1-vpc-creation)
    * [Subnets creation](#step-2-private-and-public-subnets-creation)
    * to




## Introduction
We'll create a VPC, subnets in different availability zones, routes, internet gateway, and add a security group. 
These services are the base of the AWS architecture.

## Solution

### Solution diagram






### Step 1: VPC creation

1) Authorize in an AWS Management Console.

2) Choose a region.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab1.png" width=25% height=25%>

3) Find **vpc** by the search string

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab2.png" width=80% height=80%>

4) Push **Create VPC**

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab3.png" width=80% height=80%>

5) Insert these data to create VPC

    * *Name tag:* **HoLVPC**
    * *IPv4 CIDR block:* **10.0.0.0/16**
    * *IPv6 CIDR block:* **No IPv6 CIDR block**
    * *Tenancy:* **Default**
    * *Key:* **Name**
    * *Value - optional:* **HoLVPC**

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab4.png" width=80% height=80%>

6) Push **Create VPC**

### Step 2: Private and Public subnets creation

1) Push **Subnets** in the left menu. Then push **Create subnet**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab5.png" width=35% height=35%>


2) Choose created VPC and insert data:

    * *Subnet name:* **sn-public-a**
    * *Availability Zone:* **choose any option**
    * *IPv4 CIDR block:* **10.0.1.0/24**

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab6.png" width=60% height=60%>


3) Push **Create subnet**. You created a public subnet.

4) To create a private subnet, push **Create subnet** again.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab7.png" width=60% height=60%>

5) Choose the same VPC as in the public subnet and insert data:

    * *Subnet name:* **sn-private-b**
    * *Availability Zone:* **should be different from the one selected for your public subnet**
    * *IPv4 CIDR block:* **10.0.2.0/24**

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab8.png" width=60% height=60%>  

6) Push **Create subnet**.


### Step 3: Routes creation and internet gateway setup

1) Go to the **Route tables** in the left menu.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab9.png" width=35% height=35%>  

2) Go to the **Routes** tab to see existing routes.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab10.png" width=60% height=60%>  

3) Push **Subnet Associations** to check subnets associated with this Route table.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab11.png" width=60% height=60%>  


4) Now go to **Subnets**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab12.png" width=35% height=35%>  

5) Choose a public subnet **sn-public-a**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab13.png" width=35% height=35%>

6) Go to **Actions** => **Edit subnet settings**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab14.png" width=35% height=35%>

7) Choose the **Enable auto-assign public IPv4 address**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab15.png" width=50% height=50%>

8) Push **Save**

9) To create an internet gateway go to **Internet gateways** in the left menu.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab16.png" width=35% height=35%>

10) Push **Create internet gateway** on the right and insert **hol-VPCIGW** to the *Name tag* field.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab17.png" width=50% height=50%>

11) Push **Create internet gateway** on the bottom.

12) Choose created internet gateway, go to **Actions** => **Attach to VPC**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab18.png" width=50% height=50%>

13) Add **HoLVPC** and push **Attach intenet gateway**. We connected the internet gateway to our VPC.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab19.png" width=50% height=50%>

14) Now we'll create a route table. Go to **Route tables** in the left menu. 

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab20.png" width=35% height=35%>

15) Push **Create route table** and insert this data:

    * *Name Tag*: **publicRT**
    * *VPC*: **HoLVPC**

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab21.png" width=50% height=50%>

16) Push **Create route table** in the bottom. 

17) Choose only **publicRT**. Go to tab **Routes** => push **Edit routes**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab22.png" width=50% height=50%>

18) Push **Add route** and insert this data:

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab23.png" width=50% height=50%>


    * *Destination*: **0.0.0.0/0**
    * *Target*: Select **Internet Gateway**  =>  **hol-VPCIGW**

19) Push **Save changes**.

20) Choose only **publicRT** => go to tab **Subnet associations** in the bottom => push **Edit subnet associations**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab24.png" width=50% height=50%>

21) Choose **sn-public-a** and push **Save changes**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab25.png" width=50% height=50%>

22) Go to **Subnets** in the left menu. Choose any subnet and go to **Route table** tab in the bottom to see an updated route table.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab26.png" width=50% height=50%>

### Step 4: Launching the EC2 in the public subnet

1) Go to **EC2** with the search string.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab27.png" width=50% height=50%>

2) Push **Launch instances**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab28.png" width=50% height=50%>

3) Choose these options:

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab29.png" width=50% height=50%>

4) Choose this option and push **Create new key pair**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab30_1.png" width=50% height=50%>

5) Insert **public-a-key** as a **Key pair name**. 

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab30_2.png" width=50% height=50%>

6) Push **Create key pair** to download the key. Make sure, that it is available and in a safe place.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab31.png" width=50% height=50%>

7) Choose these options:

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab32.png" width=50% height=50%>

    * *Number of Instances:* **1**
    * *Network:* **HoLVPC**
    * *Subnet:* **sn-public-a**
    * *Auto-assign Public IP:* **Use subnet setting (Enable)**
    * *Firewall:*
      * **Create a new security group**
      * *Security group name:* holpubSG
      * *Description:* holpubSG

8) Push **Launch instance** in the right menu.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab33.png" width=35% height=35%>


### Step 5: Launching the EC2 in the private subnet

1) Push **Launch instances**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab28.png" width=50% height=50%>

2) Choose these options:

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab29.png" width=50% height=50%>

3) Choose this option and push choose existing **public-a-key**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab34.png" width=50% height=50%>


4) Choose these options:

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab35.png" width=50% height=50%>

    * *Number of Instances:* **1**
    * *Network:* **HoLVPC**
    * *Subnet:* **sn-private-b**
    * *Auto-assign Public IP:* **Use subnet setting (Enable)**
    * *Firewall:*
      * **Create a new security group**
      * *Security group name:* holprivSG
      * *Description:* holprivSG
      * *Security group rule:*
        * *Type:* **SSH**
        * *Protocol:* **TCP**
        * *Port Range:* **22**
        * *Source:* **Custom 10.0.1.0/24**

5) Push **Launch instance** in the right menu.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab33.png" width=35% height=35%>


### Step 6: Connecting to the public EC2 by SSH

