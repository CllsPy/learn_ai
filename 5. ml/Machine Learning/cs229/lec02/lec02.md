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

## Questions

- How do we represente H (hypotesis)?

In Linear Regression, out h(x) = x*w + b, which is a linear equation.

If we have, let's say, more features:

- [size]
- [nº bedrooms]

we simple, multiply by it too, so: h(x) = xi*xii*w + b or $$\mathrm{h(x)} = \sum_{j=0}^{2} xjwj + b $$, where xo = 1.


