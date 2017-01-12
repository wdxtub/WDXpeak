# Edit Distance

给出两个单词word1和word2，计算出将word1 转换为word2的最少操作次数。

你总共三种操作方法：

+ 插入一个字符
+ 删除一个字符
+ 替换一个字符

样例

    给出 work1="mart" 和 work2="karma"
    返回 3

## Solution

res[i][j]表示Edit Distance between X数组的前i个元素以及Y数组的前j个元素，或者the minimum # of operations to convert X前i个元素 into Y的前j个元素

因为对于Xi 和 Yj，操作无非是 insert, delete, replace三种，所以递归式就是三项：根据上面这个图很清楚：res[i][j] = min{res[i-1][j]+1, res[i][j-1]+1, Xi == Yj ? res[i-1][j-1] : res[i-1][j-1] + 1}

## Complexity

时间复杂度 O(n^2 ) 空间复杂度 O(n^2 )，空间复杂度可以优化至 O(n)

## Code

```java
public class Solution {
    public int minDistance_1(String word1, String word2) {
        if(word1==word2) return 0;
        int len1 = word1.length();
        int len2 = word2.length();
        int[][] dp = new int[len1+1][len2+1];
        
        for(int i=0;i<=len1;i++)
            dp[i][0] = i;
        for(int i=0;i<=len2;i++)
            dp[0][i] = i;
        
        for(int i=1;i<=len1;i++){
            for(int j=1;j<=len2;j++){
                if(word1.charAt(i-1)==word2.charAt(j-1)) dp[i][j] = dp[i-1][j-1];
                else{
                    dp[i][j] = Math.min(dp[i-1][j],Math.min(dp[i][j-1],dp[i-1][j-1]))+1;
                }
            }
        }
        return dp[len1][len2];
    }
    
    public int minDistance(String word1, String word2) {
        if(word1==word2) return 0;
        int len1 = word1.length();
        int len2 = word2.length();
        int[] dp = new int[len2+1];
        
        for(int i=0;i<=len2;i++)
            dp[i] = i;
        
        for(int i=1;i<=len1;i++){
            int upperLeftBak = dp[0];
            dp[0] = i;
            for(int j=1;j<=len2;j++){
                int upperLeft = upperLeftBak;
                upperLeftBak = dp[j];
                if(word1.charAt(i-1)==word2.charAt(j-1)) dp[j] = upperLeft;
                else{
                    dp[j] = Math.min(dp[j],Math.min(dp[j-1],upperLeft))+1;
                }
            }
        }
        return dp[len2];
    }
}
```

