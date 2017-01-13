# OA

```java
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        // get input
        while (true){
            if (sc.hasNext()){
                arr.add(sc.nextInt());               
                //System.out.println(arr);
            } else {
                break;
            }     
        }
        // handle corner case
        if (arr == null || arr.size() == 0 || arr.get(0) == 0) {
            System.out.println("failure");
            return;
        }
        
        // dp process to find the path
        int[] dp = new int[arr.size()+1];
        for (int i = 0; i < arr.size(); i++){
            for (int j = i+1; j < arr.size()+1; j++){
                int tp = 0;
                if (j <= i + arr.get(i)){
                    tp = j - i;
                    dp[j] = Math.max(dp[j], tp);
                } else {
                    break;
                }
            }
        }
        
        Stack<String> resultStack = new Stack<>();
        if (dp[arr.size()] > 0){
            resultStack.push("out");
            for (int i = arr.size(); i > 0; ){
                i -= dp[i];
                resultStack.push(i+", ");
            }
            
            while(!resultStack.empty()){
                System.out.print(resultStack.peek());
                resultStack.pop();
            }
        } else {
            System.out.println("failure");
        }
        
    }
}
```

