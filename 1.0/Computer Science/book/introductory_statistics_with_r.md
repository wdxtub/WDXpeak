# Introductory Statistics with R

Peter Dalgaard walks us through an introduction of R targeting the non-statistician. The text/code
have been updated to R version 2.6.2.

Go to <http://cran.r-project.org> to download the R language. A good IDE to use is RStudio and can
be found at <http://rstudio.org>.

Be sure to install thw `ISwR` package which stands for Introductory Statistics with R. Just run
`install.packages("ISwR")`.

# Basics

From the R console, load the `ISwR` package. Then try some commands:

    > library(ISwR)
    > 2 + 2
    > exp(-2)
    > rnorm(15)

Assignments use the `<-` operator and assign to **symbolic variables**. Names can be built from
alphanumeric characters and the period symbol. Names cannot start with a digit or period. Try not to
use single letter names because they might overwrite default functions or variables `c, q, t, C, D,
F, I, T`.

    > x <- 2

**Vectors** can be created with the `c` function:

    > weight <- c(60, 72, 57, 90, 95, 72)
    > height <- c(1.75, 1.80, 1.65, 1.90, 1.74, 1.91)
    > bmi <- weight/height^2
    [1] 19.59 22.22 20.93 24.93 31.37 19.73

You can perform operations on vectors. Usually the vectors have to be the same length. If a vector
is shorter, it gets recycled. In the example above, `2` represents a vector of 1 (**scalar**) and
gets recycled so all elements are divided by 2. Some other functions:

    > sum(weight)
    > xbar <- sum(weight)/length(weight)
    > stddev <- sqrt(sum((weight - xbar)^2)/(length(weight) - 1))
    > mean(weight)
    > sd(weight)

You can plot vectors or even customize the plotting character (`pch`).

    > plot(height, weight)
    > plot(height, weight, pch=2)

A person's expected BMI should be about 22.5 where `BMI = weight/height^2`. The `lines` function
will add a line to the current plot. The first argument is a vector of x coordinates, the second is
a vector of y coordinates.

    > hh <- c(1.65, 1.7, 1.75, 1.8, 1.85, 1.9)
    > lines(hh, 22.5 * hh^2)

Some of the basic aspects of the R language:

* **expressions** are entered and they all return a value (could be NULL)
* expressions work on **objects** which are anything that can be assigned a variable in R
* **functions** are commands like `plot(height, weight)` which have **actual arguments** and
  **formal arguments**. Actual arguments are the ones that are used in a call, formal arguments get
  connected to the actual call
* functions can use named actual arguments or **keyword matching** like `plot(x=height,y=weight)`.

Use the `ls()` function to list objects in scope. Use the `args()` function to get the formal
arguments of a function. A triple ... indicates that the function will accept varargs.

    > ls()
    > args(plot)
    function (x, y, ...)

Vectors can contain numbers, characters, boolean, or NA values. You can concatenate vectors or
create named/value pairs. Vectors of different types will be coerced into the least "restrictive"
type:

    > c('Huey', 'Dewey', 'Louie')
    > c("Huey", "Dewey", "Louie", "\"\n\"")
    > c(T, T, F, T)  # T == TRUE, F == FALSE
    > c(NA)
    > c(c(1,2,3), c(4,5,6), 7)
    > x <- c(red="Huey", blue="Dewey", green="Louie")
    > names(x)
    > x["red"]
    > c(FALSE, 3)
    [1] 0 3
    > c(pi, "abc")
    [1] "3.14159" "abc"

Long vectors can be created using the `seq` function. The first argument is the beginning, the last
argument is the end. The third optional argument is the increment count. If the step size is 1, you
can use the `:` operator. Use the `rep` function to repeat values:

    > seq(4, 9)
    [1] 4 5 6 7 8 9
    > seq(4, 10, 2)
    [1] 4 6 8 10
    > 4:9
    [1] 4 5 6 7 8 9
    > rep(c(1,2), 3)
    [1] 1 2 1 2 1 2
    > rep(c(1,2), c(3,4))
    [1] 1 1 1 2 2 2 2

Matrices can be created using the `dim()` assignment function or the convenient `matrix()` function.
You can set the headers with `rownames` and `colnames`. You can transpose with the `t()` function.

    > x <- 1:12
    > dim(x) <- c(3,4)  # 3 rows, 4 columns
    > matrix(1:12, nrow=3, byrow=T)  # byrow means fill rows first
    > rownames(x) <- LETTERS[1:3]    # or letters, month.name, month.abb
    > t(x)

**Factors** are like enums attached to data in Java or C. They let you categorize values in
experiments such as pain. To create one, you'll need numeric values for each **level** and a string
description:

    > actualpain <- c(0, 3, 2, 2, 1)
    > fpain <- factor(actualpain, levels=0:3)  # you can also used `ordered`
    > levels(fpain) <- c("none", "mild", "medium", "severe")
    > fpain
    [1] none severe medium medium mild
    Levels: none mild medium severe
    > as.numeric(fpain)
    [1] 1 4 3 3 2
    > levels(fpain)
    [1] "none" "mild" "medium" "severe"

R has a `list` construct which is more like an object with fields in other languages. Use the
`list()` function to make one and the `$` operator to access the fields in a list:

    > mylist <- list(before=1, after=c(2,3))
    > mylist
    $before
     [1] 1
    $after
     [1] 2 3
    > names(mylist)
    [1] "before" "after"
    > mylist$before
    > mylist$after
    > ls(mylist)

**Data frames** are made up of vectors of the same length. The individual components can be accessed
with the `$` operator:

    > frame <- data.frame(height, weight)
    > frame$height
    > frame$weight
    > frame[1][1]  # height at row 1
    > frame[1,]    # all measurements for row 1
    > frame[1:2,]  # first two rows
    > frame[frame$height > 21,]
    > head(frame)  # first six rows
    > tail(frame)  # last six rows

There are a few ways to grab elements in a vector and assign values:

    > height[1]
    > height[1] <- 20
    > height[c(1,2,3)]     # grab multiple elements
    > height[1,2,3]        # grab from matrix
    > height[1:3]
    > height[height > 19 & height < 21]

If `NA` occurs in the indexing vector, then R will return `NA`s. A useful function is the `is.na()`
function since `x==NA` will return `NA`.

It's natural to store grouped data in a data frame with one vector and have parallel factors in
another. With R, you can manually extract the data or use the `split` function.

    > sature <- factor(c(0, 1, 1, 0), levels=0:1)
    > levels(sature) <- c("lean", "obese")
    > expend <- c(7.5, 9.2, 6.4, 8.8)
    > energy <- data.frame(expend, sature)
    > energy
      expend  sature
      1  7.5  lean
      2  9.2  obese
      3  6.4  obese
      4  8.8  lean
    > exp.lean <- energy$expend[energy$sature=="lean"]
    > exp.obese <- energy$expend[energy$sature=="obese"]
    > l <- split(energy$expend, energy$sature)  # l$expend, l$sature

The `fapply` and `sapply` functions let you apply a function to a vector and collect the results.
`sapply` will try to simplify the results if possible:

    > fapply(vector, fn, na.rm=T)
    > sapply(vector, fn, na.rm=T)

Sorting is done with the `sort` function. There's also an `order` function which returns a
corresponding vector of indexes. This vector can be used to sort other vectors in parallel:

    > sort(vector)
    > order(vector)
    [1] 4 1 3 2

# The R Environment

Here are some common functions when dealing with your workspace:

    > ls()           # lists all variables
    > ls(list)       # lists variables in `list`
    > rm(var)        # removes a variable from workspace
    > rm(list=ls())  # removes all variables in workspace
    > save.image()   # saves current workspace to .RData file
    > load(".RData") # loads workspace
    > sink("myfile") # redirects stdout to a file
    > sink()         # re-establishes stdout to REPL

Some useful functions for working with scripts:

    > source("file")         # runs script
    > source("file", echo=T) # runs script and prints commands
    > savehistory("file")    # save REPL history to file
    > loadhistory("file")    # load REPL history
    > history()              # show current history

Some commands to get help or documentation:

    > help.start()       # opens the R manual
    > help(fn)           # print function's documentation
    > ?fn                # same as above
    > apropos("arg")     # finds functions starting with arg
    > help.search("arg") # uses fuzzy matching and deeper search

R packages are centralized on CRAN (Comprehensive R Archive Network) which currently hosts over 1000
packages. Installed libraries are just directories of code on your filesystem.

    > library()                 # currently installed packages
    > install.packages("IsWR")  # installs IsWR package
    > library(IsWR)             # loads package into workspace
    > detach("package:IsWR")    # removes package from workspace
    > help(package=IsWR)        # docs for IsWR 

Packages use **lazy loading** since data sets can get large. Some packages still require explicit
calls to `data`. This function goes through data directories of each package and loads anything
present. If files are present with the `.tab` extension, it'll use `read.table`. Other file
extensions exist for special treatment. You can make R look for variables in a data frame using the
`attach`, `detach`, and `with` functions.

    > data(thuesen) # searches for file with basename thuesen
    > thuesen$blood.glucose
    > thuesen$short.velocity
    > attach(thuesen) # attaches thuesen in system's search path
    > search()
      ... "thuesen" ...
    > blood.glucose
    > short.velocity
    > detach(thuesen)
    > with(thuesen, plot(blood.glucose, short.velocity))

`subset` and `transform` are useful functions to operate on vectors and data frames. `subset` will
filter out elements/rows, `transform` can be used to add additional information. `within` is a more
flexible alternative.

    > thue2 <- subset(thuesen, blood.glucose < 7)
    > thue3 <- transform(thuesen, log.gluc=log(blood.glucose))
    > thue4 <- within(thuesen, {
    +   log.gluc <- log(blood.glucose)
    +   m <- mean(log.gluc)
    +   centered.log.gluc <- log.gluc - m
    +   rm(m)
    + })

Let's try plotting something and adding to the plot:

    > x <- runif(50, 0, 2)  # random uniform distribution
    > y <- runif(50, 0, 2)
    > plot(x, y, main="Main title", sub="subtitle", 
    +            xlab="x-label", ylab="y-label")
    > text(0.5, 0.5, "text at (0.6, 0.6)")  # adds text to point
    > abline(h=.6, v=.6)  # adds a horizontal and vertical line
    > # loop through and add margin text
    > for(side in 1:4) mtext(-1:4, side=side, at=.7, line=-1:4)
    > mtext(paste("side", 1:4), side=1:4, line=-1, font=2)

In the example below, we're building a plot from pieces:

    > # type="n" means draw no points, axes=F means draw no axes
    > plot(x, y, type="n", xlab="", ylab="", axes=F)
    > points(x, y)
    > axis(1)
    > axis(2, at=seq(0.2, 1.8, 0.2)  # alternative set of ticks
    > box()
    > title(main="Main title" sub="subtitle", xlab="x-label", ylab="y-label")

`par` is a powerful function that lets you control various settings of the plot. The author says
it's pretty confusing and you should just play around with it to learn.

Let's plot a histogram and add an overlaying curve:

    > x <- rnorm(100)
    > hist(x, freq=F)         # plot by densities instead of absolute counts
    > curve(dnorm(x), add=T)  # add=T means add to existing plot

The top of the curve is cut off because the y-axis played no role for the curve. To fix this, we can
re-use the same y values for both plots and make the plot big enough to hold both:

    > h <- hist(x, plot=F)
    > ylim <- range(0, h$density, dnorm(0))
    > hist(x, freq=F, ylim=ylim)
    > curve(dnorm(x), add=T)

You can write your own functions in R:

    functionname <- function(arg1, arg2, arg3=default, ...) {
       # body of function goes here
    }

R also has conditional and looping constructs:

    while (condition) expression
    repeat {
      if (condition) break
    }
    for (variable in vector) expression

In R, objects have a `class` attribute. Some functions will change depending on what this attribute
is, like the `print` function.

    > print
    function (x, ...)
    UseMethod("print")  # using print on class htest will use print.htest

You can read in a space delimited file with `read.table`. The `header` option is a boolean flag for
whether or not headers are present. There's also a `read.csv` function for CSVs and `read.delim` for
tab delimited. `read.delim` allows you to specify your own delimiters. The flip side to reading are
the functions `write.table` and `write.csv`. Some notes:

* `sep` option to specify the field separator
* `na.strings` option to specify not available data (`"NA"` by default)
* `quote` option to specify which characters are used for quotes
* `comment.char` option to ignore certain lines in data
* `fill` and `flush` option to ignore errors of mismatch line lengths

R lets you edit data frames using a spreadsheet-like interface via `edit`:

    > aq <- edit(airquality)
    > fix(airquality)  # modifies airquality instead of returning new data
    > # start with a new spreadsheet
    > dd <- data.frame()
    > fix(dd)

# Probability and Distributions

R can pick random samples for you:

    > sample(1:40, 5)  # pick five numbers randomly from 1 to 40
    > sample(40, 5)    # same as above
    > sample(c("H", "T"), 10, replace=T)                    # simulate coin
    > sample(c("H", "T"), 10, replace=T, prob=c(0.9, 0.1))  # unfair coin

You can use it to calculate permutations and combinations:

    > prod(40:36)   # 40 * 39 * 38 * 37 * 36
    > choose(40, 5) # choose 40 items into 5 slots

The following functions can be used for normal distributions:

* `dnorm` for density
* `pnorm` for probability
* `qnorm` for quantile
* `rnorm` for random

There are parallel functions for binomial distributions:

* `dbinom` for density
* `pbinom` for probability
* `qbinom` for quantile
* `rbinom` for random

The density for a continuous distribution is a measure of the relative probability of "getting a
value close to x". It uses `dnorm`. To plot a bell curve:

    > x <- seq(-4, 4, 0.1)
    > plot(x, dnorm(x), type="l")     # l for line graph
    > curve(dnorm(x), from=-4, to=4)  # alternative plot

The type of plot "l" is a line graph. Use "h" for a histogram.

The cumulative distribution function describes the probability of "hitting" x or less in a given
distribution. It uses `pnorm` or `pbinom`.

Say a biochemical measure in healthy individuals is described by a normal distribution with a mean
of 132 and standard deviation of 13. What is the probability a patient has a value of 160?

    > 1 - pnorm(160, mean=132, sd=13)

`pnorm` returns the probability of getting a value smaller than its first arg in a normal
distribution.

The quantile function is the inverse of cumulative distribution function. There is a probability p
of getting a value less than or equal to the p-quantile. It uses the `qnorm` and `qbinom` functions.

`rnorm` and `rbinom` are used to generate pseudo-random numbers.

# Descriptive Statistics and Graphics

Here's how to obtain the mean, standard deviation, variance, median, and quantile:

    > x <- rnorm(50)
    > mean(x)
    > sd(x)
    > var(x)
    > median(x)
    > quantile(x)  # defaults to every 25%
    > quantile(x, seq(0, 1, 0.1))  # every 10%

The `juul` data set from the `ISwR` package contains variables from a insulin study. Let's do some
operations on it:

    > attach(juul)
    > mean(igf1)  # means insulin growth factor 1, returns NA
    > mean(igf1, na.rm=T)
    > sum(!is.na(igf1))  # length function has no na.rm argument
    > summary(igf11)
    > summary(juul)
    > detach(juul)

Let's set the correct types on our variables by setting some factors:

    > juul$sex <- factor(juul$sex, labels=c("M", "F"))
    > juul$menarche <- factor(juul$menarche, labels=c("No", "Yes"))
    > juul$tanner <- factor(juul$tanner,
                            labels=c("I","II","III","IV","V"))
    > attach(juul)
    > summary(juul)  # display changes for factor variables

A shortcut for the factor setting could have been:

    > juul <- transform(juul,
    +   sex=factor(sex,labels=c("M","F"))
    +   menarche=factor(menarche,labels=c("No","yes"))
    +   tanner=factor(tanner,labels=c("I","II","III","IV","V"))
    + )

A histogram gives a reasonable shape of a distribution with the `hist` function. You can specify
cutpoints with `breaks=n` where `n` is the number of bars.

    > mid.age <- c(2.5,7.5,13,16.5,17.5,19,22.5,44.5,70.5)
    > acc.count <- c(28,46,58,20,31,64,149,316,103)
    > age.acc <- rep(mid.age, acc.count)
    > brk <- c(0,5,10,16,17,18,20,25,60,80)
    > hist(age.acc, breaks=brk)

You can also plot the empirical cumulative distribution or change it to a qqplot with a built-in
function:

    > n <- length(x)
    > plot(sort(x), (1:n)/n, type="s", ylim=c(0,1))  # type s is step function
    > qqnorm(x)

A boxplot aka "box-and-whiskers plot" is a graphical summary of a distribution. The box in the
middle are "hinges" and median. The lines ("whiskers") show the largest or smallest observation that
falls within a distance of 1.5 times the box size from the nearest hinge. Other "extreme" values are
shown separately:

    > par(mfrow=c(1,2)) # specifies layout of plot
    > boxplot(IgM)
    > boxplot(log(IgM))
    > par(mfrow=c(1,1))

You can get summary statistics within groups, for example a table of means and standard deviations.
Use the `tapply` function.

    > attach(red.cell.folate)
    > xbar <- tapply(folate, ventilation, mean)  # split according to ventilation
    > s <- tapply(folate, ventilation, sd)
    > n <- tapply(folate, ventilation, length)
    > cbind(mean=xbar, std.dev=s, n=n)

The function `aggregate` is just like `tapply` but works on the entire data frame. The function `by`
takes an entire (sub-) data frame.

For grouped data, you may want to split it up before plotting. For example, let's split up two
histograms:

    > attach(energy)
    > expend.lean <- expend[stature=="lean"]
    > expend.obese <- expend[stature=="obese"]
    > par(mfrow=c(2,1))
    > hist(expend.lean,breaks=10,xlim=c(5,13),ylim=c(0,4),col="white")
    > hist(expend.obese,breaks=10,xlim=c(5,13),ylim=c(0,4),col="grey")
    > par(mfrow=c(1,1))
    > boxplot(expend.lean, expend.obese)  # boxplot instead of histogram

A stripchart is useful to show variations:

    > opar <- par(mfrow=c(2,2), mex=0.8, mar=c(3,3,2,1)+.1)
    > stripchart(expend ~ stature)
    > stripchart(expend ~ stature, method="stack")
    > stripchart(expend ~ stature, method="jitter")
    > stripchart(expend ~ stature, method="jitter", jitter=.03)
    > par(opar)

ASCII tables are useful too and can be assembled via `matrix`.

    > caff.marital <- matrix(c(652,1537,598,242,36,46,38,21,218,327,106,67),
                             nrow=3, byrow=T)
    > colnames(caff.marital) <- c("0, "1-500", "151-300", ">300")
    > rownames(caff.marital) <- c("Married", "Prev.married", "Single")
    > names(dimnames(caff.marital)) <- c("marital", "consumption")
    > caff.marital

You can use the `as.data.frame` and `as.table` functions to convert between tables and data frames:

    > as.data.frame(as.table(caff.marital))
    > table(sex)
    > table(sex, menarche)
    > table(menarche, tanner)
    > xtab(~ tanner + sex, data=juul)  # same as table, except uses formula
    > ftable(coma + diab ~ dgn, data=stroke)  # creates a flat table
    > t(caff.marital)  # to transpose

For graphical displays of tables, you can try using a `barplot`, `dotchart`, or `pie`:

    > total.caff < margin.table(caff.marital, 2)
    > barplot(total.caff, col="white")
    > par(mfrow=c(2,2))
    > barplot(caff.marital, col="white")
    > barplot(t(caff.marital), col="white")
    > barplot(t(caff.marital), col="white", beside=T)
    > barplot(prop.table(t(caff.marital),2), col="white", beside=T)
    > par(mfrow=c(1,1))

The `dotchart` looks like a horse race with the big dots representing a horse:

    > dotchart(t(caff.marital), lcolor="black")

The `pie` function is used to make piecharts:

    > opar <- par(mfrow=c(2,2), mex=0.8, mar=c(1,1,2,1))
    > slices <- c("white", "grey80", "grey50", "black")
    > pie(caff.marital["Married",], main="married", col=slices)
    > pie(caff.marital["Prev.married",],
          main="Previously married", col=slices)
    > pie(caff.marital["Single",], main="Single", col=slices)
    > par(opar)

# One- and Two-Sample Tests

The t tests assume that data comes from a normal distribution. The key concept of the t test is the
relationship between difference of means and the standard error of the mean (sigma = std deviation
of sample):

    SEM = sigma / sqrt(n)

For normally distributed data, 95% probability means being within `mu + 2sigma`. You can calculate
the t-score:

    t = (xbar - mu) / SEM

The t-score answers the question "how many standard deviations" away from the mean we want. For
large sets, this is a z-score.

The t-table will turn t-scores into probabilities. If you're looking for a 95% confidence interval:

    -2.262 < t-score < 2.262

Alternatively, R gives you a p-value which is the probability of the null hypothesis occuring. You
can use this to accept or reject your null hypothesis. Usually a p-value < 0.05 means you can reject
your null hypothesis.

Let's say you want to investigate a data set whether it deviated from the recommended value of 7725
kJ.

    > daily.intake <- c(5260,5470,5640,6180,6390,6515,6805,7515,7515,8230,8770)
    > mean(daily.intake)
    [1] 6753.636
    > sd(daily.intake)
    [1] 1142.123
    > quantile(daily.intake)
      0%  25%  50%  75% 100%
      5260 5910 6515 7515 8770

Assuming normal distribution:

    > t.test(daily.intake,mu=7725)

         One Sample t-test

     data:  daily.intake
     t = -2.8208, df = 10, p-value = 0.01814
     alternative hypothesis: true mean is not equal to 7725
     95 percent confidence interval:
      5986.348 7520.925
     sample estimates:
     mean of x
      6753.636

We get the t statistic (-2.8208), the associated degree of freedoms, and the exact p-value. You
won't need to look up the t value tables. In this case, p < 0.05 so data does deviate significantly
from the hypothesis that the mean is 7725.

The data also gives you a range for the true mean with a 95% confidence interval (5986.348 to
7520.925).

The last line is the actual mean of the sample.

The `t.test` function has some arguments that are useful. For the previous test, our alternative
hypothesis was an exact mean. We could also specify `alternative="greater"` or `alternative="less"`.
You can change the confidence intervals with `conf.level=0.99`.

Whereas the t test assumes normal distribution, the **Wilcoxon test** is useful for data sets that
aren't normally distributed. The function call works exactly like the t test:

    > wilcox.test(daily.intake, mu=7725)

A two sample t test can be performed on two different data sets. The hypothesis is that they come
from the same distributions with the same mean.

            xbar1 - xbar2
    t = ---------------------
        sqrt(SEM1^2 + SEM2^2)

The denominator is the standard error of difference of means. An alternative test is the Welch test
which can be used when the groups differe significantly in distribution and standard deviations.

    > energy
    expend stature
    1 9.21 obese
    2 7.53 lean
    3 7.48 lean
    ...
    20 7.58 lean
    21 9.19 obese
    22 8.11 lean
    > t.test(energy$expend ~ energy$stature)
    Welch Two Sample t-test
    data:  expend by stature
    t = -3.8555, df = 15.919, p-value = 0.001411
    alternative hypothesis: true difference in means is not equal to 0
    95 percent confidence interval:
     -3.459167 -1.004081
    sample estimates:
       mean in group lean mean in group obese
                 8.066154           10.297778

The tilde operator means that `energy$expend` is described by `energy$stature`. Your two data sets
are formed via two different categories (lean vs obese). Use the option `var.equal=T` to use the
traditional t test.

The `var.test` function lets you perform an F test, which compares the variances of two data sets:

    > var.test(expend~stature)

         F test to compare two variances

    data:  expend by stature
    F = 0.7844, num df = 12, denom df =  8, p-value = 0.6797
    alternative hypothesis: true ratio of variances is not equal to 1
    95 percent confidence interval:
      0.1867876 2.7547991
    sample estimates:
     ratio of variances
               0.784446

The Wilcoxon test also works with two samples:

    > wilcox.test(expend~stature)

The paired t test can be used when there are two measurements on the same experimental units. For
exmaple, measuring pre- and postmenstrual energy intake in a group of women. Since measurements are
taken before and after for the same women, a paired t test makes sense:

    > attach(intake)
    > intake
        pre post
    1  5260 3910
    2  5470 4220
    3  5640 3885
    ....
    > t.test(pre, post, paired=T)
           Paired t-test
    data:  pre and post
    t = 11.9414, df = 10, p-value = 3.059e-07
    alternative hypothesis: true difference in means is not equal to 0
    95 percent confidence interval:
      1074.072 1566.838
    sample estimates:
      mean of the differences
                     1320.455

If you had two independent groups, one for measuring pre- and one for measuring post-, you would do
a two-sample t test.

The Wilcoxon test also has a pair option:

    > wilcox.test(pre, post, paired=T)

# Regression and Correlation

Linear regression lets you describe the relation between two variables, for example describing
`short.velocity` as a function of `blood.glucose`. The linear regression model is:

    yi = alpha + beta*xi + error

The slope of the line is also known as the regression coefficient (beta). The line intersects the
y-axis at the intercept alpha. The parameters alpha, beta, and error can be estimated using the
method of least squares. Finding the values involves minimizing the sum of squared residuals:

    SSres = SIG(yi - (alpha + B*xi))^2

Use the function `lm` which stands for linear model for linear regression analysis:

    > attach(thuesen)
    > lm(short.velocity~blood.glucose)
    Call:
    lm(formula = short.velocity ~ blood.glucose)

    Coefficients:
      (Intercept)  blood.glucose
          1.09781        0.02196

The argument to `lm` is a model formula. This works for multiple linear regression analysis also
(`lm(y ~ x1 + x2 + x2)`). The output in this case includes the estimated intercept and slope.

    short.velocity = 1.098 + 0.0220 * blood.glucose

Use the `summary()` function to extract more information:

    > summary(lm(short.velocity~blood.glucose))
    Call:
    lm(formula = short.velocity ~ blood.glucose)

    Residuals:
         Min       1Q   Median       3Q      Max
    -0.40141 -0.14760 -0.02202  0.03001  0.43490

    Coefficients:
                  Estimate Std. Error t value Pr(>|t|)
    (Intercept)    1.09781    0.11748   9.345 6.26e-09 ***
    blood.glucose  0.02196    0.01045   2.101   0.0479 *
    ---

    Residual standard error: 0.2167 on 21 degrees of freedom
      (1 observation deleted due to missingness)
    Multiple R-squared: 0.1737,     Adjusted R-squared: 0.1343
    F-statistic: 4.414 on 1 and 21 DF,  p-value: 0.0479

The summary gives a quick distribution of the residuals. The average is zero by definition so the
median shouldn't be too far out. The residuals is the difference of the actual data from our
regression line on the y-axis.

The coefficients table gives you the slope for each variable (Estimate column) and accompanying
standard errors. The standard error tells us the accuracy of our prediction when using this linear
model.

The t-value and P-values are also given. More asterisks are given to values that are significant.

The residual standard error is also given. In this case, "1 observation deleted" means that one
value is NA in our data set.

R^2 is a statistic that gives information about the goodness of fit. It tells you how well the
regression line fits the data. An R^2 of 1 means the line fits the data perfectly. The adjusted R^2
takes into account the number of data points. This is valuable if you're adding/subtracting
predictor variables - it could decrease if your new predictor variable doesn't add anything to the
linear model.

The summary includes the F-statistic for the hypothesis that the regression coefficient is zero.

You can also use the extraction functions `fitted` and `resid`:

    > lm.velo <- lm(short.velocity~blood.glucose)
    > fitted(lm.velo)
           1        2        3        4        5        6        7 
    1.433841 1.335010 1.275711 1.526084 1.255945 1.214216 1.302066 
           8        9       10       11       12       13       14 
    1.341599 1.262534 1.365758 1.244964 1.212020 1.515103 1.429449
          15       17       18       19       20       21       22
    1.244964 1.190057 1.324029 1.372346 1.451411 1.389916 1.205431
          23       24
    1.291085 1.306459
    > resid(lm.velo)
               1            2            3            4            5
     0.326158532  0.004989882 -0.005711308 -0.056084062  0.014054962
               6            7            8            9           10
     0.275783754  0.007933665 -0.251598875 -0.082533795 -0.145757649
              11           12           13           14           15
     0.005036223 -0.022019994  0.434897199 -0.149448964  0.275036223
              17           18           19           20           21
    -0.070057471  0.045971143 -0.182346406 -0.401411486 -0.069916424
              22           23           24
    -0.175431237 -0.171085074  0.393541161

The fitted values are the y-values you'd expect for the given x-values according to the best fitting
straight line. The residuals are the difference between the fitted values and the observed values.

To get a good plot of the fitted vs residuals (and remove NAs):

    > plot(blood.glucose, short.velocity)
    > ablines(blood.glucose[!is.na(short.velocity)], fitted(lm.velo))

Narrow bands around the fitted line represents the confidence bands - the uncertainty of the line.
Wide bands are prediction bands - the uncertainty about future observations.

Use the `predict` function to extract the predicted values from a linear model. You can pass it an
`interval="confidence"` or `interval="prediction"` argument to get extra band information.

The second part of this chapter deals with correlation. The values given for correlation range from
-1 to +1, extremes indicate perfect correlation and 0 indicates no correlation. Negative correlation
means when one is small the other is large (anti-correlated).

    > cor(blood.glucose,short.velocity,use="complete.obs")
    [1] 0.4167546

Here we use `use="complete.obs"` to deal with the missing data. The `cor` function performs a linear
correlation or Pearson correlation by default. It works on vectors as well as data frames.

The output doesn't tell you if the correlation is significant. To get this and more information, use
`cor.test()`.

Spearman's method can be used for nonparametric variants:

    > cor.test(blood.glucose, short.velocity, method="spearman")

You can also use Kendall's method based on concordant and discordant pairs. Concordant means the
difference in the x-coordinate is of the same sign as the difference in the y-coordinate.

    > cor.test(blood.glucose, short.velocity, method="kendall")

# Analysis of Variance and the Kruskal-Wallis Test

This chapter starts with the one-way analysis of variance (ANOVA). It works by comparing the
variation within a group to the variation between groups. For more information, check out "Khan
Academy Statistics".

The descriptive variable needs to be a factor. The call to `anova` can use the model of a linear
regression if the predictor variable is a factor:

    > attach(red.cell.folate)
    > anova(lm(folate~ventilation))
    Analysis of Variance Table
    Response: folate
                Df Sum Sq Mean Sq F value  Pr(>F)
    ventilation  2  15516    7758  3.7113 0.04359 *
    Residuals   19  39716    2090

The top line has the sum of square distance between groups (variation between groups) and mean
square between groups (normalized variation against degrees of freedom). The bottom line has the sum
of square distance within groups and mean square within groups. The F value can be calculated like
so:

    F = MSb / MSw

`pairwise.t.test` computes possible two-group comparisons

    > pairwise.t.test(folate, ventilation, p.adj="bonferroni")
           Pairwise comparisons using t tests with pooled SD
    data:  folate and ventilation
              N2O+O2,24h N2O+O2,op
    N2O+O2,op 0.042      -
    O2,24h    0.464      1.000
    P value adjustment method: bonferroni

The output is a table of p-values. The `oneway.test` is an ANOVA that doesn't assume equal variance
among groups.

    > oneway.test(folate~ventilation)
        One-way analysis of means (not assuming equal variances)
    data:  folate and ventilation
    F = 2.9704, num df =  2.000, denom df = 11.065, p-value = 0.09277 

The Kruskal-Wallis test is a nonparametric counterpart of the one-way ANOVA.

    > kruskal.test(folate~ventilation)
       Kruskal-Wallis rank sum test
    data:  folate by ventilation
    Kruskal-Wallis chi-squared = 4.1852, df = 2, p-value = 0.1234

For a two-way ANOVA, your data needs to be in a vector with two parallel factors.

    > anova(lm(hr~subj+time))
    Analysis of Variance Table
    Response: hr
              Df Sum Sq Mean Sq F value    Pr(>F)
    subj       8 8966.6  1120.8 90.6391 4.863e-16 ***
    time       3  151.0    50.3  4.0696   0.01802 *
    Residuals 24  296.8    12.4

The output reads just like the one-way ANOVA.

# Tabular Data

This chapter is about tests used to analyze tabular data:

* `prop.test`
* `binom.test`
* `chisq.test`
* `fisher.test`

Tests of single proportions are based on the binomial distribution. Let's use the example where 39
of 215 randomly chosen patients have asthma. We want to test the hypothesis that the probability of
a "random patient" having asthma is 0.15:

    > prop.test(39,215,.15)
       1-sample proportions test with continuity correction
    data:  39 out of 215, null probability 0.15
    X-squared = 1.425, df = 1, p-value = 0.2326
    alternative hypothesis: true p is not equal to 0.15
    95 percent confidence interval:
      0.1335937 0.2408799
    sample estimates:
            p
    0.1813953

`prop.test` takes the number of positive outcomes, total outcomes, and the theoretical probability
to test for (50% by default). The function `binom.test` also works for binomial distributions.

`fisher.test` works on matrices where the first column is positive outcomes and the second column is
negative outcomes:

    > matrix(c(9,4,3,9),2)
         [,1] [,2]
    [1,]    9    3
    [2,]    4    9
    > lewitt.machin <- matrix(c(9,4,3,9),2)
    > fisher.test(lewitt.machin)
             Fisher's Exact Test for Count Data
    data:  lewitt.machin
    p-value = 0.04718
    alternative hypothesis: true odds ratio is not equal to 1
    95 percent confidence interval:
      0.9006803 57.2549701
    sample estimates:
    odds ratio
      6.180528

The standard Chi-Squared test can be done with `chisq.test` and the input/output is just like
`fisher.test`.

# Multiple Regression

This chapter is about regression analysis with multiple predictors.

    y = B0 + B1*x1 + ... + Bk*xk + error

Use the `pairs` to do pairwise scatterplots of your data set:

    > par(mex=0.5)
    > pairs(cystfibr, gap=0, cex.labels=0.9)

Let's with with this data set:

    > attach(cystfibr)

Specifying multiple dependencies can be done with `+`.

    > lm(pemax~age+sex+height+weight+bmp+fav1+rv+frc+tlc)

Which means `pemax` is described by using a model that is additive in `age`, `sex`, and so forth.
Using the `summary` function along with this model will give more output.

There's usually a large difference between adjusted and non-adjusted R^2 value for muliple linear
regression models. Adjusted R^2 values take into account the degrees of freedom.

You can also perform ANOVAs on multiple regressions:

    > anova(lm(pemax~age+sex+height+weight+bmp+fav1+rv+frc+tlc))

Dalgaard mentions the `step` function which can be used to perform model searches. It's beyond the
scope of the book, though. Instead, he shows us how to reduce our model by hand. Continue to remove
a single variables which aren't significant until you get your reduced model.

# Linear Models

Linear models provide a flexible framework that most data can be fitted. Or at least transformed
before fitted.

Linear models can still be made for polynomial regressions:

    > attach(cystfibr)
    > summary(lm(pemax~height+I(height^2)))

The `I()` function makes sure the model formula is protected. It's the identity function. This also
works with interacting predictors.

Sometimes it makes sense to create a model that goes through the origin. You can use the term `-1`
in your model which means minus intercept:

    > summary(lm(y~x-1))

The `model.matrix` function gives the design matrix for a given model. The results look like this.

Although the function `anova` can take two arguments which are the two groups of data, you can also
formally create a model for it. The next two lines are equivalent:

    > anova(lm(trypsin~grp), lm(trypsin~grpf))
    > anova(lm(trypsin~grp+grpf))

**Interaction terms** occur when the level of one predictor effects another. There's a level of
synergy. For example, a stroke is much more likely to occur at older ages or in males. But if a
subject is both elderly and male then the synergy of the two interacting terms creates a very high
probability.

Interaction can occur between two factors, one factor and one continuous variable, or two continuous
variables. Interactions in models are specified with `*` operator:

    > lm(time~width*temp)

It's usually good to get a graphic description of your data before trying to fit a model.

    > plot(conc,diameter,pch=as.numeric(glucose))
    > legend(locator(n=1),legend=c("glucose","no glucose"),pch=1:2)

`locator` returns the coordinates of a point on a plot. In this case, the plot will look much nicer
for a logarithmic x-axis scale. We can transform our data before trying to fit it.

    > plot(conc,diameter,pch=as.numeric(glucose),log="x")
    > lm(log10(diameter)~log10(conc),data=tethym.nogluc)

You can use any arithmetic expressions in a model formula. Sometimes, you'll have to surround your
expression with the `I()` identity function. This is the case for multiplication and addition to
avoid confusion with interacting and additive models.

# Logistic Regression

Logistic regression is all about modeling binary outcomes. A linear model for transformed
probabilities:

    logit p = B0 + B1*x1 + B2*x2 + ... + Bk*xk

The **log odds** is:

    logit p = log[p/(1-p)]

Logistic regression analysis belongs to the class of **generalized linear models** or the `glm`
function in R. These models are characterized by their binomial distributions. Let's do some
logistic regression on tabular data:

    > no.yes <- c("No","Yes")
    > smoking <- gl(2,1,8,no.yes)
    > obesity <- gl(2,2,8,no.yes)
    > snoring <- gl(2,4,8,no.yes)
    > n.tot <- c(60,17,8,2,187,85,51,23)
    > n.hyp <- c(5,2,1,0,35,13,15,8)
    > data.frame(smoking,obesity,snoring,n.tot,n.hyp)
      smoking obesity snoring n.tot n.hyp
      1      No      No      No    60     5
      2     Yes      No      No    17     2
      3      No     Yes      No     8     1
      4     Yes     Yes      No     2     0
      5      No      No     Yes   187    35
      6     Yes      No     Yes    85    13
      7      No     Yes     Yes    51    15
      8     Yes     Yes     Yes    23     8

First, you'll need to specify the response as a matrix where one column is success and the other is
failure.

    > hyp.tbl <- cbind(n.hyp,n.tot-n.hyp)
    > hyp.tbl
         n.hyp
    [1,]    5  55
    [2,]    2  15
    [3,]    1   7
    [4,]    0   2
    [5,]   35 152
    [6,]   13  72
    [7,]   15  36
    [8,]    8  15

Finally, use the `glm` function to create a logistic regression:

    > glm(hyp.tbl~smoking+obesity+snoring,family=binomial("logit"))

Note that "logit" is the default distribution so the family argument could be left off. R also lets
you specify the proportion of success/total.

    > prop.hyp <- n.hyp/n.tot
    > glm.hyp <- glm(prop.hyp~smoking+obesity+snoring,
    +                binomial,weights=n.tot)

The output is very similar to linear models. Use the `summary` function more more detailed output.
The "deviance" is the same as sum of squares in linear models. You can use it to pinpoint cells that
deviate from the fit (that are poorly fitted).

The "Residual deviance" is similar to the residual sum of squares in ordinary regression analysis.
The "null deviance" is the deviance of a model containing only the intercept.

Once you construct your model, pass it to `anova` to analyze the deviance. You can also pass it to
`confint` to get confidence intervals.

Just like normal linear models, you may pass it to `predict` or `fitted` function for more
information about residuals and data points.

# Survival Analysis

Survival analysis is the analysis of lifetimes. **Censorship** is an important concept in survival
analysis because it occurs so often. Data is said to be censored whenever we don't know the exact
lifetime of a subject - perhaps we don't know the exact time of death or the subject survived passed
the study time.

The **survival function** S(t) measures the probability of being alive at a given time. The **hazard
function** h(t) measures the risk of dying within a short interval of time t given the subject is
still alive at time t. The density function f(t) is given as:

    h(t) = f(t)/S(t)

In R, use the `survival` package for survival analysis. We'll work with the `melanom` data set:

    > library(survival)
    > attach(melanom)
    > names(melanom)
    [1] "no"     "status" "days"   "ulc"    "thick"  "sex"

The `Surv` function is used to create an object used in survival analysis.

    > Surv(days, status==1)
    ...
    [181] 3476+ 3523+ 3667+ 3695+ 3695+ 3776+ 3776+ 3830+ 3856+ 3872+
    [191] 3909+ 3968+ 4001+ 4103+ 4119+ 4124+ 4207+ 4310+ 4390+ 4479+
    [201] 4492+ 4668+ 4688+ 4926+ 5565+

The Kaplan-Meier estimator is implemented with `survfit`.

    > survfit(Surv(days, status==1))
    Call: survfit(formula = Surv(days, status == 1))
          n  events  median 0.95LCL 0.95UCL
        205      57     Inf     Inf     Inf

More information is given with the `summary` function:

    > summary(survfit(Surv(days, status==1)))
    Call: survfit(formula = Surv(days, status == 1))
     time n.risk n.event survival std.err lower 95% CI upper 95% CI
     ...

Censoring times aren't displayed. Use `censored=T` to show them. This method is a step function with
jump points given in `time` and values right after a jump given the `survival` column.

You can plot the `Surv` object to see it graphically. You can even distinguish plots by a factor:

    > plot(survfit(Surv(days, status==1)))
    > plot(survfit(Surv(days, status==1)~sex))

The log-rank test can be used to compare two survival curves. It compares the survival rate and
survivors at each point in time. It's implemented by the `survdiff` function:

    > survdiff(Surv(days,status==1)~sex)
    Call:
    survdiff(formula = Surv(days, status == 1) ~ sex)
            N Observed Expected (O-E)^2/E (O-E)^2/V
    sex=1 126       28     37.1      2.25      6.47
    sex=2  79       29     19.9      4.21      6.47
    Chisq= 6.5  on 1 degrees of freedom, p= 0.011

The Cox proportional hazards model analyzes survival data by regression models similar to `lm` and
`glm`. It's implemented by the `coxph` function.