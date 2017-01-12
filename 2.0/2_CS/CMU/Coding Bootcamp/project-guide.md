# Project Guide

python crawler，可以用库，但是需要更多自己实现的 feature

## Teammate:

hongyis,zhizhouy,dawang,yangqiup,yitingh

## Webcrawler

## 需要讨论确定的问题

1. Python 版本 
	+ Python 2.7 
2. topic specific 的设计
	+ imdb 
3. minimum feature 分工
4. extra feature brain storm
5. 代码架构设计(解耦，方便异步开发)
	+ 爬取
	+ 数据库
	+ 内容检测
	+ unittest 
6. wiki 更新计划

### Task

The amount of information accessible via the web has become truly staggering. A virtually unlimited amount of information is now available at the fingertips of anyone who can access an internet connection. It is becoming a goal of many sophisticated projects to access this trove of data and learn from it in increasingly clever ways. Regardless of how the data of the web is converted into information, the universal first step is to retrieve the data with a crawler of some kind.

In this task, you will install develop a topic-specific web crawler that will crawl the web looking for information on a specific topic. Exactly how you accomplish this task is largely up to your team, within the boundaries set by the project.

### Minimum deliverables

+ A vision document with a list of planned features
+ Functioning web crawler written entirely in Python. All code must be checked into the Gitlab repository on Argonne. 
	+ The version of the crawler you will be evaluated on is the trunk of your project. Anything not in trunk won’t be evaluated.
	+ Check in code and update the wiki with your iteration plan and review every two days.
		+ Iteration plan must include:
			+ The list of features each member of the group will attempt to implement
			+ Estimation of time to complete each feature
		+ Iteration review must include:
			+ 1-for-1 review of the iteration plan, enumerating what features each individual finished and what features were not finished. Include a one-sentence explanation of why unfinished features could not be completed.
			+ Burndown chart comparing actual time to complete each feature versus estimated time

### Minimum Crawler Features

+ Takes as input keywords that must be present on a web page
+ Recursively crawls links on a web page
	+ User may specify breadth-first or depth-first crawling
+ Rests at least two seconds between each recursive step for pages within the same domain (no rest required for pages on other domains)
+ Can be terminated at any time by the user
+ Has no preset limit to recursion depth
+ Stores data in a database
+ Provides real-time status to the user about how many pages has been crawled, what is currently being crawled, what is planned, etc. (use some creativity here)
+ May be either command line or web-based application.
+ Define at least four additional features not listed above

Additional features:

+ sending email
+ logging
+ user query
+ data recommendation

+ imdb movie
+ reconnect
+ unittest

分工

+ 数据库 query done mysql
+ flask ui done bootstrap
+ parser
+ crawler 
	+ recommendation
	+ bfs
	+ dfs


### Due Date

Two weeks from assignment (11/13/15)

Hints:

+ Follow the Agile development pattern
+ Work at least 60-90 minutes on the project each and every day to stay ahead


### Readings and Resources

+ [Python web crawling1](http://null-byte.wonderhowto.com/inspiration/basic-website-crawler-python-12-lines-code-0132785/)
+ [Python web crawling2](http://www.netinstructions.com/how-to-make-a-web-crawler-in-under-50-lines-of-python-code/)
+ [Agile](http://www.agilemanifesto.org)
+ [This link has more process than necessary – take a lightweight version of this](http://www.allaboutagile.com/category/how-to-implement-scrum-in-10-easy-steps/)

