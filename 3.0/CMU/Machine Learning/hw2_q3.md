# Perceptron and Neural Nets

andrew id: dawang

## 3.1 Perceptron

**3.1.1**

Based on the equaions from slides

\\[ \because ||X||_2 = 100 \leq R^2 \\]

\\[ \therefore R = 10 \\]

\\[ \because m < (\frac{R}{\gamma})^2 \\]

\\[ \therefore m < 100 \\]

\\[ \therefore m = 99 \\]

**3.1.2**

No. XOR function is not linearly separable.


## 3.2 Neural Networks

1. \\[ h_1=\frac{1}{1+exp(-\omega_{i_1,h_1}i_1)} = 0.623 \\]
2. \\[ h_2=\frac{1}{1+exp(-\omega_{i_1,h_2}i_1)} = 0.500 \\]
3. \\[ o_1=\frac{1}{1+exp(-\omega_{h_1,o_1}h_1 - \omega_{h_2,o_1}h_2)} = 0.378 \\] 
4. \\[ o_2=\frac{1}{1+exp(-\omega_{h_1,o_2}h_1 - \omega_{h_2,o_2}h_2)} = 0.628 \\] 
5. \\[ \delta_{o_1}=o_1(1-o_1)(t_1-o_1)=0.146 \\] 
6. \\[ \delta_{o_2}=o_2(1-o_2)(t_2-o_2)=0.087 \\] 
7. \\[ \delta_{h_1}=o_{h_1}(1-o_{h_1})(\omega_{h_1,o_1}\delta_{o_1}+\omega_{h_1,o_2}\delta_{o_2})=-0.0015 \approx -0.002 \\] 
8. \\[ \omega_{h_1,o_1} = \omega_{h_1,o_1} + \eta\delta_{o_1}x_{h_1} = -0.391\\]
9. \\[ \omega_{h_1,o_2} = \omega_{h_1,o_2} + \eta\delta_{o_2}x_{h_1} = 0.605\\]
10. \\[ \omega_{i_1,h_1} = \omega_{i_1,h_1} + \eta\delta_{h_1}x_{i_1} = 0.500\\]



