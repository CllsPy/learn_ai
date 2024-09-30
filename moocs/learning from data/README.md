# Chapter 1
## The Learning Problem

Sometimes, because we don't have any analytical solution to our problem we need to use data. Think about that is a tree? Do you need this information or just recognize one?

![image](https://github.com/user-attachments/assets/3d9a89fd-6d86-449e-9f5a-bc960b092391)

### 1.1 Problem Setup

![image](https://github.com/user-attachments/assets/301f5416-d3ca-4cae-a5da-da1f15019abb)

#### [1.1. 1 Components of Learning ](https://colab.research.google.com/drive/1UkSEPbnI7ECT5AvGhm0An34bpzHvjj-3?usp=sharing)

The metaphor we'll use for de Learning Problem will be Credit Approval. Let's imagine that a bank wants to know if a specific client is worth to borrow money from them. Let's name our componets.
- x user info (INPUT)
- f. X  -> Y: The target function, a function that predict if the customer will pay back the bank.
- D: Dataset (per (xn, yn)
- yn = f(xn) for n = 1, ..., N (number of inputs)
- g: X -> Y (function that aproximates f (Algorithm)


![image](https://github.com/user-attachments/assets/8d75fe06-cb62-4049-86e8-47dbcb8de1cb)

#### 1. 1.2 A Simple Learning Model 

Differente of the data and of the target function the hipoteshis `H` is our choose. Also, we can call the hipoteshis, **the learning model**.

We know that x ∈ R^{d} (Euclidian Space). Where, x represents the input vector which contains informations about the credit card application e.g
- salary
- houses
- age
- [...]

We can choose a learning model, where h ∈ H. Where h(x) approximate our target function f(x) = y. For that we multiply x by weights (a vector of weight) to create a score, and based on a threshold we determine if we accept or not de application, sice y = {+1, 1} or (yes/no).

![image](https://github.com/user-attachments/assets/2e2de145-36f8-429f-8f23-dd317021a242)

### Design Problem vs Learning Problem
The Design problem has analytical solution and you can aproximate f, without any data. The learning problem aproximates f, by using the data and f don't need to have a analytical solution
