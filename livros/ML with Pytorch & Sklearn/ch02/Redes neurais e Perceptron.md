## Receita

A receita para reproduzir um **Perceptron** é como segue:

1. Obtenha um conjundo de dados **Supervisionado**
2. Perceptron faz previsões (**FeedFoward**)
   
![image](https://github.com/user-attachments/assets/0badff74-3e9f-41b1-a529-43f884e03edb)

3. Calcular o erro (**Loss**) e atualizar os pesos


## Dicionário

**Epochs**: os passos 2 e 3 precisam ser realizados em todos conjunto de dados, digamos se existem 1500 registros serão 1500 interações, cada vez que o Percpetron concluir as 1500 interações chamamos isto de **época/epoch.**

- T**amanho do Batch**: estratégia para treinar os dados em partes, digamos 15 partes de 100 amostras.

| Registro    | X1 | X2 | Target
| -------- | ------- | ------- |  ------- |
| A  | 1    | 1    |  1
| B | 0     | 0      |  0
| C    | 0    | 1    |  1


## References
[Redes neurais e Perceptron - Aula 9](https://www.youtube.com/watch?v=fEukSrpDPH0)
