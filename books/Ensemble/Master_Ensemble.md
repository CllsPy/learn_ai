## 2.1 Parallel ensembles

When using **ensemble** methods we can weight some choices prioritazing the most capable model.

- How do we create a set of base estimators with diverse opinions from a single
data set? That is, how can we ensure ensemble diversity during training?

- How can we aggregate decisions, or predictions, of each individual base estimator into a final prediction? That is, how can we perform model aggregation
during prediction?

![image](https://github.com/user-attachments/assets/b291724f-b4cb-4aa3-bb83-c99286baeef7)

- for reg we use avereginf
- for classficiation we use mojority of votes

### 2.2.1 Intuition: Resampling and model aggregation

**Booststrap sample** is when the datasets have the same length. This also implies that some values will be sampled more than one time, when other may be never sampled.

![image](https://github.com/user-attachments/assets/5502ebbf-9740-4f68-b6e5-fd0b61f4828d)

### THE OUT-OF-BAG SAMPLE

The OOB sample allowed you to validate your data, by creatinf a set of values that weren't never been seen.

> To summarize:
after one round of bootstrap sampling, we get one bootstrap sample (for training a
base estimator) and a corresponding OOB sample (to evaluate that base estimator). 
