# Week 4 Assignment

## Part I

In this part I'll use text description to describe my design after applying SOA for the ATM machine(along with small part of the bank side) as in next part a detailed diagram with layers and components will be shown in detail.

During previous week, the main focus of my design is trying to get a basic understanding of different architecture style. From my point of view, each of them has advantages in some parts while disadvantages in other parts. The result of my analysis is quite interesting. The reason why these happen is that all of the architecture styles focus on a specific problem, and try to solve them with a perfect design. Though each component is self-contained with complete functionality, they don't have a common way to communicate which makes reuse a difficult task(especially for different logic).

SOA use a different approach to solve this problem. Separating different functionality into different service and set different categories for different services(e.g. IT services, Business services, etc). Different services communicate with each other by a universal protocol thus it is flexible to reorganize as well as reuse. As it is, I'll refine my design based using SOA and create different services instead of different components. What's more, the communications and interactions among different services are no long predefine but using configuration file to customize without changing the code.

### Business Services

Business Services are services that serve the business model. Most people know CRM, SCM, ERP and HCM but it seems that they are not what we need in this part. So here are the business services in my design and basic description:

+ User Validation Service: Validate the basic information from the user such as password
+ Card/Check Validation Service: Validate the credit card as well as the Check
+ Query Service: Provide interface for user query
+ Transfer Service: Provide interface for tranfer
+ Deposit Service: Provide interface for deposit
+ Exception Handling Service: Handling common exceptiong, e.g. broken evolope
+ Printing Service: Provide interface for printing 

### Reusable Services

As I turn most of the components to services, most of them can be reused in bank side:

+ Card/Check Validation Service
+ Query Service
+ Transfer Service
+ Deposit Service
+ Printing Service

More detail can be seen in the next part

## Part II

Here is my design:

![atm_soa](media/atm_soa.png)

The horizontal and vertical layers are shown in the diagram above.

Actually I only draw the core services for my design. There are lots of sub-services that are not shown in the diagram.


