# Binary to String

Given a real number between 0 and 1 that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR"

## Solution

根据二进制转换方法进行转换

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public void binary2String(double num){
    if (num >= 1 || num <= 0){
        System.out.println("ERROR");
        return;
    }

    StringBuilder binary = new StringBuilder();
    binary.append('.');

    while (num > 0){
        if (binary.length() > 32){
            System.out.println("ERROR");
            return;
        }

        double t = num * 2; // num << 1
        if (num >= 1){
            binary.append(1);
            num = t - 1;
        }
        else{
            binary.append(0);
            num = t;
        }
    }
    System.out.println(binary.toString());
}
```

