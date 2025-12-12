"""
This script implements the optimization algorithms for Problem 3 of HW6.
It includes Newton's method and projected gradient descent for the function
f(x, y) = (3/4)x^4 + (1/2)(x+y)^2.
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
    return 0.75 * x**4 + 0.5 * (x + y)**2

def grad_f(x_vec):
    """
    Computes the gradient of f(x, y).
    
    Args:
        x_vec (np.ndarray): A 2D vector [x, y].
        
    Returns:
        np.ndarray: The gradient vector.
    """
    x, y = x_vec[0], x_vec[1]
    return np.array([3 * x**3 + (x + y), x + y])

def hessian_f(x_vec):
    """
    Computes the Hessian of f(x, y).
    
    Args:
        x_vec (np.ndarray): A 2D vector [x, y].
        
    Returns:
        np.ndarray: The Hessian matrix.
    """
    x, y = x_vec[0], x_vec[1]
    return np.array([[9 * x**2 + 1, 1], [1, 1]])

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
    print("As shown in the markdown, the iterates converge linearly to (0,0),")
    print("which contradicts the problem statement. This is due to the singular")
    print("Hessian at the minimizer.\n")

    for k in range(num_iterations + 1):
        f_x = f(x)
        history.append({'iteration': k, 'x': x[0], 'y': x[1], 'f(x,y)': f_x})
        if k == num_iterations:
            break
            
        if x[0] == 0:
            print(f"Hessian is singular at iteration {k} (x=0). Stopping.")
            break
            
        # Newton's step: x_k+1 = x_k - H_inv * g
        g = grad_f(x)
        H = hessian_f(x)
        H_inv = np.linalg.inv(H)
        x = x - H_inv @ g
        
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
        
        # As derived, the update is x_{k+1} = x_k - (3/2)*alpha*x_k^3
        x[0] = x[0] - 1.5 * alpha * x[0]**3
        x[1] = 1 - x[0]
        
    return pd.DataFrame(history)

if __name__ == "__main__":
    # --- Part (b): Newton's Method ---
    x_initial_newton = np.array([2.0, 5.0]) # An initial point with x0 != 0
    iterations_newton = 15
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
