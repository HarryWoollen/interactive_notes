# 1. Simple Linear Regression

In simplest terms:

$y = \beta_0 + \beta_1x + \epsilon$

However any combination of $\beta$ would remain a linear model.

For example 

$y = \beta_0 + \beta_1x + \beta_2x + ... \beta_nx + \epsilon$

$\beta_0$ : Represents the **true/population** intercept, the value of ${y}$ when $x = 0$

$\beta_1$ : Represents the **true/population** gradient of the slope

$\epsilon$: Represents the error present in the approximation

## 1.1. Individual Estimate

Naturally for an individual estimate

$y_i = \beta_0 + \beta_1x_i  + \epsilon_i$

where $i = 1,...,n$
(n = number of units)

## 1.2. Assumptions

The assumptions on $\epsilon$ are as follows

1. Normally Distributed
2. Mean 0
3. Constant in variance
4. Independent.

These usually form the saying $`i.i.d \sim N(0,\sigma^2)`$

Which is read as independently, indentically distributed.

### 1.2.1 Consequences

1. At any given $x_i$ the $Y_i's$ are Normally Distributed

2. If two events are dependent on eachother (one influences the other) you "shouldn't" (though most likely can) use a linear model.

    2.i. It is this that leads to checking for multi-collinearity in your EDA

## 1.3. Least Squares Method (How to get your line of best fit)

### 1.3.1 Summary

* Differentiate
* Set equal to 0 (so it is an estimate)
* Solve

#### 1.3.1.1 Solving for $\beta_0$
Minimise our error (observation $\hat{y}$ - expectation $y_i$)

   $S = \Sigma^n_{i = 1}(y_i - E[y_i|x_i])^2$
    
-> $S = \Sigma^n_{i=1}(y_i - (\beta_0 + \beta_1x_i))^2$

To minimise we set the partial differential w.r.t $\beta_0$ to 0 (this is how you minimise a function)

So for $\beta_0$

$$\frac{\partial S}{\partial \beta_0} = -2\Sigma^n_{i=1}(y_i - \beta_0 - \beta_1x_i)$$

$$\Sigma^n_{i=1}(y_i - \hat{\beta_0} - \hat{\beta_1}x_i) = 0$$

$$\Sigma^n_{i=1}(y_i) - n\hat{\beta_0} - \hat{\beta_1}\Sigma^n_{i=1}x_i = 0$$

* Recall $\frac{\Sigma^n_{i=1}(a_i)}{n} = \bar{a}$

Thus $$\hat{\beta_0} = \bar{y} - \hat{\beta_1}\bar{x}$$


#### 1.3.1.2 Solving for $\beta_1$

Solving for $\beta_1$ is a lot more involved, as it requires the covariance of X,Y. 
You are welcome to derive from first principles as done above, or seek out an alternative proof. But we will skip to the end.

$$ \hat{\beta_1} = \frac{\Sigma^n_{i=1}y_ix_i - \frac{\Sigma^n_{i=1}y_i\Sigma^n_{i=1}x_i}{n}}{\Sigma^n_{i=1}x_i^2 - \frac{(\Sigma^n_{i=1}x_i)^2}{n}}$$

This can be simplified to 

$$ \hat{\beta_1} = \frac{S_{xy}}{S_{xx}}$$

A simpler derivation for $SS_{xy}$ is $\Sigma^n_{i=1}((x_i - \bar{x})(y_i - \bar{y}))$

And for $SS_{xx}$ = $\Sigma^n_{i=1}((x_i - \bar{x})(x_i - \bar{x}))$ = $\Sigma^n_{i=1}((x_i - \bar{x})^2)$

#### 1.3.1.3 Solving for $y$

Now you have your estimates for $\beta$ you can estimate y

$$ \hat{y} = \hat{\beta_0} + \hat{\beta_1}x$$

And there you have your line of best fit.




# 2. General Linear Model

This can be covered more in depth in the future. But as a teaser, the General linear model is just what we have seen but with a $X$ matrix and vectors for $Y, \Beta$.

This is your feature matrix where you have your columns $x_i$ with individuals $j$

**y** = X**β** + ε

$$
\begin{bmatrix}
y_1 \\
y_2 \\
... \\
y_n  
\end{bmatrix} = 

 \begin{bmatrix}
1 & x_{11} & ... & x_{1i} \\
1 & x_{21} & ... & x_{2i} \\
... & ... & ... & ... \\
1 & x_{j1} & ... & x{ji} 
\end{bmatrix}
\begin{bmatrix}
\beta_0 \\
\beta_1 \\
... \\
\beta_k 
\end{bmatrix} + 
\begin{bmatrix}
\epsilon_1 \\
\epsilon_2 \\
... \\
\epsilon_n 
\end{bmatrix} 
$$
