import numpy as np

def f(x):
    return np.abs(x)**1.5

def grad_f(x):
    if x == 0:
        return 0
    return 1.5 * np.sign(x) * np.sqrt(np.abs(x))

def demonstrate_divergence(alpha):
    x0 = (0.5 * alpha)**2
    gradient = grad_f(x0)
    x1 = x0 - alpha * gradient
    
    f_x0 = f(x0)
    f_x1 = f(x1)
    
    print(f"Alpha={alpha:.2f}: x0={x0:.4f}, f(x0)={f_x0:.4f}, x1={x1:.4f}, f(x1)={f_x1:.4f}")
    if f_x1 >= f_x0:
        print("  f(x1) >= f(x0) - function value increased.")
    else:
        print("  f(x1) < f(x0) - unexpected behavior.")
    print("-" * 30)

if __name__ == "__main__":
    demonstrate_divergence(alpha=0.1)
    demonstrate_divergence(alpha=1.0)
    demonstrate_divergence(alpha=10.0)
