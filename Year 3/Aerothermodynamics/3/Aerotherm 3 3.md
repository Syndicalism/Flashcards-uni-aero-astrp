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

END_CARD


--------

START_CARD
Basic

Under what conditions does wave cancellation occur?

Back:
![[Pasted image 20231218193001.png]]
- When there is no change in flow direction before and after the incident characteristic line ($\theta_{W}=\theta_{A}$), there is no need to draw a reflected characteristic line since there is no downstream change
- This is wave cancellation and it is useful for designing nozzles that have uniform output geometries

END_CARD
 



