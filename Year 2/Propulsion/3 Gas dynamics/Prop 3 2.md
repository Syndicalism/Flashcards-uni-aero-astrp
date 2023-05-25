TARGET_DECK: Propulsion::3 Gas dynamics



START_CARD
Basic


What are the assumptions used for simplified 1D compressible flow?

Back: 
- One dimensional flow
- Steady flow
- Inviscid flow (also follows that there is no viscous heating)
- No thermal diffusion
- Ideal gas assumed

END_CARD

 
--------

START_CARD
Basic


Given this equation is related to compressible 1D flows what does it's variables mean? $\frac{dh}{dx} + U \frac{dU}{dx} =0$

Back: 
- $x=$ position along streamline
- $h=$ enthalpy
- $U=$ velocity

END_CARD



 
--------

START_CARD
Basic

Explain the following equation and name it's variables: $\rho_{1} U_{1} = \rho_{2} U_{2}$


Back: 
- This is the equation for conservation of mass along a 1D compressible flow, which makes perfect sense if you think about it.
- $U=$ velocity at some point along a streamline
- $\rho=$ density at some point along a streamline

END_CARD

 
--------

START_CARD
Basic


Explain the following equation and name it's variables: $\frac{1}{2} U^{2}_{2} + \int^{P_{2}}_{P_{1}} \frac{1}{\rho} \:dP = \frac{1}{2} U_{1}^{2}$

Back: 
- This is the equation for conservation of momentum along a 1D compressible flow.
- $U=$ velocity at some point along a streamline
- $\rho=$ density at some point along a streamline
- $P=$ pressure at some point along a streamline

END_CARD
 
--------

START_CARD
Basic

Explain the following equation and name it's variables: $h_{1} + \frac{1}{2} U_{1}^{2} = h_{2} + \frac{1}{2} U^{2}_{2}$


Back: 
- This is the equation for conservation of energy along a 1D compressible flow.
- $U=$ velocity at some point along a streamline
- $h=$ enthalpy at some point along a streamline

END_CARD

 
--------

START_CARD
Basic


Explain the following equation and name it's variables: $h_{0} = h_{1} + \frac{1}{2} U_{1}^{2}$

Back: 
- This is the equation for stagnation enthalpy along a 1D compressible flow.
- $U_{1}=$ velocity at some point along a streamline
- $h_{1}=$ enthalpy at some point along a streamline
- $h_{0}=$ stagnation enthalpy of streamline

END_CARD


 
--------

START_CARD
Basic

Explain the following equation, additional assumptions and name it's variables: $T_{0} = T_{1} + \frac{U_{1}^{2}}{c_{P}}$


Back: 
- This is the equation for stagnation temperature along a 1D compressible flow.
- $U_{1}=$ velocity at some point along a streamline
- $T_{1}=$ temperature at some point along a streamline
- $C_{p}=$ constant pressure specific heat
- $T_{0}=$ stagnation temperature of streamline
- This equation makes the additional assumption that we are dealing with a perfect gas

END_CARD


 
--------

START_CARD
Basic

Explain the following equation, additional assumptions and name it's variables: $P_{0} = P_{1} \left(\frac{T_{0}}{T_{1}}\right)^\frac{\gamma}{\gamma-1}$


Back: 
- This is the equation for stagnation temperature along a 1D compressible flow.
- $U_{1}=$ velocity at some point along a streamline
- $T_{1}=$ temperature at some point along a streamline
- $T_{0}=$ stagnation temperature of streamline
- $P_{1}=$ pressure at some point along a streamline
- $P_{0}=$ stagnation pressure of streamline
- $\gamma=$ specific heat ratio
- This equation makes the additional assumption that we are dealing with a perfect gas
- This equation makes the additional assumption that all processes along the streamline have isentropic flow, in the event of a normal shock there will be a entropy change meaning a change in stagnation pressure.

END_CARD

 
--------

START_CARD
Basic


Explain the following equation, additional assumptions and name it's variables: $\rho_{0} = \rho_{1} \left(\frac{T_{0}}{T_{1}}\right)^\frac{\gamma}{\gamma-1}$

Back: 
- This is the equation for stagnation temperature along a 1D compressible flow.
- $U_{1}=$ velocity at some point along a streamline
- $T_{1}=$ temperature at some point along a streamline
- $T_{0}=$ stagnation temperature of streamline
- $\rho_{1}=$ density at some point along a streamline
- $\rho_{0}=$ stagnation density of streamline
- $\gamma=$ specific heat ratio 
- This equation makes the additional assumption that we are dealing with a perfect gas
- This equation makes the additional assumption that all processes along the streamline have isentropic flow, in the event of a normal shock there will be a entropy change meaning a change in stagnation density.

END_CARD



 