# Climb Stairs - Triple Step

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs

## Solution

```java
private static ArrayList<Integer> result = new ArrayList<Integer>();
public static int getWays(int stairs){
    result.clear();
    result.add(1); // to stair 1 - 1 way
    result.add(2); // to start 2 - 2 ways
    result.add(4); // to stair 3 - 4 ways

    if (stairs > 3){
        for (int i = 3; i < stairs; i++){
            result.add(result.get(i-3) + result.get(i-2) + result.get(i-1));
        }
    }
    return result.get(stairs - 1);
}

static int countWays(int n){
    if (n < 0){
        return 0;
    }
    else if(n == 0){
        return 1;
    }
    else {
        return countWays(n-1) + countWays(n-2) + countWays(n-3);
    }
}

public static void testAlgo(){
    System.out.println("Stair 3: " + getWays(3) + " " + countWays(3));
    System.out.println("Stair 6: " + getWays(6) + " " + countWays(6));
    System.out.println("Stair 9: " + getWays(9) + " " + countWays(9));
}
```

