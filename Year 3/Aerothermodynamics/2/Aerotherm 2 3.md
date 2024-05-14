TARGET_DECK: Aerothermodynamics::2



START_CARD
Basic

Assuming a supersonic flow from the left $M_{1}$, predict what shocks occur and label key angles and flow velocity vectors. Discuss the values of the angles involved and where they come from.

![[Pasted image 20231218110525.png]]

Back: 
It can be seen that the streamlines for $M_{2}$ will collide with the top surface now that they are inclined, this will result in a secondary [[oblique shocks|oblique shock]]:
- The first oblique shock has [[oblique shock angles|a turning angle]] of $\theta$, by definition the flow $M_{2}$ will follow this angle. Then upon hitting a "flat" surface it will have a [[oblique shock angles|turning angle]] of $\theta$. Hence both have the same turning angle.
- Although the turning angle is the same the [[oblique shock angles|shock angle]] is not the same, since that is a function of Mach number and $M_{1}\neq M_{2}$
![[Pasted image 20231218110626.png]]

<!--ID: 1703587167985-->
END_CARD


--------

START_CARD
Basic

How would you find $M_{3}$, discuss/state the steps involved assuming $M_{1}$ and $\theta$ are known. (For practice $M_{1} = 3.6$ and $\theta=10\degree$)
![[Pasted image 20231218110904.png]]

Back: 
- Use oblique shock chart (or equivalent) to find $\beta_{1}$ (shock angle) from turning angle $\theta=\theta_{1}$ and incident Mach number.
- Finding $M_{2}$ requires using the shortcut equation (if known/available) or the normalisation method
	- Find normal component of $M_{1}$ to first shock $M_{n1} = M_{1} \sin \beta_{1}$
	- Look that $M_{n1}$ up in normal shock table to get $M_{n2}$
	- Convert to get $M_{2}$ $M_{2} = \frac{M_{n2}}{\sin(\beta_{1}-\theta_{1})}$
- When the flow hits the top surface it deflects with a turning angle $\theta=\theta_{2}$, repeat previous method to get $M_{3}$ note that $\beta_{1}\neq \beta_{2}$ since incident Mach number is different!
- Final answer $M_{3}=2.49$
<!--ID: 1703587167995-->
END_CARD


--------

START_CARD
Basic

An oblique shock hit's a wall and is reflected, sketch how this looks with the inclusion of viscosity

Back: 
![[Pasted image 20231218114537.png]]
<!--ID: 1703587168009-->
END_CARD


--------

START_CARD
Basic

What causes the formation of the separation bubble?

![[Pasted image 20231218114627.png]]

Back: 
- Across the shock $P_{2}>>P_{1}$, with this being more severe the stronger the shock, which is obviously an adverse pressure gradient
- In most regions the "information" about this pressure gradient can't back propagate as is the nature of supersonic flows
- Near the wall we have a unbroken region of subsonic flow, where information can easily back propagate
- The strong pressure gradient lead's to lots of backflow near the wall, creating separation bubbles and shearing the boundary layer
<!--ID: 1703587168021-->
END_CARD



--------

START_CARD
Basic

Why is there an expansion fan? Why does the flow relax?

![[Pasted image 20231218114627.png]]

Back: 
- The shear layer can be thought of as a compressive boundary (like a converging-diverging nozzle)
- Since there is expansion there is an expansion fan and expansion wavesw
- The flow expands after the peak, which causes the flow to accelerate and decrease in pressure
- The expansion allows for a reduction in the adversity of the pressure gradient leading to relaxation
<!--ID: 1703587168031-->
END_CARD


--------

START_CARD
Basic

Here the turning angle needed $\theta$ is greater than the maximum possible turning angle for this $M_{1}$ ($\theta>\theta_{max}$) for forming an oblique shock. What happens, describe key features.

![[Pasted image 20231218115449.png]]

Back: 
![[Pasted image 20231218115704.png]]
Something to note is the $\theta$ condition to create a [[Mach reflection]] is identical to a [[detached shock]], further the behaviour is quite similar. The primary difference is that instead of the [[normal shock properties equations|normal shock]] region being a single point, like was the case with [[detached shock]]s, a [[Mach reflection]] has a tangible length where it is normal. This region occurs between the slip line and wall.

The slip line has some strange properties:
- Across it the pressure is continuous
- The velocities, temperature and density can be discontinuous

Also note that the intersection point, where all these phenomena intersect is T on the diagram and known as the [[Mach reflection|triple point]]. Note also that since across the Mach stem there is subsonic flow, information can back propagate so downstream conditions can effect it's shape and position.
<!--ID: 1703587168043-->
END_CARD



--------

START_CARD
Basic

Complete the sketch and comment on what's going on, stop at the point of reflection:

![[Pasted image 20231218120144.png]]

Back: 

![[Pasted image 20231218120158.png]]
- The two shocks intercepted and create subsequent shocks such that thy have tangential output flows at their intercept point (along a slip line)
	- On a slip line pressure is continuous, but velocity and temperature can vary discontinuously (in this idealised model)
- This sketch does not consider Mach reflection on the wall
<!--ID: 1703587168053-->
END_CARD



--------

START_CARD
Basic

How would you solve for $M_{3B}$ and $M_{3A}$?

![[Pasted image 20231218120641.png]]

Back: 
- The two shocks intercepted and create subsequent shocks such that thy have tangential output flows at their intercept point (along a slip line)
	- On a slip line pressure is continuous, but velocity and temperature can vary discontinuously (in this idealised model)
	- The velocities across a slip line are parallel (but not continuous)
	- The pressure across a slip line is continuous
- Assume some value of $\Delta$
- For the flows to be parallel the following condition must be met: $\theta_{2A} = \theta_{A} - \Delta \text{ and } \theta_{2B} = \theta_{B} + \Delta$
- Then find $M_{3B}$ and $M_{3A}$
- Then find $P_{3B}$ and $P_{3A}$
- Using the error between the pressures iterate on the value of $\Delta$
- Do this until the pressure difference is sufficiently small
<!--ID: 1703587168064-->
END_CARD





