# Mini-Essay: Which Metrics Use For Evaluate Regression Models
Regression, different from classical problems, in regression we need predict a numerical value. So, we need differente metrics. You can't use for exemple acc for supose how good your model is. Some metrics for regression are:

 - Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- r2

## MSE

Mse is commoly used as loss function and also for evaluate regression models, Imagine we are working with mean values in dolaers of house prices, the mse (mean squared error) compute the error (y_true - y_predicted) squared. 
One important characteristc of mse is that it punishes models with high erros, once we squared the values.

![image](https://github.com/user-attachments/assets/5b31a0c0-ae05-47c0-b218-3033ab9ab590).

## MAE
Mae, short for mean absolute error can be used when we want to compare, directly, two phenomenons, that are equals. If you remember the exemple of house princes, if you want to see clearly the mean error in dollars you use mae. Another aspect is that we don't want use Mae for data in different scales, as said use mae for direct comparation.

![image](https://github.com/user-attachments/assets/a94ac9fd-efc5-4224-806d-879280b2c0ce)

**R2**
In predictive statistics R2 explain how well the model predict the target values. Somes reasons for use R2 include:

- Comparison: Use R2 to compare different regression models
- Interpretability: If our R2 is 0.8 it means that 80% of our dependent variables can be explain by our independent variables.

![image](https://github.com/user-attachments/assets/c0043d3e-64b4-4e85-b6e7-b36837274524)

## references

- [0](https://en.wikipedia.org/wiki/Mean_absolute_error)
- [1](https://machinelearningmastery.com/regression-metrics-for-machine-learning/)
- [2](https://en.wikipedia.org/wiki/Mean_squared_error)
- [Forecast Principles](https://otexts.com/fpp2/)


## Reading List 1: 
https://en.wikipedia.org/wiki/Coefficient_of_determination

- Coefficient Of Determination or Simply (R2) compute how much independent variables explain the target variables.
- In predictive statistics R2 explain how well the model predict the target values.

## Reading List 2: 
https://vitalflux.com/mean-square-error-r-squared-which-one-to-use/

R2 is a good choice when you need to compare multiples models
