# Linear Regression

andrew id: dawang

## 1.1 

**1.1.1**

> Show that $$E[\omega]=beta$$ 

\\[ \omega = (X^TX)^{-1}X^T(X\beta+\epsilon) \\]

\\[ \begin{align*}  E[\omega] &=E[(X^TX)^{-1}X^TX\beta+(X^TX)^{-1}X^T\epsilon] 
\\ 
&=E[(X^TX)^{-1}X^TX\beta]+E[(X^TX)^{-1}X^T\epsilon] 
\\
&=E[\beta]+E[E[(X^TX)^{-1}X^T\epsilon|X]]
\\
&=\beta+E[(X^TX)^{-1}X^TE[\epsilon \mid X]] 
\\
&=\beta+E[(X^TX)^{-1}X^T \times0]
\\
&=\beta
\end{align*} \\]

**1.1.2**

+ No. The data from two different columns are the same means they are linearly dependent thus the matrix is not invertible.
+ No. Sames reason as above

## 1.2 

**1.2.1**

\\[condition number = 22.155 \\]

\\[ E[\omega] = \beta = \left[
\begin{array}{cc}
0  \\
1 
\end{array}
\right]\\]

\\[ Cov[\omega] = \sigma^2[(X^TX)^{-1}] = \left[
\begin{array}{cc}
1.000 & -1.000  \\
-1.000 & 1.200 
\end{array}
\right]\\]

codes for simulationg process and plotting the data

```matlab
X=[-1 -1.5;0 0.5;1 0.5;2 1.5];
b = [0 1]';

epsilons = zeros(4,50);
ydata = zeros(4,50);
wset = zeros(2,50);
errorset = zeros(1,50);

for i = 1:50
    epsilons(:,i) = normrnd(0,1,[4 1]);
    ydata(:,i) = X*b + epsilons(:,i);
    wset(:,i) = (X'*X)\X'*ydata(:,i);
    errorset(i) = norm(wset(:,i)-b);
end

empiricalMean = mean(wset,2);
empiricalCov = cov(wset');

subplot(231);
hist(errorset);
title('error');
subplot(232);
scatter(wset(1,:),wset(2,:));
title('lse w');
subplot(233);
qqplot(wset(1,:));
title('qqplot(w1)');
subplot(236);
qqplot(wset(2,:));
title('qqplot(w2)');

ytest = zeros(1,50);

for i = 1:50
    ytest(i) = wset(:,i)'*xtest' + normrnd(0,1);
end

subplot(234);
hist(ytest);
title('ytest');
```

$$ empirical\;mean\;of\;\omega = \left[
\begin{array}{cc}
0.0275  \\
1.0518 
\end{array}
\right]$$

$$ empirical\;covariance\;of\;\omega = \left[
\begin{array}{cc}
1.2847 & -1.2378  \\
-1.2378 & 1.3569 
\end{array}
\right]$$

The following is the plotting result(Including the result for Q1.2.3 in subplot 4)

![Part1][1]

**1.2.2**

\\[condition number = 7.6984e+03\\]

\\[ E[\omega] = \beta = \left[
\begin{array}{cc}
0  \\
1 
\end{array}
\right]\\]

\\[ Cov[\omega] = \sigma^2[(X^TX)^{-1}] = \left[
\begin{array}{cc}
320.500 & -310.000  \\
-310.000 & 300.000 
\end{array}
\right]\\]

codes for simulationg process and plotting the data

```matlab
X=[-1 -1;0 0;1 1;2 2.1];
b = [0 1]';

epsilons = zeros(4,50);
ydata = zeros(4,50);
wset = zeros(2,50);
errorset = zeros(1,50);

for i = 1:50
    epsilons(:,i) = normrnd(0,1,[4 1]);
    ydata(:,i) = X*b + epsilons(:,i);
    wset(:,i) = (X'*X)\X'*ydata(:,i);
    errorset(i) = norm(wset(:,i)-b);
end

empiricalMean = mean(wset,2);
empiricalCov = cov(wset');

subplot(231);
hist(errorset);
title('error');
subplot(232);
scatter(wset(1,:),wset(2,:));
title('lse w');
subplot(233);
qqplot(wset(1,:));
title('qqplot(w1)');
subplot(236);
qqplot(wset(2,:));
title('qqplot(w2)');

ytest = zeros(1,50);

for i = 1:50
    ytest(i) = wset(:,i)'*xtest' + normrnd(0,1);
end

subplot(234);
hist(ytest);
title('ytest');
```

$$ empirical\;mean\;of\;\omega = \left[
\begin{array}{cc}
2.2932  \\
-1.3549 
\end{array}
\right]$$

$$ empirical\;covariance\;of\;\omega = \left[
\begin{array}{cc}
293.4265 & -283.1638  \\
-283.1638 & 273.4028 
\end{array}
\right]$$

The following is the plotting result(Including the result for Q1.2.3 in subplot 4)

![Part2][2]

**1.2.3**

The result can be seen from the figures in q1.2.1 & q1.2.2

**1.2.4**

+ Yes for part1, No for part2. Because for part 2 the condition number is so big that the error will also be big.
+ The distribution of $\omega$ is close to a straight line in `qqplot`. So it can be regarded as normal distribution.
+ Experiment1. With a smaller condition number, the data can be calculated with less errors.
+ No. $X_1$ and $X_2$ are positively correlated. So if $X_2$ becomes $-X_2$, the result will be just the opposite, that is $\omega_1$ and $\omega_2$ will be positive correlated.




  [1]: http://7xk3yi.com1.z0.glb.clouddn.com/mlhw2q1part1.jpg
  [2]: http://7xk3yi.com1.z0.glb.clouddn.com/mlhw2q1part2.jpg

