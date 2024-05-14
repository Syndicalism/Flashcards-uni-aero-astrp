TARGET_DECK: Aero systems control::Topic 2

---

START_CARD
Basic

Obtain a mathematical model for the system below between $v_{i}$ and $V_{0}$, then also one for just $q$.

![[Pasted image 20240101080848.png]]

Back: 
The input and output can be related:
$$ \begin{align}
 v_{i} - (v_{r} + v_{l}) &= v_{o} &&\to& v_{i} &= v_{o} + v_{r} + v_{l}
\end{align} $$
Then we can derive expressions for each component:
$$ \begin{align}
&& i &= C \frac{dv_{o}}{dt} = \frac{dq}{dt} \\
v_{r} &= iR = \frac{dq}{dt} R &&\to&  v_{r} &= C \frac{dv_{o}}{dt} R \\
v_{l} &= L \frac{di}{dt} = L\frac{d}{dt} \frac{dq}{dt}  &&\to&  v_{l} &= L \frac{d}{dt} \left(C \frac{dv_{o}}{dt}\right)= L C \frac{d^{2}v_{o}}{dt^{2}} 
\end{align} $$

Now subbing back into the previous equation:
$$ \begin{align}
v_{i} &= v_{o} + v_{r} + v_{l}&&\to& v_{i} &= v_{o} +  RC \frac{dv_{o}}{dt}  + L C \frac{d^{2}v_{o}}{dt^{2}}  
\end{align} $$

Then taking $i$ about the first loop:
$$ \begin{align}
 i &= C \frac{dv_{o}}{dt} = \frac{dq}{dt} &&\to&  \\
&& v_{i} &= v_{r} + v_{l} + v_{c} &&\to& v_{i} &= \frac{dq}{dt} R + L \frac{d^{2}q}{dt^{2}}  + \frac{1}{C} q 
\end{align} $$

<!--ID: 1704396501883-->
END_CARD



--------

START_CARD
Basic

Are these linear or non-linear, why?

![[Pasted image 20240101085145.png]]


Back: 
- e is linear, x is a function of t
- f is non-linear, x is a function of y
<!--ID: 1704396501893-->
END_CARD


--------

START_CARD
Basic

Write the force equation for the following system. Assume the bar and springs to have negligible masses.

![[Pasted image 20240101091441.png]]

Back: 
- It is critical to recognise that in this system the displacements for the top and bottom springs can be independent
- Going to assume x to be positive in the down direction
$$ \begin{align}
\sum\limits F &= mg - x_{2} k_{3} - x_{1}(k_{1} + k_{2}) 
\end{align} $$


<!--ID: 1704396501902-->
END_CARD




