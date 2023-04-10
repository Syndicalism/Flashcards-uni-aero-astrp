TARGET_DECK: Propulsion::3 Gas dynamics



START_CARD
Basic

Give a brief outline of how this equation is derived: $\frac{1}{A} \frac{dA}{dx} = \frac{1}{U} \frac{dU}{dx} (Ma^{2} - 1)$


Back: 
- This equation is derived by modelling mass flow through a nozzle of variable area and assuming isentropic flow it assumes the following:
- Steady flow
- Inviscid flow (also follows that there is no viscous heating)
- No thermal diffusion
- Ideal gas
- Additionally we know that mass is conserved in the flow hence $\rho UA=\dot{m}=\text{constant}$ hence $\frac{d}{dx}(\rho UA) = 0$ and by expanding out $\frac{d\rho}{dx} \frac{1}{\rho} + \frac{dU}{dx} \frac{1}{U} + \frac{dA}{dx} \frac{1}{A}  = 0$
- Then by combining this with equations relating to momentum and energy conservation for compressible flow along side the equation for speed of sound ($a^{2}= \frac{dP}{d\rho}$) you can get that equation
<!--ID: 1680694728150-->
END_CARD


--------

START_CARD
Basic


For the following equation: $\frac{1}{A} \frac{dA}{dx} = \frac{1}{U} \frac{dU}{dx} (Ma^{2} - 1)$
- Name it's variables
- Describe it's meaning specifically how velocity and area couple to effect changes
- State limitiations and applicability


Back: 
- This is the equation for isentropic gas flow though a variable diameter nozzle.
- $A$ is the local cross section, $x$ is displacement along the nozzle, $U$ is local velocity, $Ma$ is local mach number of the flow
- What it shows is that for a compressible flow moving through a variable diameter nozzle not only does area matter when determining velocity changes but the rate of area change, the local speed of sound and the fluids velocity matter
- In an ideal gas it should be noted that speed of sound is a function of temperature only
- This equation also predicts radically different behaviour between sub and supersonic flow
- In subsonic flow $(Ma^{2} - 1)$ is negative which predicts that for subsonic flow $\frac{dA}{dx}$ and $\frac{dU}{dx}$ have negative correlation, hence a narrowing will increase flow rate and vice versa
- But in supersonic flow $(Ma^{2} - 1)$ is positive which predicts that for supersonic flow $\frac{dA}{dx}$ and $\frac{dU}{dx}$ have positive correlation, hence a widening will increase flow rate!
- This equation is based on theory that assumes:
- Steady flow
- Inviscid flow (also follows that there is no viscous heating)
- No thermal diffusion
- Ideal gas
- Isentropic flow
- Small changes in diameter such that changes are gradual
<!--ID: 1680694728163-->
END_CARD



--------

START_CARD
Basic


What does this equation tell us about what fluid velocity change is achieveable with a converging nozzle? 
$$\frac{1}{A} \frac{dA}{dx} = \frac{1}{U} \frac{dU}{dx} (Ma^{2} - 1)$$

Back: 
- It shows us that for a converging nozzle ($\frac{dA}{dx}<1$) in the subsonic regime, gas can only be accelerated to mach 1. Here gas will alwayse be accelerated.
- Also that for the supersonic regime, the lowest velocity that can be achieved will be mach 1. Here gas will alwayse be deccelerated.
<!--ID: 1680694728177-->
END_CARD



--------

START_CARD
Basic


What does this equation tell us about what fluid velocity change is achieveable with a diverging nozzle? $\frac{1}{A} \frac{dA}{dx} = \frac{1}{U} \frac{dU}{dx} (Ma^{2} - 1)$ 


Back: 
- It shows us that for a diverging nozzle ($\frac{dA}{dx}>1$) in the subsonic regime, gas can be deccelerated to zero and only deccelerated.
- Also that for the supersonic regime, the gas can be accelerated infinitely but only accelerated.
- Of course in reality the amount the gas can be accelerated does have limits, you can't get gas past the speed of light using a big enough nozzle. (sadly)
<!--ID: 1680694728192-->
END_CARD


--------

START_CARD
Basic

For a converging-diverging nozzle, why does choked flow occur and why does mach 1 have to occur at the throat?
![[Pasted image 20230402145155.png]]

Back: 
- If the conditions of the nozzle are such that the flow can reach mach 1 at or before the throat then the flow will be choked AT the throat (where it is at mach 1)
- This is because a subsonic flow will accelerate in a converging nozzle
- When it exceeds mach 1 it will become a supersonic flow, hence it will deccelerate in a converging nozzle... making it subsonic
- It can be seen that regardless of ability to reach supersonic flow before the throat it will be stuck at mach 1 for the duration of the converging region.
<!--ID: 1680694728204-->
END_CARD



--------

START_CARD
Basic

For a converging-diverging nozzle operating correctly, where in the nozzle does the normal shock form?


Back: 
- If the nozzle is operating correctly there will be no normal shocks inside the nozzle
- In correct operation, although supersonic flow exists the conditions are such that no shocks will form and the flow will remain supersonic as it leaves the nozzle
<!--ID: 1680694728215-->
END_CARD
 
--------

START_CARD
Basic



For the following equation: $\frac{\dot{m}}{\rho_{0} \sqrt{2c_{p} T_{0}}} = A_{t} \left(\frac{2}{\gamma+1}\right)^{\frac{1}{\gamma-1}} \sqrt\frac{\gamma-1}{\gamma+1}$
- Name it's variables
- Describe it's meaning
- Specifically descibe how it relates to pressure differentials
- State limitiations and applicability

Back: 
- This is the equation for isentropic choked flow in a converging diverging nozzle
- $\rho_{0},T_{0}$ are stagnation temperature and density respectively
- $c_{p}$ is constent pressure specific heat capacity
- $\gamma$ is specific heat ratio of the gas
- $\dor{m}$ is mass flow rate
- $A_{t}$ is the cross sectional area of the throat
- It makes the assumption of a perfect gas along with basically every assumption you can make except for compressibility
- The equation itself is the result of the fact that choked flow through a nozzle has maximum flow rate which is independent of pressure differential across the nozzle
- The equation shows that the only way to incerease flow throughput is by increasing stagnation pressure or temperature or by increasing throat area
<!--ID: 1680694728228-->
END_CARD


--------

START_CARD
Basic

For a given gas and converging diverging nozzle connected to a large gas reseviour, experiencing choked flow, state how do these changes effect mass flow rate:
- Increasing reseviour pressure
- Increasing reseviour temperature
- Increasing reseviour density
- Decreasing output ambient pressure
- (for all these assume the other properties of the reseviour gas are constant)

Back: 
- Increasing reseviour pressure - no change
- Increasing reseviour temperature - increases mass flow rate
- Increasing reseviour density - increases mass flow rate
- Decreasing output ambient pressure - no change
<!--ID: 1680694728243-->
END_CARD




--------

START_CARD
Basic

Where does the energy for accelerating a gas in the diverging section of a converging diverging nozzle come from?


Back: 
- The pressure and temperature get converted into kinetic energy
- ![[Pasted image 20230402153915.png]]
<!--ID: 1680694728256-->
END_CARD



--------

START_CARD
Basic

For a converging diverging nozzle describe and explain the gas behaviour if the input pressure and output pressure are the same?


Back: 
- There is no pressure gradient across the nozzle
- Hence there is no velocity change across the nozzle
- In realistic conditions there must be no flow at all
- On the diagram below this state would correspond to (1)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728268-->
END_CARD

 
--------

START_CARD
Basic


For a converging diverging nozzle describe and explain the gas behaviour if there is a pressure difference across the nozzle but it doesn't reach critical pressure at the throat?

Back: 
- The pressure potential means that there is flow across the nozzle
- The flow accelerates in the converging region
- At the throat the flow is not at critical pressure hence is not at mach 1
- The flow deccelerates in the diverging region and never reaches supersonic speeds
- On the diagram below this state would correspond to (2)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728280-->
END_CARD


 
--------

START_CARD
Basic

For a converging diverging nozzle describe and explain the gas behaviour if there is  a pressure difference across the nozzle but such that it just barely can reach critical pressure at the throat?


Back: 
- The pressure potential means that there is flow across the nozzle
- The flow accelerates in the converging region
- At the throat the flow reaches critical pressure hence it's at mach 1
- The back pressure is too high and a normal shock forms
- The flow is subsonic and hence deccelerates during the diverging region
- On the diagram below this state would correspond to (3)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728293-->
END_CARD



--------

START_CARD
Basic

For a converging diverging nozzle describe and explain the gas behaviour if  there is a normal shock inside the nozzle after the throat?


Back: 
- The pressure potential means that there is flow across the nozzle
- The flow accelerates in the converging region
- Since there is a normal shock the flow must of been supersonic, hence it must be choked
- The flow must be accelerating in the diverging region since it's supersonic
- At some point in the diverging region the pressure gradient is too great leading to a normal shock and a transition into subsonic flow
- Now it's subsonic it will deccelerate in the remaining region of the diverging nozzle
- On the diagram below this state would correspond to (4)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728306-->
END_CARD



--------

START_CARD
Basic


For a converging diverging nozzle describe and explain the gas behaviour if there is a normal shock at the nozzle exit.

Back: 
- The pressure potential means that there is flow across the nozzle
- The flow accelerates in the converging region
- Since there is a normal shock the flow must of been supersonic, hence it must be choked
- The flow must be accelerating in the diverging region since it's supersonic
- At the exit of the diverging region the pressure gradient is too great leading to a normal shock and a transition into subsonic flow
- On the diagram below this state would correspond to (5)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728318-->
END_CARD



--------

START_CARD
Basic

For a converging diverging nozzle describe and explain the gas behaviour if the back pressure is low enough to have no normal shock in the nozzle, but is still higher than the design condition.

Back: 
- Since there are no normal shocks inside the nozzle we know the inerior of the nozzle is operating normally (as far as lack of shocks are concerned)
- The pressure of the exiting gas is too low, this means that oblique shocks will form outside the nozzle (in a vehicle this causes inefficiency)
- On the diagram below this state would correspond to (6)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728330-->
END_CARD


--------

START_CARD
Basic


For a converging diverging nozzle describe and explain the gas behaviour if the back pressure is at the design condition.

Back: 
- At design condition we know the interior of the nozzle will be working as desired (as far as lack of shocks are concerned)
- The pressure of the exhaust matches ambient pressure
- The flow outside the nozzle continues as supersonic flow
- This is the ideal operating condition
- On the diagram below this state would correspond to (7)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728344-->
END_CARD



--------

START_CARD
Basic


For a converging diverging nozzle describe and explain the gas behaviour if the back pressure is lower than the nozzle exit pressure.

Back: 
- At/above design condition we know the interior of the nozzle will be working as desired (as far as lack of shocks are concerned)
- The pressure of the exhaust is so high that it exceeds ambient pressure and expands until it forms shocks (in a vehicle this causes inefficiency)
- On the diagram below this state would correspond to (8)
- ![[Pasted image 20230402152035.png]]
<!--ID: 1680694728357-->
END_CARD
 
