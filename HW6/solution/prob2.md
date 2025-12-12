## Problem 2

We are given the optimization problem:
$$ 
\min_{x} f(x) = x^T A x, \quad \text{where} \quad A = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix} 
$$ 
This can be written as $f(x_1, x_2) = 2x_1^2 + 5x_2^2$.
The initial point is $x_0 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

The gradient of $f(x)$ is $\nabla f(x) = 2Ax = \begin{pmatrix} 4 & 0 \\ 0 & 10 \end{pmatrix} x = \begin{pmatrix} 4x_1 \\ 10x_2 \end{pmatrix}$.

At the initial point $x_0 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$:
- $f(x_0) = 2(1)^2 + 5(1)^2 = 7$.
- $\nabla f(x_0) = \begin{pmatrix} 4(1) \\ 10(1) \end{pmatrix} = \begin{pmatrix} 4 \\ 10 \end{pmatrix}$.
- $\|\nabla f(x_0)\|^2 = 4^2 + 10^2 = 16 + 100 = 116$.

The gradient descent update rule is $x_{k+1} = x_k - \alpha_k \nabla f(x_k)$.

### (a) Compute one step of gradient descent

#### i. Constant step size $\alpha_k = 0.1$

For $k=0$, $\alpha_0 = 0.1$.
$$ x_1 = x_0 - \alpha_0 \nabla f(x_0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - 0.1 \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} 1 - 0.4 \\ 1 - 1.0 \end{pmatrix} = \begin{pmatrix} 0.6 \\ 0 \end{pmatrix} $$ 
So, $x_1 = \begin{pmatrix} 0.6 \\ 0 \end{pmatrix}$.

#### ii. Exact line search

We need to find the step size $\alpha_0$ that minimizes $g(\alpha) = f(x_0 - \alpha \nabla f(x_0))$.
For a quadratic function $f(x) = x^T A x$, the optimal step size is given by:
$$ \alpha_k = \frac{\nabla f(x_k)^T \nabla f(x_k)}{2 \nabla f(x_k)^T A \nabla f(x_k)} $$ 
At $k=0$:
- Numerator: $\nabla f(x_0)^T \nabla f(x_0) = \|\nabla f(x_0)\|^2 = 116$.
- Denominator: $2 \begin{pmatrix} 4 & 10 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 4 \\ 10 \end{pmatrix} = 2 \begin{pmatrix} 8 & 50 \end{pmatrix} \begin{pmatrix} 4 \\ 10 \end{pmatrix} = 2(8 \cdot 4 + 50 \cdot 10) = 2(32 + 500) = 2(532) = 1064$.
$$ \alpha_0 = \frac{116}{1064} = \frac{29}{266} \approx 0.109 $$ 
Now we compute $x_1$:
$$ x_1 = x_0 - \alpha_0 \nabla f(x_0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - \frac{29}{266} \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} 1 - \frac{116}{266} \\ 1 - \frac{290}{266} \end{pmatrix} = \begin{pmatrix} \frac{150}{266} \\ -\frac{24}{266} \end{pmatrix} = \begin{pmatrix} \frac{75}{133} \\ -\frac{12}{133} \end{pmatrix} $$ 
So, $x_1 = \begin{pmatrix} 75/133 \\ -12/133 \end{pmatrix} \approx \begin{pmatrix} 0.5639 \\ -0.0902 \end{pmatrix}$.

#### iii. Backtracking line search

We use parameters $\gamma = \frac{1}{2} = 0.5$ and $\sigma = 0.2$. We start with an initial step size, usually $\alpha=1$.
The Armijo condition is $f(x_k - \alpha \nabla f(x_k)) \le f(x_k) - \gamma \alpha \|\nabla f(x_k)\|^2$.

At $k=0$, we have $f(x_0)=7$ and $\|\nabla f(x_0)\|^2 = 116$. The condition is:
$$ f(x_0 - \alpha \nabla f(x_0)) \le 7 - 0.5 \cdot \alpha \cdot 116 = 7 - 58\alpha $$ 
Let's test values for $\alpha$, starting with $\alpha=1$:
- **Try $\alpha = 1$**:
  - $x_{try} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - 1 \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} -3 \\ -9 \end{pmatrix}$.
  - $f(x_{try}) = 2(-3)^2 + 5(-9)^2 = 2(9) + 5(81) = 18 + 405 = 423$.
  - Condition: $423 \le 7 - 58(1) = -51$. This is **false**.
- **Update $\alpha$**: $\alpha \leftarrow \sigma \alpha = 0.2 \cdot 1 = 0.2$.
- **Try $\alpha = 0.2$**:
  - $x_{try} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - 0.2 \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} 1 - 0.8 \\ 1 - 2 \end{pmatrix} = \begin{pmatrix} 0.2 \\ -1 \end{pmatrix}$.
  - $f(x_{try}) = 2(0.2)^2 + 5(-1)^2 = 2(0.04) + 5(1) = 0.08 + 5 = 5.08$.
  - Condition: $5.08 \le 7 - 58(0.2) = 7 - 11.6 = -4.6$. This is **false**.
- **Update $\alpha$**: $\alpha \leftarrow \sigma \alpha = 0.2 \cdot 0.2 = 0.04$.
- **Try $\alpha = 0.04$**:
  - $x_{try} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} - 0.04 \begin{pmatrix} 4 \\ 10 \end{pmatrix} = \begin{pmatrix} 1 - 0.16 \\ 1 - 0.4 \end{pmatrix} = \begin{pmatrix} 0.84 \\ 0.6 \end{pmatrix}$.
  - $f(x_{try}) = 2(0.84)^2 + 5(0.6)^2 = 2(0.7056) + 5(0.36) = 1.4112 + 1.8 = 3.2112$.
  - Condition: $3.2112 \le 7 - 58(0.04) = 7 - 2.32 = 4.68$. This is **true**.

The condition is satisfied for $\alpha_0 = 0.04$.
$$ x_1 = x_0 - \alpha_0 \nabla f(x_0) = \begin{pmatrix} 0.84 \\ 0.6 \end{pmatrix} $$ 
So, $x_1 = \begin{pmatrix} 0.84 \\ 0.6 \end{pmatrix}$.