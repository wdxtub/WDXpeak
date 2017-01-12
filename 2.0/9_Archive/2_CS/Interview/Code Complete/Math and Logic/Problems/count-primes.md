# Count Primes

Count the number of prime numbers less than a non-negative number, n.

## Solution

埃拉托斯特尼筛法 (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

## Complexity

时间复杂度 O(nsqrt(n))，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int countPrimes(int n) {
        boolean notPrime[] = new boolean[n + 2];
        notPrime[0] = notPrime[1] = true;
        for (int i = 2; i * i < n; i++) {
            if (!notPrime[i]) {
                int c = i * i;
                while (c < n) {
                    notPrime[c] = true;
                    c += i;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!notPrime[i])
                ans ++;
        }
        return ans;
    }
}
```

