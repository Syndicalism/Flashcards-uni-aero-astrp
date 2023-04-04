TARGET_DECK: Propulsion::3 Gas dynamics



START_CARD
Basic

What is the difference between an isentropic and an adiabatic process?


Back: 
- isentropic refers to having constant entropy
- adiabatic process is a thermodynamic process in which heat is not either lost or gained by the thermodynamic system
- Isentropic process is a type of adiabatic process, but an adiabatic process is not nessisarily a isentropic one

END_CARD


 
--------

START_CARD
Basic

Explain what stagnation enthalpy is?


Back: 
- Enthalpy is the sum of internal energy and the product of pressure volume ($H = U + PV$) 
- If a fluid is moving then it has non internal energy
- If you take a moving fluid and convert that KE into other forms of energy that can contribute to enthalpy then that is equivilent to stagnation enthalpy
- This is why another name for stagnation enthalpy is static enthalpy
- Somewhat intuitively that is why it's equation is $h_{0} = h + \frac{V^{2}}{2}$
- Stagnation enthalpy is also sometimes called total enthalpy, because 

END_CARD

 
--------

START_CARD
Basic

How does stagnation enthalpy change in a adiabatic process where no work is done?


Back: 
- In a adiabatic process by defenition no heat is transferred
- If no work is also done then there is no change in the total energy of the system
- Stagnation enthalpy is essentially the sum of energy of a system
- Hence there is no change in stagnation enthalpy

END_CARD


 
--------

START_CARD
Basic

How does enthalpy change in a adiabatic process where no work is done?


Back: 
- In a adiabatic process by defenition no heat is transferred
- If no work is also done then there is no change in the total energy of the system
- Although there may be no total energy change, if the fluids velocity changes then it's enthalpy will also change
- Calculating how it changes may make use of the equation for stagnation enthalpy ($h_{0} = h + \frac{V^{2}}{2}$) since in this process that will not change

END_CARD

 
--------

START_CARD
Basic


Why doesn't stagnation enthalpy change across a normal shock?

Back: 
- In a normal shock no work is done and no heat is transferred
- Hence stagnation enthalpy will not change

END_CARD

 
--------

START_CARD
Basic

What is the approximate process for deriving the equations in normal shock analysis?


Back: 
- The shock wave excerts extreme changes in fluid properties over a very small region (the shock wave itself is only like a micrometer thick ~0.001mm)
- The event itself can be modelled as adiabatic compression
- We use this thin region as the control volume
- Since the regions so thin there is negligible change in area 
- Starting point will be conservation equations (mass, momentum and energy) taking the 1D compressible streamline equations derived previously
- We can assume a perfect gas to get additional equations
- Across a normal shock there is no change in stagnation enthalpy (since no work is done and it's adiabatic) it's equation can be used
- The equation for mach number can be used to rearange equations interms of mach number
- Using these facts together can be used to manipulate the equations into what are known as the "Rankine-Hugoniot equations"
- ![[Pasted image 20230402105715.png]]

END_CARD


 
--------

START_CARD
Basic


For the following equation: $\text{Ma}^{2}_{2} = \frac{(\gamma - 1)\text{Ma}_{1}^{2} + 2}{ 2\gamma \text{Ma}^{2}_{1} + 1 - \gamma }$
- Name it's variables
- Describe it's meaning
- State limitiations and applicability

Back: 
- This is one of the Rankie-Hugonoit equations, it shows the mach number after a normal shock
- $\text{Ma}_1$ is the mach number before the normal shock
- $\text{Ma}_2$ is the mach number after the normal shock
- $\gamma=$ specific heat ratio of the gas
- This equation is supposed to be applied on the boundaries of the normal shock
- It assumes a perfect gas as well as all the assumptions related to the compressible gas flow equations (viscosity ect)

END_CARD



--------

START_CARD
Basic

For the following equation: $\frac{P_{2}}{P_{1}} = 1 + \frac{2\gamma}{\gamma+1}(\text{Ma}_{1}^{2} - 1)$
- Name it's variables
- Describe it's meaning
- State limitiations and applicability

Back: 
- This is one of the Rankie-Hugonoit equations, it shows the pressure change assosiated with a shock
- $\text{Ma}_1$ is the mach number before the normal shock
- $\gamma=$ specific heat ratio of the gas
- $P_{2}/P_{1}=$ The ratio of the pressure after to before the normal shock
- This equation is supposed to be applied on the boundaries of the normal shock
- It assumes a perfect gas as well as all the assumptions related to the compressible gas flow equations (viscosity ect)

END_CARD


 
--------

START_CARD
Basic

After a normal shock how does pressure, density, temperature and velocity change? How does the magnitude of this change differ with initial higher mach numbers?


Back: 
- Pressure increases, the increase is exponential with mach number increase
- Density increases, but tends to a value with mach number increase
- Temperature increases, the increase is exponential with mach number increase
- Velocity decreases, the decrease tends towords zero with higher mach numbers
- ![[Pasted image 20230402134249.png]]

END_CARD


 
--------

START_CARD
Basic


Explain why there is no entropy change across a normal shock.

Back: 
- There is entropy change across a normal shock!
- The process may be adiabatic but isn't isentropic
- The shock itself is caused by extreme instability in the fluid state which leads to a rapid conversion of KE into other forms of energy, during this some is used to increase the fluids temperature, this produces entropy.

END_CARD



 
--------

START_CARD
Basic

By using the Rankie-Hugoniot equations it is possible to derive an eqaution showing entropy change, by plotting it you get the following graph. What does this tell us about the equations themselfs?
![[Pasted image 20230402135309.png]]
 
Back: 
- This shows that at a mach number of 1 there is no change in entropy
- It shows that for mach numbers greater than 1 entropy increases, probably leading to loss of useful energy
- The equations predict a reduction in entropy if applied to a mach number less than 1
- This violates the seond law of thermodynamics and is not possible
- This is evedence that as expected the equations only work when analysing the transition from supersonic to subsonic flows (aka $Ma_{1}>1>Ma_{2}$)

END_CARD

 
--------

START_CARD
Basic


Why is a shock wave so abrupt? In the context of normal shocks how can pressure difference initiate one?

Back: 
- Shock waves are caused by the local gas state not being in equilibrium, unlike typical processes this discontiniouty in conditions is abrupt (rather than smooth propertie transitions usually observed)
- The reason abrupt changes in conditions can exist is because of the nature of supersonic flows: a flow so fast that information cannot back propigate
- This means that even 1mm before the shock the flow may have perfectly undisterbed behaviour (rather than the continous transitions seen in things like potential flow)
- Various conditions will contribute to where a shock wave forms but a common one is pressure difference, a normal shock will often form such that it produces a pressure equal to the opposing pressure which caused the transition. (for example atmospheric pressure) 

END_CARD

 
