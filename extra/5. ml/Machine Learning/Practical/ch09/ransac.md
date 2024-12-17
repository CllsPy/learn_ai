**RANSAC**

RANSAC is an acronimous for RANdom SAmple Consensus, we can use to peform linear regression task when the data have lots of outliers. It works as follow:

- fit a model in a sample of the data
- choose the model model (precisely the sample with less outliers)

To decide if a data point is a outliers or not, the model use the MAD concept, which is how far the datapoint is from the mean, we can adjust out mad. To calculate mad, we do: mean(abs(data-mean(data))

Evan RANSAC is really good with outliers by selecting inliers, there is no guaratee that the model i'll have a good performance on unseen data.
