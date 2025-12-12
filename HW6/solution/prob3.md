## Problem 3

Given the function $f: \mathbb{R}^2 \to \mathbb{R}$:
$$ f(x, y) = \frac{3}{4}x^{\frac{4}{3}} + \frac{1}{2}(x + y)^2 $$

### (a) Find its global minimizer.

Critical points are found by setting the gradient of $f$ to zero.
The gradient is:
$$ \nabla f(x, y) = \begin{pmatrix} x^{\frac{1}{3}} + (x+y) \\ x+y \end{pmatrix} $$
Setting $\nabla f(x,y) = \mathbf{0}$:
From the second equation, $x+y=0$.
Substituting this into the first equation gives $x^{1/3} = 0 \implies x=0$.
Since $x+y=0$, we have $y = -x = 0$.
The only critical point is $(0, 0)$.

Global minimizer verification:
The function $f(x,y)$ is a sum of two non-negative terms: $\frac{3}{4}x^{\frac{4}{3}} \ge 0$ and $\frac{1}{2}(x+y)^2 \ge 0$.
Thus, $f(x, y) \ge 0$ for all $(x, y) \in \mathbb{R}^2$.
At $(0,0)$, $f(0,0) = 0$.
Since $f(x,y) \ge f(0,0)$ for all $(x,y)$, the point $(0,0)$ is the global minimizer.

### (b) Newton's method

The update rule for Newton's method is $\mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$.
The Hessian matrix is:
$$ \nabla^2 f(x, y) = \begin{pmatrix} \frac{1}{3}x^{-\frac{2}{3}}+1 & 1 \\ 1 & 1 \end{pmatrix} $$
The determinant is $\det(\nabla^2 f) = \frac{1}{3}x^{-\frac{2}{3}}$. The inverse exists for $x \ne 0$.
The Newton step $[\nabla^2 f]^{-1} \nabla f$ at $(x_k, y_k)$ is:
$$ [\nabla^2 f]^{-1} \nabla f = \begin{pmatrix} 3x_k \\ -3x_k + (x_k+y_k) \end{pmatrix} $$
The update rule is:
$$ \begin{pmatrix} x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} x_k \\ y_k \end{pmatrix} - \begin{pmatrix} 3x_k \\ -3x_k + (x_k+y_k) \end{pmatrix} = \begin{pmatrix} -2x_k \\ 2x_k - (x_k+y_k) + y_k \end{pmatrix} = \begin{pmatrix} -2x_k \\ 2x_k \end{pmatrix} $$

Convergence analysis:
Starting from $(x_0, y_0)$ with $x_0 \ne 0$, the iterates are $x_k = (-2)^k x_0$ and $y_k = 2x_{k-1} = 2(-2)^{k-1}x_0 = (-2)^k x_0$ for $k \ge 1$.
Since $|-2| > 1$, the magnitude $|x_k| = 2^k |x_0|$ diverges to infinity.
Therefore, $(x_k, y_k)$ does not converge to the global minimizer $(0,0)$.

### (c) Projected gradient descent

Minimize $f$ subject to the constraint $\Omega = \{(x, y) : x + y = 1\}$.
One iteration of the projected gradient descent method:
1. Compute an intermediate point: $\mathbf{z}_{k+1} = \mathbf{x}_k - \alpha_k \nabla f(\mathbf{x}_k)$.
2. Project onto constraint: $\mathbf{x}_{k+1} = \text{Proj}_{\Omega}(\mathbf{z}_{k+1})$.

For $\mathbf{x}_k = (x_k, y_k)$ on $x_k+y_k=1$:
$$ \nabla f(x_k, y_k) = \begin{pmatrix} x_k^{\frac{1}{3}} + 1 \\ 1 \end{pmatrix} $$
$$ z_{k+1,1} = x_k - \alpha_k(x_k^{\frac{1}{3}} + 1) $$
$$ z_{k+1,2} = y_k - \alpha_k $$
The projection of a point $(z_1, z_2)$ onto the line $x+y=c$ is $( (z_1-z_2+c)/2, (z_2-z_1+c)/2 )$. Here $c=1$.
$$ x_{k+1} = \frac{(x_k - \alpha_k(x_k^{\frac{1}{3}} + 1)) - (y_k - \alpha_k) + 1}{2} $$
Since $y_k = 1 - x_k$:
$$ x_{k+1} = \frac{x_k - (1-x_k) - \alpha_k x_k^{\frac{1}{3}} + 1}{2} = x_k - \frac{\alpha_k}{2} x_k^{\frac{1}{3}} $$
And $y_{k+1} = 1 - x_{k+1}$.
The iteration is:
$$ x_{k+1} = x_k - \frac{\alpha_k}{2} x_k^{\frac{1}{3}} $$
$$ y_{k+1} = 1 - x_{k+1} $$