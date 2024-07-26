Por padrão alguns algorítimos de ML não suportam classificação de múltiplos **labels**, apenas classificação binária (e.x Logit, Perceptron e SVM). Existe no entanto uma forma de possibilitar que modelos limitados a classificação binária possam realizar classificações múltiplas, duas estratégias são:

1. **One-vs-Rest (OvR)**
2. **One-vs-One  (OvO)**

Na estatégia OvR um problema multiclass é transformado em um problema binário para cada classe, na OvO o problema é dividido em um problema binária a cada par de classes.

## OvR
Um exemplo de como os dados ficariam dispostos na aplicação do OvR seria:

- Binary Classification Problem 1: red vs [blue, green]
- Binary Classification Problem 2: blue vs [red, green]
- Binary Classification Problem 3: green vs [red, blue]

*considerando que inicialmente tinhamos ‘red,’ ‘blue,’ and ‘green‘.*

### Implementação do método OvR para Logit

```python
# logistic regression for multi-class classification using built-in one-vs-rest
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
# define model
model = LogisticRegression(multi_class='ovr')
# fit model
model.fit(X, y)
# make predictions
yhat = model.predict(X)
```

## OvO
Um exemplo de como os dados ficariam dispostos na aplicação do OvO seria:


- Binary Classification Problem 1: red vs. blue
- Binary Classification Problem 2: red vs. green
- Binary Classification Problem 3: red vs. yellow
- Binary Classification Problem 4: blue vs. green
- Binary Classification Problem 5: blue vs. yellow
- Binary Classification Problem 6: green vs. yellow

*considerando que inicialmente tinhamos ‘red,’ ‘blue,’ and ‘green‘.*

A fórmula para calcular o número de datasets é como segue: $(NumClasses * (NumClasses – 1)) / 2$

### Implementação do método OvR para SVM

```python
# SVM for multi-class classification using built-in one-vs-one
from sklearn.datasets import make_classification
from sklearn.svm import SVC
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
# define model
model = SVC(decision_function_shape='ovo')
# fit model
model.fit(X, y)
# make predictions
yhat = model.predict(X)
```


## **Futher Reading**

***Books**
- Page 503, Machine Learning: A Probabilistic Perspective, 2012.

**Blogs Mencionados**
- [One-vs-Rest and One-vs-One for Multi-Class Classification](https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/)
