# Semi-Supervised Learning, Graphical Models

andrew id: dawang

## 1 Probability

### 1.1

X and Y are independent.

\\[ 
P(X=1)=0.5 \\
P(X=0)=0.5 \\
P(Y=1)=0.25 \\
P(X=0)=0.75 
\\]

\\[ 
P(X=1|Y=0) = P(X=1) = 0.5 \\
P(X=0|Y=0) = P(X=0) = 0.5 \\
P(X=1|Y=1) = P(X=1) = 0.5 \\
P(X=0|Y=1) = P(X=0) = 0.5 \\
we\;have\;\forall (i,j)\;P(X=x_i|Y=y_j) = P(X=x_i) 
\\]

### 1.2

X and Y are not independent if conditioned on Z. (Z=X+y)

\\[
P(X=1|Z=0)=0 \\
P(X=0|Z=0)=1 \\
P(X=1|Z=1)=\frac{3}{4} \\
P(X=0|Z=1)=\frac{1}{4} \\
P(X=1|Z=2)=1 \\
P(X=0|Z=2)=0 \\
but \; P(X=1|Y=0,Z=1)=1 \ne P(X=1|Z=1)
\\]

### 1.3

X and Y are not independent if conditioned on W. (W=XY)

\\[
P(X=1|W=0)=\frac{3}{7} \\
P(X=0|W=0)=\frac{4}{7} \\
P(X=1|W=1)=1 \\
P(X=0|W=1)=0 \\
P(X=1|Y=0,W=0)=0.5 \ne P(X=1|W=0) \\
P(X=0|Y=0,W=0)=0.5 \ne P(X=0|W=0) \\
P(X=1|Y=1,W=0)=0 \ne P(X=1|W=0) \\
P(X=0|Y=1,W=0)=1 \ne P(X=0|W=0) 
\\]

### 1.4

X and Y are not independent if conditioned on C.

Suppose

+ X - Your first coin flip is heads
+ Y - Your second coin flip is heads
+ C - Your first two flips were the same

A and B here are independent. However, A and B are conditionally dependent given C, since if you know C then your first coin flip will inform the other one.


