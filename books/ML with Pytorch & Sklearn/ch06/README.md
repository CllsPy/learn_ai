## The holdout method
The holdout method is split our data in train and test set. Use test for performing evaluation and train to feed our model. Tody is not recommendade to use test set for hyperparameter tunning.

Se the ideia is to split in three parts:

- train
- test
- val

This way we'll have a less biased test set for eval our ml model.

![image](https://github.com/user-attachments/assets/b8b93ec3-54a9-4f04-b53f-9fa79918b99e)

The disavantage of the hold-out set is that, the quality depens of the dataset. So, for minimize that we'll use another strategy of cross-val (K-fold). K-fold creates a hold-out for k folds and we can verify how the model interages with each one.
