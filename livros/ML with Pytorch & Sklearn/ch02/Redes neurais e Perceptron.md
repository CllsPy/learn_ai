## Receita

A receita para reproduzir um **Perceptron** é como segue:

1. Obtenha um conjundo de dados **Supervisionado**
2. Perceptron faz previsões (**FeedFoward**)
   
![image](https://github.com/user-attachments/assets/0badff74-3e9f-41b1-a529-43f884e03edb)

3. Calcular o erro (**Loss**) e atualizar os pesos


## Dicionário

**Epochs**: os passos 2 e 3 precisam ser realizados em todos conjunto de dados, digamos se existem 1500 registros serão 1500 interações, cada vez que o Percpetron concluir as 1500 interações chamamos isto de **época/epoch.**

**Tamanho do Batch**: estratégia para treinar os dados em partes, digamos 15 partes de 100 amostras.

**Interações**: quantas vezes o algoritimo processa os batchs para completar a época, no caso acima seria 15 (15 x 100 = 1500).

| Registro    | X1 | X2 | Target
| -------- | ------- | ------- |  ------- |
| A  | 1    | 1    |  1
| B | 0     | 0      |  0
| C    | 0    | 1    |  1


##  FeedForward

![image](https://github.com/user-attachments/assets/2b9ac3d5-6ceb-4557-b968-44d52080f914)

## Error
Após o processamento precisamos corrigir os pesos (w) que foram iniciados de forma aleatória. Para isto usamos a seguinte fórmula:

```error = target (o que eu queria) - predição (o que o modelo achou)```

Agora para corrigir os erros, precisamos corrigir ele, desta forma:

```novo peso = peso + learning_rate * erro * input```

![image](https://github.com/user-attachments/assets/5e0649b4-d632-4f49-b71d-4a87570c48d1)

## Bias
O Bias é um peso adicional para dar "flexibilidade" ao modelo. Ele ajuda a determinar o limiar (**TRHESHOLD**). Por exemplo um modelo que computou 0 com Bias de 1 poderia disparar porque 0+1 seria 1.

## Limitações
O Perceptron é útill para problemas linearmente separáveis ou seja onde eu consigo claramente separar os dados.
![image](https://github.com/user-attachments/assets/049efa6e-b279-4b3b-83a5-ae548495e264)

Em suma, o Perceptron é ruim para resolver o problema do XOR (Ou exclusivo).


# References
[Redes neurais e Perceptron - Aula 9](https://www.youtube.com/watch?v=fEukSrpDPH0)
[Perceptron For Dummies](https://jilp.org/cbp/Daniel-slides.PDF)
[Perceptrons, Marvin](https://www.amazon.fr/Perceptrons-Intro-Computational-Geometry-Exp/dp/0262631113)
