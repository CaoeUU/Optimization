## Problem 4

Given line $L = \{x \in \mathbb{R}^n : x = p + tv, t \in \mathbb{R}\}$ (with $v \ne 0$) and closed ball $B = \{x \in \mathbb{R}^n : \|x - c\|_2 \le r\}$ (with $r > 0$).
Let $C = L \cap B$. We want to compute $P_C(x) = \text{arg min}_{y \in C} \|y-x\|^2$.

### (a) Show that the projection onto $L$ can be expressed as $P_L(x) = p + \frac{v^T(x-p)}{\|v\|^2}v$.

The projection $P_L(x)$ minimizes $\|y-x\|^2$ for $y \in L$.
Let $y(t) = p + tv$. We minimize $h(t) = \|(p - x) + tv\|^2 = \|p-x\|^2 + 2t(p-x)^T v + t^2\|v\|^2$.
Setting $\frac{dh}{dt} = 2(p-x)^T v + 2t\|v\|^2 = 0$, we find $t^* = \frac{(x-p)^T v}{\|v\|^2} = \frac{v^T(x-p)}{\|v\|^2}$.
Thus, $P_L(x) = p + t^*v = p + \frac{v^T(x-p)}{\|v\|^2}v$.

### (b) Explain that if the projection of $x$ onto $L$ lies in $B$ (i.e., $P_L(x) \in B$), then $P_C(x) = P_L(x)$.

Let $y_L = P_L(x)$. By definition, $y_L$ is the unique point on line $L$ closest to $x$.
If $P_L(x) \in B$, then $y_L \in B$. Since $y_L \in L$, it follows that $y_L \in L \cap B$, so $y_L \in C$.
For any $y \in C$, we know $y \in L$. By the definition of $P_L(x)$, $\|y_L - x\|^2 \le \|y - x\|^2$ for all $y \in L$.
Since $C \subseteq L$, this inequality also holds for all $y \in C$.
As $y_L \in C$ and it is the closest point to $x$ among all points in $C$, $y_L$ must be $P_C(x)$.
Thus, if $P_L(x) \in B$, then $P_C(x) = P_L(x).$
