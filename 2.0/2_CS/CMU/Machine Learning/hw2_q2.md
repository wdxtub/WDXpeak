# Decision Trees

andrew id: dawang

## 2.1

(a) The entorpy will be

\\[ entropy = -\sum_{i=0}^{1}P(i)*log_2P(i) \\]

\\[ P(i) = \frac{(number\;of\;samples\;y=i)}{total numbers\;of\;samples} \\]

\\[ P(0) = \frac{4}{6} = 0.667\\]

\\[ P(1) = \frac{2}{6} = 0.333\\]

\\[ Entropy=-\frac{2}{3}*log_2(\frac{2}{3}) - \frac{1}{3}*log_2(\frac{1}{3})=0.918\\]

(b) The information gain of $X_1$ will be

\\[ C = [2+,4-]\\]

\\[ C_{X_1=T} = [2+,1-]\\]

\\[ C_{X_1=F} = [0+,3-]\\]

\\[ \begin{align*}
Gain(C,X_1) &= Entropy(C) - Entorpy(C|X_1) \\
&=0.918 - \frac{1}{2}(-\frac{2}{3}log_2\frac{2}{3}-\frac{1}{3}log_2\frac{1}{3}) - \frac{1}{2}(-\frac{3}{3}log_2\frac{3}{3}) \\
&=0.918-0.459-0 \\
&=0.459
\end{align*}\\]

## 2.2

(a) The entropy of Appealing is

\\[ Appealing = [5+,5-] \;\; +\;means\; Yes,\; -\;means\; No\\]

\\[ Entropy(Appealing)=-\frac{1}{2}log_2\frac{1}{2} - \frac{1}{2}log_2\frac{1}{2}=1
\\]

For Temperature

\\[ Temperature=Hot[2+,3-] \\]

\\[ Temperature=Cold[3+,2-] \\]

\\[ \begin{align*}
Gain(Appealing,Temperature) &= 1-\frac{5}{10}(-\frac{2}{5}log_2\frac{2}{5}-\frac{3}{5}log_2\frac{3}{5})\\
& -\frac{5}{10}(-\frac{3}{5}log_2\frac{3}{5}-\frac{2}{5}log_2\frac{2}{5}) \\
&= 0.029
\end{align*}\\]

For Taste

\\[ Taste=Salty[0+,3-] \\]

\\[ Taste=Sweet[2+,2-] \\]

\\[ Taste=Sour[3+,0-] \\]

\\[ Gain(Appealing,Taste)=1-0-\frac{4}{10}(-\frac{2}{4}log_2\frac{2}{4}-\frac{2}{4}log_2\frac{2}{4})-0=0.6\\]

For Size

\\[ Size=Small[4+,1-] \\]

\\[ Size=Small[1+,4-] \\]

\\[ \begin{align*}
Gain(Appealing,Size) &= 1-\frac{5}{10}(-\frac{4}{5}log_2\frac{4}{5}-\frac{1}{5}log_2\frac{1}{5})\\
& -\frac{5}{10}(-\frac{1}{5}log_2\frac{1}{5}-\frac{4}{5}log_2\frac{4}{5}) \\
&= 0.278
\end{align*}\\]
	
(b) The information gain for Taste as the root is the largest. So I use Taste as the root. Also we can learn from the data the Sour and Salty only have either positive or negative output, we get:

		     Taste
		   /\      \ 
	 Salty/  \Sour  \Sweet
		 /    \      \
		No    Yes
		
As the information gain of temperature for the second level is zero, I use Size for the seconde level. The tree will be:

		     Taste
		   /\      \ 
	 Salty/  \Sour  \Sweet
		 /    \      \
		No    Yes   Size
					 /\
		 	   Small/  \Large
			  	   /    \
				Yes      No

## 2.3

+ (a) The maximum training error will be $\frac{m-1}{m}$, Suppose we have m different category but all the trainning data is the same, in this case, we can clarify $\frac{1}{m}$ data correctly.
+ (b) No. With different node selections there may be one label is important in Tree A but useless in Tree B. As it is they don't need to have the same number of nodes.
+ (c) No. The boundary of a decision tree is not linear, so for a linear separated dataset, there could be some errors in the classification.


