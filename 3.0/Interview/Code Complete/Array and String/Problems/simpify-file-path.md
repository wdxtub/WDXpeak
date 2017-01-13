# Simplify File Path

给定一个文档(Unix-style)的完全路径，请进行路径简化。

样例

    "/home/", => "/home"
    "/a/./b/../../c/", => "/c"

挑战

+ 你是否考虑了 路径 = "/../" 的情况？在这种情况下，你需返回"/"。
+ 此外，路径中也可能包含双斜杠'/'，如 "/home//foo/"。 在这种情况下，可忽略多余的斜杠，返回 "/home/foo"。

## Solution

先根据 `/` 来进行字符串分割，然后根据不同情况来进行处理

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param path the original path
     * @return the simplified path
     */
    public String simplifyPath(String path) {
        String result = "/";
        String[] stubs = path.split("/+");
        ArrayList<String> paths = new ArrayList<String>();
        for (String s : stubs){
            if(s.equals("..")){
                if(paths.size() > 0){
                    paths.remove(paths.size() - 1);
                }
            }
            else if (!s.equals(".") && !s.equals("")){
                paths.add(s);
            }
        }
        for (String s : paths){
            result += s + "/";
        }
        if (result.length() > 1)
            result = result.substring(0, result.length() - 1);
        return result;
    }
}
```

