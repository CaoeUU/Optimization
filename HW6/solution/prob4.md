## Problem 4

Let $L = \{x \in \mathbb{R}^n : x = p + tv, t \in \mathbb{R}\}$ be a line through a point $p \in \mathbb{R}^n$ with direction vector $v \ne 0$.
Let $B = \{x \in \mathbb{R}^n : \|x - c\|_2 \le r\}$ be a closed ball of radius $r > 0$ centered at $c \in \mathbb{R}^n$.
Let $C = L \cap B$.
We want to compute the projection of a point $x \in \mathbb{R}^n$ onto $C$, denoted as $P_C(x) = \text{arg min}_{y \in C} \|y-x\|^2$.

### (a) Show that the projection onto $L$ can be expressed as $P_L(x) = p + \frac{v^T(x-p)}{\|v\|^2}v$.

The projection of $x$ onto the line $L$, denoted $P_L(x)$, is the point $y \in L$ that minimizes the squared Euclidean distance $\|y-x\|^2$.
A point $y$ on the line $L$ can be parameterized by $t \in \mathbb{R}$ as $y(t) = p + tv$.
We want to find the value of $t$ that minimizes the distance. Let the squared distance be a function of $t$:
$$ h(t) = \|y(t) - x\|^2 = \|(p - x) + tv\|^2 $$
To minimize $h(t)$, we can minimize its squared value. We expand the expression:
$$ h(t) = ((p-x)+tv)^T((p-x)+tv) = \|p-x\|^2 + 2t(p-x)^T v + t^2\|v\|^2 $$
This is a quadratic function of $t$. To find the minimum, we take the derivative with respect to $t$ and set it to zero:
$$ \frac{dh}{dt} = 2(p-x)^T v + 2t\|v\|^2 = 0 $$
Solving for $t$:
$$ 2t\|v\|^2 = -2(p-x)^T v = 2(x-p)^T v $$
$$ t^* = \frac{(x-p)^T v}{\|v\|^2} = \frac{v^T(x-p)}{\|v\|^2} $$
The projection point $P_L(x)$ is $y(t^*)$:
$$ P_L(x) = p + t^*v = p + \frac{v^T(x-p)}{\|v\|^2}v $$
This completes the proof.

### (b) Explain that if the projection of $x$ onto $L$ lies in $B$ (i.e., $P_L(x) \in B$), then $P_C(x) = P_L(x)$.

The projection $P_C(x)$ is the solution to the constrained optimization problem:
$$ \min_{y} \|y-x\|^2 \quad \text{subject to} \quad y \in C $$
The constraint set is $C = L \cap B$. This means any feasible point $y$ must belong to both the line $L$ and the ball $B$.

Let $y_L = P_L(x)$. By definition, $y_L$ is the unique point on the line $L$ that is closest to $x$. This means that for any point $y \in L$ where $y \ne y_L$, we have:
$$ \|y_L - x\|^2 < \|y - x\|^2 $$
We are given the condition that $P_L(x) \in B$. This means $y_L \in B$.
Since $y_L$ is on the line $L$ by definition, and we are given that it is also in the ball $B$, it follows that $y_L \in L \cap B$, which means $y_L \in C$.

Now consider the optimization problem for $P_C(x)$. We are looking for a point in $C$ that is closest to $x$.
Since $C$ is a subset of $L$ ($C \subseteq L$), any point in $C$ is also in $L$.
From the property of $y_L$ as the projection onto $L$, we know that it is closer to $x$ than any other point on $L$.
Since all other points in $C$ are also on $L$, $y_L$ must also be closer to $x$ than any other point in $C$.
$$ \|y_L - x\|^2 \le \|y - x\|^2 \quad \text{for all } y \in C $$
And since we have already established that $y_L$ is itself an element of $C$, it must be the solution to the minimization problem over $C$.

Therefore, if $P_L(x) \in B$, then $P_C(x) = P_L(x).$