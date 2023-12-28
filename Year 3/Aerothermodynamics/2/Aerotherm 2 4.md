TARGET_DECK: Aerothermodynamics::2



START_CARD
Basic

Sketch what happens to a tangential supersonic flow around a diverging corner. Labelling key values and stating what they are.

Back: 
![[Pasted image 20231218121249.png]]


- $\mu_{1}=$ angle of the first Mach line
- $\mu_{2}=$  angle of the last Mach line
- $\theta=$  turning angle (just like [[oblique shock angles|turning angle]] for [[oblique shocks]])
- Since this is supersonic expansion $M_{2}>M_{1}$

<!--ID: 1703587193611-->
END_CARD


--------

START_CARD
Basic

State the equations of $\mu_{1}$, $\mu_{2}$ and $M_{2}$ as well as the name of the phenomena.

![[Pasted image 20231218121526.png]]

Back: 
![[Pasted image 20231218121633.png]]
<!--ID: 1703587193622-->
END_CARD


--------

START_CARD
Basic

State what the values in this equation are and what the equation means, then describe it's practical use.

$$\begin{align*} \nu(M) &= \sqrt{ \frac{\gamma+1}{\gamma-1} } arctan\sqrt{ \frac{\gamma-1}{\gamma+1} (M^{2} - 1) } - \arctan\sqrt{M^{2} - 1}   \end{align*}$$

Back: 
- $\nu(M)=$ the angle divergence (in radians) required to accelerate a flow from Mach 1 to target Mach $M$
- $M=$ output Mach number after the expansion fan
- Since this equation on it's own only works for a $M_{init}=1$, we use it along side $\theta = \nu(M_{2}) - \nu(M_{1})$
- Here $M_{1}$ is any initial supersonic flow
<!--ID: 1703587193630-->
END_CARD


--------

START_CARD
Basic
What would happen if $M_{1}<1$
![[Pasted image 20231218121526.png]]

Back: 
- Then input flow is subsonic
- Subsonic flows decelerate as they expand
- $M_{2}<M_{1}$ and the expansion phenomena would be different
<!--ID: 1703587193639-->
END_CARD


--------

START_CARD
Basic

How can the size of the expansion fan ($\Delta \mu$) be found, given only $M_{1}$ and $\theta$?

![[Pasted image 20231218121526.png]]

Back: 
- The output flow must be tangential to the wall so our turning angle's clearly $\theta$ 
- We can find the streamline angle change with the Prandtl-Meyer function
- Then using $\theta = \nu(M_{2}) - \nu(M_{1})$ we rearrange into $\theta + \nu(M_{1}) = \nu_{2}$ using the normal shock table (or the equation) to get $\nu_{1}$
- To evaluate $\nu^{-1}(\nu_{2})=M_{2}$ we make use of the normal shock table to find the $M_{2}$ for the closest $\nu_{2}$ value
- The $\mu$ values are found from the Mach triangle relation $\sin \mu = \frac{1}{ M}$
- The difference can then be easily evaluated
<!--ID: 1703587193647-->
END_CARD


--------

START_CARD
Basic

State the equation relating $M_{1}$ and $M_{2}$ in an expansion fan. Naming the terms.

Back: 
$$ \begin{align}
\theta = \nu(M_{2}) - \nu(M_{1})
\end{align} $$

-  $\nu=$ [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]] (the angle divergence (in radians) required to accelerate a flow from Mach 1 to some target Mach)
-  $M_{1}=$ the initial Mach number
-  $M_{2}=$ the final Mach number
-  $\theta=$ the angle divergence required to expand the flow from $M_{1}\to M_{2}$
<!--ID: 1703587193657-->
END_CARD



--------

START_CARD
Basic



Back: 
- 

END_CARD






