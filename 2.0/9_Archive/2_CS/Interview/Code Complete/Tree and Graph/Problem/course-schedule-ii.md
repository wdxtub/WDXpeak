# Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented

## Solution

这题是之前那道 Course Schedule 课程清单的扩展，那道题只让我们判断是否能完成所有课程，即检测有向图中是否有环，而这道题我们得找出要上的课程的顺序，即有向图的拓扑排序，这样一来，难度就增加了，但是由于我们有之前那道的基础，而此题正是基于之前解法的基础上稍加修改，我们从queue中每取出一个数组就将其存在结果中，最终若有向图中有环，则结果中元素的个数不等于总课程数，那我们将结果清空即可。

If we use the DFS solution of Course Schedule, a valid sequence can easily be recorded.

## Complexity

## Code

```java
public int[] findOrder(int numCourses, int[][] prerequisites) {
    if(prerequisites == null){
        throw new IllegalArgumentException("illegal prerequisites array");
    }
 
    int len = prerequisites.length;
 
    //if there is no prerequisites, return a sequence of courses
    if(len == 0){
        int[] res = new int[numCourses];
        for(int m=0; m<numCourses; m++){
            res[m]=m;
        }
        return res;
    }
 
    //records the number of prerequisites each course (0,...,numCourses-1) requires
    int[] pCounter = new int[numCourses];
    for(int i=0; i<len; i++){
        pCounter[prerequisites[i][0]]++;
    }
 
    //stores courses that have no prerequisites
    LinkedList<Integer> queue = new LinkedList<Integer>();
    for(int i=0; i<numCourses; i++){
        if(pCounter[i]==0){
            queue.add(i);
        }
    }
 
    int numNoPre = queue.size();
 
    //initialize result
    int[] result = new int[numCourses];
    int j=0;
 
    while(!queue.isEmpty()){
        int c = queue.remove();
        result[j++]=c;
 
        for(int i=0; i<len; i++){
            if(prerequisites[i][1]==c){
                pCounter[prerequisites[i][0]]--;
                if(pCounter[prerequisites[i][0]]==0){
                    queue.add(prerequisites[i][0]);
                    numNoPre++;
                }
            }
 
        }
    }
 
    //return result
    if(numNoPre==numCourses){
        return result;
    }else{
        return new int[0];
    }
}
```

