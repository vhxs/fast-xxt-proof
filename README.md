# RXTX Proof of Correctness with SymPy

[This paper](https://arxiv.org/pdf/2505.09814) proposes an algorithm to compute XX^T, for any given matrix X, using fewer arithmetic operations than previous work. The algorithm is recursive and decomposes the problem into computing YY^T for matrices Y that is a quarter the of the size of X in each dimension.

Page 2 of the paper enumerates all equations to compute XX^T. These equations are complex. Hypothetically, one could verify by hand that the end result of the computing is in fact XX^T. This Python script uses SymPy to do it instead, and is essentially a proof of correctness of the algorithm.