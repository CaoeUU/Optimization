## Problem 1

We are given the function $f(x) = |x|^{3/2}$. We assume $x \in \mathbb{R}$.

### (a) Prove $f$ is not Lipschitz smooth.

A function $f$ is Lipschitz smooth with constant $L>0$ if its gradient is Lipschitz continuous, i.e., $\|\nabla f(x) - \nabla f(y)\| \le L \|x - y\|$ for all $x, y$. In our 1D case, this is $|f'(x) - f'(y)| \le L|x-y|$.

First, let's find the derivative of $f(x)$.
- For $x > 0$, $f(x) = x^{3/2}$, so $f'(x) = \frac{3}{2}x^{1/2}$.
- For $x < 0$, $f(x) = (-x)^{3/2}$, so $f'(x) = \frac{3}{2}(-x)^{1/2} \cdot (-1) = -\frac{3}{2}(-x)^{1/2}$.
We can write this as $f'(x) = \frac{3}{2} \text{sign}(x)\sqrt{|x|}$.

Let's find the derivative at $x=0$:
$$ f'(0) = \lim_{h\to 0} \frac{f(h) - f(0)}{h} = \lim_{h\to 0} \frac{|h|^{3/2}}{h} $$
- If $h \to 0^+$, $\lim_{h\to 0^+} \frac{h^{3/2}}{h} = \lim_{h\to 0^+} h^{1/2} = 0$.
- If $h \to 0^-$, $\lim_{h\to 0^-} \frac{(-h)^{3/2}}{h} = \lim_{h\to 0^-} \frac{-(-h)\sqrt{-h}}{h} = \lim_{h\to 0^-} -\sqrt{-h} = 0$.
So, $f'(0) = 0$.

Now, let's check the Lipschitz condition for $f'(x)$. Let's pick $y=0$ and $x > 0$.
The condition is $|f'(x) - f'(0)| \le L|x-0|$.
$$ |\frac{3}{2}\sqrt{x} - 0| \le L|x| $$
$$ \frac{3}{2}\sqrt{x} \le Lx $$
$$ \frac{3}{2\sqrt{x}} \le L $$
As $x \to 0^+$, the term $\frac{3}{2\sqrt{x}}$ goes to infinity. It is impossible to find a finite constant $L$ that satisfies this inequality for all $x$.

Therefore, $f(x) = |x|^{3/2}$ is not Lipschitz smooth.

### (b) Prove that for any constant step size $\bar{\alpha} > 0$, there exists an initial point $x_0$ for which $f(x_1) \ge f(x_0)$.

The gradient descent update rule is $x_1 = x_0 - \bar{\alpha} \nabla f(x_0)$. In our case, $x_1 = x_0 - \bar{\alpha} f'(x_0)$.

We want to show that there exists an $x_0$ such that $f(x_1) \ge f(x_0)$, which is equivalent to $|x_1|^{3/2} \ge |x_0|^{3/2}$, or $|x_1| \ge |x_0|$.

Let's choose $x_0 > 0$. The update rule becomes:
$$ x_1 = x_0 - \bar{\alpha} \left(\frac{3}{2}\sqrt{x_0}\right) $$
We want to find an $x_0 > 0$ such that:
$$ \left|x_0 - \frac{3}{2}\bar{\alpha}\sqrt{x_0}\right| \ge x_0 $$
Let $\sqrt{x_0} = z$. Since $x_0 > 0$, we have $z > 0$. The inequality becomes:
$$ |z^2 - \frac{3}{2}\bar{\alpha}z| \ge z^2 $$
$$ |z(z - \frac{3}{2}\bar{\alpha})| \ge z^2 $$
Since $z > 0$, we can divide by $z$:
$$ |z - \frac{3}{2}\bar{\alpha}| \ge z $$
For any given $\bar{\alpha} > 0$, we can choose $z$ to be small enough such that $z < \frac{3}{2}\bar{\alpha}$. For example, we can choose $z \le \frac{3}{4}\bar{\alpha}$.
If $0 < z \le \frac{3}{4}\bar{\alpha}$, then $z - \frac{3}{2}\bar{\alpha}$ is negative. So, its absolute value is:
$$ |z - \frac{3}{2}\bar{\alpha}| = \frac{3}{2}\bar{\alpha} - z $$
The inequality becomes:
$$ \frac{3}{2}\bar{\alpha} - z \ge z $$
$$ \frac{3}{2}\bar{\alpha} \ge 2z $$
$$ z \le \frac{3}{4}\bar{\alpha} $$
So, for any $\bar{\alpha} > 0$, we can choose any $x_0$ such that $0 < \sqrt{x_0} \le \frac{3}{4}\bar{\alpha}$. For example, we can pick $x_0 = (\frac{3}{4}\bar{\alpha})^2$. For such an $x_0$, the gradient descent step will result in an increase in the function value. This proves the statement.