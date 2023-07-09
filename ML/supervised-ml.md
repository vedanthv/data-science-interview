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

4. How do we check if a variable is normally distributed?

- Box Plot
- QQ Plot
- KS Test
The Kolmogorov Smirnov test computes the distances between the empirical distribution and the theoretical distribution and defines the test statistic as the supremum of the set of those distances. [p value > 0.05 then its normal distribution]

5. What are the assumptions in Linear Regression?

1. **Linear relationship** between features and target variable.
2. **Additivity** means that the effect of changes in one of the features on the target variable does not depend on values of other features. For example, a model for predicting revenue of a company have of two features - the number of items _a_ sold and the number of items _b_ sold. When company sells more items _a_ the revenue increases and this is independent of the number of items _b_ sold. But, if customers who buy _a_ stop buying _b_, the additivity assumption is violated.
3. Features are not correlated (no **collinearity**) since it can be difficult to separate out the individual effects of collinear features on the target variable.
4. Errors are independently and identically normally distributed (y<sub>i</sub> = B0 + B1*x1<sub>i</sub> + ... + error<sub>i</sub>):
   1. No correlation between errors (consecutive errors in the case of time series data).
   2. Constant variance of errors - **homoscedasticity**. For example, in case of time series, seasonal patterns can increase errors in seasons with higher activity.
   3. Errors are normally distributed, otherwise some features will have more influence on the target variable than to others.



