Por padrão algo algorítimos de ML não suportam classificação de múltiplos **labels**, apenas classificação binária (e.x Logit, Perceptron e SVM). Existe no entanto uma forma de possibilitar que modelos limitados a classificação binária possam realizar classificações múltiplas, duas estratégias são:

1. **One-vs-Rest (OvR)**
2. **One-vs-One  (OvO)**

Na estatégia OvR um problema multiclass é transformado em um problema binário para cada classe, na OvO o problema é dividido em um problema binária a cada par de classes.

**Blogs Mencionados**
- [One-vs-Rest and One-vs-One for Multi-Class Classification](https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/)
