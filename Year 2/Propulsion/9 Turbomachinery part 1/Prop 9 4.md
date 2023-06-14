TARGET_DECK: Propulsion::9 Turbomachinery part 1




START_CARD
Basic

Using the equation of stagnation enthalpy describe gas property changes through the compressor stator and compressor rotor.

Back: 
$$ \begin{align}
&&&&&& V_{r} &\approx 0 \\
&&&&&& \Delta V_{x} &\approx 0 \\
h_{0} &= h + \frac{1}{2} V^{2} & &\to &  h_{0} &= h + \frac{1}{2} (V_{\theta}^{2} + V_{r}^{2} + V_{x}^{2})& &\to &  \Delta h_{0} &= \Delta h + \frac{1}{2} (\Delta V_{\theta} )^{2}
\end{align} $$

We know according to SFEE ($Q-W_{out} = \Delta H_{0}$) that:
- Work is done on the gas in the rotor hence:
	- Stagnation enthalpy must increase
	- Swirl velocity increases
	- With enough work static enthalpy may also increase
- No work is done in the stator, but swirl is reduced hence:
	- Stagnation enthalpy must be constant (no work/heat transfer)
	- Swirl decreases
	- To balance it out static enthalpy must increase

- We can see that the net effect is that across a compressor stage
	- Swirl remains constant(ish)
	- Static enthalpy increases (so pressure/density/temp will also probably increase)

![[Pasted image 20230527155445.png]]
<!--ID: 1685200388314-->
END_CARD


--------

START_CARD
Basic

Do a rough sketch of a graph of velocity and pressure across many compressor stages in a axial compressor.

Back: 

![[Pasted image 20230527155519.png]]
<!--ID: 1685200388328-->
END_CARD


--------

START_CARD
Basic

Why do we use alternating rotors and stators, why not just use rotors?

Back: 
- Because it would be impractical to just use rotors
- Just using rotors would result in large amounts of energy becoming swirl
- Mechanically it would require each rotor stage to be rotating faster consecutively (stupid)
- Basically it makes no sense at all 
<!--ID: 1685200388340-->
END_CARD


--------

START_CARD
Basic

What is the rough ratio of compressor stages to turbine stages? Why?

Back: 
- Generally for every turbine stage you can have ~6 compressor stages.
- A turbine stage can have a significantly higher pressure ratio across it than a compressor stage
- So a turbine stage can extract much more energy than a single compressor stage can impart
- Hence you can power multiple compressor stages off less turbine stages
- No reason to have excess turbine stages so you want as few as possible for as many compressor stages (duh)
<!--ID: 1685200388353-->
END_CARD



--------

START_CARD
Basic

For a turbine blade, what is the:
- Span
- Tip
- Root
- Chord
- Axial chord
- Pitch
- Hub

Give symbols where appropriate.

Back: 
- Span ($h$), this is the length of a blade from hub connection to tip
- Tip, this is the end of the blade
- Root, this is where the blade connects into the hub
- Chord ($c$), this is the length from the leading edge to the trailing edge
- Axial chord ($c_{x}$), this is the component of the chord in the axial direction
- Pitch ($s$), this is the separation between the blades in the circumferential direction
- Hub, this is where the roots connect into the shaft


![[Pasted image 20230527160715.png]]
![[Pasted image 20230527160752.png]]
<!--ID: 1685200388366-->
END_CARD



--------

START_CARD
Basic

What is meridional velocity?

Back: 
- The component of velocity along the centre stream tube
<!--ID: 1685355931783-->
END_CARD






