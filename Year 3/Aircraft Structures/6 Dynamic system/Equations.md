TARGET_DECK: Aircraft Structures::6 Dynamic system

---

START_CARD
Basic


State the equation of motion for damped free vibrations of a SDoF system. Then state the equations for:
- Critical damping the value
- Damping in non dimensional form, what the values mean
- The undamped natural frequency

Back: 
![[Pasted image 20240517151028.png]]
- critical damping the value
![[Pasted image 20240517151016.png]]
- damping in non dimensional form (damping ratio), when it's less than one their is oscillation (a complex component $\xi<1$) else there isn't ($\xi\geq1$)
$$ \begin{align}
\xi &= \frac{c}{c_{c}} =  \frac{c}{2\sqrt{mk}}
\end{align} $$
- Undamped nat freq
$$ \begin{align}
\omega_{0} &= \sqrt{ \text{Re}(\lambda)^{2} + \text{Im}(\lambda)^{2} }
\end{align} $$
<!--ID: 1716056916715-->
END_CARD


--------

START_CARD
Basic

What is the damped frequency equation if:
- damping ratio is between 0 and 1
- it's greater than 1
- it is 1

Back: 
- Subcritical Damping Ratio $\xi=0\to1$
![[Pasted image 20240517152855.png]]
- Supercritical Damping Ratio $\xi\geq1$:
$$ \begin{align}
\omega &= \infty
\end{align} $$

<!--ID: 1716056916724-->
END_CARD


--------

START_CARD
Basic

Describe the possible behaviour of a system depending on damping ratio.

Back: 
![[Pasted image 20240517153232.png]]

<!--ID: 1716056916729-->
END_CARD


--------

START_CARD
Basic

Write the roots of a 1 degree of freedom system interms of it's damping ratio and natural frequency. Additionally sketch a labelled root loci.

Back: 
![[Pasted image 20240518152810.png]]
![[Pasted image 20240518153012.png]]
<!--ID: 1716056916736-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20240518153816.png]]

Back: 
![[Pasted image 20240518153834.png]]
<!--ID: 1716056916743-->
END_CARD


--------

START_CARD
Basic

State the equations for "dynamic amplification factor" and "phase shift".

Back: 
![[Pasted image 20240518154031.png]]
- These equations describe how the system responds under the effects of the forcing function $F_{0}$.
![[Pasted image 20240518154015.png]]
![[Pasted image 20240518154005.png]]
<!--ID: 1716056916749-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20240518155727.png]]

Back: 
![[Pasted image 20240518155739.png]]
<!--ID: 1716056916754-->
END_CARD



--------

START_CARD
Basic

State the first and second natural frequencies of bending vibration for the following characteristic equation:

$$ \begin{align}
0 &= a \lambda^{4} + b \lambda^{2} + c 
\end{align} $$

Back: 
$$ \begin{align}
\lambda^{2}_{1} &= \frac{-b + \sqrt{b^{2} - 4ac}}{2a} = - \omega^{2}_{1} &&\to& \omega_{1}&=\sqrt{\frac{b - \sqrt{b^{2} - 4ac}}{2a}} \\

\lambda^{2}_{2} &= \frac{-b - \sqrt{b^{2} - 4ac}}{2a} = - \omega^{2}_{2} &&\to& \omega_{2}&=\sqrt{\frac{b + \sqrt{b^{2} - 4ac}}{2a}} 

\end{align} $$

$$ \begin{align}
\therefore \:& \omega_{1} \leq \omega_{2} 
\end{align} $$
<!--ID: 1716056916760-->
END_CARD




--------

START_CARD
Basic

State the equation for divergence dynamic pressure

Back: 
![[Pasted image 20240518190900.png]]
<!--ID: 1716056916766-->
END_CARD






