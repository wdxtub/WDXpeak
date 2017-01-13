# The Heavy Pill

You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides and exact measurement, how would you find the heavy bottle? You can only use the scale once.

## Solution

1. Take 1 pill from the #1 bottle, 2 from the #2 bottle,..., 20 from #20 bottle.
2. The total number of pills are (1+20)*20/2 = 210
3. Check the total weights, to see how much heavier than 210 gram
4. Suppose it is x gram heavier, then the heavy bottle is #(x/0.1)


