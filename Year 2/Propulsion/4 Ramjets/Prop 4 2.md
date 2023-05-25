TARGET_DECK: Propulsion::4 Ramjets

 



 
--------

START_CARD
Basic


Why do we tend to use ramjets at high velocities?

Back: 
- At supersonic velocities the incoming gas has very high KE
- This allows the diffuser to achieve sufficiently high compression ratios without the need of a compressor
- Hence the compressor isn't needed, so then the turbine isn't needed
- Without the need for a turbine the exhaust temperature doesn't need to be sufficiently low to allow the turbine to operate
- Hence higher combustion temperatures can be used allowing for greater efficiency
END_CARD


--------

START_CARD
Basic


Why do we use turbine jets at low velocities?

Back: 
- The compression ratio achieved with just a diffuser is not high enough
- A turbine is used to ensure the incoming gas has desireable properties
END_CARD


 
--------

START_CARD
Basic

How does the diffuser of a ramjet operate under ideal conditions? Explain why and how it maintains operation over a range of velocities?
![[Pasted image 20230403093242.png]]


Back: 
- In a typical ramjet operation, the air intake is supersonic, and needs to be converted to subsonic conditions in the diffuser. 
- A series of oblique shocks slow the air flow down, followed by a normal shock, after which the flow will be subsonic. 
- The area of the diffuser will then widen allowing the subsonic air to slow down further
- Depending on whether the nozzle is convergent or divergent and the flow is super or sub-sonic, changes if the gas will accelerate or deccelerate
- If the flow does not reach subsonic velocities before the diverging section it could lead to the ramjet completely failing, as that would lead to the flow re accelerating rather than deccelerating
- To ensure the normal shock occurs at the correct location the inlet geometry must be adjusted depending on operating conditions
-  A common way this is achieved is by moving the middlebit (thaat is the technical term) forwards/backwards.
END_CARD


 
--------

START_CARD
Basic


Why do we not instantly instigate a normal shock in the inlet?
![[Pasted image 20230403093242.png]]

Back: 
- The closer the mach number approaching the normal shock is to mach 1, the lower the entropy increase
- So to reduce the entropy increase (and therefor increase the amount of useful energy avaliable) we design the geometry to use oblique shocks to reduce the mach number as close to 1 as possible
- ![[Pasted image 20230403103650.png]]
- ![[Pasted image 20230403103713.png]]
END_CARD

 
--------

START_CARD
Basic


Describe the conditions underwhich combustion occurs in a correctly operating ramjet? What differences are there between a ramjet combustion chamers operation and a jet turbines?

Back: 
- For combustion to occur the air must be travelling sufficiently slowly so subsonic
- Since there is no downstream turbine, a ramjet combustor can safely operate at stoichiometric fuel: air ratios
- Since it's closer to the stoichiometric ratio, the combustion temperatures achieved can be higher (typically ~2400K)
END_CARD



 
--------

START_CARD
Basic


Describe the operation of a correctly operating ramjet exit nozzle, highlight and explain differences compared to a subsonic turbine jet.

Back: 
- The nozzle will use the high enthalpy (pressure and temperature) generated in the combustion chamber to accelerate the combustion products and thereby generate thrust.
- For thrust to be generated the exhausts exit velocity must exceed the free stream velocity, in typical supersonic operation this means the exhaust must be supersonic
- To achieve this a converging diverging nozzle is used to accelerate the exhuast to supersonic speeds
- This is another difference to (subsonic) turbine jets, efficiency decreases with greater differences between exhaust velocity and freestream hence (subsonic) turbine jets do not need to have supersonic exhaust so they don't use converging diverging nozzles
END_CARD

 
--------

START_CARD
Basic

What is the typical operating range of ramjets? What limits the upper and lower operating speeds.


Back: 
- The standard optimal operating range of a ramjet is around Mach 3 to Mach 4, though they can operate somewhat effectively at mach 2
- Ramjets generally can't produce sufficient thrust for operation below mach 0.5 and have extremely poor performance in this range
- They can't operate at low speeds due to the low compression ratios
- At high speeds it becomes difficult to generate subsonic conditions in the combustion chamber, though it is possible to design ramjets to operate usefully to about mach 6
END_CARD



 
--------

START_CARD
Basic

Given the following diagram for a ramjet, what assumptions are made in basic modelling and what models are used for the processes at each stage? 
![[Pasted image 20230403100637.png]]


Back: 
- We assume that we're working with a perfect gas and that all processes are adiabatic
- We also assume that the exhaust is fully expanded aka $P_{4}=P_{A}$
- Assume combustion occurs at negligible kinetic energy
- In the diffuser (1-2) isentropic (no entropy change) compression
- In the combustion chamber (2-3) isobaric (constant pressure) combustion
- In the diffuser (3-4) isentropic (no entropy change) compression
END_CARD

 
--------

START_CARD
Basic


The basic model used for an ideal ramjet does not account for entropy losses related to normal shocks, how does this make sense considering a normal shock must exist when we are dealing with supersonic operation?
![[Pasted image 20230403093242.png]]

Back: 
- Although entropy is generated across a normal shock and the properties of gas change across one, in the event that the mach number is neglegibly greater than one the change is also negligible
- In a ideal ramjet we can assume perfect implementation of systems to minimise entropy changes, if so we can assume that the geometry of the intake is perfect such that the oblique shocks bring the flow velocity down to almost exactly mach 1 such that no entropy is produced across the normal shock
- Since the effect of the normal shock is nothing we can essentially ignore the maths related to it such that the ideal diffuser is able to deal with supersonic flows using the same set of principles as subsonic flows
- ![[Pasted image 20230403103650.png]]
- ![[Pasted image 20230403103713.png]]
END_CARD


 
--------

START_CARD
Basic

How is the following equation simplified when applied to ramjets? $F = \dot{m}_{a} [ (1+f)V_{j} - V ] + A_{j} (P_{j} - P_A)$


Back: 
- Unlike how we simplify turbofans, we cannot neglect $f$ since ramjets require a non insignificant amount of fuel compared to air for operation
- Since exhaust is fully expanded we can neglect the effect of pressure
- Final equation will be something like: $F = \dot{m}_{a} [ (1+f)V_{j} - V ]$ also written as $\frac{F}{\dot{m}_{a}} = (1+f)V_{j} - V$
END_CARD


 
--------

START_CARD
Basic

Starting with the following equation (SFEE) $q-w = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right)$ assuming a perfect gas, show that for any given no work adiabatic process the stagnation temperature is constant ($T_{0,in} = T_{0,out}$).


Back: 
- Adiabatic ($q=0$) and no work is done ($w=0$) so $q-w_{x} = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right) \:\to\: 0 = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right)$
- We know that stagnation enthalpy is equal to the sum of enthalpy and kinetic energy, so we can rewrite the equation interms of stagnation enthalpy $0 = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right) \:\to\: 0 = h_{0,out}-h_{0,in}$
- Since we are working with a perfect gas we know that enthalpy is related to temperature by $\Delta h = c_{p} (\Delta T)$
- Since stagnation enthalpy is the enthalpy for the stagnent equivilent of some fluid, at stagnation enthalpy it will also be at sagnation temperature using this with the point above: $0 = h_{0,out}-h_{0,in} \:\to\: 0 = c_{p}(T_{0,out}-T_{0,in}) \:\to\: T_{0,in} = T_{0,out}$
END_CARD


 
--------

START_CARD
Basic


For an ideal ramjet diffuser, why is the stagnation temperature at the input the same as the normal temperature at the outlet?

Back: 
- An ideal ramjet diffuer performs a zero work-adiabatic gas compression
- A zero work adiabatic process will not produce any change in stagnation enthalpy
- Since we are working with a perfect gas stagnation temperature is a function of stagnation enthalpy
- There will be no change in stagnation temperature between the inlet and outlet $T_{0,in}=T_{0,out}$
- In an ideal ramjet diffuser the velocity at the outlet will be neglegible, hence $T_{out}=T_{0,out}$ so $T_{out}=T_{0,in}$
END_CARD

 
--------

START_CARD
Basic

Starting with the following equation (SFEE) $q-w = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right)$, derive an expression for stagnation enthalpy change and enthalpy change. Explain if the derived expressions makes sense.


Back: 
- Adiabatic ($q=0$) and no work is done ($w=0$) so $q-w_{x} = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right) \:\to\: 0 = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right)$
- This can then become $h_{out} - h_{in} = \frac{1}{2} V^{2}_{out} - \frac{1}{2} V^{2}_{in}$ or $\Delta h = \Delta \text{KE}$, which makes sense because of the first law of thermodynamics and the defenition of enthalpy
- We know that stagnation enthalpy is equal to the sum of enthalpy and kinetic energy, so we can rewrite the equation interms of stagnation enthalpy $0 = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right) \:\to\: 0 = h_{0,out}-h_{0,in} \:\to\: h_{0,out} = h_{0,in}$
- We can see for a zero work adiabatic process the stagnation enthalpy is constant, which makes sense because of the first law of thermodynamics and the defenition of enthalpy
- Note this does not require us to be working with a ideal gas
END_CARD


 
--------

START_CARD
Basic


For an ideal ramjet diffuser the stagnation temperature at the input the same as the normal temperature at the outlet. Using this fact explain how the following equation is derived: $T_{2} = T_{1}\left(1 + \frac{\gamma-1}{2} \text{Ma}_{1}^{2}\right)$
Explain the significants of the equation.

Back: 
- The equation can be very quickly derived using the defenition for stagnation temperature derived in previous lectures $\frac{T_{0}}{T} =  1+ \frac{\gamma-1}{2} \text{Ma}^{2}$
- This can be written as $T_{0,1} = T_{1}\left(1+ \frac{\gamma-1}{2} \text{Ma}_{1}^{2}\right)$
- For an ideal ramjet diffuser the stagnation temperature at the input the same as the normal temperature at the outlet, hence $T_{2}=T_{1,0}$
- Finally $T_{2} = T_{1}\left(1+ \frac{\gamma-1}{2} \text{Ma}_{1}^{2}\right)$ as required
- This equation shows that the diffusor output temperature is a direct function of the mach number squared
- Which in a ramjet is also the input temperature for the combustion gas
END_CARD


 
--------

START_CARD
Basic


For the following equation which is related to ideal ramjets: $f= \frac{T_{3}-T_{2}}{\frac{\text{LCV}}{c_{p}} - T_{3}}$
- Name it's variables
- Describe it's use

Back: 
- $f$ is fuel to air ratio
- $T_{3}$ is temp after the combustion chamber
- $T_{3}$ is temp before the combustion chamber
- $\text{LCV}$ is the lower calorific value of the fuel
- This equation describes the relationship between input temperature, output temperature, LCV and fuel to air ratio in a ideal ramjet combustion chamber
- If designing a ramjet then often $T_{3}$ will be equal to the maximum operating temperature of the ramjet, since the higher $T_{3}$ the better the jet's performance
- So this equation can be used to figure out what fuel to air ratio is required for operation
END_CARD


 
--------

START_CARD
Basic


How is the following equation which describes nozzle exit velocity in a ideal ramjet derived? $V_{j} = \sqrt{2 c_{p} (T_{3} - T_{4})}$

Back: 
- Starting with the SFEE: $q-w = \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right)$
- We know that it is adiabatic and now work is done, hence $q=0$ and $w=0$
- The exit velocity from the combustion chamber is neglected hence $V^{2}_{in}=0$
- So SFEE simplifies to $0=h_{4} - \left(\frac{1}{2}V_{4}^{2} + h_{3}\right)$
- Then we know that this thing's exit velocity is often written as $V_{j}$
- In an ideal ramjet we're dealing with a perfect gas, hence $\Delta h = c_{p} (\Delta T)$
- So $0=h_{4} - \left(\frac{1}{2}V_{4}^{2} + h_{3}\right) \:\to\:  V_{4}  = \sqrt{2(h_{4} - h_{3})} \:\to\:  V_{jet}  = \sqrt{2 c_{p} (T_{3} - T_{4})}$
END_CARD


 
--------

START_CARD
Basic


For the following equation: $V_{j} = \sqrt{2c_{p} T_{3} \left[1- \left(\frac{P_{A}}{P_{3}}\right)^\frac{\gamma-1}{\gamma} \right]}$
- Name it's variables
- Describe it's meaning
- State the physical mechanism behined the energy conversion

Back: 
- This is the equation for the jet velocity from an ideal ramjet engine
- $V_{j}$ is exit velocity
- $c_{p}$ is constant pressure spefific pressure of the exhaust
- $\gamma$ is the ratio of specific heats
- $T_{3}$ is the temperature exiting the combustion chamger
- $P_{3}$ is the pressure exiting the combustion chamger
- $P_{A}$ is the ambient pressure (which is equal to the exhaust pressure since it is fully expanded)
- It shows that the higher $T_{3}$ we achieve the greater the exit velocity from the ramjet
- Using the $\gamma$ of air we can see that it is desireable to maximise $P_{3}$ to increase $V_{j}$
- The mechanism which permits conversion from temperatre into velocity is a converging diverging nozzle
END_CARD

  