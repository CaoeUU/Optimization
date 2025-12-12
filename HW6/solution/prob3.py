"""
This script implements the optimization algorithms for Problem 3 of HW6.
It includes Newton's method and projected gradient descent for the function
f(x, y) = (3/4)x^(4/3) + (1/2)(x+y)^2.
"""
import numpy as np
import pandas as pd

def f(x_vec):
    """
    Computes the function value f(x, y).
    
    Args:
        x_vec (np.ndarray): A 2D vector [x, y].
        
    Returns:
        float: The function value.
    """
    x, y = x_vec[0], x_vec[1]
    # Use np.cbrt for cube root to handle negative numbers, then raise to power 4
    return 0.75 * (np.cbrt(x)**4) + 0.5 * (x + y)**2

def grad_f(x_vec):
    """
    Computes the gradient of f(x, y).
    
    Args:
        x_vec (np.ndarray): A 2D vector [x, y].
        
    Returns:
        np.ndarray: The gradient vector.
    """
    x, y = x_vec[0], x_vec[1]
    # Derivative of x^(4/3) is (4/3)*x^(1/3)
    return np.array([np.cbrt(x) + (x + y), x + y])

def hessian_f(x_vec):
    """
    Computes the Hessian of f(x, y).
    
    Args:
        x_vec (np.ndarray): A 2D vector [x, y].
        
    Returns:
        np.ndarray: The Hessian matrix.
    """
    x, y = x_vec[0], x_vec[1]
    # Derivative of x^(1/3) is (1/3)*x^(-2/3)
    # np.cbrt(x)**(-2) is equivalent to x^(-2/3) and handles negative numbers
    # Handle x=0 for x^(-2/3) which is undefined
    if x == 0: # Check before division
        # This case should ideally be handled by avoiding evaluation at x=0 for Hessian inverse
        # or by setting a large value to mimic "infinity" or handling a singular matrix.
        # For this problem, Newton's method already checks x[0] == 0 and stops.
        return np.array([[np.inf, 1], [1, 1]]) # Return with inf to trigger error/handling
    return np.array([[(1/3) * (np.cbrt(x)**(-2)) + 1, 1], [1, 1]])

def newtons_method(x0_vec, num_iterations):
    """
    Performs Newton's method.
    
    Args:
        x0_vec (np.ndarray): The initial point [x0, y0].
        num_iterations (int): The number of iterations.
        
    Returns:
        pd.DataFrame: History of iterates and function values.
    """
    x = x0_vec.copy()
    history = []
    
    print("Running Newton's Method...")
    print("As shown in the markdown, for this corrected function, Newton's method")
    print("diverges, with the magnitude of iterates growing for x_0 != 0.\n")

    for k in range(num_iterations + 1):
        f_x = f(x)
        history.append({'iteration': k, 'x': x[0], 'y': x[1], 'f(x,y)': f_x})
        if k == num_iterations:
            break
            
        # Handle x close to 0 to avoid division by zero in Hessian
        if np.isclose(x[0], 0.0):
            print(f"Hessian becomes singular or ill-conditioned near x=0 at iteration {k}. Stopping.")
            break
            
        # Newton's step: x_k+1 = x_k - H_inv @ g
        g = grad_f(x)
        H = hessian_f(x) # Hessian calculation now handles x=0 itself.
        
        # Check for singular Hessian and potential numerical issues.
        # det is (1/3) * (np.cbrt(x)**(-2))
        if np.isclose(np.linalg.det(H), 0.0) or np.any(np.isinf(H)) or np.any(np.isnan(H)):
            print(f"Hessian is singular, infinite, or NaN at iteration {k}. Stopping.")
            break
        
        try:
            H_inv = np.linalg.inv(H)
            x = x - H_inv @ g
        except np.linalg.LinAlgError:
            print(f"Could not compute inverse of Hessian at iteration {k}. Stopping.")
            break
        
    return pd.DataFrame(history)

def projected_gradient_descent(x0_vec, num_iterations, alpha):
    """
    Performs projected gradient descent on the constraint x+y=1.
    
    Args:
        x0_vec (np.ndarray): The initial point [x0, y0]. Must sum to 1.
        num_iterations (int): The number of iterations.
        alpha (float): The step size.
        
    Returns:
        pd.DataFrame: History of iterates and function values.
    """
    if not np.isclose(x0_vec[0] + x0_vec[1], 1.0):
        raise ValueError("Initial point must be on the line x+y=1.")
        
    x = x0_vec.copy()
    history = []
    
    for k in range(num_iterations + 1):
        f_x = f(x)
        history.append({'iteration': k, 'x': x[0], 'y': x[1], 'f(x,y)': f_x})
        if k == num_iterations:
            break
        
        # As derived, the update is x_{k+1} = x_k - (alpha/2)*x_k^(1/3)
        x_val = x[0]
        # np.cbrt handles negative numbers correctly, no special checks needed for real results
        x[0] = x_val - (alpha/2) * np.cbrt(x_val)
            
        x[1] = 1 - x[0]
        
    return pd.DataFrame(history)

if __name__ == "__main__":
    # --- Part (b): Newton's Method ---
    x_initial_newton = np.array([1.0, 0.0]) # An initial point with x0 != 0
    iterations_newton = 5 # Fewer iterations as it diverges quickly
    history_newton = newtons_method(x_initial_newton, iterations_newton)
    print("--- Newton's Method Results ---")
    print(history_newton.to_string(index=False))
    print("\n" + "="*70 + "\n")
    
    # --- Part (c): Projected Gradient Descent ---
    # Initial point must be on the line x+y=1
    x_initial_pgd = np.array([2.0, -1.0])
    iterations_pgd = 10
    step_size_pgd = 0.1
    history_pgd = projected_gradient_descent(x_initial_pgd, iterations_pgd, step_size_pgd)
    print("--- Projected Gradient Descent Results (alpha=0.1) ---")
    print(history_pgd.to_string(index=False))
    print("\n" + "="*70 + "\n")
