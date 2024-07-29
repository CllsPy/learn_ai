## Parte I
Logistic Regression é usado, principalmente, para **Binary Classification** (e.g rain/no rain).

![image](https://github.com/user-attachments/assets/8de06392-f58b-4e4e-af65-4a22ac4b75d5)

_Fig.1 Observe que as funções são linearmente separáveis._
## Parte II
Na **PARTE I** do vídeo [Krish Naik](https://www.youtube.com/watch?v=uFfsSgQgerw) explica porque não devemos usar Regressão Linear para problemas de Classificação.

![image](https://github.com/user-attachments/assets/830c48ba-86f5-4702-b50f-4603092dcae0)


_Fig.2 Messe caso é possível desenhar uma linha capaz de separar a parte **positiva** da **negativa** (Image Source: https://www.researchgate.net/figure/Figura-5-Exemplos-de-padroes-linearmente-e-nao-linearmente-separavel-respectivamente_fig4_266411199)_

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

**Acima** do plano  $y = w^t x$  > 0 e **abaixo** dele  $y = w^t x$  < 0. Isso significa que se o valor está acima do gráfico e é positivo, ele foi classificado corretamente (caso 1). No caso 2, vamos ter que $y = w^t x  < 0$ é negativo e como para a classe negativa $y= -1$, significa que na parte superior o valor da distância precisa ser positiva para darmos o ponto como classificado corretamente.


$$y*w^t x = -1(w^t x )$$

para, $w^t x > 0$


A função de custo precisa ter o maior valor possível, deste modo:

$$\max \sum_{i=1}^{n}  yiwi^t xi$$

Porque quando temos que $w^t x > 0$, sabemos que as classes foram classificadas corretamente.

Para evitar que outliers afetam o classificação, calculamos:

$$max \sum_{i=1}^{n} f(yiwi^t xi)$$

Isso para então a ser uma **SIGMOID-FUNCTION**.

![image](https://github.com/user-attachments/assets/9b562e8e-4470-4a4b-a357-96b424fd9385)
Fig.3 Sigmoid-Function (Image Source: https://www.researchgate.net/figure/The-Sigmoid-function-with-scaling-parameter-l-and-translation-parameter-e_fig3_340025904)

## Futher Readings

### YouTube
- [Tutorial 35- Logistic Regression Indepth Intuition- Part 1| Data Science](https://www.youtube.com/watch?v=L_xBe7MbPwk)

- [Tutorial 36- Logistic Regression Indepth Intuition- Part 2| Data Science](https://www.youtube.com/watch?v=uFfsSgQgerw)

### Blogs
- [Why Is Logistic Regression Called “Logistic Regression” And not a Logistic Classification?](https://medium.com/@praveenraj.gowd/why-is-logistic-regression-called-logistic-regression-and-not-a-logistic-classification-5a418293040d#:~:text=Linear%20regression%20gives%20a%20continuous,%E2%80%9CRegression%E2%80%9D%20in%20its%20name.)
