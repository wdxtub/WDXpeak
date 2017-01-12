# Semi-Supervised Learning, Graphical Models

andrew id: dawang

## 6 Bayesian Networks Learning

For the first E step, with any given combination of A, B, D, there is only one possible answer for C=1 and another one for C=2,

So, we have

1. $P(C_{17}=1\;|\;A_{17},B_{17},C_{17}) = \frac{\frac{1}{16}}{\frac{1}{16}+\frac{1}{16}}=\frac{1}{2}$
2. $P(C_{17}=0\;|\;A_{17},B_{17},C_{17}) = \frac{\frac{1}{16}}{\frac{1}{16}+\frac{1}{16}}=\frac{1}{2}$

For the first M step, the value of C can be both 1 and 0 with equal posibility, so we can treat the 17th sample as a sample with 0.5 weight for C=1 and C=0

So, we have

$P(C=0\;|\;B=1)=\frac{4+\frac{1}{2}}{8+1}=\frac{1}{2}$

$P(C=1\;|\;B=1)=\frac{4+\frac{1}{2}}{8+1}=\frac{1}{2}$

$P(C=0\;|\;B=0)=\frac{4}{8}=\frac{1}{2}$

$P(C=1\;|\;B=0)=\frac{4}{8}=\frac{1}{2}$

If we stop here

$$ 
\begin{align*}
&P(A=0,B=1,C=0,D=1) \\
=\;&P(A=0)\times P(B=1\;|\;A=0)\times P(C=0\;|\;B=1)\times P(D=1\;|\;B=1,C=0) \\
=\;&\frac{9}{17}\times \frac{5}{9}\times \frac{1}{2}\times \frac{4}{9} \\
=\;&\frac{10}{153}
\end{align*} 
$$

For the second E step

$$P(A=0,B=1,C=0,D=1)=\frac{9}{17}\times \frac{5}{9}\times \frac{1}{2}\times \frac{5}{9}=\frac{25}{306}$$

$$P(A=0,B=1,C=1,D=1)=\frac{9}{17}\times \frac{5}{9}\times \frac{1}{2}\times \frac{5}{9}=\frac{25}{306}$$

According to the calculation above

$$P(C_{17}=1\;|\;A_{17},B_{17},C_{17})=\frac{1}{2}$$


