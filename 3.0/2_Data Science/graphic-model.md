# Graphic Model 学习笔记

+ A compact wawy to represent joint distributions
+ Useful to query various conditional probabilites
+ A powerful language to model real-world systems
+ Easy to plug in prior knowledge
+ Extremely widely used

## Graphcial model notation

+ Nodes: variables (with domains)
	+ Can be assigned (observed) or unassigned (unobserved)
+ Arcs: iteractions
	+ Indicate "direct influence" between variables
	+ Formally: encode conditional independence

## Probabilities in BNs

Bayes nets implicitly encode joint distributions.

+ As a product of local conditional distributions
+ To see what probability a BN gives to a full assignment, multiply all the relevant conditionals together

$$P(x_1,x_2,...,x_n)=\prod_{i=1}^n P(x_i\;|\;parents(X_i))$$

## Causal Chains

$$X \to Y \to Z$$

$$P(x,y,z)=P(x)P(y|x)P(z|y)$$

Is X independent of Z given Y?

$$\because P(z|x,y)=\frac{P(x,y,z)}{P(x,y)}=\frac{P(x)P(y|x)P(z|y)}{P(x)P(y|x)}=P(z|y)$$

Answer is Yes. Evidence along the chain "blocks" the influence.

---

Another configuration

$$X \gets Y \to Z$$

+ Are X and Z independent? No
+ Are X and Z independent given Y? Yes

$$\because P(z|x,y)=\frac{P(x,y,z)}{P(x,y)}=\frac{P(y)P(x|y)P(z|y)}{P(y)P(x|y)}=P(z|y)$$

Observing the cause blocks influence between effects

---

Last configuration: two causes of one effect(v-structures)

$$X \to Y \gets Z$$

+ Are X and Z independent? Yes
+ Are X and Z independent given Y? No

This is backwards from the other cases. Observing an effect activates influence between possible causes.  

---

The general case

+ Any complex example can be analyzed using these three canonical cases
+ General question: in a given BN, are two variables independent (given evidence)?

## Probabilistic Inference

Posterior probabilities: Probabilityof any even given any evidence

### Bayesian inference

+ Bayesian probability treats parameters as random variables
+ Learning / parameter estimation is replaced by probabilistic inference $P(\theta|D)$

Pros

+ Elegant - no distinction between parameters and other hidden variables
+ Can us priors to learn from small data sets

Cons

+ Math can get hairy
+ Often computatoinally intractable


