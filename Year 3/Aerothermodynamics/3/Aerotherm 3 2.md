TARGET_DECK: Aerothermodynamics::3



START_CARD
Basic

For some [[irrotational, homentropic, supersonic flow]] how can we calculate the properties downstream through the method of characteristics?

Back: 
![[Pasted image 20231218165202.png]]
1) Get the [[method of characteristics|Riemann invariants]] ($\text{Along line C}^{+}:\:\: \text{ R}^{+}  = \nu-\theta =\text{constant}$, and $\text{Along line C}^{-}:\:\: \text{ R}^{-} = \nu+\theta =\text{constant}$)
2) Find where 2 [[Mach lines and domains of influence|characteristic lines]] intercept, then solve to get that points $\nu$ and $\theta$ (since the exit Mach and $\theta$ must be the same)
3) Use the calculated $\nu$ to determine Mach number and any other gas properties
4) Find the new $\mu$ (Mach number changed, use [[Mach cone|Mach triangle]])
5) Use geometric properties to determine location of point
<!--ID: 1703587253200-->
END_CARD


--------

START_CARD
Basic

What is the fundamental principle behind the method of characteristics? State the equation.

Back: 
![[Pasted image 20231218165243.png]]
$$\begin{align*}  \text{Along line C}^{+}:\:\: \text{ R}^{+} &= \nu-\theta =\text{constant}&&&\text{Along line C}^{-}:\:\: \text{ R}^{-} &= \nu+\theta =\text{constant}   \end{align*}$$
- We know that along characteristic lines (lines that lie along angle $\mu$ to the stream line $\theta$) the remain invariants are constant
- Then information about downstream conditions can be found by considering the consequences of this fact
<!--ID: 1703587253213-->
END_CARD


--------

START_CARD
Basic

What determines if a characteristic line is positive or negative?

Back: 
![[Pasted image 20231218170024.png]]
- Depends on if the absolute angle of the line $\alpha$ is given by a positive or negative offset from the stream $\theta$
	- $R^{+}:$ $\alpha^{+}=\theta+\mu$
	- $R^{+}:$ $\alpha^{-}=\theta-\mu$
- Where $\mu$ is the Mach angle $\sin\mu = \frac{1}{M}$
<!--ID: 1703587253223-->
END_CARD


--------

START_CARD
Basic

State the positive and negative characteristic line relations.

Back: 
$$\begin{align*}  \text{Along line C}^{+}:\:\: \text{ R}^{+} &= \nu-\theta =\text{constant}&&&\text{Along line C}^{-}:\:\: \text{ R}^{-} &= \nu+\theta =\text{constant}   \end{align*}$$
<!--ID: 1703587253234-->
END_CARD




--------

START_CARD
Basic

You are given 2 point's A and B, the values at these point's are known. Where do the characteristic lines from these points meet? Derive an expression. Comment on it's range of applicability.

Back: 
![[Pasted image 20231218165728.png]]
- It's not so trivial, first we need to know the Mach number at the point of interception! Using the characteristic line properties:
$$\begin{align*}
\text{ R}^{+}_{A} &= \nu(M_{A})-\theta_{A} &&& \text{ R}^{-}_{B} &= \nu(M_{B})+\theta_{B} \\
   && &\downarrow \text{At P}\\
\text{ R}^{+}_{A} &= \nu(M_{P})-\theta_{P} &&& \text{ R}^{-}_{B} &= \nu(M_{P})+\theta_{P} \\
   && &\downarrow \text{Solve}\\
 \nu(M_{P}) &=  \frac{\text{R}^{-}_{B}+\text{R}^{+}_{A}}{2} &&&\theta_{P} &=\frac{\text{R}^{-}_{B}-\text{R}^{+}_{A}}{2} \\
\end{align*}$$
- From $\nu$ we can find $M_{P}$
- In reality the characteristic lines aren't straight. To account for this a more accurate $\alpha$ can be found by averaging the $\alpha$ at the intercept point and their previous point
$$\begin{align*}
\alpha_{AP} &= \frac{(\theta+\mu)_{A} + (\theta+\mu)_{P}}{2}  & \alpha_{BP} &= \frac{(\theta-\mu)_{B} + (\theta-\mu)_{P}}{2}
\end{align*}$$
- Then using that we simply draw two straight lines from their respective origins:
$$ \begin{align}
\text{Line B: }y &= \tan\alpha_{BP} (x - x_{B}) +y_{B} &&& \text{Line A: }y &= \tan\alpha_{AP} (x - x_{A}) +y_{A}
\end{align} $$
- These are simple equations, the interception point can be easily found
<!--ID: 1703587253245-->
END_CARD


--------

START_CARD
Basic

Comment on this diagrams accuracy:

![[Pasted image 20231218171919.png]]

Back: 
This sucks, in reality at each characteristic line interception, they should bend slightly to reflect the change in Mach number
![[Pasted image 20231218172411.png]]
Secondly, these both represent a discretised version of the expansion. In reality Mach number changes continuously as it expands so straight lines will always just be an approximation (of course more lines means less error as a more accurate discretisation is captured.)
<!--ID: 1703587253256-->
END_CARD




