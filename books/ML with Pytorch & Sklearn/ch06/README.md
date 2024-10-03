## The holdout method
The holdout method is split our data in train and test set. Use test for performing evaluation and train to feed our model. Tody is not recommendade to use test set for hyperparameter tunning.

Se the ideia is to split in three parts:

- train
- test
- val

This way we'll have a less biased test set for eval our ml model.

![image](https://github.com/user-attachments/assets/b8b93ec3-54a9-4f04-b53f-9fa79918b99e)

The disavantage of the hold-out set is that, the quality depens of the dataset. So, for minimize that we'll use another strategy of cross-val (K-fold). K-fold creates a hold-out for k folds and we can verify how the model interages with each one.

K-folds works that way: The train data is splited in (for k=5). 4 folds and the model is tested in the lefted fold. It helps better estimation.

![image](https://github.com/user-attachments/assets/5739e615-8f9e-45a8-8307-01d69cf2fb14)

## Debugging algorithms with learning and validation curves

One can use learning curves and validation curves to verify the model performance and look for overfitting (high variance) or underfitting (high bias).

![image](https://github.com/user-attachments/assets/fd97068f-1642-4240-b00a-529903ccf23c)

In Underfitting problems use change de model complexity (improve it) e.g:
- more parameters
- less regularization

 For overfitting we do the reverse:

 - less parameters
 - more regularization
 - also, we can use feature selection
