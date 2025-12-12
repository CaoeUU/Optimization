import numpy as np
import pandas as pd

A = np.array([[2., 0.], [0., 5.]])

def f(x):
    return x.T @ A @ x

def grad_f(x):
    return 2 * A @ x

def gradient_descent_constant_step(x0, num_iterations, alpha):
    x = x0.copy()
    history = []
    for k in range(num_iterations + 1):
        history.append({'iteration': k, 'x1': x[0], 'x2': x[1], 'f(x)': f(x)})
        if k == num_iterations:
            break
        x = x - alpha * grad_f(x)
    return pd.DataFrame(history)

def gradient_descent_exact_line_search(x0, num_iterations):
    x = x0.copy()
    history = []
    for k in range(num_iterations + 1):
        history.append({'iteration': k, 'x1': x[0], 'x2': x[1], 'f(x)': f(x)})
        if k == num_iterations:
            break
        gradient = grad_f(x)
        alpha = (gradient.T @ gradient) / (2 * gradient.T @ A @ gradient)
        x = x - alpha * gradient
    return pd.DataFrame(history)

def gradient_descent_backtracking(x0, num_iterations, gamma=0.5, sigma=0.2, alpha_init=1.0):
    x = x0.copy()
    history = []
    for k in range(num_iterations + 1):
        history.append({'iteration': k, 'x1': x[0], 'x2': x[1], 'f(x)': f(x)})
        if k == num_iterations:
            break
        gradient = grad_f(x)
        grad_norm_sq = gradient.T @ gradient
        
        alpha = alpha_init
        while f(x - alpha * gradient) > f(x) - gamma * alpha * grad_norm_sq:
            alpha = sigma * alpha
            
        x = x - alpha * gradient
    return pd.DataFrame(history)

if __name__ == "__main__":
    x_initial = np.array([1., 1.])
    iterations = 10
    
    print("Constant Step Size (alpha = 0.1)")
    history_constant = gradient_descent_constant_step(x_initial, iterations, alpha=0.1)
    print(history_constant.to_string(index=False))
    print("\n" + "="*70 + "\n")
    
    print("Exact Line Search")
    history_exact = gradient_descent_exact_line_search(x_initial, iterations)
    print(history_exact.to_string(index=False))
    print("\n" + "="*70 + "\n")
    
    print("Backtracking Line Search (gamma=0.5, sigma=0.2)")
    history_backtracking = gradient_descent_backtracking(x_initial, iterations, gamma=0.5, sigma=0.2)
    print(history_backtracking.to_string(index=False))
    print("\n" + "="*70 + "\n")
