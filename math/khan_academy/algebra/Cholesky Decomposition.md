# Cholesky Decomposition (Mathematics > Linear Algebra)

## Definition
The **Cholesky decomposition** is a matrix factorization of a symmetric positive definite matrix $A$ into the product of a lower triangular matrix $L$ and its transpose:
$$
A = LL^\top
$$
where:
- $L$ is a lower triangular matrix with positive diagonal entries.
- $L^\top$ is the transpose of $L$.

This decomposition is used to simplify computations, particularly in numerical methods for solving linear systems.

## Key Concepts
- Only symmetric positive definite matrices can be decomposed using the Cholesky method.
- The decomposition is unique for such matrices.
- The Cholesky decomposition can be used to solve $A\mathbf{x} = \mathbf{b}$ efficiently by solving two triangular systems: $L\mathbf{y} = \mathbf{b}$ and $L^\top\mathbf{x} = \mathbf{y}$.

## Important Properties
1. The diagonal elements of $L$ are given by:
   $$
   L_{ii} = \sqrt{A_{ii} - \sum_{k=1}^{i-1} L_{ik}^2}
   $$
2. The off-diagonal elements of $L$ are computed as:
   $$
   L_{ij} = \frac{1}{L_{ii}} \left( A_{ij} - \sum_{k=1}^{i-1} L_{ik}L_{jk} \right) \quad \text{for } j > i
   $$
3. The Cholesky decomposition is numerically stable for well-conditioned matrices.

## Essential Formulas
1. Factorization formula:
   $$
   A = LL^\top
   $$
2. Solving $A\mathbf{x} = \mathbf{b}$:
   - Forward substitution: $L\mathbf{y} = \mathbf{b}$
   - Backward substitution: $L^\top\mathbf{x} = \mathbf{y}$

## Core Examples
1. **Basic Example**  
   For $A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}$:
   - $L = \begin{bmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{bmatrix}$ since:
     $$
     L_{11} = \sqrt{4} = 2, \quad L_{21} = \frac{2}{2} = 1, \quad L_{22} = \sqrt{3 - 1^2} = \sqrt{2}
     $$
   - $A = LL^\top = \begin{bmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 0 & \sqrt{2} \end{bmatrix}$.

2. **Advanced Example**  
   For $A = \begin{bmatrix} 25 & 15 & -5 \\ 15 & 18 &  0 \\ -5 &  0 & 11 \end{bmatrix}$:
   - Compute $L$ step by step using the formulas for diagonal and off-diagonal elements.

## Related Theorems/Rules
- **Positive Definiteness**: A matrix $A$ is positive definite if all its eigenvalues are positive.
- **LU Decomposition**: Cholesky decomposition is a specialized version of LU decomposition for symmetric positive definite matrices.

## Common Pitfalls
- Applying Cholesky decomposition to a matrix that is not symmetric positive definite (e.g., indefinite matrices will result in failure).
- Incorrectly assuming that all symmetric matrices are suitable for Cholesky decomposition.
- Numerical issues for nearly singular or poorly conditioned matrices.

## Related Topics
- [[LU Decomposition]]
- [[Positive Definite Matrices]]
- [[Numerical Linear Algebra]]

## Quick Review Questions
1. What type of matrices can be decomposed using the Cholesky method?
2. How is the Cholesky decomposition used to solve $A\mathbf{x} = \mathbf{b}$?
3. Why is the Cholesky decomposition numerically stable for positive definite matrices?
