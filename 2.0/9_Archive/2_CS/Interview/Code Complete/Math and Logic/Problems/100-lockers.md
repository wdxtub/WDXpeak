# 100 Lockers

There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers. Next he closes every second locker. Then on his third pass, he toggles every third locker (closes it if it is open or opens it if it is closed). This process continues for 100 passes, such that on each pass i, the man toggles every ith lokcer. After his 100th pass in the hallway, in which he toggles only locker #100, how many lockers are open?

## Solution

1. A door n is toggles once for each factor of n, including itself and 1.
2. A door is left open if the number of factors is odd. 
3. 3. The value x(the number of factors) is odd if n is a perfect square.
4. There are 10 perfect squares within 1~100

Answer is 10

