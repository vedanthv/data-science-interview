## Supervised Machine Learning

1. What is supervised Machine Learning?

Supervised machine learning is a type of machine learning algorithm that involves training a model using labeled examples. In this approach, the algorithm is provided with a dataset that consists of input data and corresponding output labels. The goal is for the model to learn a mapping function that can accurately predict the output labels for new, unseen input data.

2. What is Regression? Which models are used in regression?

Regression is a statistical technique and a fundamental concept in machine learning that focuses on predicting a continuous numerical output variable based on input features. It is commonly used for tasks where the goal is to understand the relationship between a dependent variable and one or more independent variables.

In regression, the dependent variable, also known as the target variable or the response variable, is a continuous variable. The independent variables, also called predictors, features, or input variables, are used to predict the value of the dependent variable. The relationship between the independent variables and the dependent variable is typically represented by a mathematical equation.

- *Linear Regression* establishes a linear relationship between target and predictor (s). It predicts a numeric value and has a shape of a straight line.
- *Polynomial Regression* has a regression equation with the power of independent variable more than 1. It is a curve that fits into the data points.
- *Ridge Regression* helps when predictors are highly correlated (multicollinearity problem). It penalizes the squares of regression coefficients but doesn’t allow the coefficients to reach zeros (uses L2 regularization).
- *Lasso Regression* penalizes the absolute values of regression coefficients and allows some of the coefficients to reach absolute zero (thereby allowing feature selection).

3. What is linear regression? When do we use it?

Linear regression is a type of statistical analysis used to predict the relationship between two variables. It assumes a linear relationship between the independent variable and the dependent variable, and aims to find the best-fitting line that describes the relationship. The line is determined by minimizing the sum of the squared differences between the predicted values and the actual values.

<img src = "https://editor.analyticsvidhya.com/uploads/375512.jpg">

3. What is Normal Distribution?

The normal distribution, also known as the Gaussian distribution, is the most important probability distribution in statistics for independent, random variables. Most people recognize its familiar bell-shaped curve in statistical reports.

The normal distribution is a continuous probability distribution that is symmetrical around its mean, most of the observations cluster around the central peak, and the probabilities for values further away from the mean taper off equally in both directions. 

Extreme values in both tails of the distribution are similarly unlikely. While the normal distribution is symmetrical, not all symmetrical distributions are normal. For example, the Student’s t, Cauchy, and logistic distributions are symmetric.

![formula](https://mathworld.wolfram.com/images/equations/NormalDistribution/NumberedEquation1.gif)

The normal distribution derives its importance from the **Central Limit Theorem**, which states that if we draw a large enough number of samples, their mean will follow a normal distribution regardless of the initial distribution of the sample, i.e **the distribution of the mean of the samples is normal**. It is important that each sample is independent from the other.

This is powerful because it helps us study processes whose population distribution is unknown to us.

4. How do we check if a variable is normally distributed?

- Box Plot
- QQ Plot
- KS Test
The Kolmogorov Smirnov test computes the distances between the empirical distribution and the theoretical distribution and defines the test statistic as the supremum of the set of those distances. [p value > 0.05 then its normal distribution]

5. What are the assumptions in Linear Regression?

- **Linear relationship** between features and target variable.

- **Additivity** means that the effect of changes in one of the features on the target variable does not depend on values of other features. For example, a model for predicting revenue of a company have of two features - the number of items _a_ sold and the number of items _b_ sold. When company sells more items _a_ the revenue increases and this is independent of the number of items _b_ sold. But, if customers who buy _a_ stop buying _b_, the additivity assumption is violated.

- Features are not correlated (no **collinearity**) since it can be difficult to separate out the individual effects of collinear features on the target variable.

- Errors are independently and identically normally distributed (y<sub>i</sub> = B0 + B1*x1<sub>i</sub> + ... + error<sub>i</sub>):
   1. No correlation between errors (consecutive errors in the case of time series data).
   2. Constant variance of errors - **homoscedasticity**. For example, in case of time series, seasonal patterns can increase errors in seasons with higher activity.
   3. Errors are normally distributed, otherwise some features will have more influence on the target variable than to others.

<br/>

**What if we want to build a model for predicting prices? Are prices distributed normally? Do we need to do any pre-processing for prices?**

Data is not normal. Specially, real-world datasets or uncleaned datasets always have certain skewness. Same goes for the price prediction. Price of houses or any other thing under consideration depends on a number of factors. So, there's a great chance of presence of some skewed values i.e outliers if we talk in data science terms. 

Yes, you may need to do pre-processing. Most probably, you will need to remove the outliers to make your distribution near-to-normal.

<br/>

**What methods for solving linear regression do you know? **

To solve linear regression, you need to find the coefficients <img src="https://render.githubusercontent.com/render/math?math=\beta"> which minimize the sum of squared errors.

Matrix Algebra method: Let's say you have `X`, a matrix of features, and `y`, a vector with the values you want to predict. After going through the matrix algebra and minimization problem, you get this solution: <img src="https://render.githubusercontent.com/render/math?math=\beta = (X^{T}X)^{-1}X^{T}y">. 

But solving this requires you to find an inverse, which can be time-consuming, if not impossible. Luckily, there are methods like Singular Value Decomposition (SVD) or QR Decomposition that can reliably calculate this part <img src="https://render.githubusercontent.com/render/math?math=(X^{T}X)^{-1}X^{T}"> (called the pseudo-inverse) without actually needing to find an inverse. The popular python ML library `sklearn` uses SVD to solve least squares.

Alternative method: Gradient Descent. See explanation below.

<br/>

**What is gradient descent? How does it work?️**

Gradient descent is an algorithm that uses calculus concept of gradient to try and reach local or global minima. It works by taking the negative of the gradient in a point of a given function, and updating that point repeatedly using the calculated negative gradient, until the algorithm reaches a local or global minimum, which will cause future iterations of the algorithm to return values that are equal or too close to the current point. It is widely used in machine learning applications.

<br/>

**What is the normal equation?**

Normal equations are equations obtained by setting equal to zero the partial derivatives of the sum of squared errors (least squares); normal equations allow one to estimate the parameters of a multiple linear regression.

<br/>

**What is SGD  —  stochastic gradient descent? What’s the difference with the usual gradient descent?**

In both gradient descent (GD) and stochastic gradient descent (SGD), you update a set of parameters in an iterative manner to minimize an error function.

The difference lies in how the gradient of the loss function is estimated. In the usual GD, you have to run through ALL the samples in your training set in order to estimate the gradient and do a single update for a parameter in a particular iteration. In SGD, on the other hand, you use ONLY ONE or SUBSET of training sample from your training set to estimate the gradient and do the update for a parameter in a particular iteration. If you use SUBSET, it is called Minibatch Stochastic gradient Descent.

<br/>

**Which metrics for evaluating regression models do you know?**

1. Mean Squared Error(MSE)
2. Root Mean Squared Error(RMSE)
3. Mean Absolute Error(MAE)
4. R² or Coefficient of Determination
5. Adjusted R²

<br/>

**What are MSE and RMSE? **

MSE stands for <strong>M</strong>ean <strong>S</strong>quare <strong>E</strong>rror while RMSE stands for <strong>R</strong>oot <strong>M</strong>ean <strong>S</strong>quare <strong>E</strong>rror. They are metrics with which we can evaluate models.

<br/>

**What is the bias-variance trade-off? **

**Bias** is the error introduced by approximating the true underlying function, which can be quite complex, by a simpler model. **Variance** is a model sensitivity to changes in the training dataset.

**Bias-variance trade-off** is a relationship between the expected test error and the variance and the bias - both contribute to the level of the test error and ideally should be as small as possible:

```
ExpectedTestError = Variance + Bias² + IrreducibleError
```

But as a model complexity increases, the bias decreases and the variance increases which leads to *overfitting*. And vice versa, model simplification helps to decrease the variance but it increases the bias which leads to *underfitting*.

<br/>

