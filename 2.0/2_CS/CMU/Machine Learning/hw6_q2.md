# 2 PAC Learning

Set of hypotheses $H=\{h:X\to\{0,1\}\}$

Set of possible target functions $C=\{c:X\to\{0,1\}\}$

The possible number of input value $|X|=2^n=2^{20}$

The possible number of label assignment: $2^{2^{20}}$

## 2.1

Yes. It contains all the possible label assignments.

## 2.2

The size of hypothesis space for $H_1$: $|H_1|=2^{2^{20}}$

## 2.3

$$m\ge \frac{1}{\epsilon}(ln|H_1|+ln(1/\delta))=100(2^{20}ln2+ln20)=72682050$$

## 2.4

No. The hypothesis space may not cover all the concept

## 2.5

$$|H_2|=2^{20\times19\times2\times2}$$

## 2.6

$$m\ge \frac{1}{\epsilon}(ln|H_2|+ln(1/\delta))=100(ln|H_2|+ln20)=105658$$

## 2.7

H2. Because it is simpler

