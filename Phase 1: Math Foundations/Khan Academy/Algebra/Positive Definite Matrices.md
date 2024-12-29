# Positive Definite Matrices (Mathematics > Linear Algebra)

## Definition
A square matrix $A \in \mathbb{R}^{n \times n}$ is positive definite if it satisfies the following conditions:  
1. $A$ is symmetric: $A = A^\top$.  
2. For all nonzero vectors $x \in \mathbb{R}^n$, the quadratic form $x^\top A x > 0$.  

In formal terms, $A$ is positive definite if:  
$$x^\top A x > 0, \quad \forall x \neq 0 \in \mathbb{R}^n.$$

## Key Concepts
- Positive definiteness is a property of symmetric matrices.  
- The eigenvalues of a positive definite matrix are all positive.  
- The quadratic form $x^\top A x$ defines a strictly convex function.

## Important Properties
1. If $A$ is positive definite, then $A^{-1}$ exists and is also positive definite.
2. A matrix $A$ is positive definite if and only if all its principal minors are positive (Sylvester's criterion).
3. The Cholesky decomposition exists for positive definite matrices: $A = LL^\top$, where $L$ is a lower triangular matrix.

## Essential Formulas
- Quadratic form condition:  
  $$x^\top A x > 0 \quad \forall x \neq 0.$$
- Eigenvalue condition:  
  $$\lambda_i > 0, \quad \forall i,$$  
  where $\lambda_i$ are the eigenvalues of $A$.

## Core Examples
1. **Example 1**: The identity matrix $I \in \mathbb{R}^{n \times n}$ is positive definite because $x^\top I x = \|x\|^2 > 0$ for all $x \neq 0$.  
2. **Example 2**: For $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, $A$ is positive definite because:  
   - Symmetric: $A = A^\top$.  
   - Eigenvalues: $\lambda_1 = 3$, $\lambda_2 = 1$, both positive.  
   - Quadratic form: $x^\top A x = 2x_1^2 + 2x_2^2 + 2x_1x_2 > 0$ for all $x \neq 0$.  

## Related Theorems/Rules
- **Sylvester's Criterion**: A symmetric matrix is positive definite if all its leading principal minors are positive.
- **Cholesky Decomposition**: A positive definite matrix can be decomposed into $A = LL^\top$.

## Common Pitfalls
- Confusing positive definiteness with positive semi-definiteness, where $x^\top A x \geq 0$.  
- Assuming symmetry alone implies positive definiteness (symmetry is necessary but not sufficient).  
- Misinterpreting eigenvalues: Ensure all eigenvalues are strictly positive, not just non-negative.

## Related Topics
- [[Eigenvalues and Eigenvectors (Mathematics > Linear Algebra)]]
- [[Cholesky Decomposition (Mathematics > Linear Algebra)]]

## Quick Review Questions
1. Prove that the matrix $A = \begin{bmatrix} 4 & 1 \\ 1 & 3 \end{bmatrix}$ is positive definite.  
2. Explain why a matrix with at least one negative eigenvalue cannot be positive definite.
