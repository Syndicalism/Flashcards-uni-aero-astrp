TARGET_DECK: Aerothermodynamics::3



START_CARD
Basic

Draw a labelled sketch of wall wave reflection. Derive the relationships. How can we find $M_{W}$?

Back: 
![[Pasted image 20231218173017.png]]
- Since $R^{+}_{A}$ intercepts with the wall, the flow MUST be tangential to the wall (Else we'd have some fucked vacuum or mass deletion... so yeah), hence $\theta$ is the walls angle
- At point $W$ we can draw the downstream characteristic lines $R^{+}_{W}$ and $R^{-}_{W}$, of course the positive one doesn't exist as a wall is there
- Since both $R^{+}_{A}$ and $R^{-}_{W}$ intercept at $W$ we can relate the two using shared point properties $\theta$ and $\nu$
- Finding $M_{W}$ is trivial:
$$\begin{align*}
R^{-}_{A} &= \nu_{W} - \theta_{W} & &\to & R^{-}_{A} + \theta_{W} &= \nu_{W} \\\\
&&&&&& \nu^{-1}(\nu_W) &= M_{W}
\end{align*}$$
<!--ID: 1703587262862-->
END_CARD


--------

START_CARD
Basic

Why do Mach angles come up so much? What actually does it mean and how does that relate to characteristic lines?

Back: 
![[Pasted image 20231218165202.png]]
- Fundamentally Mach angle is defined as the angle of a Mach cone, what it therefor signifies is the boundary of "information" propagation in a supersonic flow
- This in fact goes both ways, if we consider some point P then the only points that can be influenced by the event's at P (aka: receive P's information) are in a cone bounded by the Mach cone. Also known as $\mu$. 
- Then we also know that P is under the same restriction, only points within a certain upstream "cone" of P can propagate information to it
- This lines up exactly with what characteristic lines follow
<!--ID: 1703587262875-->
END_CARD


--------

START_CARD
Basic

Why are characteristic lines actually a visible real phenomena?

Back: 
![[Pasted image 20231218165202.png]]
- Fundamentally characteristic lines are equivalent to the boundaries of sonic information flow in a supersonic fluid (hence their relationship with $\sin\mu = \frac{1}{M}$)
- Hence if some significant property change occurs inside a flow at some "point" in the flow such that there is a visible difference, then this visual effect will be bounded by the characteristic lines
- This results in the potential for real visible lines appearing due to the abrupt changes in flow properties
<!--ID: 1703587262886-->
END_CARD


--------

START_CARD
Basic

Under what conditions does wave cancellation occur?

Back:
![[Pasted image 20231218193001.png]]
- When there is no change in flow direction before and after the incident characteristic line ($\theta_{W}=\theta_{A}$), there is no need to draw a reflected characteristic line since there is no downstream change
- This is wave cancellation and it is useful for designing nozzles that have uniform output geometries
<!--ID: 1703587262896-->
END_CARD
 


--------

START_CARD
Basic

![[Pasted image 20231231165440.png]]
Proof that for a min length nozzle:

$$ \begin{align}
\theta_{max} &= \frac{\nu(M_{e})}{2}
\end{align} $$



Back: 

Taking characteristic lines:

$$ \begin{align}
&& && \theta &= 0\\
(3\to5):&& R^{+}_{3} &= \nu(M_{e}) + \theta &&\to& R^{+}_{3} &= \nu(M_{e}) = R_{3}^{-}
\end{align} $$

Using an expansion fan and the fact that $M_{init}=1$, it's clear that $\nu(M_{B})-\nu(M_{A})=\theta$ applied at the corner becomes $\nu_{0} = \theta_{max}$.

Using the characteristic lines we can finally get the relationship.

$$ \begin{align}
&& && \nu(M_{e}) &= R_{3}^{-} = R^{-}_{0}\\
&& && \nu_{0} &= \theta_{max}\\
 
(0\to3):&& R^{-}_{0} &= \nu_{0} + \theta_{max} &&\to& \nu(M_{e}) &=   \theta_{max} &&\to& \frac{\nu(M_{e})}{2}&=   \theta_{max} 
\end{align} $$


<!--ID: 1704035194765-->
END_CARD




