# Ants on a Triangle

There are three ants on different vertices of a triangel. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangel? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen, and that they walk at the same speed.

Similarly, find the probability of collision with n ants on an n-vertex polygon

## Solution

* P(clockwise) = (1/2)^3
* P(conter clockwise) = (1/2)^3
* P(same direction) = 1/4
* P(collision) = 1 - P(same direction) = 3/4
* For n: P(collision) = 1 - (1/2)^(n-1)

