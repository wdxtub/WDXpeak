# Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:

Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

## Solution

DFS.

## Code

```java
public class Solution {
    public List<String> restoreIpAddresses(String s) {
         List<String> res = new ArrayList<String>();
        dfs(s, new String(), 0, 0, res);
        return res;
    }
    public void dfs(String s, String ip, int start, int step, List<String> res) {
        if (step == 4 && start == s.length()) {
            res.add(ip);
        }
        if (step == 4) return;
        if(s.length()-start>(4-step)*3) return ;
        if(s.length()-start<4-step) return ;
        if (ip.length() != 0) ip+=".";
        int num = 0;
        for (int i = start; i < start + 3 && i < s.length(); ++i) {
            num =  num*10 + s.charAt(i) - '0';
            if (num > 255) break;
            ip += s.charAt(i);
            dfs(s, ip, i + 1, step + 1, res);
            if (num == 0) break;
        }
    }
}
```

