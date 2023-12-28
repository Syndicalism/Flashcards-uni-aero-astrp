TARGET_DECK: Aerothermodynamics::2



START_CARD
Basic

Sketch in detail what occurs in an over-expanded exhaust. Where a Mach disk is included.

Back: 
- In an over expanded exhaust the exit flow is below ambient pressure
![[Pasted image 20231218142715.png]]

<!--ID: 1703587226457-->
END_CARD


--------

START_CARD
Basic

Sketch and explain in detail what occurs in an over-expanded exhaust. Where a Mach disk is included.

Back: 
![[Pasted image 20231218142715.png]]
- (Compression) In the first section, the exit pressure is sub atmospheric by definition of an [[over and under  expanded nozzles]]. Hence for pressure equalisation a compressive shock must occur, this takes the form of:
	- [[oblique shocks|Oblique shocks]] - This shock forms such that the resulting pressure is equal to the atmospheric pressure across the [[Mach reflection|slip line]], it should be noted that the flow will still be supersonic across this shock. This then proceeds into another [[oblique shocks|oblique shock]] further increasing the pressure.
	- [[normal shock properties equations|A normal shock]] - The streamlines through the "Mach disk" suggest that the angle allows for [[oblique shocks|oblique shock]] formation (it's in the bounds of the [[oblique shock chart]]), which means the normal shock formation is caused due to pressure. To reach a pressure as high as the double oblique shocks in the surrounding streamlines a normal shock is required. This also means the flow directly after the [[over and under  expanded nozzles|Mach disk]] is subsonic.
- (Acceleration) What occurs next is really fucky, look at the streamlines. They actually form a [[converging diverging nozzles|converging diverging nozzle]], this causes the flow in the centre to potential reach the supersonic domain again. So once the flow starts expanding again it's supersonic but now higher than ambient pressure. 
- (Expansion -> Compression) Now the flow continues to expand, so expansion mechanisms take place, specifically [[Prandtl–Meyer expansion fan|expansion fans]]. The fans form such that the [[Mach reflection|slip line]] (free jet boundary) matches atmospheric pressure. This essentially creates a diverging nozzle, accelerating the flow. 
	- The now over expanded state causes the flow to recompress and converge, so the reflected [[compression fans]] coalesce into a [[oblique shocks|oblique shock]].
	- The process repeats.
<!--ID: 1703587226466-->
END_CARD


--------

START_CARD
Basic

Sketch and explain in detail what occurs in an over-expanded exhaust. Where a Mach disk is excluded.


Back: 
![[Pasted image 20231218143408.png]]
<!--ID: 1703587226482-->
END_CARD



--------

START_CARD
Basic

Sketch and explain in detail what occurs in an under-expanded exhaust. Where a Mach disk is included.

Back: 
![[Pasted image 20231218144229.png]]
- (Expansion -> Compression) The flow expands, so expansion mechanisms take place, specifically [[Prandtl–Meyer expansion fan|expansion fans]]. The fans form such that the [[Mach reflection|slip line]] (free jet boundary) matches atmospheric pressure. This essentially creates a diverging nozzle, accelerating the flow.
	- The now over expanded state causes the flow to recompress and converge, so the reflected [[compression fans]] coalesce into a [[oblique shocks|oblique shock]], 
- (Compression) the pressure is sub atmospheric by definition of an [[over and under  expanded nozzles]]. Hence for pressure equalisation a compressive shock must occur, this takes the form of:
	- [[oblique shocks|Oblique shocks]] - This shock forms such that the resulting pressure is equal to the atmospheric pressure across the [[Mach reflection|slip line]], it should be noted that the flow will still be supersonic across this shock. This then proceeds into another [[oblique shocks|oblique shock]] further increasing the pressure.
	- [[normal shock properties equations|A normal shock]] - The streamlines through the "Mach disk" suggest that the angle allows for [[oblique shocks|oblique shock]] formation (it's in the bounds of the [[oblique shock chart]]), which means the normal shock formation is caused due to pressure. To reach a pressure as high as the double oblique shocks in the surrounding streamlines a normal shock is required. This also means the flow directly after the [[over and under  expanded nozzles|Mach disk]] is subsonic.
- (Acceleration) What occurs next is really fucky, look at the streamlines. They actually form a [[converging diverging nozzles|converging diverging nozzle]], this causes the flow in the centre to potential reach the supersonic domain again. So once the flow starts expanding again it's supersonic but now higher than ambient pressure. 
	- Back where we started, the process repeats
<!--ID: 1703587226492-->
END_CARD


--------

START_CARD
Basic

Sketch an idealised wind tunnel, labelling key features.

Back: 
![[Pasted image 20231218144535.png]]
- $A_{t2}<A_{t1}$
- One is ensuring the normal shock occurs in the correct location, the only location in an empty wind tunnel that should have a normal shock is where we want supersonic flow to transition to subsonic.
- So we want the normal shock to occur in the second throat.
<!--ID: 1703587226500-->
END_CARD


--------

START_CARD
Basic

Why is the second throat area designed the way it is in a supersonic wind tunnel?

Back: 
![[Pasted image 20231218145348.png]]
$$ \dot{m}  = p_{0}  A^{*} \sqrt{\frac{\gamma}{RT_{0}}} \left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}} $$
- The second throat in a wind tunnel is larger than the first
- Looking at the mass flow equation it becomes clear why that is, there will be a loss of stagnation pressure due to interference of the model/natural entropy increasing things
- The stagnation temp wont change (no energy gain/loss in the system)
- So if the throat area is unchanged mass flow wouldn't be sufficient, which would prevent supersonic flow in the first throat as the second has too high back pressure
- So the second throat must be larger
<!--ID: 1703587226512-->
END_CARD
 


--------

START_CARD
Basic

Sketch a Ludwig tube, explain how it operates and use that to discuss advantages and disadvantages.

Back: 
![[Pasted image 20231218145710.png]]
- This is a type of supersonic wind tunnel. It's operation is relatively "simple" but a disadvantage is it can only operate for about 100ms. The operation is as follows:
- A storage tube contains ultra high pressure gas, heating elements are used to ensure that as it expands the temperature can be maintained
- A diaphragm or high speed valve is used to release the gas, the test area is initially at low pressure or near vacuum
- The enters the Laval nozzle above Mach 1, it accelerates rapidly and enters the test section
- The flow front moves into the dump tank, it rapidly reaches the end creating all sorts of supersonic shockwaves which start propagating back up stream
- Once these shockwaves reach the test section, data collection ends hence the limited run time
<!--ID: 1703587226525-->
END_CARD



--------

START_CARD
Basic

Briefly describe the two methods for wind tunnel flow visualisations we need to know.

Back: 
![[Pasted image 20231218145950.png]]
(Image of [[wind tunnel flow visualisation|Schlieren]])
- Shadowgraph - Here a parallel beam is shone through a test section directly onto a screen or camera, this results in an image representing the gradient of the density gradient (a double [[differentiation|derivative]]). 
- Schlieren - Similar to a shadowgraph, but a convex lens focuses the light onto a "knife cut off" which effects the light such that the projected image represents a density gradient (single derivative)
- From density gradient, we can quite easily estimate relative flow velocities (for supersonic, if the density decreases then velocity increases and vice versa)
- Generally we prefer the [[wind tunnel flow visualisation|Schlieren]] method as the data is simpler to manage.
<!--ID: 1703587226534-->
END_CARD







