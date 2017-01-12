# Semi-Supervised Learning, Graphical Models

andrew id: dawang

## 2 Semi-Supervised Learning

### 2.1

adding two mails for smoothing, one contains the word, one not

\\[ \begin{align*}
P(Label_5=T) &= P(Label_5=T)\times\prod P(\omega_i\;|\;Label_5=T) \\
&=\frac{1}{2}\times P(linux=1\;|\;Label_5=T)\times P(credit=1\;|\;Label_5=T) \\
&=\frac{1}{2}\times \frac{0+1}{2+2} \times \frac{0+1}{2+2} \\
&=\frac{1}{32}
\end{align*} \\]

\\[ \begin{align*}
P(Label_5=F) &= P(Label_5=F)\times\prod P(\omega_i\;|\;Label_5=F) \\
&=\frac{1}{2}\times P(linux=1\;|\;Label_5=F)\times P(credit=1\;|\;Label_5=F) \\
&=\frac{1}{2}\times \frac{1+1}{2+2} \times \frac{1+1}{2+2} \\
&=\frac{1}{8}
\end{align*} \\]

According to the calculation above, we have:

$$P(Label_5=T\;|\;Email_5)=\frac{1}{5}$$

$$P(Label_5=F\;|\;Email_5)=\frac{4}{5}$$


### 2.2

adding two mails for smoothing, one contains the word, one not

\\[ \begin{align*}
P(Label_6=T) &= P(Label_6=T)\times\prod P(\omega_i\;|\;Label_6=T) \\
&=\frac{1}{2}\times P(reply=1\;|\;Label_6=T)\times P(to=1\;|\;Label_6=T) \times P(sale=1\;|\;Label_6=T) \\
&=\frac{1}{2}\times \frac{2+1}{2+2} \times \frac{2+1}{2+2} \times \frac{1+1}{2+2} \\
&=\frac{9}{64}
\end{align*} \\]

\\[ \begin{align*}
P(Label_6=F) &= P(Label_6=F)\times\prod P(\omega_i\;|\;Label_6=F) \\
&=\frac{1}{2}\times P(reply=1\;|\;Label_6=T)\times P(to=1\;|\;Label_6=T) \times P(sale=1\;|\;Label_6=T) \\
&=\frac{1}{2}\times \frac{1+1}{2+2} \times \frac{0+1}{2+2} \times \frac{0+1}{2+2} \\
&=\frac{1}{64}
\end{align*} \\]

According to the calculation above, we have:

$$P(Label_6=T\;|\;Email_6)=\frac{9}{10}$$

$$P(Label_6=F\;|\;Email_6)=\frac{1}{10}$$

### 2.3

The new Email(name $Email_7$) will be "to credit" and based on the result from the previous two parts, we have

\\[ \begin{align*}
P(Label_7=T\;|\;Email_7) &= P(Label_7=T)\times\prod P(\omega_i\;|\;Label_7=T) \\
&=\frac{2+\frac{1}{5}+\frac{9}{10}}{4+2}\times P(to=1\;|\;Label_7=T)\times P(credit=1\;|\;Label_7=T) \\
&=\frac{31}{60}\times \frac{2+\frac{9}{10}+1}{2+\frac{9}{10}+\frac{1}{5}+2} \times \frac{0+\frac{1}{5}+1}{2+\frac{1}{5}+\frac{9}{10}+2} \\
&= \frac{31}{60}\times \frac{39}{51} \times \frac{12}{51}\\
&=\frac{403}{3430}
\end{align*} \\]

\\[ \begin{align*}
P(Label_7=F\;|\;Email_7) &= P(Label_7=F)\times\prod P(\omega_i\;|\;Label_7=F) \\
&=\frac{2+\frac{4}{5}+\frac{1}{10}}{4+2}\times P(to=1\;|\;Label_7=F)\times P(credit=1\;|\;Label_7=F) \\
&=\frac{29}{60}\times \frac{0+\frac{1}{10}+1}{2+\frac{1}{10}+\frac{4}{5}+2} \times \frac{1+\frac{4}{5}+1}{2+\frac{1}{10}+\frac{4}{5}+2} \\
&=\frac{29}{60}\times \frac{11}{49} \times \frac{28}{49} \\
&=\frac{319}{1715}
\end{align*} \\]


As $P(Label_7=F\;|\;Email_7)$ < $P(Label_7=T\;|\;Email_7)$

The new email will be classified to T.

