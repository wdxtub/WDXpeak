# Khan Academy: Probability

My notes form Khan Academy's Probability videos. Full videos can be viewed at
<http://www.khanacademy.org>.

Videos overlapping with the statistics series can be found my in Khan Academy stats notes.

# Basic Probability

Let's say we have a "fair coin" - a coin that's equally likely to land on either side. If we flip
it, what is the probability that it lands with heads facing up? You can write the function out like
this:

    P(H) = ?

A basic probability equation that fits in this case is:

        # of possibilities that meet criteria
    P = -------------------------------------
          # of equally likely probabilities

For the coin it's:

    P = (1/2) = 50%

Another way to think about it is to run an **experiment** at a large scale. Flipping the coin
millions of times, what percentage of the results would be heads? The larger the scale, the closer
you'll get to 50%.

# Probability with Playing Cards and Venn Diagrams

The following examples use a deck of playing cards - assume there's no joker card. The deck of cards
have properties:

* 4 suits: spades, clubs, diamonds, hearts
* Each suit has 13 types of cards: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
* 52 cards total

If you shuffle the deck and pick a card randomly, what's the probability that the card is a jack?

            4 jacks in deck
    P(J) = ---------------- = 1/13
           52 possibilities

What's the probability that it's a heart?

           13 hearts in deck
    P(H) = ----------------- = 1/4
           52 probabilities

What's the probability that it's a jack of hearts? Well, there's only one card in the deck that
satisfies the condition.

    P(J and H) = 1/52

What's the probability that it's a jack OR a heart? Khan draws a venn diagram so we can understand
the question better. There are 4 possible jacks and 13 possible hearts. Of the 13 hearts, there is
one overlap which is both a jack and a heart. You can't just add 4 + 13, you have to take the
overlap into account.

    P(J or H) = (4 + 13 - 1)/52 = 4/13

# Addition Rule for Probability

Let's say there's a bag with:

* 8 green cubes
* 9 green spheres
* 5 yellow cubes
* 7 yellow spheres

Shake the bag and pull a random item out. What's the probability that it's a cube?

              13 possible cubes
    P(cube) = ----------------- = 13/29
              29 total possible

What's the probability of getting a yellow item?

    P(yellow) = (5 + 7) / 29 = 12/29

What's the probability of getting a yellow cube?

    P(cube and yellow) = 5/29

What's the probability of getting a yellow item or a cube? There are 12 yellow items and 13 cubes.
But we can't just add the two numbers because there's an overlap 5 yellow cubes.

    P(cube or yellow) = (12 + 13 - 5) / 29 = 20/29

What's interesting is the relationship between all of these probabilities:

    P(cube or yellow) = P(cube) + P(yellow) - P(cube and yellow)
    20/29 = 13/29 + 12/29 - 5/29

We can generalize this rule:

    P(A or B) = P(A) + P(B) - P(A and B)

This will account for the overlap so you don't double count it. This rule is called the **addition
rule for probability**.

When there is no overlap, P(A and B) = 0. If this is the case, the sets are said to be **mutually
exclusive**.

# Compound Probability of Independent Events

We'll try finding the probability of a sequence of events. If you flip a coin twice, what's the
probability of getting heads twice? You can think of all the different possibilities:

    HH
    HT
    TH
    TT

There are four distinct equally likely outcomes.

    P(HH) = 1/4

These are independent events - what happens in the first flip does not affect the second flip. This
is called the **gambler's fallacy**, where people assume there are better odds getting a tail after
many heads.

To figure out the probability of a sequence of independent events, just multiply the probabilities
of each individual event:

    P(HH) = P(H) * P(H) = 1/2 * 1/2 = 1/4

# Getting at Least One Heads

If you flip a coin three times, what's the probability of getting at least one head?

There are 8 possibilities, we can figure that out because there are 2 possibilities per flip:

    8 = 2 * 2 * 2

Think about it in terms of a tree. At each branch, there are 2 possible paths. So given that you
need to traverse 3 levels, you'll get 2^3 possible leaf nodes.

Instead of writing out all the possible combinations, re-frame the question:

    P(at least one H) = P(not getting all tails)
    P(at least one H) = 1 - P(TTT)
    P(at least one H) = 1 - (1/2 * 1/2 * 1/2)
    P(at least one H) = 7/8

# Frequency Probability and Unfair Coins

A quick review:

           # of events that satisfy A
    P(A) = --------------------------
           # of equally likely events

What about non-equally likely events? We'll use the example of an unfair coin. There's more than a
50% chance of getting heads.

    P(H) = 60% = 0.6 = 6/10
    P(T) = 40% = 0.4 = 4/10

What's the probability of getting heads on two flips?

    P(HH) = P(H) * P(H) = 0.6 * 0.6 = 0.36

What about T1, H2, and T3?

    P(T1 H2 T3) = 0.4 * 0.6 * 0.4 = 0.096

# Getting Exactly Two Heads (Combinatorics)

Flipping a fair coin four times, what's the probability of getting exactly one heads?

    P(exactly 1 "heads")

There are four flips, with 2 possible results on each flip:

    _ _ _ _
    2*2*2*2 = 16 total possibilities

We could use the addition rule:

    P(exactly 1 "heads") = P(HTTT) + P(THTT) + P(TTHT) + P(TTTH) = 4/16

What's the probability of getting exactly two heads?

         _ _ _ _
    Flip 1 2 3 4

Thinking about it generally, we need two heads where order doesn't matter:

    Ha Hb T T
    Hb Ha T T

Ha is the first head and Hb is the second head. The two events listed above are identical for our
purposes.

Ha has four places it can show up in. If the first head occupies one place, the second heads can
only be in three different places.

    Ha  Hb
     4 * 3 = 12 scenarios

But Ha and Hb are interchangeable, ordering doesn't matter. So there are actually only 6 different
scenarios (12 divided by 2).

    P(exactly 2 "heads") = 6/16

# Exactly Three Heads in Five Flips

Let's flip a fair coin five times. What's the probability of getting exactly three heads?

    _ _ _ _ _ = 2^5 = 32 equally likely possibilities
    2 2 2 2 2

We want exactly three heads: Ha, Hb, Hc. The resulting sets should look like this: {Ha, Hb, Hc, T,
T}. Ordering doesn't matter.

So for Ha, there are five possible slots. For Hb, there are four possible slots since Ha is
occupying one. Hc has three possible slots. There are `5 * 4 * 3 = 60` different scenarios if
ordering mattered. But ordering doesn't matter, so we need to divide 60 by the ways we can arrange
the heads.

How did we come up with `5 * 4 * 3`? Think of it as a tree, where the root node has 5 children (each
child being a choice). As you go down a level, you lose a choice because you already used one up
(whereas with coins, you can always get another heads/tails). So the total number of leaf numbers is
simply `5 * 4 * 3`.

Ha can go into any slot. Hb can go into two slots afterwards. Hc can only go into one slot. This
means you can arrange three heads in 6 different ways.

    # of three heads events = 60/6 = 10
    P(exactly 3 "heads") = 10 / 32 = 5/16

# Generalizing with Binomial Coefficients

Let's generalize to find the probability of getting "K" heads in "N" flips of the fair coin:

    P(K heads in N flips)

The number of equally likely possible events is **2^n**. We can determine the number of possible
events that include K heads when ordering matters:

    Ka = n possibilities
    Kb = (n - 1) possibilities
    Kc = etc...
    # events = n * (n-1) * ... * (n-(k-1))

Now we need to determine the number of events if ordering doesn't matter:

    Ha Hb Hc
    is the same as
    Hc Ha Hb

We need to find a generic way to discover how many ways to order things:

    T1, T2, T3, ... TK
    K * K-1 * K-2 * ... * 1
    K!

This is just K factorial. T1 can occupy K slots, T2 can occupy K-1 slots, all the way down to TK
which can occupy just one slot. Our formula becomes:

               n * (n-1) * ... * (n-(k-1))
    # events = ---------------------------
                           K!

    # events = n!/(k! * (n-k)!)

This is called the **generalized formula for binomial coefficients**.

Back to our original problem:

                            # events
    P(K heads in N flips) = -------- = n!/(2^n * k! * (n-k)!)
                               2^n

# Probability (part 2) - Explaining Compound Rule

Here's another way to view how multiply odds yields the probability. Sal uses a probability tree to
explain it:

                  HH
             H -[ HT
    start -[      
             T -[ TH
                  TT

Let's go along a path:

    start => H => H

Getting a heads on the first flip is a 1/2 chance. Getting a heads again is 1/2 of that initial 1/2
change. So `P(HH) = 0.5 * 0.5 = 0.25`. And this holds true to get to any of the leaf nodes of the
tree.

What's the probability of getting 1 heads and 1 tails?

    P(TH U HT) = P(TH) + P(HT) = 1/4 + 1/4 = 1/2

The reason we can multiply probabilities is because the fair coin's flip is independent of any
initial flips.

# Probability (part 5) - Probability of Getting a Certain Number Roll

What's the probability of getting a 7 when rolling two die?

        1  2  3  4  5  6
      +-------------------+
    1 | 2  3  4  5  6  7  |
    2 | 3  4  5  6  7  8  |
    3 | 4  5  6  7  8  9  |
    4 | 5  6  7  8  9  10 |
    5 | 6  7  8  9  10 11 |
    6 | 7  8  9  10 11 12 |
      +-------------------+

    P(7) = 6/36 = 1/6

You're most likely to get a 7 than any other number from rolling two die. How about getting a 2 or
11?

    P(2 U 11) = P(2) + P(11) = 1/36 + 2/36 = 1/13

Let's find the probability without using the grid. What's the probability of getting a 5?

Figure out the ways to get a 5: (1,4), (2,3), (3,2), (4,1). That's 4 events that satisfy the
criteria out of 36.

    P(5) = 4/36 = 1/9

# Probability (part 6) - Intro to Conditional Probability

Given a bag of coins where:

* 9 are fair coins
* 1 is a two-sided head coin

If you pick a random coin from the bag and flip it five times, what's the probability that you get
five heads?

    P(normal picked) = 9/10
    P(two-sided picked) = 1/10

Now figure out the probability of getting all heads given each event:

    P(five heads | normal) = 1/32
    P(five heads | two-sided) = 1

Given these probabilities, we can solve for our initial question.

    P(five heads) = P(five heads | normal) * P(normal picked) +
                    P(five heads | two-sided) * P(two-sided picked)
    P(five heads) = 1/32 * 9/10 + 1/10 * 1
    P(five heads) = 9/320 + 1/10 = 41/320 = ~12.8%

# Probability (part 7) - Touch on Bayes' Theorem

Let's figure out the probability that you picked a two-sided coin given that you got 5 heads in a
row (given the bag of coins from the previous section):

    P(2s | five heads) = ?

Intuitively, if you flip a coin hundreds of times and got heads - you'll conclude that you probably
got the two-sided coin.

    P(five heads | normal) * P(normal picked) = 1/32 * 9/10 = 9/320
    P(five heads | two-sided) * P(two-sided) = 1 * 1/10 = 32/320

The probability of getting five heads is 41/320. Of this, 9/320 was due to picking a normal coin and
32/320 was due to picking a two-sided coin. Sal draws a rectangle with areas to show relativity of
each coin.

    P(2s | five heads) = 32/320 / (41/320) = 32/41 =~ 78%

Let's go through what Bayes' Theorem is and use it to solve instead:

    P(a AND b) = P(a | b) * P(b)
    P(a AND b) = P(b AND a) = P(b | a) * P(a)
    P(a | b) * P(b) = P(b | a) * P(a)
    P(b | a) = P(a | b) * P(b) / P(a)

# Probability (part 8) - Using Bayes' Theorem

We're trying to solve using Bayes' Theorem:

    P(2s | five heads) = P(five heads | 2s) * P(2s picked) / P(five heads)

We already solved for these probabilities in the previous videos, so we can just sub in:

    P(2s | five heads) = 1 * 1/20 / 41/320
    P(2s | five heads) = 32/41

# Permutations

Given three chairs and seven people, how many different ways can these seven people sit in these
three chairs?

    _ _ _  A B C D E F G
    1 2 3

There are seven possibilities for people to sit in chair 1. Then there are six possibilities for
people to sit in chair 2. Last, there's five possibilities for the final chair.

    7 * 6 * 5 = 210 possibilities

Think of it like the compounding rule for independent events. For the coin, we used 2^n where n is
the number of slots. In this case, there are 7 likely events instead of 2. But every time someone
sits down, the number of possible events decreases by one.

We care about the ordering of people. The ways we can order them are called **permutations**.
Permutations can be written in a few ways:

    7^P*3, P^7(sub 3), P(7,3)

Let's generalize this, how many ways can you put n things into k spaces?

    P(n,k) = n * n-1 * n-2 * ... * (n-(k-1))
    P(n,k) = n! / (n-k)!

# Combinations

The permutations formula was great when ordering mattered. But there are many times when we didn't
care about ordering. What if we didn't care who's in which seat? Instead, we only care about the set
of people who's sitting.

A **combination** is just like a **permutation**, except you don't care about the order.

How many different ways can you arrange 3 people?

    A B C
    A C B
    ...
    C B A

It's the same as permutations, except the number of items and slots are the same.

    3! / (3 - 3)! = 3! = 6

Combinations are usually written like this:

    sub(5) P sub(3)
    sub(n) P sub(k) = n items in k slots
    |n| where two vertical bars is actually a parenthesis
    |k|

So how many different groups can be seated given 5 people and 3 seats? Just figure out the number of
permutations and divide that by the times you've double-counted due to ordering:

    P(5,3) / 3! = 60 / 6 = 10

We can generalize this formula:

    P(n,r) / r! 
    n! / r!(n-r)!

Since I'm limited to ascii, I'll use P(n,r) for permutations and C(n,r) for combinations.

# Probability Using Combinations

What's the probability of getting 3 heads out of 8 flips of a fair coin?

    P(3H/8) = # of events with 3 heads / total possible events

The total possible events is just 2^8 = 256.

For the 8 flips, it's similar to picking 3 people to sit down out of 8. It's just like combinations:

    8! / 3!(8-3)! = 8! / 3!5! = (8*7*6)/(3*2*1) = 56 possible events
    P(3H/*) = 56/256 =~ 21.9%

# Probability and Combinations (Part 2)

Given a free throw percentage of 80%, if I shoot 5 free throws what's the probability that I make 3
shots?

     B  B  B  M  M  ==  B  M  B  M  B
    .8*.8*.8*.2*.2     .8*.2*.8*.2*.8

No matter how you order it, it's always going to be `.8^3 * .2^2`. But that's only for a single
arrangement, what about all arrangements?

For the 5 shots, we need to pick 3 - it's a combinatorial problem:

     = 5! / 3!(5-3)!
     = 5 * 4 * 3 / (3 * 2 * 1)
     = 10 combinations

So the probability of making at least 3 shots is the probability of making 3 shots times the number
of possible combinations:

     P(3/5) = .8^3 * .2^2 * 10 = 20.48%

What's the probability of getting at least 3 shots out of 5?

     P(at least 3) = P(3/5) + P(4/5) + P(5/5)
     P(at least 3) = 20.48% + 40.96% + 32%
     P(at least 3) = 94.21%

# Conditional Probability and Combinations

This problem involves everything we've done so far - probability, conditions, and combinations.
Given a bag with:

* 5 fair coins
* 10 unfair coins - 80% heads, 20% tails

Let's say I picked a coin randomly, flipped it 6 times and got 4 heads, what's the probability that
I picked out a fair coin?

    P(fair | 4/6 heads)

Quick review of Bayes' theorem, you should be able to figure this out intuitively without memorizing
the formula:

    P(A and B) = P(A|B) * P(B)
    P(B and A) = P(B|A) * P(A)
    P(B|A) * P(A) = P(A|B) * P(B)
    P(A|B) = P(B|A) * P(A) / P(B)

So for our initial problem:

                          P(4/6 heads | fair) * P(fair)
    P(fair | 4/6 heads) = -----------------------------
                                  P(4/6 heads)

Let's figure out the probability of getting 4 out of 6 heads first.

    P(4/6 heads) = P(4/6 heads | fair) * P(fair) +
                   P(4/6 heads | unfair) * P(unfair)
    P(4/6 heads | fair) = (1/2)^6 * 6!/4!2! = (1/2)^6 * 15 = 15/64
    P(fair) = 5/15 = 1/3
    P(4/6 heads | unfair) = (4/5)^4 * (1/5)^2 * 6!/4!2! = 1/3 * 1/25 * 15 = 1/5
    P(unfair) = 10/15 = 2/3
    P(4/6 heads) = 15/64 * 1/3 + 1/5 * 2/3 = 15/192 + 2/15 = 21.1%

Now we can sub that into Bayes' theorem:

    P(fair | 4/6 heads) = 15/64 * 1/3 / 21.1%
    P(fair | 4/6 heads) = 32.3%

Another way to re-derive Bayes' theorem is to think about areas. What portion of the total
probability accounts for the part we want? We want the probability of getting `P(4/6 heads AND
fair)`. Divide that by the total probability of getting 4/6 heads.