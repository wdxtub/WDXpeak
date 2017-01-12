# Semi-Supervised Learning, Graphical Models

andrew id: dawang

## 5 Bayesian Network Inference

### 5.1 

$$ 
\begin{align*}
&P(A=false,B=false,C=false,D=false) \\
=\;&P(D=false\;|\; B=false,C=false)P(C=false\;|\; B=false)P(B=false\;|\; A=false)P(A=false) \\
=\;&0.1\times 0.8\times 0.6\times 0.8 \\
=\;&0.0384
\end{align*} 
$$

### 5.2

$$ 
\begin{align*}
&P(B=true,A=true,C=false) \\
=\;&P(A=true)P(B=true\;|\;A=true)P(C=false\;|\; B=true) \\
=\;&0.2\times 0.5\times 0.1 \\
=\;&0.01
\end{align*} 
$$

$$ 
\begin{align*}
&P(B=false,A=true,C=false) \\
=\;&P(A=true)P(B=false\;|\;A=true)P(C=false\;|\; B=false) \\
=\;&0.2\times 0.5\times 0.8 \\
=\;&0.08
\end{align*} 
$$

According to the calculation above:

$$P(B=true\;|\; A=true,C=false)=\frac{0.01}{0.01+0.08}=\frac{1}{9} $$

$$P(B=false\;|\; A=true,C=false)=\frac{0.08}{0.01+0.08}=\frac{8}{9} $$


### 5.3

$$ 
\begin{align*}
&P(D=false,A=false) \\
=\;&P(A=false)\sum_{b\in B}P(b\;|\;A=false)\sum_{c\in C}P(c\;|\; b)P(D=false\;|\;b,c) \\
=\;&0.8\times (0.4\times \sum_{c\in C}P(c\;|\;b=true)P(D=false\;|\;b=true,c) + 0.6\times \sum_{c\in C}P(c\;|\;b=false)P(D=false\;|\;b=false,c)) \\
=\;&0.8\times (0.4\times (0.9\times 0.01+0.1\times 0.02) + 0.6\times (0.2\times 0.05+0.8\times 0.1))) \\
=\;&0.04672
\end{align*} 
$$

$$ 
\begin{align*}
&P(D=true,A=false) \\
=\;&P(A=false)\sum_{b\in B}P(b\;|\;A=false)\sum_{c\in C}P(c\;|\; b)P(D=true\;|\;b,c) \\
=\;&0.8\times (0.4\times \sum_{c\in C}P(c\;|\;b=true)P(D=true\;|\;b=true,c) + 0.6\times \sum_{c\in C}P(c\;|\;b=false)P(D=true\;|\;b=false,c)) \\
=\;&0.8\times (0.4\times (0.9\times 0.99+0.1\times 0.98) + 0.6\times (0.2\times 0.95+0.8\times 0.9))) \\
=\;&0.75328
\end{align*} 
$$

According to the calculation above:

$$P(D=false\;|\; A=false)=\frac{0.04672}{0.04672+0.75328}=0.0584 $$

$$P(D=true\;|\; A=false)=\frac{0.75328}{0.04672+0.75328}=0.9416 $$


### 5.4

$$ 
\begin{align*}
&P(D=false,B=false) \\
=\;&\sum_{a\in A}P(a)P(B=false\;|\;a)\sum_{c\in C}P(c\;|\; B=false)P(D=false\;|\;B=false,c) \\
=\;&0.2\times 0.5\times \sum_{c\in C}P(c\;|\;B=false)P(D=false\;|\;B=false,c) + 0.8\times 0.6\times \sum_{c\in C}P(c\;|\;B=false)P(D=false\;|\;B=false,c) \\
=\;&0.1\times (0.2\times 0.05+0.8\times 0.1)+0.48\times (0.2\times 0.05+0.8\times 0.1) \\
=\;&0.0522
\end{align*} 
$$

$$ 
\begin{align*}
&P(D=true,B=false) \\
=\;&\sum_{a\in A}P(a)P(B=false\;|\;a)\sum_{c\in C}P(c\;|\; B=false)P(D=true\;|\;B=false,c) \\
=\;&0.2\times 0.5\times \sum_{c\in C}P(c\;|\;B=false)P(D=true\;|\;B=false,c) + 0.8\times 0.6\times \sum_{c\in C}P(c\;|\;B=false)P(D=true\;|\;B=false,c) \\
=\;&0.1\times (0.2\times 0.95+0.8\times 0.9)+0.48\times (0.2\times 0.95+0.8\times 0.9) \\
=\;&0.5278
\end{align*} 
$$

According to the calculation above:

$$P(D=false\;|\; B=false)=\frac{0.0522}{0.0522+0.5278}=0.09 $$

$$P(D=true\;|\; B=false)=\frac{0.5278}{0.0522+0.5278}=0.91 $$

### 5.5

According to figure 3, A and D are d-separated conditioned on B and C

$$ \therefore P(D=true\;|\;A=true,B=true,C=true)=P(D=true\;|\;B=true,C=true)=0.99 $$


