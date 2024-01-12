TARGET_DECK: Aero systems control::Topic 4

---

START_CARD
Basic


State the generic first and second order system equations, commenting on the names of each of the variables and how they'd effect a generated graph to a step input.

Back: 
$$\begin{align*}
2nd: G(s)&= \frac{K \omega_{n}^{2}}{s^{2} + 2\zeta \omega_{n}s+ \omega_{n}^{2}}\\\\
1st: G(s)&= \frac{K }{\tau s+1}

\end{align*}$$
- In both, K is the system gain. It determines the "resting" position as a multiple of the input magnitude (assuming stability). So a step input of 1 will converge on a response value of K.
- In first order systems $\tau$ is time constant, it determines the rate of response. A higher value will result in a faster decay.
- In second order systems $\zeta$ is damping factor, with less than one resulting in oscillations and more than 1 resulting in no oscillations
- In second order systems $\omega_{n}$ is natural frequency, a higher natural frequency results in higher frequency oscillations
<!--ID: 1704396522463-->
END_CARD


--------

START_CARD
Basic

What is the value of $c$ at $t=10$ for a system with transfer function $2\frac{0.1}{s+0.1}$ under a step input at t=0? Then sketch it's graph. What would be the value at $t=10$ if the system started at $R=1$ then went to $R=0$ at $t=0$?

Back: 
- First get it into a standardish form:
$$ \begin{align}
2\frac{0.1}{s+0.1} &= \frac{2}{10s+1}
\end{align} $$
- Gain is clearly $K=2$ and the time constant is $\tau=10$, with the high value it's reasonably responsive
- To a step response:
$$ \begin{align}
K\left(1-e^{-\frac{t}{\tau}}\right) &= x &&\to& 2\left(1-e^{-\frac{10}{10}}\right) \approx 1.264 
\end{align} $$

- Plotted this is:
![[Pasted image 20240101105509.png]]

- Finally that would just be $Ke^{-\frac{t}{\tau}}=x$ so clearly $x=(2-1.1264)=0.736$
<!--ID: 1704396522473-->
END_CARD


--------

START_CARD
Basic

Make rough sketches of each of the following responding to a step input:

![[Pasted image 20240101112706.png]]

Back: 

![[Pasted image 20240101112739.png]]
![[Pasted image 20240101112759.png]]
<!--ID: 1704396522480-->
END_CARD


--------

START_CARD
Basic
Comment on how the poles will influence the response to a step input for each of the following:
![[Pasted image 20240101112706.png]]

Back: 
1) No imaginary component, no oscillations. Negative, stable.
2) Imaginary component, oscillations. Negative, stable.
3) Imaginary but no real component, will oscillate at the magnitude of the system
4) No imaginary component, no oscillations. Positive, unstable.
5) Imaginary component, oscillations. Positive, unstable.
6) No imaginary component, no oscillations. Tiny difference in real means it will have $\zeta\approx1$.
<!--ID: 1704396522486-->
END_CARD


--------

START_CARD
Basic

Sketch the step response to the following, justifying approximations:

![[Pasted image 20240101115117.png]]

Back: 
- Sketching the pole plot gives:
![[Pasted image 20240101115204.png]]

- Both sets are negative, hence the system is stable
- The second set of poles have a significantly smaller real component (by orders of magnitude), hence they will have significantly more influence in the system; to such extent it can be approximated as:
$$ \begin{align}
\frac{50(s+1)(s+2)}{s^{2} + 0.03 s+0.06}  
\end{align} $$
- Plotted this is just an oscillator with MASSIVE overshoot that will eventually settle ($\zeta=0.06$, $\omega_{n}=0.245$):
![[Pasted image 20240101115600.png]]
<!--ID: 1704396522492-->
END_CARD


--------

START_CARD
Basic

I'm adding the following block into my transfer function:

![[Pasted image 20240101115955.png]]

The system is stable, how does this influence the response as $T_{a}$ increases?

Back: 
$$ \begin{align}
\frac{1}{1+T_{a}s} &= \frac{1/T_{a}}{1/T_{a}+s}
\end{align} $$
- We can see this means that as $T_{a}$ increases it's added pole will have a decreasing real magnitude (with no imaginary contribution)
- This means with high $T_{a}$ the influence of this added pole will become more significant, drowning out the previous response
- As $T_{a}$ increases it's smaller real pole will then have a decreasing responsiveness assosiated with it, meaning the final system will become less and less responsive

![[Pasted image 20240101120413.png]]
<!--ID: 1704396522497-->
END_CARD



--------

START_CARD
Basic

State the 4 basic Laplace transforms

Back: 
![[Pasted image 20240110104950.png]]
![[Pasted image 20240110105029.png]]
<!--ID: 1704973040198-->
END_CARD






