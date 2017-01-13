# 10-601 Final Project Proposal

*Da Wang(dawang) Jinhong Chen(jinhongc)*

## Features

We will use the following features in our machine learning algorithm: **Histogram of oriented gradients (HOG)**, **GIST descriptor**, **Bag-of-words**.

We would add a pre-processing stage in order to get the most significant features from the image including smoothing, whitening, etc. PCA method will also be applied to reduce the number of dimensions of the features to accelarate training and testing.

## Classifiers

We will use four different classifiers to see which one can reach the best performance: **Neural network**, **Support Vector Machine**, **KMeans**, **K-Nearest Neighbor**.

We'll also try some unsupervised learning algorithm to see the differences among different method.

## Methods

After extracting all the features from the training data, for supervised learning algorithm, we will train the classifiers with the training data to find the best parameter. For unsupervised learning algorithm, we will make different attempts with different initial point to check its performance. To avoid overfitting, k-fold validation will be applied.

All in all, we will as many combination of features and algorithms as possible to find the best solution for this image classification problem.
