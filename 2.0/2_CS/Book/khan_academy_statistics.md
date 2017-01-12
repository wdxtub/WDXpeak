# Khan Academy: Statistics

My notes form Khan Academy's Statistics videos. Full videos can be viewed at
<http://www.khanacademy.org>.

# Intro and The Average

In broad terms, statistics is getting your head around data. There's a few branches:

* descriptive - find indicative numbers without going over the entire data set
* inferential - using data to make conclusions like from a sample population

We're starting with descriptive statistics. The average of a set of numbers is also known as the
**central tendency**. In formal terms, the average could be one of:

* arithmetic mean (most people are talking about this)
* median
* mode

To calculate the mean, divide the sum by the number of items in the set.

    avg({1, 1, 2, 3, 4}) = (1 + 1 + 2 + 3 + 4) / 5

To find the median, sort the numbers and find the number where there's an equal amount of numbers to
the left and right of it:

    1, 1, 2, 3, 4
         ---

What if it's an even number set? Just take the middle two numbers and find their arithmetic mean.

    1, 1, 2, 3, 4, 4
          ____

The mode is the number that occurs most frequently. For our set, it's the number 1.

# Sample vs Population Mean

Let's say we wanted to know the average height of all men in America. The total population would be
~150 million men. It would be almost impossible to get everyone's height.

The best way to get a sense is to take the average of a sample. Find random people in random
situations so it's not skewed (don't use your basketball team).

    {5, 6, 5.5, 5.75, 6.5}

The above set would be a sample of the population. Instead of taking the mean of the entire
population, we can just use the mean of the sample. In statistics, the population mean is
represented by the **greek letter mu**. The sample mean is represented by an **x with a line over
it**.

The formulas are (unfortunately, working with ascii):

    mu = (Sigma i=1 to N) x (sub i) / N
    -x = (Sigma i=1 to n) x (sub i) / n

Big N means total population. Small n means just a sample. It's a convention.

# Variance of a Population

The central tendency numbers lose a lot of information. We don't know if the numbers in the set are
spread or near. That's what the measure of **dispersion** is for.

    {2, 2, 3, 3}
    mu = (2 + 2 + 3 + 3)/4 = 2.5

    {0, 0, 5, 5}
    mu = (0 + 0 + 5 + 5)/4 = 2.5

The arithmetic mean for both populations are the same, but the distance of the numbers in the bottom
set are much further from the mean. You can think of it as being more dispersed.

Variance is usually represend by the **lowercase greek letter sigma squared**.

    sig^2 = (Sigma i=1 to N) (x (sub i) - mu)^2 / N

`x (sub i) - mu` is just the distance of the number from the mean. Let's find the variance for the
first set:

    sig^2 = (.5^2 + .5^2 + .5^2 + .5^2) / 4
    sig^2 = .25

Let's find the variance for the second set:

    sig^2 = (2.5^2 + 2.5^2 + 2.5^2 + 2.5^2) / 4
    sig^2 = 6.25

# Sample Variance

Variance is represented by the lowercase sigma character. Sample variance is usually represented by
the **lowercase 's' squared**:

    s^2 = (Sigma i=1 to n) (x (sub i) - -x)^2 / n

It uses lowercase 'n' instead of uppercase 'N'. It also uses the x with a line over it to represent
the sample mean instead of population mean.

The sample variance will often underestimate the actual population variance. There's another formula
which is usually closer to the population variance and is sometimes represented by the letter s or s
(sub n-1):

    s^2 (sub n-1) = (Sigma i=1 to n) (x (sub i) - -x)^2 / (n - 1)

The difference is that it's divided by a slightly smaller number `n-1`.

# Standard Deviation

Standard deviation is the square root of the variance. It's represented by the **lowercase sigma**
for populations and **lowercase 's'** for samples.

    sig = ((Sigma i=1 to N) (x (sub i) - mu)^2 / N) ^ (1/2)
    s = ((Sigma i=1 to n) (x (sub i) - -x)^2 / n) ^ (1/2)

Let's try calculating it.

    {1, 2, 3, 8, 7}
    mu = 21/5 = 4.2
    sig^2 = ((1-4.2)^2 + (2-4.2)^2 + (3-4.2)^2 + (8-4.2)^2 + (7-4.2)^2) / 5
    sig^2 = 38.8/5 = 7.76
    sig = 2.79

If the set was just a sample, we would divide by 4 (n - 1) instead of 5. The standard deviation was
just the square root of the variance.

# Alternate Variance Formulas

For the equations below, let SIG represent Sigma i = 1 to N

    sig^2 = SIG (x (sub i) - mu)^2 / N
    sig^2 = SIG (x^2 (sub i) - 2x (sub i) mu + mu^2) / N
    sig^2 = (SIG (x^2 (sub i)) - 2mu * SIG (x (sub i)) + mu^2 * SIG (1)) / N
    sig^2 = (SIG (x^2 (sub i)) - 2mu * SIG (x (sub i)) + mu^2*N) / N
    sig^2 = SIG(x^2 (sub i))/N - 2mu^2 + mu^2
    sig^2 = SIG(x^2 (sub i))/N - mu^2

This is getting close to the **raw score** method, which is a faster way of calculating the
variance.

    sig^2 = SIG(x^2 (sub i))/N - SIG(x (sub i))^2/N^2

The formula above may seem more complicated, but it can be faster because you don't have to
calculate the mean ahead of time.

# Introduction to Random Variables

**Random Variable** can take on multiple values like a variable, but it's not something you usually
solve for. It's usually a capital letter (like capital X). It's really a function that maps from the
world of random processes to an actual number.

Let's say we want to quantify: is it going to rain tomorrow?

    X = { 1 if it rains tomorrow
        { 0 doesn't rain tomorrow

X is going to be random - we don't know if it's going to rain tomorrow. It can take on either value.

It could also be something more obvious:

    X = number facing up when I roll a fair dice
    X = { 1 if heads
        { 0 if tails

There are two types of random variables: **discrete** or **continuous**. Discrete is like rolling a
dice - you have a countable set of results 1-6. A continuous variable can take on an infinite set of
values - like the amount of rain tomorrow. It could be 1.1 inches, 1.2 inches, etc...

Let's use the random variable for number facing up when rolling a dice. Here's the probability
distribution for it (unfortunately in ascii!):

         |
         |
         |
         |
     1/6 |   |   |   |   |   |   |   |
         |___|___|___|___|___|___|___|___
             1   2   3   4   5   6   7   

The probability distribution is just a bar graph with the results on the x-axis and the probability
on the y-axis.

If X is equal to the number facing up described by the probability function above, what is `P(X=6)`?
It's just `1/6`.

# Probability Density Functions

Let's give an example of continuous random variables.

    Y = exact amount of rain tomorrow

What's the probability that Y = 2? Not 2.01, not 1.99, we need exactly 2 inches. We don't even have
tools to tell us if it's exactly 2 inches.

    P(Y = 2) = 0

Instead, for continuous random variables we can think in terms of "almost".

    P(|Y - 2| < .1)
    P(1.9 < Y < 2.1)

Sal draws a line graph and highlights the area underneath the curve between 1.9 and 2.1. The x-axis
represents inches of rain, the y-axis represents the probability (0 to 1). The are underneath the
curve is the total probability.

    P(1.9 < Y < 2.1) = integral(1.9 to 2.1) f(x) dx

The area underneath the entire curve should be 1, since the graph represents all possibilities:

    integral(0 to infinity) f(x) dx = 1

From now on, I'm going to abbreviate integral to $(a->b).

# Binomial Distribution 1

Given a fair coin and five flips:

    X = number of heads after five flips

What's the probability that you get no heads?

    P(X = 0) = P(5 tails) = (1/2)^5 = 1/32

What's the probability of getting one heads?

    P(X = 1) = P(HTTTT + THTTT + ...) = 5/32

What's the probability of getting two heads? There are five flips, two of them can be chosen as
head. Ordering doesn't matter.

    P(X = 2) = (5*4/2) * 1/32 = 10/32

What's the probability of getting three heads? We can use the same approach as above.

    P(X = 3) = (5*4*3/3!) * 1/32 = 10/32

What's the probability of getting four heads?

    P(X = 4) = (5*4*3*2/4!) * 1/32 = 5/32

Finally, what's the probability of getting five heads?

    P(X = 5) = 1/32

# Binomial Distribution 2

The probability distribution below isn't the scale.

    .31 |       |  |
        |       |  |
        |       |  |
    .17 |    |  |  |  |
        |    |  |  |  |
    .03 |_|__|__|__|__|__|_
          0  1  2  3  4  5

The graph above is a particular instance of a **binomial probability distribution**. As you get
towards continuous random variables, this graph would appear like the famous bell curve.

A binomial distribution is the distribution of the number of successes in a sequence of N
independent yes/no experiments. It's also called the Bernoulli experiment.

It's really important to understand that not all probability distributions are this normal
distribution (in a bell curve form). Don't assume!

A binomial is just a pair like (n - x) or (n + x). That's why the formula for combinations are
called binomial coefficients. It's also why it's called the binomial distribution.

For the notes below, I'll be using the notation C(n, k) as the combinations method for binomial
coefficients.

Side note, in algebra we learned the binomial theorem. Here's an example:

    (x + y)^2
    x^2 + xy + y^2
    
The coefficient of each term (in the case above, it's always 1) is known as the binomial
coefficient:

    n = b + c
    a = x^b * y^c  <-- a is the binomial coefficient
    a = C(n,b) = C(n,c)

# Binomial Distribution 3

Let's say we make 6 free throws and the free throw percentage is 30%.

    X = # of shots made

Let's figure out the probability for each outcome:

    P(X = 0) = .7^6
    P(X = 1) = 6 * .3 * .7^5    // multiply by 6 because there are 6 scenarios
    P(X = 2) = (6 * 5 / 2!) * .3^2 * .7^4
    P(X = 3) = (6 * 5 * 4 / 3!) * .3^3 * .7^3
    P(X = 4) = (6 * 5 * 4 * 3 / 4!) * .3^4 * .7^2
    P(X = 5) = (6 * 5 * 4 * 3 * 2 / 5!) * .3^5 * .7^1
    P(X = 6) = .3^6

# Binomial Distribution 4

Sal input the formulas into excel to output a nice graph. This ascii one doesn't really do it
justice, but here it is!

       |        |
       |     |  |
    .2 |     |  |
       |     |  |  |
       |  |  |  |  |
       |__|__|__|__|__|__:__.__
          0  1  2  3  4  5  6

The x-axis is number of shots made and the y-axis is the probability.

This probability distribution is based on a 30% free throw percentage. If we changed it to 50%, we
get a nice symmetrical bell curve. If you change the free throw percentage to 80%, you'll see the
peak shift to the right.

# Expected Value E(X)

Let's say our population was: 3, 3, 3, 4, 5. The population mean would just be the sum divided by
how many numbers we have:

    (3 + 3 + 3 + 4 + 5) / 5
    (3(3) + 1(4) + 1(5)) / 5
    1/5 ( 3*3 + 1*4 + 1*5 )
    3/5 * 3 + 1/5 * 4 + 1/5 * 5
    60% * 3 + 20% * 4 + 20% * 5

The last expression is different. We don't know how many numbers there are, but we're stating the
frequencies of the numbers. 60% of the numbers are 3, 20% are 4, and 20% are 5.

Let's set a random variable to the number of heads from 6 tosses of a fair coin:

    X = # of heads from 6 tosses of coin

The population of results is actually infinite. You can always toss the coin again to get another
result. The random variable is just a specific result from some experiments - it's just a sample of
an endless population.

The expected value of a random variable is the same thing as the population mean. It works with
infinite sets - you can't really calculate the average of infinite sets.

Sal goes back to the spreadsheet he created in the last video and substitutes a 50/50 percentage to
imitate a fair coin toss:

    P(0H) = 1.563%
    P(1H) = 9.375%
    P(2H) = 23.438%
    P(3H) = 31.25%
    P(4H) = 23.438%
    P(5H) = 9.375%
    P(6H) = 1.563%

With this information, you can find the population mean aka the expected value.

    E(X) = 0*1.563% + 1*9.375% + 2*23.438% + 3*31.25% +
           4*23.438% + 5*9.375% + 6*1.563%

We're finding the arithmetic mean (or expected value) of an infinite set.

    E(X) = 3

That's kind of an expected outcome with a 50/50 chance. If you flip a coin six times, you'll expect
to get three heads the most times. The expected value isn't always the most probable value - in this
case it is.

# Expected Value of Binomial Distribution

Let's set some general values:

    X = # of successes with probability p after n trials
    E(X) = n * p

Let's use a more concrete example:

    X = # of baskets made after 10 shots where my shooting pct is 40%
    E(X) = 10 shots * 40% = 4 shots

For binomial distributions, you can view the expected value as the most likely and probable outcome.

Let's prove that the general case is true for any binomial distributions:

    P(X = k) = C(n, k) P^k (1-P)^(n-k)

The expected value is just a probability weighted sum:

    E(X) = (Sigma k=0 to n) k * C(n, k) * p^k * (1-p)^(n-k)

The first simplification we can make is that when `k = 0`, the entire value is 0. So we can leave
out the initial `k = 0`.

    E(X) = (Sigma k=1 to n) k * n!/(k!(n-k)!) * p^k * (1-p)^(n-k)
    E(X) = (Sigma k=1 to n) n!/((k-1)!(n-k)!) * p^k * (1-p)^(n-k)
    E(X) = np * (Sigma k=1 to n) (n-1)!/((k-1)!(n-k)!) * p^(k-1) * (1-p)^(n-k)

Since our formula is so complicated, let's make some substitutions:

    a = k - 1
    b = n - 1
    b - a = n - k

Now our equation is a bit easier to read:

    E(X) = n * p * (Sigma k=a to b) b! / (a!(b-a)!) * p^a * (1-p)^(b-a)
    E(X) = n * p * (Sigma k=a to b) C(b,a) * p^a * (1-p)^(b-a)
    E(X) = n * p * 1
    E(X) = n * p

# Poisson Process 1

Let's say you're a traffic engineer and you want to figure out how many cars pass by in a given time
frame:

    X = # of cars pass in an hour

The goal is to figure out the probability distribution of this random variable. From that, you can
figure it out for any time frame. That's assuming any hour is the same on this street which is
usually not the case. You could also get the value for multiple hours and average them out.

    E(X) = lambda = n * p
    lambda cars/hours = 60 minutes/hour * lambda/60 cars/minutes
    P(X = k) = C(60, k) * (lambda / 60)^k * (1 - lambda/60)^(60-k)

But success here is defined as one car passing in one minute? What if more cars passes in that
single minute? We could do it more granular:

    P(X = k) = C(3600, k) * (lambda / 3600)^k * (1 - lambda/3600)^(3600-k)

But the same problem applies. What if two cars go by in one second? If we keep getting more and more
granular, we'll get the **Poisson distribution**.

Some refreshers:

    lim x -> inf (1 + a/x)^x = e^a
    lim x -> a [f(x)g(x)] = lim x -> a [f(x)] * lim x -> a [g(x)]
    x!/(x-k)! = (x)(x-1)(x-2)...(x-k+1)

# Poisson Process 2

Let's take our binomial distribution as the intervals approaches infinity:

    E(X) = lambda = n*p
    P(X=k) = lim n->inf [C(n, k) (lambda / n)^k (1 - lambda/n)^(n-k)]
    P(X=k) = lim n->inf [n!/(k!(n-k)!) * lambda^k/n^k *
                         (1-lambda/n)^n * (1-lambda/n)^-k]
    P(X=k) = lim n->inf [(n^k + ...)/n^k] * lambda^k/k! * 
             lim n->inf [1-lambda/n]^n * lim n->inf [1-lambda/n]^-k
    P(X=k) = 1 * (lambda^k)/k! * e^-lambda * 1
    P(X=k) = (lambda^k)/k! * e^-lambda

So what's the probability that two cars pass in a given hour?

    P(X=2) = (9^2)/2! * e^-9

The Poisson distribution is also known as the **Poisson law of small numbers**.

# Law of Large Numbers

Let's say we have a random variable X and know E(X). As the number of experiments you perform
approaches infinity, the arithmetic mean and expected value will converge:

                x1 + x2 + ... + xn
    -x(sub n) = ------------------
                        n
    -x(sub n) -> E(X) for n -> infinity
    -x(sub n) -> mu

Let's use a more concrete example.

    X = # of heads after 100 tosses of fair coin
    E(X) = 100 * 0.5 = 50
                55 + 65 + 45 + ... + n
    -x(sub n) = ----------------------
                          n
    -x(sub n) = 50 as n -> infinity

It's not telling you that if you continually get high values of X, the next trial has a higher
probability of getting a lower X to make up. That's known as the gambler's fallacy.

This is what the casinos use to make money. While a small number of people will win, over the long
term the casino wins due to the game's probabilities.

# Normal Distribution Excel Exercise

The **normal distribution** is also known as the **Gaussian distribution** or the **bell curve**:

                   1
    P(x) = ----------------- * e ^ [-1/2 * ((x-mu)/sigma)^2 ]
           sigma * sqrt(2pi)

It's a good approximation for the binomial distribution and vice versa, if you're taking enough
trials.

# Introduction to the Normal Distribution

To get the probability given the distribution, you get the area under the curve:

    integral 4.5 to 5.5 [P(x) dx]

The **central limit theorem** states that if you take the sum of all of your experiments, as you
approach an infinite number you'll converge to a normal distribution (sounds a lot like law of large
numbers).

Sal plays around with the normal distribution formula to give some intuition about it. He recommends
that you just memorize it.

# Normal Distribution Problems: Qualitative Sense of Normal Distributions

Which of the following is more likely to follow a normal distribution? a) The hand span (measured
from tip of thumb to tip of 5th extended finger) of a random sample of high school seniors. b) The
annual salaries of all employees of a large shipping company. c) The annual salaries of a random
sample of 50 CEOs of major companies, 25 men and 25 women. d) The dates of 100 pennies taken from a
cash drawer in a convenience store.

The hand span is a factor of genetics and environment, like how much milk a peron drank. It is very
close to a random process so it should be pretty close to a normal distribution. It won't be a
perfect normal distribution because it would never go into the negative region. The right side also
has a growth limit. It's also possible to have a **bi-modal distribution**, one for men and one for
women.

The salaries of a large shipping company probably has two spikes in its distribution. There's a $40k
mean for minimum wage workers and executives would have $200k mean. It would not be a normal
distribution. It would definitely be bi-modal.

The salaries of 50 CEOs is probably close to normal distribution. It would be a **right-skewed
distribution** due to a base salary and then slowly decreasing value. Here's my best attempt at a
right skewed distribution:

    |      ______
    |     /      \
    |     |       ----
    |     |           \
    |_____|____________----____

The initial vertical incline is due to the base salary and the diminishing slope is the variance.
Sometimes a right-skewed distribution is called a **positively skewed distribution**. The mean is on
the right of the median due to the diminishing tail.

Most pennies are newer pennies because they have a higher chance of survival. The older pennies have
been lost, destroyed, or melted. You'll find a ton of current year pennies and it goes down from
there. It's a left-skewed distribution.

(a) the hand span is most likely to follow a normal distribution.

# Normal Distribution Problems: z-score

The grades on a statistics mid-term for a high school are normally distributed with `mu = 81` and
`sigma = 6.3`. Calculate the z-score for each of the following exam grades. Draw and label a sketch
for each example.

a) 65 b) 83 c) 93 d) 100

The **z-score** is just how many standard deviations `sigma` away it is from the arithmetic mean
`mu`. Here's the formula:

    z-score(x) = (x - mu) / sigma

Let's use it to figure out each z-score:

    z-score(65) = (65 - 81) / 6.3 = -2.54
    z-score(83) = (83 - 81) / 6.3 = .32
    z-score(93) = (93 - 81) / 6.3 = 1.9
    z-score(100) = (100 - 81) / 6.3 = 3.02

For labeling a sketch, draw a normal distribution and label the middle as the mean. Draw vertical
axises for 1, 2, and 3 standard deviations in each direction from the mean. Now you can label where
each exam falls.

           _____
          /  :  \
         -.  :  .-
        / .  :  . \
       /  .  :  .  \
    _--___.__:__.___--_
           mu=81

# Central Limit Theorem

The **central limit theorem** states conditions under which the mean of a sufficiently large number
of independent random variables, each with finite mean and variance, will be approximately normally
distributed.

Let's say we have a discrete distribution that can take on the values 1 to 6:

    |                 x
    |                 x
    |  x              x
    |  x     x  x     x
    |__x_____x__x_____x__
       1  2  3  4  5  6

Let's say the sample size is `n = 4`, the resulting sets of dice rolls are:

    s(1) = [1, 1, 3, 6]
    xbar(1) = 2.75

    s(2) = [3, 4, 3, 1]
    xbar(2) = 2.75

    s(3) = [1, 1, 6, 6]
    xbar(3) = 3.5

Let's plot the frequency of the sample means above:

    |
    |       x
    |_______x_____x__
           2.75   3.5

Let's say we keep running the experiment over and over again and plot the means:

    |       x
    |      xxx
    |    xxxxxxx
    |  xxxxxxxxxxx
    |xxxxxxxxxxxxxxx

Over time, you'll start having a plot that resembles the normal distribution. That's what the
central limit theorem states. It applies to the mean of a set as well as the sum.

As you sample size approaches infinity, the plot will approach a normal distribution.

For a lot of experiments, we don't know the actual probability distributions. That's why the central
limit theorem is useful - we always know that the frequencies of the mean approaches a normal
distribution.

# Sampling Distribution of the Sample Mean

The plots of the frequency of the means above are called the **sampling distribution of the sample
mean**. Let's dissect it:

* it's a plot of the sample mean
* it's a distribution of the means
* we derive if from sampling of experiments

The mean of the plots will have the same mean as your original probability distribution.

Sal reviews some terms: skew and kurtosis. Both are used to describe a distribution. Positive skew
means the peak is more towards the left with a long tail towards the right. Negative skew is the
opposite. Positive kurtosis means the peak is more narrow/pointy and longer tails. Negative kurtosis
means the peak is round and smaller tails on the sides.

When your sample size is larger, the sampling distribution of the sample mean has skew/kurtosis
closer to zero. It's a tighter normal distribution. This makes sense because when your sample size
is larger, you have better odds of getting closer to the mean.

Another way to say it: the standard deviation gets smaller.

# Standard Error of the Mean

The **standard error of the mean** is also known as the standard deviation of the sampling
distribution of the sample mean.

    SEM = s / sqrt(n)

Where `s` is the standard deviation and `n` is the sample size.

Sal reminds us that as our sample size increases, the distribution gets tighter and the standard
deviation decreases. So it makes sense, intuitively, that the standard error of the mean is
inversely proportional to the sample size.

The variance of the original probability distribution is equal to the variance of the sampling
distribution of sample mean divided by number of experiments:

    s(sampling dist)^2 = s(original dist)^2 / n

The standard error of the mean (aka standard deviation of sampling distribution) can be obtained by
just taking the square root of both sides.

# Sampling Distribution Example Problem

The average male drinks 2L of water when active outdoors with a standard deviation of .7L. You're
planning a full day nature trip for 50 men and will bring 110L of water. What's the probability
you'll run out?

    mu = 2L
    sigma = .7L

The probability of running out of water is the probability of using more than 110L of water. This is
the same as the probability of the average water use is greater than 2.2L (110L divided by 50 men)
per man:

    P(average water use > 2.2L per man)

Now let's figure out some properties of the sampling distribution of sample mean:

    mu(xbar) = mu = 2L
    sigma(xbar)^2 = sigma^2 / n
    sigma(xbar) = sigma / sqrt(n) = 0.7 / sqrt(50) = 0.099

Notice the standard deviation of the sample mean is much smaller than the standard deviation of the
population. The distribution will be much narrower.

We just need to figure out how many standard deviations 2.2L is away from the mean (known as the
z-score):

    2.2 - mu   2.2 - 2
    -------- = ------- = 2.02
     sigma      0.099

The probability that average water us > 2.2L per man is the same as probability that the sample mean
will be more than 2.02 standard deviations above the mean. Now you can use a z-table to figure out
that probability:

    0.9783 is the probability that we're less than 2.02 standard deviations
    above the mean
    P(running out of water) = 1 - .9783 = .0217

# Confidence Interval 1

**Confidence interval** indicates the reliability of an estimate.

# Mean and Variance of Bernoulli Distribution Example

Let's say we go out and survey the population. We'd ask them what they thought of the current
president. They have two options: unfavorable and favorable.

    |         x        unfavorable => 40%
    |    x    x        favorable   => 60%
    |____x____x_____
         U    F

In order to do calculations, we'll need to assign values to `U` and `F`. Let's assign `U = 0` and `F
= 1`.

    mu = .4 * 0 + .6 * 1 = 0.6
    sig^2 = .4(0 - .6)^2 + .6(1 - .6)^2 = 0.24
    sig = sqrt(0.24) = 0.49

This is an interesting case, the expected value is actually not a valid option for the survey.

The **Bernoulli Distribution** is a special case of the binomial distribution where the probability
of one result is equal to 1 minutes the probability of the other result.

# Bernoulli Distribution Mean and Variance Formulas

Here's a general Bernoulli Distribution:

    |         x        P(failure) = 1 - P(success)
    |    x    x        0 => 1 - P
    |____x____x_____   1 => P
         0    1

Let's generalize the calculations above so it works for any Bernoulli Distribution:

    mu = (1-P)*0 + P*1 = P
    sig^2 = (1-P)(0-P)^2 + P(1-P)^2 = P(1-P)
    sig = sqrt(P(1-P))

We're going to build on this later on during inferential statistics.

# Margin of Error #1

The **margin of error** expresses the amount of random sampling error in a survey results.

Let's say there's an election coming up and everyone is going to vote for either candidate A or
candidate B.

    |         x        B => P
    |    x    x        A => 1 - P
    |____x____x_____   mu = P
        A=0  B=1

Let's survey 100 people. 57 say they'll vote for A, 43 say they'll vote for B.

    xbar = 0.43
    s^2 = (57(0 - 0.43)^2 + 43(1 - 0.43)^2) / 99 = 0.2475
    s = 0.5

We can't figure out the standard error of the mean because we don't have the population standard
deviation. We can estimate it using the sample standard deviation though:

    SEM = sigma / sqrt(100)
    SEM estimate = 0.5 / sqrt(100) = 0.05

For any normal distribution, the probability of an outcome falling within two standard deviations is
roughly ~95.4%.

# Margin of Error #2

Now we want to find an interval such that we're "reasonably confident" that there is a 95% chance
that the true mean of the population (mu=P) is in that interval:

    P(xbar is within 2sig(xbar) of mu(xbar)) = 95.4%
    P(mu(xbar) is within 2sig(xbar) of xbar) = 95.4%
    P(P is within 2sig(xbar) of xbar) = 95.4%
    P(P is within 2*0.05 of xbar) =~ 95%
    P(P is within 0.1 of xbar) =~ 95%
    P(P is within 0.43 +/- 0.1) =~ 95%

This gives us a 95% confidence interval of 33% to 53%:

    43% will vote for candidate B
    57% will vote for candidate A
    margin of error: 10%

If you want a smaller margin of error, you'll need to increase your sample size. Increasing the
sample size will decrease your standard deviation of the mean, which will decrease the margin of
error.

# Hypothesis Testing and P-values

A neurologist is testing the effect of a drug on response time by injecting 100 rats with a unit
dose of the drug, subjecting each to neurological stimulus, and recording its response time. The
neurologist knows that the mean response time for rats not injected with the drug is 1.2 seconds.
The mean of the 100 injected rats' response times is 1.05 seconds with a sample standard deviation
of 0.5 seconds. Do you think that the drug has an effect on response time?

We're going to come up with two hypothesis. The null hypothesis is that the drug has no effect. The
null hypothesis will always be the status quo.

    H(0): Drug has no effect  =>  mu = 1.2 seconds (even with drug)
    H(1): Drug has an effect  =>  mu != 1.2 seconds when drug is given

The way to proceed is to assume the null hypothesis is true. Figure out the probability of the
results with the null hypothesis, if the probability is small then we can believe in the alternative
hypothesis.

    mu(xbar) = mu = 1.2s
    sig(xbar) = sig/sqrt(100) =~ s/sqrt(100) = 0.5/10 = 0.05

How many standard deviations away from the mean is 1.05 seconds?

    z = (1.2 - 1.05) / 0.05 = 3

Now that we have the z-score, we can figure out the probability of getting that value by looking it
up in the z-table (both in negative and positive directions).

* 99.7% probability that the result is within 3 standard deviations of mean
* 0.3% probability that it's 3 standard deviations away from mean

The 0.003 probability is known as the **P-value**.

If the null hypothesis was true, there is a 0.3% of our results occurring. Our alternative
hypothesis seems more likely. We're going to reject our null hypothesis.

# One-Tailed and Two-Tailed Tests

The test we did above was a two-tailed test, our alternative hypothesis was just that the drug had
no effect. If we wanted to do a one-tailed test:

    H(0): Drug has no effect; mu = 1.2 seconds (even with drug)
    H(1): Drug lowers response time; mu < 1.2 seconds when drug given

Let's say the drug doesn't lower our response time. What's the probability of getting the response
time at the lower extreme?

Now we're only considering only the left tail. The P-value is halved, or 0.15%.

# Z-statistics vs T-statistics

We've been plotting the sampling distribution of sample mean. We've also been asking "what's the
probability" of getting a result that's # standard deviations away from the sample mean:

                                   xbar - mu(xbar)
    how many standard deviations = ---------------
                                      sig(xbar)

`sig(xbar)` is the standard error of the mean, which can be calculated as:

    sig(xbar) = sig / sqrt(n)

We can substitute that into the equation above:

              xbar - mu(xbar)
    z-score = ---------------
               sig / sqrt(n)

This is a z-statistic. We can look up the probability using a z-table. We usually don't know what
`sig` is (standard deviation of the population). We can sub in the standard deviation of the sample
`s` instead:

               xbar - mu(xbar)
    z-score =~ ---------------
                 s / sqrt(n)

If your sample size is over 30, your standard deviation is going to be a good approximation. If it's
small, then it will no longer be a z distribution. It will be a **t-distribution** and you'll need
to use a **t-table** to get the probability. A t-distribution is similar to a normal distribution,
but it has fatter tails.

# Type 1 Errors

**Type 1 error** is also known as a **false positive**. It occurs when you reject the null
hypothesis even though it's true.

A **type 2 error** is a **false negative**. It occurs when you accept a null hypothesis that's
false.

When doing hypothesis testing, we usually have a probability threshold. For example, there's less
than a 1% chance of the experiment result to occur given that the null hypothesis is true. Since
it's so unlikely, we decide to reject the null hypothesis.

Another way to view it, there's a 1% chance that we made a type 1 error.

# Small Sample Hypothesis Test

The mean emission of all engines of a new design needs to be below 20 ppm to meet new requirements.
Ten engines are manufactured for testing and the emission level is determined for each:

    15.6 16.2 22.5 20.5 16.4 19.4 16.6 17.9 12.7 13.9

Does the data supply sufficient evidence to conclude this engine meets the new requirements? We are
willing to risk a Type 1 error with probability = 0.01.

    xbar = 17.17
    s = 2.98

Let's define what our null and alternative hypothesis are:

    H(0) = we don't meet our new requirements, mu = 20ppm
    H(1) = we do meet our new requirements, mu < 20ppm

Assume that `H(0)` is true. If the probability of getting a sample mean of `17.17` is less than 1%,
we can reject our null hypothesis.

Next, we need to think about what type of distribution to use. We have a small sample size so we're
going to be dealing with a t-distribution and t-statistic.

          17.7 - 20
    t = ------------- = -3.00
        2.98/sqrt(10)

T-tables usually only give positive values. T-distributions are symmetric around their means. Use
the t-table to figure out a t-value where the probability of getting a value below it is 99%.

Our sample size is `10` so we have `10 - 1 = 9` degrees of freedom. This is used to look up the
probability in the T-table.

The t-value threshold is -2.821. Our t-value is less than that, so it's less probable than 1%. From
that, we can reject our null hypothesis.

Based on the sample data, we can safely conclude this engine meets the new requirements.

# T-Statistic Confidence Interval

Let's use the same data from the last video to come up with a 95% confidence interval. The
thresholds for the t-score are:

    -2.262 < t-score < 2.262

Now we can plug in the formula for the t-score:
      
               17.7 - mu
    -2.262 < ------------- < 2.262
             2.98/sqrt(10)
    19.3 > mu > 15.05

There's a 95% probability that `19.3 > mu > 15.05` is true.

# Large Sample Proportion Hypothesis Testing

We want to test the hypothesis that more than 30% of US households have internet access (with a
significance level of 5%). We collect a sample of 150 households and find that 57 have access.

    H(0): P <= 30%
    H(1): P > 30%

Assume null hypothesis is true. Our sample proportion:

    pbar = 57/150 = 0.38

Our assumption distribution:

    |  x       P(H0) = 0.3
    |  x       0 => 70%
    |__x__x__  1 => 30%
       0  1

Now we need to figure out the z-score:

    mu(H0) = 0.3
    sig(H0) = sqrt(.3 * .7) = sqrt(.21)
    sig(pbar) = sig(H0) / sqrt(150) = 0.037

        pbar - mu(pbar)
    z = --------------- = 2.14
           sig(pbar)

We can look up the 95% probability in the z-table which is `1.65` (the critical z-value). Our actual
z-value is `2.14`, the probability of getting it is less than 5%. So we can reject our null
hypothesis and accept that more than 30% of US households have internet access.

# Variance of Differences of Random Variables

Let's review some statistics. Given that `X` and `Y` are independent random variables:

    E(X) = mu(X)
    E(Y) = mu(Y)
    var(X) = E((X - mu(X))^2) = sig(X)^2
    var(Y) = E((Y - mu(Y))^2) = sig(Y)^2

    Z = X + Y
    E(Z) = E(X + Y) = E(X) + E(Y)
    mu(Z) = mu(X) + mu(Y)
    var(Z) = var(X) + var(Y)
    sig(Z)^2 = sig(X + Y)^2 = sig(X)^2 + sig(Y)^2

    A = X - Y
    E(A) = E(X - Y) = E(X) - E(Y)
    mu(A) = mu(X) - mu(Y)
    var(A) = var(X) + var(Y)  <-- it's the sum, not the difference
    sig(A)^2 = sig(X - Y)^2 = sig(X)^2 + sig(-Y)^2

# Difference of Sample Means Distribution

Given two distributions and two different sampling distributions of the mean:

    z = xbar - ybar

`z` is another random variable that's just the difference between the two sampling means.

    mu(xbar - ybar) = mu(xbar) - mu(ybar)

The whole point of this is to eventually do inferential statistics about the difference of means. We
can ask questions like how likely the difference of mean is a random chance or not random chance. Or
what is the confidence interval of difference of means.

    sig(xbar - ybar)^2 = sig(xbar)^2 + sig(ybar)^2
    sig(xbar - ybar)^2 = sig(x)^2/n + sig(y)^2/m

Just take the square root of both sides to get the standard deviation:

    sig(xbar - ybar) = sqrt(sig(x)^2/n + sig(y)^2/m)

# Confidence Interval of Difference of Means

We're testing that a new diet helps obese people lose weight. 100 randomly assigned obese people are
assigned to group 1 placed on the diet. Another 100 are assigned to group 2 and placed on a normal
diet. After 4 months, the mean weight loss was 9.31 lbs for group 1 (s=4.67) and 7.40 lbs for group
2 (s=4.04).

    Low-Fat:
    x1bar = 9.31
    s1 = 4.67

    Control:
    x2bar = 7.40
    s2 = 4.04

    x1bar - x2bar = 9.31 - 7.4 = 1.91

The difference of the means is `1.91 lbs`. Let's get a 95% confidence interval around this number.
The critical z-value required for that is `1.96` standard deviations.

Let's construct an exact phrase of what we want:

    95% chance that mu(x1bar - x2bar) is within 1.96 sig(x1bar - x2bar) of
    1.91 lbs.

We need to figure out what `sig(x1bar - x2bar)` is:

    sig(x1bar - x2bar) = sqrt(s1^2/n1 + s2^2/n2)
    sig(x1bar - x2bar) = sqrt(4.67^2/100 + 4.04^2/100)
    sig(x1bar - x2bar) = 0.617

We can calculate our interval:

    1.96 * 0.617 = 1.21

We can reconstruct our confidence interval phrase:

    95% chance that mu(x1bar - x2bar) is 0.7 to 3.12 lbs

# Hypothesis Test for Difference of Means

Let's use the same data from the last video to do a hypothesis test:

    H0: diet does nothing
        mu1 - mu2 = 0 // aka population mean should be the same
        mu(xbar1) - mu(xbar2) = 0 // aka mean of sampling dist should be same
        mu(xbar1 - xbar2) = 0
    H1: diet does something
        mu1 - mu2 > 0
        mu(xbar1 - xbar2) > 0

We're going to assume that our null hypothesis is true. We need to pick a probability threshold and
if the probability of our result is past it, we can reject our null hypothesis. Our threshold will
be `95%`.

We need to figure out the critical z-value by looking at the z-table. At the `95%` threshold, the
critical z-value is `1.65`.

    1.65 * sig(xbar1 - xbar2)

We know the standard deviation from the last video:

    sig(xbar1 - xbar2) = 0.617

What this means is there's a 5% chance that the difference of the means is greater than `0.617 *
1.65 = 1.02`. The difference of the mean we got was `1.91`, which means there is a less than 5%
chance of that occurring.

We can reject our null hypothesis.

# Comparing Population Proportions 1

Let's say there's an election and you want to find out if there's a meaningful difference between
the proportion of men or women who vote for a candidate.

For the men:
* `P1` proportion voting for valued at `1`
* `(1-P1)` not votiing for valued at `0`
* `mu1 = P1`
* `sig1^2 = P1(1 - P1)`

For the women:
* `P2` proportion voting for valued at `1`
* `(1-P2)` not voting for valued at `0`
* `mu2 = P2`
* `sig2^2 = P2(1 - P2)`

We're going to come up with a 95% confidence interval for whether `P1 - P2` is significant or not.

Let's assign some concrete numbers. 1000 men, 642 vote for, the rest don't. 1000 women, 591 vote
for, the rest don't.

    P1 = mu1 = P1bar = 0.642
    P2 = mu2 = P2bar = 0.591

We're going to do some work with the sampling distribution:

    sig(P1bar)^2 = P1(1-P1)/1000
    sig(P2bar)^2 = P2(1-P2)/1000

Let's combine both sampling distributions so we can analyze the difference between the two data
sets:

    mu(P1bar - P2bar) = P1 - P2
    sig(P1bar - P2bar)^2 = P1(1-P1)/1000 + P2(1-P2)/1000
    sig(P1bar - P2bar) = sqrt(P1(1-P1)/1000 + P2(1-P2)/1000)

# Comparing Population Proportions 2

In this video we find the confidence interval. Note that `P1-P2=0.051`.

    95% chance that P1 - P2 is within d of 0.051

The z-table gives you a cumulative percentage up to a value. We're looking for a 95% chance with
2.5% on both tails. So look for 97.5% on the z-table. Our critical z-score is `1.96`.

    95% chance that P1 - P2 is within 1.96 * sig(P1bar - P2bar) of 0.051

We have the standard deviation of our sample (which is the best estimate for the standard deviation
of our population). We figured it out in the last video, its value is `0.022`.

    95% chance that 0.008 < P1 - P2 < 0.094

# Squared Error of Regression Line

Given many points on a graph, we want to find a line that minimizes the squared error. For each
point, the error is the vertical distance between the point and the line.

    y = mx + b

We're trying to find the `m` slope and `b` y-intercept. The error for each point is just the
difference between its y-value and the line's y-value or:

    error1 = y1 - (mx1 + b)

We want to minimize the square of the error:

    SE(line) = SIGMA (yi - (mxi + b))^2

The equation for `m` slope is:

        xbar*ybar - xybar
    m = -----------------
         xbar^2 - x^2bar

And the equation for `b` intercept is:

    b = ybar - m*xbar

# Regression Line Example

Let's get the regression line for these three points:

    (1,2), (2,1), (4,3)

We need to figure out some mean values:

    xbar = (1 + 2 + 4)/3 = 7/3
    ybar = (2 + 1 + 3)/3 = 2
    xybar = (1*2 + 2*1 + 4*3)/3 = 16/3
    x^2bar = (1^2 + 2^2 + 4^2)/3 = 7

With these values we can find the optimal slope and y-intercept:

        (7/3 * 2) - 16/3
    m = ---------------- = 3/7
          (7/3)^2 - 7

    b = 2 - (3/7)*(7/3) = 1

Our regression line is:

    y = (3/7)*x + 1

# R-Squared or Coefficient of Determination

The regression line attempted to minimize the square of the error:

    SE(line) = SIGMA (yi - (mxi + b))^2

Given a regression line, how much (what %) of the total variation in y is described by the variation
in x?

    SE(ybar) = total variation in y = SIGMA (yi - ybar)^2

If we divide it by `n`, you'd get the variance of y. Now we need to figure out how much of this
total variation is described by the variation in x.

What % of variation is **not** described by the regression line (variation in x)?

    SE(line) / SE(ybar)

We just want the leftover percentage which is the percentage of total variation described by the
regression line (variation in x):

    1 - SE(line)/SE(ybar)

This is also known as the **coefficient of determination** or **R-Squared**. Some properties of
R-Squared:

* if SE(line) is small, the line is a good fit
* if SE(line) is small, R^2 will be close to 1 and a lot of variation in y is described by variation
  in x
* if SE(line) is large, R^2 is close to 0 and very little variation in y is described by variation
  in x

# Covariance and the Regression Line

**Covariance** is the measure of how much two variables change together.

For the formula below, the expected value of X or Y can be thought of as its population mean:

    Cov(X,Y) = E[(X-E[X])(Y-E[Y])]

Every X and Y coordinates can be placed into the covariance formula. Let's use the coordinate `X=1,
Y=3` and we know `E[X] = 0, E[Y]=4`:

    Cov(1,3) = E[1 * -1]

X was above its expected value while Y was below its expected value. When they go in different
directions, the covariance is negative. If they both go up or both go down, the covariance is
positive.

Another way to describe covariance:

    Cov(X,Y) = XYbar - Ybar*Xbar

You'll notice that this formula is actually the numerator for the slope of the regression line. The
denominator for the slope could be viewed as Cov(X,X):

    Cov(X,X) = XXbar - Xbar*Xbar = X^2bar - Xbar^2

The covariance of a variable with itself is just the variance.

    Regression Line Slope = Cov(X,Y) / Cov(X,X)

# Chi-Square Distribution Introduction

Let's say X is normally distributed with a mean of 0 and variance of 1:

    X ~ N(0,1) or E[X] = 0 and Var(X) = 1

Let there be a random variable `Q`:

    Q = X^2

The distribution for the random variable Q is the Chi-Square Distribution.

    Q ~ Chi^2

The above means Q is a member of Chi squared. Since it's a sum of one independent variable, we say
it only has one degree of freedom. Let's say we have another random variable Q2:

    Q2 = X1^2 + X2^2

Q2 is a Chi Square distributed random variable with two degrees of freedom.

Q1 and Q2 are smooth curves. With three degrees of freedom, you'll start getting a vertical hump.
The more degrees of freedom you add, the further right the hump goes.

There's a Chi Square table which includes probabilities depending on the degrees of freedom.

# Pearson's Chi Square Test (Goodness of Fit)

We're thinking about buying a restaurant and we ask the owner for the distribution of customers:

           Day:   M   T   W   T   F   S
    Expected %:  10  10  15  20  30  15
      Observed:  30  14  34  45  57  20

Let's analyze this distribution to see if it fits the observed data. We'll do a hypothesis test with
a significance level of 5%:

    H0: owner's distribution is correct
    H1: owner's distribution is not correct

Assuming the owner's distribution is correct, what would have been the actual observed distribution?
Note that total customers is 200.

           Day:   M   T   W   T   F   S
    Expected %:  10  10  15  20  30  15
      Observed:  30  14  34  45  57  20
      Expected:  20  20  30  40  60  30

To calculate the Chi-Square statistic, for each day take the squared difference of each day and
divide by the expected:

    X^2 = (30-20)^2/20 + (14-20)^2/20 + (34-30)^2/30 +
          (45-40)^2/40 + (57-60)^2/20 + (20-30)^2/30 = 11.44

We're taking six sums, so we might be tempted to say there are 6 degrees of freedom. But the first
five determine the last sum, so we only have 5 degrees of freedom.

Is `11.44` a more extreme result than the critical Chi-Square value for our significance level of
5%? We'll look it up in the Chi-Square table.

Our critical Chi-Square value is 11.07. Our statistic is even less likely than that. So we're going
to reject our null hypothesis.

# ANOVA 1 - Calculating SST (Total Sum of Squares)

ANOVA stands for **analysis of variance**. It's a collection of statistical models and procedures
where observed variance is partitioned by sources.

We're going to be doing calculations on this data set to give us an intuitive sense on what analysis
of variance is all about:

    1:  2:  3:
    3   5   5
    2   3   6
    1   4   7

The sum of squares total can be viewed as the numerator when you calculate the variance. First,
let's calculate the grand mean (the mean of all means):

    xbarbar = (3 + 2 + 1 + 5 + 3 + 4 + 5 + 6 + 7)/9 = 4
    x1bar = (3 + 2 + 1)/3 = 2
    x2bar = (5 + 3 + 4)/3 = 4
    x3bar = (5 + 6 + 7)/3 = 6

We can use this information to calculate the sum of squares total:

    (3-4)^2 + (2-4)^2 + (1-4)^2 +
    (5-4)^2 + (3-4)^2 + (4-4)^2 +
    (5-4)^2 + (6-4)^2 + (7-4)^2 = 30

For the matrix with dimensions `m` by `n`, the degrees of freedom will be:

    m * n - 1 = 8

So we need to figure out how much of the total variation is coming from within each group or is
coming from between each group.

# ANOVA 2 - Calculating SSW and SSB (Total Sum of Squares Within And Between)

SSW means Sum of Squares Within. SSB means Sum of Squares Between. For SSW, we use xnbar instead of
xbarbar.

    SSW = (3-2)^2 + (2-2)^2 + (1-2)^2 +
          (5-4)^2 + (3-4)^2 + (4-4)^2 +
          (5-6)^2 + (6-6)^2 + (7-6)^2 = 6

Our total variation was 30, 6 of that 30 comes from the variation within these samples. Sal reasons
that each group has `n-1` degrees of freedom since you know the mean for each group. So there's 6
degrees of freedom.

Another way to think about SSB is how much variation is between the means of each group. For each
element in a group, calculate the squared difference between the grand mean and group mean:

    SSB = 3(2-4)^2 + 3(4-4)^2 + 3(6-4)^2 = 24

In this case there is 2 degrees of freedom `m-1`. If you know two means, you can calculate the third
mean since we know the grand mean.

    SSW = 6 with 6 degrees of freedom
    SSB = 24 with 2 degrees of freedom
    SST = 30 with 8 degrees of freedom

Notice that `SST = SSB + SSW`, even with the degrees of freedom.

# ANOVA 3 - Hypothesis Test with F-Statistic

We've been dealing with these numbers in the abstract but let's imagine that they were a part of an
experiment: Food #1, Food #2, Food #3. Does the type of food people take really affect their scores?
Is the difference purely random chance or can we be confident that the different would show up in
population means also?

    mu1 = mu2 = mu3 ?

Let's do a hypothesis test with confidence level of 10%.

    H0: Food doesn't make a difference or mu1 = mu2 = mu3
    H1: Food does make a difference

We're going to assume that H0 is true. Sal uses an F-statistic, which can be thought of as two
Chi-Square distributions:

                    SSB/(m-1)
    F-Statistic = -------------
                  SSW/(m*(n-1))

Let's think about this formula. If the numerator is much larger than the denominator, it tells us
the variation in the data is mostly due to the difference between groups telling us our null
hypothesis is not likely. If it's smaller than the denominator, the variation comes from within each
data set. That would make us believe that the difference between the means is random.

    F-Statistic = (24/2)/(6/6) = 12

Looking at our F-Table for the critical F-value using the degrees of freedom 2 and 6, the value is
3.46. We got 12, a much larger value. The probability of getting this is very low, we we reject our
null hypothesis.