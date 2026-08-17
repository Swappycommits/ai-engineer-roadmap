# Linear Regression From Raw NumPy

Linear regression implemented completely from scratch using only NumPy - no scikit-learn - via two independent methods: the Normal Equation and gradient descent.

## What it does

Fits a line to synthetic house price data (price predicted from size, and separately from size + bedrooms) using:
1. The Normal Equation - a direct matrix formula that solves for optimal parameters in one step
2. Gradient descent - an iterative approach that starts from a random guess and repeatedly improves

Both methods are validated against the known true relationship used to generate the synthetic data, and against each other.

## Usage

Open linear_reg.ipynb in VS Code (with the Jupyter extension) and run all cells in order.

## Key results

- Normal Equation recovered parameters very close to the true generating values for single-feature regression
- First gradient descent attempt failed to converge due to unscaled features (bias column always 1, house size in the thousands) making one learning rate ineffective for both parameters at once - diagnosed via the loss curve (instant drop then flatline) and fixed with feature standardization
- After scaling, gradient descent converged smoothly, with a genuine gradual decline in the loss curve
- The same Normal Equation code, unmodified, correctly generalized from one input feature (size) to two (size + bedrooms), since it was written using general matrix operations rather than hardcoded for a single variable

## What I learned
- What MSE actually measures, and why squaring residuals prevents errors from canceling out and penalizes large mistakes more heavily
- The Normal Equation as a direct matrix solution to regression: (X^T X)^-1 X^T y
- Matrix operations in NumPy: transpose (.T), matrix multiplication (@), and matrix inverse (np.linalg.inv)
- Gradient descent as an iterative alternative, and the update rule theta = theta - learning_rate * gradient
- Why gradient descent can silently fail to converge when input features are on very different scales, and how to diagnose this from the shape of the loss curve
- Feature standardization ((value - mean) / std) as the fix, and that scaled parameters must be interpreted in the rescaled space rather than compared directly to an unscaled model
- Why writing regression code in general matrix form (rather than hardcoded for one variable) lets it generalize automatically to multiple input features