## Problem 3

We are given the function $f: \mathbb{R}^2 \to \mathbb{R}$:
$$ f(x, y) = \frac{3}{4}x^4 + \frac{1}{2}(x + y)^2 $$

### (a) Find its global minimizer.

To find the minimizer, we first find the critical points by setting the gradient of $f$ to zero.
The gradient is:
$$ \nabla f(x, y) = \begin{pmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{pmatrix} = \begin{pmatrix} 3x^3 + (x+y) \\ x+y \end{pmatrix} $$
Set the gradient to zero:
$$ \begin{pmatrix} 3x^3 + (x+y) \\ x+y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$
From the second equation, we have $x+y=0$.
Substituting this into the first equation gives $3x^3 = 0$, which implies $x=0$.
Since $x+y=0$, we have $y = -x = 0$.
The only critical point is $(0, 0)$.

Now, we must determine if this point is a global minimizer.
The function $f(x,y)$ is a sum of two non-negative terms:
- $\frac{3}{4}x^4 \ge 0$ for all $x$.
- $\frac{1}{2}(x+y)^2 \ge 0$ for all $x, y$.
Thus, $f(x, y) \ge 0$ for all $(x, y) \in \mathbb{R}^2$.
At the critical point $(0,0)$, the function value is $f(0,0) = 0$.
Since $f(x,y) \ge f(0,0)$ for all $(x,y)$, the point $(0,0)$ is the global minimizer.

### (b) Newton's method

The update rule for Newton's method is:
$$ \mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k) $$
where $\mathbf{x}_k = (x_k, y_k)^T$.

First, we compute the Hessian matrix $\nabla^2 f(x, y)$:
$$ \nabla^2 f(x, y) = \begin{pmatrix} 9x^2+1 & 1 \\ 1 & 1 \end{pmatrix} $$
The inverse of the Hessian is:
$$ [\nabla^2 f(x, y)]^{-1} = \frac{1}{\det(\nabla^2 f)} \begin{pmatrix} 1 & -1 \\ -1 & 9x^2+1 \end{pmatrix} $$
The determinant is $\det(\nabla^2 f) = (9x^2+1)(1) - (1)(1) = 9x^2$.
The inverse is defined for $x \ne 0$. The problem states we start with an initial point $(x_0, y_0)$ with $x_0 \ne 0$.

Let's compute the Newton step at a point $(x_k, y_k)$ where $x_k \ne 0$:
$$ [\nabla^2 f]^{-1} \nabla f = \frac{1}{9x_k^2} \begin{pmatrix} 1 & -1 \\ -1 & 9x_k^2+1 \end{pmatrix} \begin{pmatrix} 3x_k^3 + x_k+y_k \\ x_k+y_k \end{pmatrix} $$
The top component of the resulting vector is:
$$ \frac{1}{9x_k^2} [ (3x_k^3 + x_k+y_k) - (x_k+y_k) ] = \frac{3x_k^3}{9x_k^2} = \frac{x_k}{3} $$
The bottom component is:
$$ \frac{1}{9x_k^2} [ -(3x_k^3 + x_k+y_k) + (9x_k^2+1)(x_k+y_k) ] = \frac{1}{9x_k^2} [ -3x_k^3 - (x_k+y_k) + 9x_k^2(x_k+y_k) + (x_k+y_k) ] = \frac{-3x_k^3 + 9x_k^2(x_k+y_k)}{9x_k^2} = -\frac{x_k}{3} + x_k+y_k $$
So, the update rule is:
$$ \begin{pmatrix} x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} x_k \\ y_k \end{pmatrix} - \begin{pmatrix} x_k/3 \\ -x_k/3 + x_k+y_k \end{pmatrix} $$
$$ x_{k+1} = x_k - \frac{x_k}{3} = \frac{2}{3}x_k $$
$$ y_{k+1} = y_k - (-\frac{x_k}{3} + x_k+y_k) = y_k + \frac{x_k}{3} - x_k - y_k = -\frac{2}{3}x_k $$
The expression for $(x_{k+1}, y_{k+1})$ is $(\frac{2}{3}x_k, -\frac{2}{3}x_k)$.

The problem asks to prove that Newton's method does not converge to the global minimizer. However, my derivation shows that it does converge.
Let's analyze the sequence of iterates starting from $(x_0, y_0)$ with $x_0 \ne 0$:
- $x_k = (\frac{2}{3})^k x_0$
- For $k \ge 1$, $y_k = -\frac{2}{3}x_{k-1} = -\frac{2}{3}(\frac{2}{3})^{k-1}x_0 = -(\frac{2}{3})^k x_0$.
As $k \to \infty$, since $|\frac{2}{3}| < 1$, both $x_k \to 0$ and $y_k \to 0$. The sequence of iterates $(\mathbf{x}_k)_{k \ge 1}$ converges to $(0,0)$.

**Note on Convergence:** The method *does* converge to the global minimizer $(0,0)$. The likely intent of the question relates to the *rate* of convergence. Newton's method typically exhibits quadratic convergence. However, at the minimizer $(0,0)$, the Hessian is $\nabla^2 f(0,0) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, which is singular. A non-singular Hessian at the solution is a condition for quadratic convergence. Because the condition is not met, the method converges linearly (with a rate of 2/3), not quadratically. This might be what was meant by "does not converge [as expected for Newton's method]".

### (c) Projected gradient descent

We want to minimize $f$ subject to the constraint $\Omega = \{(x, y) : x + y = 1\}$.
One iteration of the projected gradient descent method is:
1. Compute an intermediate point: $\mathbf{z}_{k+1} = \mathbf{x}_k - \alpha_k \nabla f(\mathbf{x}_k)$.
2. Project the point onto the constraint set: $\mathbf{x}_{k+1} = \text{Proj}_{\Omega}(\mathbf{z}_{k+1})$.

Given a point $\mathbf{x}_k = (x_k, y_k)$ on the line $x_k+y_k=1$.
1. Compute $\mathbf{z}_{k+1} = (z_{k+1,1}, z_{k+1,2})^T$:
   $$ \nabla f(x_k, y_k) = \begin{pmatrix} 3x_k^3 + (x_k+y_k) \\ x_k+y_k \end{pmatrix} = \begin{pmatrix} 3x_k^3 + 1 \\ 1 \end{pmatrix} $$
   $$ z_{k+1,1} = x_k - \alpha_k(3x_k^3 + 1) $$
   $$ z_{k+1,2} = y_k - \alpha_k(1) $$
2. Project $\mathbf{z}_{k+1}$ onto the line $x+y=1$. The projection of a point $(z_1, z_2)$ onto the line $x+y=c$ is given by $x = \frac{z_1-z_2+c}{2}, y = \frac{-z_1+z_2+c}{2}$. Here $c=1$.
   $$ x_{k+1} = \frac{z_{k+1,1} - z_{k+1,2} + 1}{2} $$
   $$ y_{k+1} = \frac{-z_{k+1,1} + z_{k+1,2} + 1}{2} = 1 - x_{k+1} $$
Substituting the expressions for $z_{k+1,1}$ and $z_{k+1,2}$:
$$ z_{k+1,1} - z_{k+1,2} = (x_k - \alpha_k(3x_k^3 + 1)) - (y_k - \alpha_k) = x_k - y_k - 3\alpha_k x_k^3 - \alpha_k + \alpha_k = x_k - y_k - 3\alpha_k x_k^3 $$
Now substitute this into the expression for $x_{k+1}$:
$$ x_{k+1} = \frac{(x_k - y_k - 3\alpha_k x_k^3) + 1}{2} $$
Since $(x_k, y_k)$ is on the line, $y_k = 1 - x_k$.
$$ x_{k+1} = \frac{x_k - (1-x_k) - 3\alpha_k x_k^3 + 1}{2} = \frac{2x_k - 1 - 3\alpha_k x_k^3 + 1}{2} = x_k - \frac{3}{2}\alpha_k x_k^3 $$
And $y_{k+1} = 1 - x_{k+1}$.

So, one iteration is:
$$ x_{k+1} = x_k - \frac{3}{2}\alpha_k x_k^3 $$
$$ y_{k+1} = 1 - x_{k+1} $$
This is the expression for one iteration of projected gradient descent.