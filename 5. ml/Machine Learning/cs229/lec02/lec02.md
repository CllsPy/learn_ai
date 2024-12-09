# Stanford CS229: Machine Learning - Linear Regression and Gradient Descent | Lecture 2 (Autumn 2018)

Outline

- Linear Regression
- Batch GD/ Stochastic GD
- Normal Equations

## Notes

In supervised learning we have:

train data [Size, Price] > Learning Algo. [Size] > Make Predictions H [Price]

$$ 
w =
\begin{bmatrix}
wo   \\
wi   \\
wii 
\end{bmatrix}
$$

$$ 
x =
\begin{bmatrix}
xo  \\
xi   \\
xii  
\end{bmatrix}
$$

wo = 1 and xo = 1. xi = size, xii = nº bedrooms

- we call w -> parameters.

Our learning algorithm job is choose, the best w.

- m -> number of rows (training exemples)
- x -> number of colums/features/inputs
- y -> output/arget
- (x, y) -> one training exemple
- $(x^{i}, y^{i})$ -> ith training exemple
- n (number of features,n=2)

Linear Regression Algorithm is also called.  **ordinary least squares**. We want a θ that, minimaze


$$\frac 1{2} \sum_{j=0}^{m} {(hθ(x^{i}) - y^{i})}^2$$ 

## Questions

- **How do we represente H (hypotesis)?**

    In Linear Regression, out h(x) = x*w + b, which is a linear equation.

    If we have, let's say, more features:

    - [size]
    - [nº bedrooms]

    we simple, multiply by it too, so: h(x) = xi*xii*w + b or $$\mathrm{h(x)} = \sum_{j=0}^{2} xjwj + b $$, where xo = 1.

- **How to we choose the parameters?**

    We need choose a w(theta) such that h(x) ~ y. For our (x, y), training exemples.

    hθ(x) = h(x)

