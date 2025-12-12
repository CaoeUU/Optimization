## Problem 2

Minimize $f(x) = x^T A x$, where $A = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$. This implies $f(x_1, x_2) = 2x_1^2 + 5x_2^2$.
Initial point: $x_0 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

Gradient of $f(x)$ is $\nabla f(x) = 2Ax = \begin{pmatrix} 4x_1 \\ 10x_2 \end{pmatrix}$.
At $x_0$: $f(x_0) = 7$, $\nabla f(x_0) = \begin{pmatrix} 4 \\ 10 \end{pmatrix}$, and $\|\nabla f(x_0)\|^2 = 116$.

The gradient descent update rule is $x_{k+1} = x_k - \alpha_k \nabla f(x_k)$.

### (a) Compute one step of gradient descent

#### i. Constant step size $\alpha_k = 0.1$

For $k=0$, $\alpha_0 = 0.1$:
$$ x_1 = x_0 - \alpha_0 \nabla f(x_0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - 0.1 \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} 0.6 \\ 0 \end{pmatrix} $$ 
Thus, $x_1 = \begin{pmatrix} 0.6 \\ 0 \end{pmatrix}$.

#### ii. Exact line search

The optimal step size for a quadratic function $f(x) = x^T A x$ is:
$$ \alpha_k = \frac{\nabla f(x_k)^T \nabla f(x_k)}{2 \nabla f(x_k)^T A \nabla f(x_k)} $$ 
At $k=0$:
$$ \alpha_0 = \frac{\|\nabla f(x_0)\|^2}{2 \nabla f(x_0)^T A \nabla f(x_0)} = \frac{116}{2 \begin{pmatrix} 4 & 10 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 4 \\ 10 \end{pmatrix}} = \frac{116}{2 \cdot 532} = \frac{116}{1064} = \frac{29}{266} \approx 0.109 $$ 
Then, $x_1$:
$$ x_1 = x_0 - \alpha_0 \nabla f(x_0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - \frac{29}{266} \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} \frac{75}{133} \\ -\frac{12}{133} \end{pmatrix} \approx \begin{pmatrix} 0.5639 \\ -0.0902 \end{pmatrix} $$ 
Thus, $x_1 = \begin{pmatrix} 75/133 \\ -12/133 \end{pmatrix}$.

#### iii. Backtracking line search

Parameters: $\gamma = 0.5$, $\sigma = 0.2$. Initial $\alpha=1$.
Armijo condition: $f(x_k - \alpha \nabla f(x_k)) \le f(x_k) - \gamma \alpha \|\nabla f(x_k)\|^2$.
At $k=0$, the condition is $f(x_0 - \alpha \nabla f(x_0)) \le 7 - 58\alpha$.

-   Try $\alpha = 1$: $f(\begin{pmatrix} -3 \\ -9 \end{pmatrix}) = 423$. Condition: $423 \le -51$ (False).
-   Update $\alpha = 0.2 \cdot 1 = 0.2$:
    -   Try $\alpha = 0.2$: $f(\begin{pmatrix} 0.2 \\ -1 \end{pmatrix}) = 5.08$. Condition: $5.08 \le -4.6$ (False).
-   Update $\alpha = 0.2 \cdot 0.2 = 0.04$:
    -   Try $\alpha = 0.04$: $f(\begin{pmatrix} 0.84 \\ 0.6 \end{pmatrix}) = 3.2112$. Condition: $3.2112 \le 4.68$ (True).

The condition is satisfied for $\alpha_0 = 0.04$.
$$ x_1 = x_0 - \alpha_0 \nabla f(x_0) = \begin{pmatrix} 0.84 \\ 0.6 \end{pmatrix} $$ 
Thus, $x_1 = \begin{pmatrix} 0.84 \\ 0.6 \end{pmatrix}$.