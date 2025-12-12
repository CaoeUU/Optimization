"""
This script demonstrates the point made in Problem 1(b) of HW6.
It shows that for the function f(x) = |x|^(3/2), and for any constant
step size alpha, we can find an initial point x0 such that a gradient
descent step increases the function value.
"""
import numpy as np

def f(x):
    """
    Computes the function value f(x) = |x|^(3/2).
    """
    return np.abs(x)**1.5

def grad_f(x):
    """
    Computes the gradient of f(x).
    Note that the gradient at x=0 is 0.
    """
    if x == 0:
        return 0
    return 1.5 * np.sign(x) * np.sqrt(np.abs(x))

def demonstrate_divergence(alpha):
    """
    For a given step size alpha, finds an x0 that demonstrates
    f(x1) >= f(x0).
    
    Args:
        alpha (float): The constant step size for gradient descent.
    """
    # From the derivation in prob1.md, we know that if we choose x0 such that
    # 0 < sqrt(x0) <= (3/4)*alpha, the condition will be met.
    # Let's choose sqrt(x0) = 0.5 * alpha.
    x0 = (0.5 * alpha)**2
    
    # Perform one step of gradient descent
    gradient = grad_f(x0)
    x1 = x0 - alpha * gradient
    
    # Get the function values
    f_x0 = f(x0)
    f_x1 = f(x1)
    
    print(f"For step size alpha = {alpha}:")
    print(f"  - We chose x0 = {x0:.4f}")
    print(f"  - The gradient at x0 is grad_f(x0) = {gradient:.4f}")
    print(f"  - The next iterate is x1 = x0 - alpha * grad_f(x0) = {x1:.4f}")
    print(f"  - The function value at x0 is f(x0) = {f_x0:.4f}")
    print(f"  - The function value at x1 is f(x1) = {f_x1:.4f}")
    
    if f_x1 >= f_x0:
        print("  - As shown, f(x1) >= f(x0), so the function value increased.")
    else:
        # This part should not be reached given the correct derivation
        print("  - f(x1) < f(x0). Something is wrong with the logic.")
    print("-" * 30)

if __name__ == "__main__":
    # Demonstrate for a few different step sizes
    demonstrate_divergence(alpha=0.1)
    demonstrate_divergence(alpha=1.0)
    demonstrate_divergence(alpha=10.0)
