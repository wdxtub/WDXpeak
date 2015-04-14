# Term Project

## Timeline

Email to 18645@sv.cmu.edu by 22:00(PST)

+ Abstract: March 31th (1 page)
    * what you propose to do for this project
    * Baseline performance, expected outcome
    * submit early!
+ Draft Project Report: April 16th (5-10 pages)
    * Project overview including preliminary results
+ Final Project Report: April 23th (5-10 pages)
    * Final graded report: 5-10 pages

## Report

Apply skills learned in this course to a problem that is important to you

+ Technical report describing your work (5-10 pages)
    * 0.5 page: Overview of the problem you tackled. Why this problem?
    * 0.5 - 1 page: Literature survey, related work. What have others done?
    * 1 - 2 pages: Detailed description of techniques. What did you do?
    * 1.5 - 3 pages: Analysis of results What are the results? What do they mean?
    * 0.5 - 1 page: Conclusion. What is the take home message?
+ Size of report should reflect size of team
+ Report could be basis for a conference submission


## 期末项目

+ location_tool: 读数据
+ location: 类
+ pso_algo: 算法
+ reference_point: 参考点类

## 3.1.2 OpenMP version

Besides the method using CUDA, it is also possible to optimize the performance using OpenMP. Though it may not be as efficient as the CUDA version, it can still boost the performance with little modification of the code as well as the data structure.

However, simply adding several openmp statement can not meet our needs as most of the time it can not make full use of the powerful cores of our CPUs. First we redesign our variables used in the algorithm so that less shared spaces are used as well as the sync issue.

Also as the n+1 step needs the result of the n step, we have to add barriers to make sure that the computations are performed in the correct order.

## 4.3 Fast Platform OpenMP

not finish yet
