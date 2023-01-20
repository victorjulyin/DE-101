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


### Step 3: Routes creation and internet gateway setup

1) Go to the **Route tables** in the left menu.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab9.png" width=60% height=60%>  

2) Go to the **Routes** tab to see existing routes.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab10.png" width=60% height=60%>  

3) Push **Subnet Associations** to check subnets associated with this Route table.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab11.png" width=60% height=60%>  


4) Now go to **Subnets**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab12.png" width=35% height=35%>  

5) Choose a public subnet **sn-public-a**.

    <img src="https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab13.png" width=35% height=35%>