## Parte I
Logistic Regression é usado, principalmente, para **Binary Classification** (e.g rain/no rain).

![image](https://github.com/user-attachments/assets/8de06392-f58b-4e4e-af65-4a22ac4b75d5)

_Fig.1 Observe que as funções são linearmente separáveis._
## Parte II
Na **PARTE I** do vídeo [Krish Naik](https://www.youtube.com/watch?v=uFfsSgQgerw) explica porque não devemos usar Regressão Linear para problemas de Classificação.

![image](https://github.com/user-attachments/assets/3bfae1f1-13f5-4147-b8ba-ce4e1522bfd8)

_Fig.2 Messe caso é possível desenhar uma linha capaz de separar a parte **positiva** da **negativa** (Image Source: https://automaticaddison.com/linear-separability-and-the-xor-problem/)_

Essa linha que separa as classes tem equação dada por:

- $y = mx + c$
- $y = \beta o + \beta ix$ ou
- $y = w^t x + b$

onde,

-  $m$ --> slope
-  $c$ --> intercept
-  $x$ --> data points

Na Regressão logistica a classe positiva é denotada por +1 e a classe negativa -1.

Se tamarmos como base a equação $y = w^t x + b$ e assumirmos que o intercept é zero ou seja, que sai da origem a equação se torna $y = w^t x$ e $w^t x$ nada mais é do que a distância entre o ponto e o plano. Como existem múltiplos pontos a soma das distância é dada por:

$$\sum_{i=1}^{n}  wi^t xi$$

## Futher Readings

### YouTube
- [Tutorial 35- Logistic Regression Indepth Intuition- Part 1| Data Science](https://www.youtube.com/watch?v=L_xBe7MbPwk)

- [Tutorial 36- Logistic Regression Indepth Intuition- Part 2| Data Science](https://www.youtube.com/watch?v=uFfsSgQgerw)

### Blogs
- [Why Is Logistic Regression Called “Logistic Regression” And not a Logistic Classification?](https://medium.com/@praveenraj.gowd/why-is-logistic-regression-called-logistic-regression-and-not-a-logistic-classification-5a418293040d#:~:text=Linear%20regression%20gives%20a%20continuous,%E2%80%9CRegression%E2%80%9D%20in%20its%20name.)
