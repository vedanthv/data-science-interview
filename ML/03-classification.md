## Classification

**What is classification? Which models would you use to solve a classification problem?**

Classification problems are problems in which our prediction space is discrete, i.e. there is a finite number of values the output variable can be. Some models which can be used to solve classification problems are: logistic regression, decision tree, random forests, multi-layer perceptron, one-vs-all, amongst others.

<br/>

**What is logistic regression? When do we need to use it?**

Logistic regression is a Machine Learning algorithm that is used for binary classification. You should use logistic regression when your Y variable takes only two values, e.g. True and False, "spam" and "not spam", "churn" and "not churn" and so on. The variable is said to be a "binary" or "dichotomous".

<br/>

**Is logistic regression a linear model? Why?**

Yes, Logistic Regression is considered a generalized linear model because the outcome always depends on the sum of the inputs and parameters. Or in other words, the output cannot depend on the product (or quotient, etc.) of its parameters.

<br/>

**What is sigmoid? What does it do? **

A sigmoid function is a type of activation function, and more specifically defined as a squashing function. Squashing functions limit the output to a range between 0 and 1, making these functions useful in the prediction of probabilities.

Sigmod(x) = 1/(1+e^{-x})

<br/>

**How do we evaluate classification models? **

Depending on the classification problem, we can use the following evaluation metrics:

1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. Logistic loss (also known as Cross-entropy loss)
6. Jaccard similarity coefficient score

<br/>

**What is accuracy?**

Accuracy is a metric for evaluating classification models. It is calculated by dividing the number of correct predictions by the number of total predictions.

<br/>

**Is accuracy always a good metric?**

Accuracy is not a good performance metric when there is imbalance in the dataset. For example, in binary classification with 95% of A class and 5% of B class, a constant prediction of A class would have an accuracy of 95%. In case of imbalance dataset, we need to choose Precision, recall, or F1 Score depending on the problem we are trying to solve.

<br/>

**What is the confusion table? What are the cells in this table?**

Confusion table (or confusion matrix) shows how many True positives (TP), True Negative (TN), False Positive (FP) and False Negative (FN) model has made.

||                |     Actual   |        Actual |
|:---:|   :---:        |     :---:    |:---:          |
||                | Positive (1) | Negative (0)  |
|Predicted|   Positive (1) | TP           | FP            |
|Predicted|   Negative (0) | FN           | TN            |

* True Positives (TP): When the actual class of the observation is 1 (True) and the prediction is 1 (True)
* True Negative (TN): When the actual class of the observation is 0 (False) and the prediction is 0 (False)
* False Positive (FP): When the actual class of the observation is 0 (False) and the prediction is 1 (True)
* False Negative (FN): When the actual class of the observation is 1 (True) and the prediction is 0 (False)

Most of the performance metrics for classification models are based on the values of the confusion matrix.

<br/>

**What are precision, recall, and F1-score?**

* Precision and recall are classification evaluation metrics:
* P = TP / (TP + FP) and R = TP / (TP + FN).
* Where TP is true positives, FP is false positives and FN is false negatives
* In both cases the score of 1 is the best: we get no false positives or false negatives and only true positives.
* F1 is a combination of both precision and recall in one score (harmonic mean):
* F1 = 2 * PR / (P + R).
* Max F score is 1 and min is 0, with 1 being the best.

<br/>

**Precision-recall trade-off**

Tradeoff means increasing one parameter would lead to decreasing of other. Precision-recall tradeoff occur due to increasing one of the parameter(precision or recall) while keeping the model same. 

In an ideal scenario where there is a perfectly separable data, both precision and recall can get maximum value of 1.0. But in most of the practical situations, there is noise in the dataset and the dataset is not perfectly separable. 

There might be some points of positive class closer to the negative class and vice versa. In such cases, shifting the decision boundary can either increase the precision or recall but not both. Increasing one parameter leads to decreasing of the other. 

<br/>

**What is the ROC curve? When to use it?**

ROC stands for *Receiver Operating Characteristics*. The diagrammatic representation that shows the contrast between true positive rate vs false positive rate. It is used when we need to predict the probability of the binary outcome.

<br/>

**What is AUC (AU ROC)? When to use it?**

AUC stands for *Area Under the ROC Curve*. ROC is a probability curve and AUC represents degree or measure of separability. It's used when we need to value how much model is capable of distinguishing between classes.  The value is between 0 and 1, the higher the better.

<br/>

**How to interpret the AU ROC score?**

AUC score is the value of *Area Under the ROC Curve*. 

If we assume ROC curve consists of dots, <img src="https://render.githubusercontent.com/render/math?math=(x_1, y_1), (x_2, y_2), \cdots, (x_m,y_m)">, then

<img src="https://render.githubusercontent.com/render/math?math=AUC = \frac{1}{2} \sum_{i=1}^{m-1}(x_{i%2B1}-x_i)\cdot (y_i%2By_{i%2B1})">

An excellent model has AUC near to the 1 which means it has good measure of separability. A poor model has AUC near to the 0 which means it has worst measure of separability. When AUC score is 0.5, it means model has no class separation capacity whatsoever. 

<br/>

**What is the PR (precision-recall) curve? ‍⭐️**

A *precision*-*recall curve* (or PR Curve) is a plot of the precision (y-axis) and the recall (x-axis) for different probability thresholds. Precision-recall curves (PR curves) are recommended for highly skewed domains where ROC curves may provide an excessively optimistic view of the performance.

<br/>

**What is the area under the PR curve? Is it a useful metric? ‍⭐️**

The Precision-Recall AUC is just like the ROC AUC, in that it summarizes the curve with a range of threshold values as a single score.

A high area under the curve represents both high recall and high precision, where high precision relates to a low false positive rate, and high recall relates to a low false negative rate.

<br/>

**In which cases AU PR is better than AU ROC? ‍⭐️**

What is different however is that AU ROC looks at a true positive rate TPR and false positive rate FPR while AU PR looks at positive predictive value PPV and true positive rate TPR.

Typically, if true negatives are not meaningful to the problem or you care more about the positive class, AU PR is typically going to be more useful; otherwise, If you care equally about the positive and negative class or your dataset is quite balanced, then going with AU ROC is a good idea.

<br/>

**What do we do with categorical variables? ‍⭐️**

Categorical variables must be encoded before they can be used as features to train a machine learning model. There are various encoding techniques, including:
- One-hot encoding
- Label encoding
- Ordinal encoding
- Target encoding

<br/>

**Why do we need one-hot encoding? ‍⭐️**

If we simply encode categorical variables with a Label encoder, they become ordinal which can lead to undesirable consequences. In this case, linear models will treat category with id 4 as twice better than a category with id 2. 

One-hot encoding allows us to represent a categorical variable in a numerical vector space which ensures that vectors of each category have equal distances between each other. 

This approach is not suited for all situations, because by using it with categorical variables of high cardinality (e.g. customer id) we will encounter problems that come into play because of the curse of dimensionality.

<br/>

**What is "curse of dimensionality"? ‍⭐️**

The curse of dimensionality is an issue that arises when working with high-dimensional data. It is often said that "the curse of dimensionality" is one of the main problems with machine learning. The curse of dimensionality refers to the fact that, as the number of dimensions (features) in a data set increases, the number of data points required to accurately learn the relationships between those features increases exponentially.

A simple example where we have a data set with two features, x1 and x2. If we want to learn the relationship between these two features, we need to have enough data points so that we can accurately estimate the parameters of that relationship. 

However, if we add a third feature, x3, then the number of data points required to accurately learn the relationships between all three features increases exponentially. 

This is because there are now more parameters to estimate, and the number of data points needed to accurately estimate those parameters increases exponentially with the number of parameters.

Simply put, the curse of dimensionality basically means that the error increases with the increase in the number of features.

<br/>

