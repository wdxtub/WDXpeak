# 作业中相关概念

<!-- MarkdownTOC -->

- Invertible Matrix Theorem
- MLE and MAP

<!-- /MarkdownTOC -->


## Invertible Matrix Theorem

The invertible matrix theorem is a theorem in linear algebra which gives a series of equivalent conditions for an n×n square matrix A to have an inverse. In particular, A is invertible if and only if any (and hence, all) of the following hold:

1. A is row-equivalent to the n×n identity matrix I_n.
2. A has n pivot positions.
3. The equation Ax=0 has only the trivial solution x=0.
4. The columns of A form a linearly independent set.
5. The linear transformation x|->Ax is one-to-one.
6. For each column vector b in R^n, the equation  Ax=b has a unique solution.
7. The columns of A span R^n.
8. The linear transformation x|->Ax is a surjection.
9. There is an n×n matrix C such that CA=I_n.
10. There is an n×n matrix  D such that AD=I_n.
11. The transpose matrix A^(T) is invertible.
12. The columns of A form a basis for R^n.
13. The column space of A is equal to R^n.
14. The dimension of the column space of A is n.
15. The rank of A is n.
16. The null space of A is {0}.
17. The dimension of the null space of A is 0.
18. 0 fails to be an eigenvalue of A.
19. The determinant of A is not zero.
20. The orthogonal complement of the column space of A is {0}.
21. The orthogonal complement of the null space of A is R^n.
22. The row space of A is R^n.
23. The matrix A has n non-zero singular values.

## MLE and MAP

MAP uses Bayes with a prior estimation while MLE just find the maximum value of probability.

