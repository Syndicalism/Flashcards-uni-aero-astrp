TARGET_DECK: Propulsion::1 Introduction




START_CARD
Basic

![[Pasted image 20230308150311.png]]
What is the basic derivation of the rocket thrust equation?

Back: 
![[Pasted image 20230308150311.png]]
- Setup a control volume around the rocket.
- Get an equation of momentum flux, mainly that $\dot{M}_{out} - \dot{M}_{in} = \sum\limits F$, aka sum of momentum flow in (which is none) vs momentum flow out (exhaust) against pressure and thrust.
- Expand equations on pressure forces and describe exhaust momentum flux using ex velocity and mass flow rate
- Sub into momentum flux equation and rearrange:
$$  F  = \dot{m} V_{j} + A_{j} (P_{j} - P_{A}) $$
<!--ID: 1680694889485-->
END_CARD

 
--------

START_CARD
Basic


Explain what each variable in this equation means and where it is applicable, and common approximations that may be applied:
$$ F =  \dot{m} V_{ex} + A_{j}( P_{j} - P_{A} ) $$

Back: 
![[Pasted image 20230309115202.png]]
$$ F =  \dot{m} V_{ex} + A_{j}( P_{j} - P_{A} ) $$
It is the equation for force out of a rocket engine. Often since the pressure contribution is tiny relative to the velocity out it may be neglected.
 - $\dot{m}=$  mass flow rate through rocket nozzle
 - $V_{ex}=$ exhaust velocity from rocket nozzle
 - $A_{j}=$ cross sectional area of end of rocket nozzle
 - $P_{j}=$ pressure on rocket nozzle end
 - $P_{A}=$ atmospheric pressure
<!--ID: 1680694889511-->
END_CARD

 

--------

START_CARD
Basic

Explain what each variable in this equation means and where it is applicable, and common approximations that may be applied:
$$ F  = \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + A_{j}(P_{j}-P_{a}) $$

Back: 
![[Pasted image 20230309115149.png]]
$$ F  = \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + A_{j}(P_{j}-P_{a}) $$
This is the equation for force from a jet engine. The variables mean:
 - $\dot{m}_{a}=$ air mass flow through engine
 - $f=\frac{\dot{m}_{f}}{\dot{m}_{a}}=$ air to fuel ratio
 - $V_{jet}=$ exhaust velocity of jet
 - $V_{\infty}=$ free stream velocity
 - $A_{j}=$ area of jet
 - $P_{j}=$ pressure on jet end
 - $P_{A}=$ atmospheric pressure
 - $F=$ thrust of engine
   
Approximations might be:
 - Pressure contribution is tiny relative to the velocity out it may be neglected.
 - Fuel mass flow may be negligible relative to air mass flow $f<<1$ so it's contribution may be neglected
<!--ID: 1680694889529-->
END_CARD


--------

START_CARD
Basic

Define air to fuel ratio. Describe it's common characteristics.


Back: 
The rato of air mass flow to fuel mass flow:
$$ f=\frac{\dot{m}_{f}}{\dot{m}_{a}} = \frac{\text{fuel mass flow}}{\text{air mass flow}} $$
It is often small $f<<1$ which depending on the equation may be used to simplify it using $f\approx0$.
<!--ID: 1680694889545-->
END_CARD

 

--------

START_CARD
Basic

Define $\text{TSFC}$? Describe it's relationship with efficiency.


Back: 
Thrust Specific Fuel Consumption.
$$ \text{TSFC} = \frac{m_{f}}{I} = \frac{\dot{m}_{f}}{F} $$
It is the mass of fuel required per unit impulse, or by dividing by time it is the mass flow rate required for one newton of force. Basically a measure of engine fuel efficiency where the lower the better, since then less fuel is burned per unit thrust.
<!--ID: 1680694889562-->
END_CARD

 

--------

START_CARD
Basic

What is the following equation, what assumptions does it use and what do each of it's variables mean?
$$ s = - \frac{L}{D} \frac{V}{g_{0} \text{TSFC}} \ln( \frac{W_{1}}{W_{2}} ) $$

Back: 
This is the Breguet range equation, gives the range of an aircraft given its initial and final weight.
 - $s=$ range for weight change
 - $V=$ true airspeed
 - $\text{TSFC}=$ Thrust specific fuel consumption, the fuel needed per unit thrust produced
 - $g_{0}=9.81m/s^2=$ earth standard gravity
 - $\frac{L}{D}= \frac{C_{L}}{C_{D}} =$ lift to drag ration
 - $W_1=$ starting total weight
 - $W_2=$ ending total weight
Assumes:
- Constant speed
- Constant lift to drag ratio
- Constant $\text{TSFC}$
<!--ID: 1680694889579-->
END_CARD


 
--------

START_CARD
Basic


Explain the following equation and describe it's variables:
$$ \eta_{O} = \eta_{P} \times \eta_{th} $$

Back: 
This equation descirbes how well an engine converts heat into kinetic energy and then into displacement work. AKA heat $\to$ movement.
- $\eta_{O}=$ overall efficiency, indicates how well an engine converts heat into displacement work. AKA the OVERALL efficiency (shock)
- $\eta_{th}=$ thermal efficiency, indicates how well an engine can convert heat into kinetic energy
- $\eta_{P}=$ propulsive efficiency, indicates how well an engine can convert the kinetic energy into displacement work
<!--ID: 1680694889595-->
END_CARD


--------

START_CARD
Basic

What is propulsive efficiency and it's definitional equation?

Back: 
The propulsive efficiency is defined as the ratio of aircraft power to the rate of kinetic energy of the working fluid produced by the engine.
$$ \eta_{P} = \frac{\dot{W}_{aircraft}}{\dot{W}_{jet}} = \frac{\text{Thrust}\times\text{Speed}}{\Delta\text{KE through jet}} $$
<!--ID: 1680694889610-->
END_CARD




--------

START_CARD
Basic

Describe using an equation $\dot{W}_{aircraft}$ (the power used to propel the aircraft).

Back: 
$$ \dot{W}_{aircraft} = \text{Speed} \times \text{Total thrust} $$
<!--ID: 1680694889627-->
END_CARD

 
--------

START_CARD
Basic

Describe using an equation $\dot{W}_{jet}$ (the kinetic energy produced by the engine).

Back: 
$$ \dot{W}_{jet} = \text{KE}_{out} - \text{KE}_{in} = \frac{1}{2}(\dot{m}_{a} + \dot{m}_{f}) V_{j}^{2} - \frac{1}{2} \dot{m}_{a} V^{2} $$
<!--ID: 1680694889642-->
END_CARD


 
--------

START_CARD
Basic

What is the following equation, describe it's variables and simplifications done for it.  
$$ \eta_{P} = \frac{2}{\frac{V_{j}}{V}+1} $$

Back:  
- This is the equation for propulsive efficiency of a jet engine
- $\eta_{P}=$ propulsive efficiency
- $V_{j}=$ velocity of jet exhaust relative to vehicle
- $V=$ velocity of air relative to vehicle
- The main splifications are: Neglecting contributions from fuel mass since $f<<1$, neglecting pressure contributions 
<!--ID: 1680694889656-->
END_CARD


 
--------

START_CARD
Basic

Explain the practical meaning of the following equation, and the limitations of implementation:
$$ \eta_{P} = \frac{2}{\frac{V_{j}}{V}+1} $$

Back: 
-  This is the equation for (a simplified version of) propulsive efficiency of a jet engine, indicating how the propulsive efficiency changes with the ratio of the exhaust jet velocity to aircraft velocity.
- Considering a constant aircraft velocity, we can see that the propulsive efficiency drops with increasing exhaust speed, and that the efficiency increases as the exhaust speed approaches the aircraft speed. From a propulsive efficiency point of view, we therefore want to minimize the difference between $V_{j}$ and $V$.
- Since thrust is a function of the difference in momentum in vs out ($F=\dot{m}_{a}(V_{j} - V)$), to achieve adiquate thrust for flight the mass flow rate will have to be increased to compensate. (hence why engines often have high bypass ratios and are increasing in size)
![[Pasted image 20230309121703.png]]
<!--ID: 1680694889670-->
END_CARD



--------

START_CARD
Basic

Explain the equation and it's variables:
$$ \dot{Q} = \dot{m}_{f} \text{LCV} $$

Back: 
- This equation describes the relationship between heat production and fuel burn rate, relating them using the lower calorific value of the fuel.
- $\dot{Q}=$ this is the heat produced (per second) by burning some fuel
- $\dot{m}_{f} =$ the mass of fuel burned (per second)
- $\text{LCV}=$ lower calorific value of fuel burned. Is the amount of heat that the fuel releases per unit mass. Basically a measure of energy density of the fuel.
<!--ID: 1680694889682-->
END_CARD

 

