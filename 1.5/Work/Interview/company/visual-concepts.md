# Visual Concepts

<!-- MarkdownTOC -->

- Programming Challenge: Imperial Messengers
    - Requirements
    - Problem
    - Input
    - Output
    - Sample Input
    - Output for the Sample Input
    - 解题思路
- Wiki
- NBA 2K Title
- Top 21 Interviewing Questions
- 他人面试经历

<!-- /MarkdownTOC -->

## Programming Challenge: Imperial Messengers

### Requirements

Code must be ANSI Standard C, to allow for easy testing. Read input from standard in and write output to standard out. Please write the code entirely from scratch, without referencing any sources for code or algorithms (referencing a C manual for syntax is fine). Please keep track of the amount of time you spend on the solution and include that with your solution. Your coding style should reflect your average professional work, don’t just hack together a solution so that you can say you finished it quickly. If you considered algorithms other than the one you wound up using, briefly describe them in your documentation. Please submit the source code for your solution as a .c file.

### Problem

The empire has a number of cities. For communicating important messages from the capitol to other cities, a network of messengers is going to be set up. Some number of messengers will be stationed in the capitol city. Each messenger will ride to one other city, where the message will be posted in the town square, and handed off to some number of new messengers, each of whom will ride of to a different city, repeating the process. The empire’s unemployment rate is such that there are no limits placed upon the number of messengers in each city, the only goal is to get the message communicated throughout the empire as quickly as possible.

### Input

The input will describe the routes between the n cities. All cities are reachable using some path from the capitol city. The first line of the input will be n, the number of cities, such that 1 <= n <= 100. The rest of the input defines an adjacency matrix, A. The adjacency matrix is square and of size n×n. Each of its entries will be either an integer or the character x. The value of A(i, j) indicates the time required to travel from city i to city j. A value of x for A(i, j) indicates that a message cannot be sent directly from city i to city j.
Note that for a city to send a message to itself does not require a messenger, so A(i, i) = 0 for 1 <= i <= n. Also, you may assume that the adjacency matrix is undirected (messengers can travel in either direction in equal time), so that A(i, j) = A(j, i). Thus only the entries on the (strictly) lower triangular portion of A will be supplied as input. The input to your program will be the lower triangular section of A. That is, the second line of input will contain one entry, A(2, 1). The next line will contain two entries, A(3, 1) and A(3, 2), and so on.

### Output

Your program should output the minimum time required before a message sent from the capitol (city #1) is known throughout the empire, i.e. the time it is received in the last city to get the message.

### Sample Input

    5
    50
    30 5
    100 20 50
    10 x x 10

### Output for the Sample Input

    35

### 解题思路

已经写在纸上，做完了确定正确了再写上来


## Wiki

Visual Concepts is a video game developer based in Novato, California best known for developing Take-Two Interactive's 2K series of sports games. After the success of the series, they were acquired by Sega and became a wholly owned studio with Sega, usually termed a first-party developer. However, Sega at the time termed non-internal studios that the company either set up or purchased as "1.5 development studios" in order to differentiate them from their own internal studios. In January 2005, Visual Concepts was sold to Take-Two Interactive along with their wholly owned subsidiary Kush Games. With the purchase of Visual Concepts, Take-Two created 2K Games, a new publishing label.[1] Although the company started out developing quirky titles such as Lester the Unlikely, development efforts are now primarily centered on sports titles such as Basketball and Wrestling.

## NBA 2K Title

+ 2K16 - Curry, Harden, Davis
+ 2K15 - Durant
+ 2K14 - James
+ 2K13 - Griffin, Durant, Rose
+ 2K12 - Bird, Jackson, Jordon
+ 2K11 - Jordon - Best
+ 2K10 - Bryant
+ 2K9 - Garnet

## Top 21 Interviewing Questions

> What applicable attributes do you have for this position?

Enthusiasm, hard working, never give up

> Was there a person in your career who really made a difference?

My team leader in Microsoft. He taught me how to be an interesting people balance work and life.

> What concerns do you have about working in this position or for this organization?

Create great games or help others create great games

> What criteria are you using to evaluate the company for which you hope to work?

The culture, the people, also the salary

> What is the most competitive work situation you have experienced? How did you handle it? What was the result?

When I create the kinect game "shadow play", with the limited precision provided by the hardware, it is difficult to determine where the direction of user's head, so I create a machine learning method to predict the direction using the history acts

> Have you ever worked in a situation where the rules and guidelines were not clear? Tell me about it.

Yes, when I was the team leader of a cooperative research team, I have to build everything from scratch. Rules, meetings, framework, code.

> Describe your production deployment process.

Plan ideas, sort them by need, focus on the essentials first. Getting a working model to test for bugs. Reiterate with additional features.

> What are your technical certifications?

Basically I did masters in computer science and engineering so I feel comfortable with programming languages with a little training.

> What development tools have you used?

Like stated before, I used different IDEs such as Eclipse/android studio (Java), Visual Studios (C++ and C#) and Unity/cocos2d (for game dev)

> What automated-build tools or processes have you used?

several python script to glue everything in my graduate project, as it contains three dofferent parts: knowledge graph, note system and book recommender system.

> How did your education help prepare you for this job?

I have the ability to learn really quick and try different methods to get the job done.

I know the hardware and how the code runs on it.

It helped by exposing me to several languages and projects that helped me build confidence in my programming and providing me with motivation to start my own projects.

Coming from an engineering background has taught me to be very analytical, break down into small pieces and look at the bigger picture. But what it has helped me on the personal front is to work in collaboration.

> How would you rate your key competencies for this job?

General conversational ability and call control Ability to remain calm under pressure Ability to communicate clearly and confidently Ability to follow an enquiry through from the initial call to any follow-up correspondence Attention to detail Grammar and spelling.

> Give an example of where you have applied your technical knowledge in a practical way.

In my experience in past roles I found once I put myself in the position of the end user I then translated that through either explaining technical issues or dealing with issues in the least disruptive way as possible.

> In databases, what is the difference between a delete statement and a truncate statement?

Delete removes all records but space still allocated, truncate removes all space used.

Delete function deletes rows of data, and can be specified with a WHERE function, truncate removes all data quickly and cannot be defined, it is "all or nothing"

Delete can be rolled back, truncate will permanently delete all the rows.

> Define authentication and authorization and the tools that are used to support them in enterprise deployments.

Authentication is showing the system or person who you are in order for the system to know that you have access to whatever it is blocking access to. Authorization is someone that gives you access.

> What is the role of continuous integration systems in the automated-build process?

Immediate knowledge of downstream effects of local changes.

> When is the last time you downloaded a utility from the internet to make your work more productive, and what was it?

I am not 100% comfortable with using the command line and therefore used a software called Github Desktop in order to help me push and pull projects and assignments from github.

> How important is it to work directly with your business users?

Very important to get as much details as possible and have a better idea of the type of software that the user wants. The better idea we get, the easier it is to code the software correctly.

> When is it appropriate to denormalize database design?

Denormalization is required when querying the data from database becomes very slow.

> What have you done to ensure consistency across unit, quality, and production environments?

Clean data, appropriate testing, continuous integration, Agile.

> How much reuse do you get out of the code that you develop, and how?

Image Processing Library optimized for mobile devices

A lot of code written in my game dev projects can be reused since a lot of the functionality can be used in several projects. An example of this is a movement algorithm for character movement, or collision detection for projectiles.

## 他人面试经历

這邊有點規模的公司對於 “通 C++” 的定義都至少要弄懂整本 Effective C++ .

大家都叫 2K Sports , 不過正式的名稱是 Visual Concepts Studio . 2K( 正確來說應該叫 Take-Two Interactive ) 其實是 Visual Concepts 的第三任老闆. 2K 之前是 Sega , 再之前是 EA .

老實說在這抓蟲 還. 蠻. 痛. 苦. 的…

一個原因是因為整個 code base 很大, 大到整個讀進 Visual Studio 一定會把 Visual Studio 炸掉. 不過這當然是次要的原因, 有稍微念過軟體工程的都知道如果 interface / module 有好好切.
是不需要跑整個 code base 的.

但這也就帶出主要的原因了, 就是這 code based 超級老又超級醜 …0rz

因為一年要出一款遊戲, 很多時候大家就是便宜行事, 繞過該有的架構.如果做完遊戲之後有好好修回去的話那就算了, 但是實際上是大家都這樣繞,然後這種東西累積了十五年以上. (最老的 code 的最後修改是 1996)

我們這邊用的語言叫做 Visual Concepts C , 他其實有一部分的 C++ . 有 Class , 能做 polymorphism, virtual function 跟 overloading . 沒有 template 支援. 同時有很多額外文法做家用主機上的 data alignment.

但是它不是閹割 C++ 的語言, 某人是從 C89 一路加上來的. 沒錯, 手工改造 C89 的 Lexical Analyzar , 手工雕 Compiler , 手工雕 Make, 然後拿來做遊戲.
