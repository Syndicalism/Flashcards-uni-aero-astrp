TARGET_DECK: Aerothermodynamics::2



START_CARD
Basic

Sketch what happens in, assuming a large $M_{1}$, provide sufficient labels:

![[Pasted image 20231218131808.png]]

Back: 
![[Pasted image 20231218131838.png]]

END_CARD


--------

START_CARD
Basic

| $M_{1}=2$ | $P_{1}=30\:kN/m^{2}$ | $c=1\:m$ |   $\alpha=10\degree$  | 
| --------- | -------------------- | -------- | --- |
For the following, how would you go about calculating lift and drag, give only a high level analysis. State the order key values are found.
![[Pasted image 20231218131932.png]]

Back: 
- For lift and drag the $M_{3}$ values aren't needed
- Initial stagnation pressure $P_{01}$ can be found from pressure and isentropic flow tables
- Top surface
	- $M_{2U}$ is found after using Prandtl-Meyer relations, making use of $\alpha=\theta_{1U}$
	- Expansion fans are isentropic, isentropic flow tables can simply be used to find $P_2$ since $P_{0}$ is unchanged
- Bottom
	- $M_{2L}$ is found from $\alpha=\theta_{1L}$ using oblique shock methods
	- Entropy increases across oblique shocks, so pressure loss makes use of normal shock tables
- The net force can be found by summing pressures (constant along plate) against area (length)
- Net force is broken into lift and drag by basic trig ($L = F\sin\alpha$ and $D = F\cos\alpha$)

END_CARD


--------

START_CARD
Basic

A supersonic flow travels over a angled flat plate, where is the centre of pressure and aerodynamic centre? Why?

Back: 
![[Pasted image 20231218131932.png]]
- The centre of pressure's pretty easy to figure out intuitively, it will be at $c=0.5$ since the pressure is constant on the upper and lower surfaces.
- The [[aerodynamic centre]] is equally trivial, since the [[centre of pressure]] is constant we know the [[aerodynamic centre]] must be located at the same spot ($c=0.5$).
- This is quite different to what we generally see in normal aerofoils

END_CARD


--------

START_CARD
Basic

Why is there drag, even though we have the inviscid assumption, for supersonic flows?

Back: 
- In supersonic flows, even with the inviscid assumption, drag is present due to the generation of shock waves. These shock waves lead to changes in pressure, density, and temperature, causing an increase in drag.
- The shocks involved generally produce entropy even in the case of the inviscid assumption, leading to the generation of useful energy losses and hence drag

END_CARD




