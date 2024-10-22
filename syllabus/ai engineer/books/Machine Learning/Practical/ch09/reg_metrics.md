# Mini-Essay: Regression Metrics
Regression, different from classical problems, in regression we need predict a numerical value. So, we need differente metrics. You can't use for exemple acc for supose how good your model is. Some metrics for regression are:

 - Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- r2

## MSE

Mse is commoly used as loss function and also for evaluate regression models, Imagine we are working with mean values in dolaers of house prices, the mse (mean squared error) compute the error (y_true - y_predicted) squared. 
One important characteristc of mse is that it punishes models with high erros, once we squared the values.

![image](https://github.com/user-attachments/assets/5b31a0c0-ae05-47c0-b218-3033ab9ab590).

## MAE
Mae, short for mean absolute error can be used when we want to compare, directly, two phenomenons, that are equals. If you remember the exemple of house princes, if you want to see clearly the mean error in dollars you use mae.

![image](https://github.com/user-attachments/assets/a94ac9fd-efc5-4224-806d-879280b2c0ce)

**R2**

references

R1: [1](https://machinelearningmastery.com/regression-metrics-for-machine-learning/)

R2: [2](https://en.wikipedia.org/wiki/Mean_squared_error)
