## 2.1 Parallel ensembles

When using **ensemble** methods we can weight some choices prioritazing the most capable model.

- How do we create a set of base estimators with diverse opinions from a single
data set? That is, how can we ensure ensemble diversity during training?

- How can we aggregate decisions, or predictions, of each individual base estimator into a final prediction? That is, how can we perform model aggregation
during prediction?

![image](https://github.com/user-attachments/assets/b291724f-b4cb-4aa3-bb83-c99286baeef7)

- for reg we use avereginf
- for classficiation we use mojority of votes
