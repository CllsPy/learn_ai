Por padrão algo algorítimos de ML não suportam classificação de múltiplos **labels**, apenas classificação binária (e.x Logit, Perceptron e SVM). Existe no entanto uma forma de possibilitar que modelos limitados a classificação binária possam realizar classificações múltiplas, duas estratégias são:

1. **One-vs-Rest (OvR)**
2. **One-vs-One  (OvO)**

Na estatégia OvR um problema multiclass é transformado em um problema binário para cada classe, na OvO o problema é dividido em um problema binária a cada par de classes.

## OvR
Um exemplo de como os dados ficariam dispostos na aplicação do OvR seria:

- Binary Classification Problem 1: red vs [blue, green]
- Binary Classification Problem 2: blue vs [red, green]
- Binary Classification Problem 3: green vs [red, blue]

*considerando que inicialmente tinhamos ‘red,’ ‘blue,’ and ‘green‘.*

**Futher Reading**
- Page 503, Machine Learning: A Probabilistic Perspective, 2012.

**Blogs Mencionados**
- [One-vs-Rest and One-vs-One for Multi-Class Classification](https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/)
