Regression, different from classical problems, in regression we need predict a numerical value. So, we need differente metrics. You can't use for exemple acc for supose how good your model is. Some metrics for regression are:

- mae
- mse
- r2

**mse**

Mse is commoly used as loss function and also for evaluate regression models, Imagine we are working with mean values in dolaers of house prices, the mse (mean squared error) compute the error (y_true - y_predicted) squared. 
One important characteristc of mse is that it punishes models with high erros, once we squared the values.

![image](https://github.com/user-attachments/assets/5b31a0c0-ae05-47c0-b218-3033ab9ab590).

**mae**

**r2**

references

R1: https://machinelearningmastery.com/regression-metrics-for-machine-learning/

R2: https://en.wikipedia.org/wiki/Mean_squared_error
