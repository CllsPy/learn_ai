# Eigenvalues and Eigenvectors (Mathematics > Linear Algebra)

## Definition
An **eigenvalue** of a square matrix $A$ is a scalar $\lambda$ such that there exists a nonzero vector $\mathbf{v}$ (called an **eigenvector**) satisfying the equation:
$$
A\mathbf{v} = \lambda\mathbf{v}
$$
Here, $\mathbf{v}$ is the eigenvector associated with the eigenvalue $\lambda$.

## Key Concepts
- Eigenvalues represent the factors by which eigenvectors are scaled during a linear transformation.
- Eigenvectors are direction vectors that remain invariant (up to scaling) under the transformation.
- The equation $A\mathbf{v} = \lambda\mathbf{v}$ can be rewritten as $(A - \lambda I)\mathbf{v} = \mathbf{0}$.
- The eigenvalues are roots of the **characteristic polynomial** $\det(A - \lambda I) = 0$.

## Important Properties
1. A matrix $A$ has at most $n$ eigenvalues, where $n$ is the dimension of the matrix.
2. Eigenvalues can be real or complex, even if $A$ has real entries.
3. If $A$ is symmetric, all eigenvalues are real, and eigenvectors corresponding to distinct eigenvalues are orthogonal.

## Essential Formulas
- Characteristic equation:
$$
\det(A - \lambda I) = 0
$$
- Eigenvector equation:
$$
(A - \lambda I)\mathbf{v} = \mathbf{0}
$$
- Spectral decomposition (for diagonalizable matrices):
$$
A = Q\Lambda Q^{-1}
$$
where $Q$ contains eigenvectors and $\Lambda$ is the diagonal matrix of eigenvalues.

## Core Examples
1. **Basic Example**  
   For $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$:
   - Characteristic polynomial: $\det\begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = (\lambda-5)(\lambda-2)$.
   - Eigenvalues: $\lambda = 5$, $\lambda = 2$.
   - Eigenvectors: Solve $(A - 5I)\mathbf{v} = 0$ and $(A - 2I)\mathbf{v} = 0$.

2. **Advanced Example**  
   For $A = \begin{bmatrix} 1 & -1 \\ 1 & 3 \end{bmatrix}$:
   - Characteristic polynomial: $\det(A - \lambda I) = (\lambda - 2)^2$.
   - Eigenvalue: $\lambda = 2$ (with algebraic multiplicity $2$).
   - Eigenvectors: Solve $(A - 2I)\mathbf{v} = 0$.

## Related Theorems/Rules
- **Cayley-Hamilton Theorem**: Every square matrix satisfies its own characteristic equation.
- **Diagonalization**: A matrix is diagonalizable if it has $n$ linearly independent eigenvectors.
- [[Spectral Theorem]]: Symmetric matrices can be diagonalized using an orthogonal basis of eigenvectors.

## Common Pitfalls
- Confusing eigenvalues with singular values (related to the SVD).
- Forgetting that eigenvalues can be complex for real matrices.
- Assuming all matrices are diagonalizable.

## Related Topics
- [[Determinants and Matrices]]
- [[Diagonalization]]
- [[Spectral Theorem]]

## Quick Review Questions
1. How do you compute the eigenvalues of a $2 \times 2$ matrix?
2. What condition guarantees that a matrix has only real eigenvalues?
3. If $\lambda$ is an eigenvalue of $A$, what is the eigenvalue of $A^2$ corresponding to the same eigenvector?
