TARGET_DECK: Propulsion::4 Ramjets



START_CARD
Basic

A ideal gas experiences no-work adiabatic flow through a nozzle, explain how the following change:
- Enthalpy
- Stagnation enthalpy
- Stagnation temperature
- Stagnation pressure
- Stagnation density

For each of the variables does it matter if the flow is isentropic?

Back: 
Stagnation enthalpy:
- Stagnation enthalpy will not change as there is no heat added or work done (which can be shown using SFEE but cba to write the proof)
- A change in entropy will not effect this, hence it doesn't matter if the flow is isentropic

Enthalpy:
- Enthalpy will change if the velocity of the gas changes ($h = h_{0} - \frac{1}{2} U^{2}$) so it is possible it will change, but insufficient information to predict direction of change if any
- If entropy is produced then it will likely lead to less energy being KE and hence higher entropy

Stagnation temperature:
- In a ideal gas temperature is a direct function of enthalpy, since stagnation enthalpy doesn't change stagnation temperature will also not change
- Just like stagnation enthalpy entropy generation does not change stagnation temperature

Stagnation pressure:
- In isentropic flow temperature and pressure are directly linked by the function $T = k P^{\frac{\gamma-1}{\gamma}}$, hence pressure and temperature are direct functions of eachother
- Since we know stagnation temperature doesn't change, we know stagnation pressure will not change (if it is isentropic)
- In the event the flow isn't isentropic so entropy is generated then there will be a loss of useful energy resulting in a drop in stagnation pressure

Stagnation density:
- We know density, temperature and pressure are coupled for an ideal gas by $P=\rho RT \:\to\: \frac{P_{0}}{RT_{0}} = \rho_{0}$, hence using the information derived so far:
	- In an isentropic flow $P_{0},T_{0}$ are constant hence stagnation density will not change
	- In a non isentropic flow $T_{0}$ will be cosntant but $P_{0}$ will decrease, hence for an ideal gas stagnation density will increase

END_CARD


--------

START_CARD
Basic

In a ideal ramjet the stagnation temperature changes but somehow the stagnation pressure is constant, explain this.

Back: 
- In an ideal ramjet 
	- Kinetic energy is taken to be negligible at both the inlet and outlet ($\text{KE}_{2}=\text{KE}_{3}=0$) 
	- Combustion is assumed to be a isobaric process ($P_{2}=P_{3}$)
- Stagnation properties are defined as the stagnant equivilent of some fluid, since:
	- KE is zero $P_{2}=P_{2,0}$ and $P_{3}=P_{3,0}$, since $P_{2}=P_{3}$ it becomes clear that $P_{2,0}=P_{3,0}$
	- Stagnation temperature is equivilent to temperature at the inlet and outlet
- Heat is added enthalpy will increase, it is an ideal gas this will cause a temperature increase
- Hence the stagnation temperature must increase

END_CARD


--------

START_CARD
Basic

In a ideal ramjet how does stagnation temperature and stagnation pressure change across the nozzle?

Back: 
- In an ideal ramjet the nozzle is isentropic, no work is done and we are working with a perfect gas
- Hence there will be no change in either stagnation temperature or pressure

END_CARD



--------

START_CARD
Basic

State how stagnation pressure and stagnation temperature change through each component of a ideal ramjet.

Back: 
- Stagnation pressure is constant throughout the entire ramjet
- Stagnation temperature is constant in the diffuser and nozzle but increases in the combustion chamber

END_CARD


--------

START_CARD
Basic

What are the 2 main sources of losses in a real ramjet?

Back: 
- Pressure losses, as a result of friction
- Heat losses, as a result of incomplete combustion and conduction to environment

END_CARD


--------

START_CARD
Basic

How are pressure losses quantified in a ramjet? State how we express them mathamatically.

Back: 
- In an ideal ramjet stagnation pressure is constant throughout the entire thing
- So we describe pressure losses as the ratio of the stagnation pressure before and after each component

| Diffuser ($1\to2$)                     | Combustion ($2\to3$)                   | Nozzle ($3\to4$)                       | 
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| $$\Gamma{d}= \frac{P_{0,2}}{P_{0,1}}$$ | $$\Gamma{c}= \frac{P_{0,3}}{P_{0,2}}$$ | $$\Gamma{n}= \frac{P_{0,4}}{P_{0,3}}$$ |

END_CARD




--------

START_CARD
Basic

How are heat losses quantified in a ramjet? State how we express them mathamatically.

Back: 
- Heat losses are the main concern in the combustion stage, which result from incomplete combustion and heat transfer to the environment
- We quantify these losses using a single combustion efficiency parameter $\eta_{\text{comb}}$ 
- This parameter is just slapped onto the heat added for the combustion chamber:

$$ \begin{align}
&\text{ideal}  && & &\text{real}\\
\dot{Q} &= \text{LCV} \: \dot{m}_{f} &&\to& \dot{Q} &= \eta_\text{comb} \: \text{LCV} \: \dot{m}_{f} 
\end{align} $$

END_CARD


--------

START_CARD
Basic

Why is the full thrust equation used when dealing with real ramjets?

Back: 
- The exhaust is not nessisarilly fully expanded, so the full thrust equation must be used:
$$ F = \dot{m} [ (1+f)V_{j} - V ] \underline{+ (P_{j} - P_{A})A_{j}}$$

END_CARD


--------

START_CARD
Basic

If looking at the TS diagram of a ideal machine vs a real machine how do they differ?

Back: 
![[Pasted image 20230404120044.png]]

- Real machines will have additional increases in entropy
- Depending on if the machine is supposed to extract/do work or just reach a specific target temperature the exact disruption varies

END_CARD


--------

START_CARD
Basic

State the meaning of the variables in the following equations and state their contexts:
$$ \begin{align}
P_{2} &= \Gamma_{d} P_{A} \left(1 + \frac{\gamma-1}{2} \text{Ma}^{2}_{1}\right)^\frac{\gamma}{\gamma-1} & P_{2} &= P_{A} \left(1 + \frac{\gamma-1}{2} \text{Ma}^{2}_{1}\right)^\frac{\gamma}{\gamma-1}
\end{align} $$
State how they relate to stagnation pressure.

Back: 
- They are both equations for the pressure at the outlet of a diffusor in a ramjet
	- The first equation is for a more realistic ramjet
	- The second one is for a ideal ramjet

- $\Gamma_{d}$ is the stagnation pressure loss across a realistic diffusor
- $P_{A}$ is atmospheric pressure
- $\text{Ma}$ is the mach number of the incoming air

- Since KE is negligible in both cases $P_{2} = P_{2,0}$

END_CARD




--------

START_CARD
Basic

State the meaning of the variables in the following equations and state their contexts:
$$ \begin{align}
f &= \frac{T_{3}-T_{2}}{\frac{\text{LCV} \eta_\text{comb}}{c_{p}} - T_{3}} &f &= \frac{T_{3}-T_{2}}{\frac{\text{LCV}}{c_{p}} - T_{3}} 
\end{align} $$ 

Back: 
- They are both equations for the air to fuel ratio required to reach a specific $T_{3}$ in a ramjets combustion chamber
	- The first equation is for a more realistic ramjet
	- The second one is for a ideal ramjet

- $f$ is fuel to air ratio
- $\text{LCV}$ is lower calorific value of the fuel 
- $\eta_{\text{comb}}$ is combustion efficiency paramiter
 

END_CARD



--------

START_CARD
Basic

State the relationship between the stagnation pressure at the diffuer inlet compared to the nozzle outlet in a ideal ramjet and a more realistic ramjet. 

Back: 
$$ \begin{align}
\text{Ideal:} & & P_{0,4} &= P_{0,1}\\
\text{Real:} & & P_{0,4} &= \Gamma_{d} \Gamma_{c} \Gamma_{n} P_{0,1}
\end{align} $$


END_CARD



--------

START_CARD
Basic

Use the following diagram to explain how the non ideal nozzle has reduced thrust:
![[Pasted image 20230404123300.png]]

Back: 
- Entropy is produced due to pressure losses, leading to $T_{4}$ being greater than in the ideal case when the gas is full expanded ($P_{4}=P_{A}$)
- The equation $V_{j} = \sqrt{2 c_{p} (T_{3} - T_{4}) }$ shows that velocity is a function of the temperature difference across the nozzle
- The drop in exhaust velocity will result in lower thrust

END_CARD








