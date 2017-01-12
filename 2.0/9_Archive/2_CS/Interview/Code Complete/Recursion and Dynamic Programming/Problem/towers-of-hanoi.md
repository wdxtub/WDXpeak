# Towers of Hanoi

In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slid onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
 
1. Only one disk can be moved at a time
2. A disk is slid off the top of one tower onto the next rod
3. A disk can only be placed on top of a larger disk

Write a program to move the disks from the first tower to the last using Stacks.

## Solution

```java
private static Stack<Integer> start = new Stack<Integer>();
private static Stack<Integer> buff = new Stack<Integer>();
private static Stack<Integer> end = new Stack<Integer>();

public static void hanoi(int n){

    // from n to 1
    for (int i = n; i > 0; i--){
        start.push(i);
    }

    move(n, start, buff, end);
}

public static void move(int n, Stack<Integer> s, Stack<Integer> b, Stack<Integer> e){
    if (n > 0){
        move(n - 1, s, e, b);
        if (!e.isEmpty() && e.peek() <= s.peek()){
            System.out.println("Wrong Operation");
        }
        else {
            int tmp = s.peek();
            System.out.println("Move " + tmp + " From [" + s + "] to [" + e + "]" );
            e.push(tmp);
            s.pop();

        }
        move(n - 1, b, s, e);
    }
}   
```

