# EC2 in VPC (public and private)

#### The plan

  * [Introduction](#introduction)
  * [Solution](#solution)
    * [VPC creation](#step-1-vpc-creation)
    * [Subnets creation](#step-2-privat-and-public-subnets-creation)
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

### Step 2: Privat and Public subnets creation






<p align="center"><img  src="_"></p>

![](https://github.com/victorjulyin/DE-101/blob/main/Module5/5.2.1%20EC2%20in%20VPC%20(public%20and%20private)/pics/lab1.png)
