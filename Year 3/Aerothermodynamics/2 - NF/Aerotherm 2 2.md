TARGET_DECK: Aerothermodynamics::2 - NF



START_CARD
Basic

What is the idealised reasoning for using oblique shocks inside of intakes?

Back: 
- Efficiency gains
- For an oblique shock the larger the change in Mach number, the larger the stagnation pressure loss. 
- This effect follows a non-linear exponential-ish curve, in an idealised system we can increase efficiency by using many smaller oblique shocks rather than single large ones. 
- EXTRA (Of course in non-idealised systems such as those in real life, other trade offs would also take consideration leading to some optimal shock configuration rather than just adding more forever)

![[Pasted image 20231025102011.png]]

END_CARD


--------

START_CARD
Basic

Under what conditions do detached shocks occur?

Back: 
- Looking at the oblique shock chart, you can see that $\theta>\theta_{max}$ has no valid solutions. But obviously something must exist there, the shock phenomena that occurs in this range is known as a detached shock.

END_CARD


--------

START_CARD
Basic

Describe the general shape of a detached shock and a brief outline of it's exit Mach numbers and shock angle.

Back: 
![[Pasted image 20231117004619.png]]

- As the name describes, they are often detached
- In the centre is a infinitesimally small normal shock, here crossing flow is subsonic
- Around the normal shock it is a gradual increasing shock angle, it slowly transitions out from subsonic back into supersonic as you leave the centre
- The crossing Mach number approaches the value in the free stream as the shock angle increases leaving the centre

END_CARD


--------

START_CARD
Basic

How do you calculate the angle and Mach number ($M_{2}$) at the middle of a detached shock?

Back: 
- Centre is an normal shock, hence $\beta=0$ and $\theta=0$
- Mach number can be calculated using normal shock table or relevant normal shock equation

END_CARD


--------

START_CARD
Basic

State where each of the labelled locations lie on a oblique shock chart. Stating properties of the points that are distict.

![[Pasted image 20231117005040.png]]

Back: 
- This is a detached shock

![[Pasted image 20231117005059.png]]
- $a=$ flow inline with the tip, it is where the angle is $90\degree$ and is equivalent to a [[normal shock properties equations|normal shock]] 
- $b=$ occurs between $a$ and $c$, here you'll find the maximum [[oblique shock angles|turning angle]] if comparing to a [[oblique shocks|oblique shock table]]
- $c=$ this is the point on the surface where $M_{2}=1$, beyond which flow past the detached shock will be supersonic
- $d=$ around here are [[oblique shock chart|weak solutions]]
- $e=$ here a Mach wave occurs as you get really far from the object

END_CARD


--------

START_CARD
Basic

How do points along a detached shock relate to oblique shocks.

Back: 
- What makes these nasty is unlike normal shocks or oblique shocks which have single angles they operate at, detached shocks form a curved surface meaning different turning angles ($\beta$) across the entire surface leading to very complex behaviour ($M_{2}$ varies across the whole surface).
- Effectively, we can treat any point on the detached shock as an instantaneous oblique shock, given $\beta$ at that point: oblique shock methods can find $M_{2}$ and $\theta$

END_CARD






