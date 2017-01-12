# Poison

You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which can be used to detect poison. A single drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once and you can reuse a test strip as many times as you'd like (as long as the results are negative). However, you can only run tests once per day and it takes seven days to return a result. How would you figure out the poisoned bottle in as few days as possible?

Follow up: Write code to simulate your approach.

## Solution

2^10 = 1024, so bottle 1 is 0000000001 -> one drop to strip 1; bottle 2 is 0000000010 -> one drop to strip 2.

Using the strips as the binary bit, after 1000 drops we can know which bottle contains poison.

