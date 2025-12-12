import numpy as np
import pandas as pd

def f(x_vec):
    x, y = x_vec[0], x_vec[1]
    return 0.75 * (np.cbrt(x)**4) + 0.5 * (x + y)**2

def grad_f(x_vec):
    x, y = x_vec[0], x_vec[1]
    return np.array([np.cbrt(x) + (x + y), x + y])

def hessian_f(x_vec):
    x, y = x_vec[0], x_vec[1]
    if x == 0:
        return np.array([[np.inf, 1], [1, 1]])
    return np.array([[(1/3) * (np.cbrt(x)**(-2)) + 1, 1], [1, 1]])

def newtons_method(x0_vec, num_iterations):
    x = x0_vec.copy()
    history = []
    
    for k in range(num_iterations + 1):
        history.append({'iteration': k, 'x': x[0], 'y': x[1], 'f(x,y)': f(x)})
        if k == num_iterations:
            break
            
        if np.isclose(x[0], 0.0):
            print(f"Hessian singular near x=0 at iteration {k}. Stopping.")
            break
            
        g = grad_f(x)
        H = hessian_f(x)
        
        if np.isclose(np.linalg.det(H), 0.0) or np.any(np.isinf(H)) or np.any(np.isnan(H)):
            print(f"Hessian singular/ill-conditioned at iteration {k}. Stopping.")
            break
        
        try:
            H_inv = np.linalg.inv(H)
            x = x - H_inv @ g
        except np.linalg.LinAlgError:
            print(f"Inverse of Hessian failed at iteration {k}. Stopping.")
            break
        
    return pd.DataFrame(history)

def projected_gradient_descent(x0_vec, num_iterations, alpha):
    if not np.isclose(x0_vec[0] + x0_vec[1], 1.0):
        raise ValueError("Initial point must be on the line x+y=1.")
        
    x = x0_vec.copy()
    history = []
    
    for k in range(num_iterations + 1):
        history.append({'iteration': k, 'x': x[0], 'y': x[1], 'f(x,y)': f(x)})
        if k == num_iterations:
            break
        
        x_val = x[0]
        x[0] = x_val - (alpha/2) * np.cbrt(x_val)
        x[1] = 1 - x[0]
        
    return pd.DataFrame(history)

if __name__ == "__main__":
    x_initial_newton = np.array([1.0, 0.0])
    iterations_newton = 5
    history_newton = newtons_method(x_initial_newton, iterations_newton)
    print("--- Newton's Method Results ---")
    print(history_newton.to_string(index=False))
    print("\n" + "="*70 + "\n")
    
    x_initial_pgd = np.array([2.0, -1.0])
    iterations_pgd = 10
    step_size_pgd = 0.1
    history_pgd = projected_gradient_descent(x_initial_pgd, iterations_pgd, step_size_pgd)
    print("--- Projected Gradient Descent Results (alpha=0.1) ---")
    print(history_pgd.to_string(index=False))
    print("\n" + "="*70 + "\n")
