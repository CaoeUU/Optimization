"""
This script implements and compares three gradient descent strategies
for the function f(x) = 2*x1^2 + 5*x2^2, as described in Problem 2 of HW6.
"""
import numpy as np
import pandas as pd

# Define the function and its gradient
A = np.array([[2., 0.], [0., 5.]])

def f(x):
    """
    Computes the function value f(x) = x^T A x.
    
    Args:
        x (np.ndarray): The 2D input vector.
    
    Returns:
        float: The function value.
    """
    return x.T @ A @ x

def grad_f(x):
    """
    Computes the gradient of f(x).
    
    Args:
        x (np.ndarray): The 2D input vector.
        
    Returns:
        np.ndarray: The gradient vector.
    """
    return 2 * A @ x

def gradient_descent_constant_step(x0, num_iterations, alpha):
    """
    Performs gradient descent with a constant step size.
    
    Args:
        x0 (np.ndarray): The initial point.
        num_iterations (int): The number of iterations to run.
        alpha (float): The constant step size.
        
    Returns:
        pd.DataFrame: A DataFrame with the history of iterates and function values.
    """
    x = x0.copy()
    history = []
    for k in range(num_iterations + 1):
        f_x = f(x)
        history.append({'iteration': k, 'x1': x[0], 'x2': x[1], 'f(x)': f_x})
        if k == num_iterations:
            break
        gradient = grad_f(x)
        x = x - alpha * gradient
    return pd.DataFrame(history)

def gradient_descent_exact_line_search(x0, num_iterations):
    """
    Performs gradient descent with exact line search.
    
    Args:
        x0 (np.ndarray): The initial point.
        num_iterations (int): The number of iterations to run.
        
    Returns:
        pd.DataFrame: A DataFrame with the history of iterates and function values.
    """
    x = x0.copy()
    history = []
    for k in range(num_iterations + 1):
        f_x = f(x)
        history.append({'iteration': k, 'x1': x[0], 'x2': x[1], 'f(x)': f_x})
        if k == num_iterations:
            break
        gradient = grad_f(x)
        # Optimal alpha for f(x) = x^T A x is (g^T g) / (2 * g^T A g)
        alpha = (gradient.T @ gradient) / (2 * gradient.T @ A @ gradient)
        x = x - alpha * gradient
    return pd.DataFrame(history)

def gradient_descent_backtracking(x0, num_iterations, gamma=0.5, sigma=0.2, alpha_init=1.0):
    """
    Performs gradient descent with backtracking line search.
    
    Args:
        x0 (np.ndarray): The initial point.
        num_iterations (int): The number of iterations to run.
        gamma (float): Armijo condition parameter.
        sigma (float): Step size reduction factor.
        alpha_init (float): Initial step size to try.
        
    Returns:
        pd.DataFrame: A DataFrame with the history of iterates and function values.
    """
    x = x0.copy()
    history = []
    for k in range(num_iterations + 1):
        f_x = f(x)
        history.append({'iteration': k, 'x1': x[0], 'x2': x[1], 'f(x)': f_x})
        if k == num_iterations:
            break
        gradient = grad_f(x)
        grad_norm_sq = gradient.T @ gradient
        
        # Backtracking line search
        alpha = alpha_init
        while f(x - alpha * gradient) > f_x - gamma * alpha * grad_norm_sq:
            alpha = sigma * alpha
            
        x = x - alpha * gradient
    return pd.DataFrame(history)

if __name__ == "__main__":
    # Initial point and number of iterations
    x_initial = np.array([1., 1.])
    iterations = 10
    
    # --- Run and print results for each method ---
    
    print("--- 1. Gradient Descent with Constant Step Size (alpha = 0.1) ---")
    history_constant = gradient_descent_constant_step(x_initial, iterations, alpha=0.1)
    print(history_constant.to_string(index=False))
    print("\n" + "="*70 + "\n")
    
    print("--- 2. Gradient Descent with Exact Line Search ---")
    history_exact = gradient_descent_exact_line_search(x_initial, iterations)
    print(history_exact.to_string(index=False))
    print("\n" + "="*70 + "\n")
    
    print("--- 3. Gradient Descent with Backtracking Line Search (gamma=0.5, sigma=0.2) ---")
    history_backtracking = gradient_descent_backtracking(x_initial, iterations, gamma=0.5, sigma=0.2)
    print(history_backtracking.to_string(index=False))
    print("\n" + "="*70 + "\n")
