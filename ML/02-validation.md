**What is overfitting?**

When your model perform very well on your training set but can't generalize the test set, because it adjusted a lot to the training set.

<br/>

**How to validate your models?**

One of the most common approaches is splitting data into train, validation and test parts.
Models are trained on train data, hyperparameters (for example early stopping) are selected based on the validation data, the final measurement is done on test dataset.
Another approach is cross-validation: split dataset into K folds and each time train models on training folds and measure the performance on the validation folds.
Also you could combine these approaches: make a test/holdout dataset and do cross-validation on the rest of the data. The final quality is measured on test dataset.

<br/>

**Why do we need to split our data into three parts: train, validation, and test?**

The training set is used to fit the model, i.e. to train the model with the data. The validation set is then used to provide an unbiased evaluation of a model while fine-tuning hyperparameters. This improves the generalization of the model. 

Finally, a test data set which the model has never "seen" before should be used for the final evaluation of the model. This allows for an unbiased evaluation of the model. The evaluation should never be performed on the same data that is used for training. Otherwise the model performance would not be representative.

<br/>

**Can you explain how cross-validation works?**

Cross-validation is the process to separate your total training set into two subsets: training and validation set, and evaluate your model to choose the hyperparameters. But you do this process iteratively, selecting different training and validation set, in order to reduce the bias that you would have by selecting only one validation set.

<br/>

**What is K-fold cross-validation? **

K fold cross validation is a method of cross validation where we select a hyperparameter k. The dataset is now divided into k parts. Now, we take the 1st part as validation set and remaining k-1 as training set. Then we take the 2nd part as validation set and remaining k-1 parts as training set. Like this, each part is used as validation set once and the remaining k-1 parts are taken together and used as training set.
It should not be used in a time series data.

<br/>

