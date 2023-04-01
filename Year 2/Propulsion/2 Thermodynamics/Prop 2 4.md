---
cards-deck: Propulsion::Thermodynamics
---

- What is the following equation: $\dot{Q}-\dot{W} = \sum\limits_\text{out} \dot{m} e_{T} -  \sum\limits_\text{in} \dot{m} e_{T}$
- Name it's variables
- Describe it's meaning
#card 
- This is the general steady flow energy equation, it's the result of taking the first law of thermodynamics and applying it to a control volume
- $\dot{Q}=$ heat added per unit time
- $\dot{W}=$ work extracted per unit time
- $e_{T}=$ specific energy of some input/output
- $\dot{m}=$ mass flow rate
- Essentially it is just a way of writing that the energy change of some substance flowing through a control volume is related to the work done on it and the heat added/removed, this is the starting point for most gas analysis we do.
- ![[Pasted image 20230401145540.png]]







![[Pasted image 20230401150343.png]]
In the simple model of a turbojet engine: 
- explain what each component is
- explain the processes that occur moving between the stages
- state additional things worth keeping in mind
#card 
- Diffuser, This is a passive component, where no work is done and no heat is transferred (hence is a adiabatic process). Air typically flows in at a high velocity, but is slowed down significantly such that KE can be neglected.
- Compressor, The compressor is doing work on the fluid, increasing its pressure and temperature. This is an adiabatic component (no heat transfer) and the kinetic energy can be neglected at the inlet and the outlet.
- Burner, the heat addition from combustion can be modelled as a constant pressure heat addition process, no work is done on the fluid and KE is neglected again.
- Turbine, this extracts work from the gas (equivalent to what the compressor needs) and with no heat transfer is modelled as a adiabatic process. (again KE ignored)
- Nozzle, this is the fun end of the thing where gas becomes thrust. The model is basically just a diffuser in reverse so adiabatic modelling where input KE is neglected but output KE is important (because thrust).


Explain this equation: $\frac{T_{2}}{T_{1}} = \left(\frac{P_{2}}{P_{1}}\right)^\frac{\gamma-1}{\gamma}$
#card 
- It describes the relationship between temperature and pressure for an adiabatic process dealing with a perfect gas
- $\gamma$ is the ratio of specific heats




What is the macroscopic equation relating entropy increase, heat transfer into a system and temperature? What does it tell you about entropy?
#card 
- Simply $dS = \frac{dQ}{T}$ or $ds = \frac{dq}{T}$ 
- This shows that adding heat to a cold system results in a greater entropy increase that adding an equivilent amount of heat to a hot system
- By understanding entropy as a measure of energy dispersal this makes sense, extreme temperatures tend to be useful so if you want to do something useful with heat you'll get more done by adding that heat to something that's already hot rather than heating something cold




What is the following equation, name it's variables, describe it's applicability and uses: $T\:dS = dU - p\:dV$
#card 
- This is known as the first TdS equation
- $dS$ is entropy increase, $dU$ is internal energy increase, $p$ is pressure, $dV$ is volume increase
- This form makes no assumptions and is universally applicable
- It is a equation that describes how changes in internal energy relate to entropy changes



What is the following equation, name it's variables, describe it's applicability, uses and give the specific version: $T\:dS = dH - V\:dp$
#card 
- This is known as the second TdS equation
- $dS$ is entropy increase, $dH$ is enthalpy increase, $dp$ is pressure increase
- This form makes no assumptions and is universally applicable
- Just like the first TdS equation it describes how entropy changes relates to other changes in the system
- To make it specific you just divide by mas and sub in specific mass: $T\:dS = dH - V\:dp \:\to\: T\:ds = dh - \frac{V}{m}\:dp \:\to\: T\:ds = dh - \nu\:dp$




Briefly state what assumptions go into the following equation and state variable names and the use of the equation: $s_{2}-s_{1} = c_{V} \ln\left(\frac{T_{2}}{T_{1}}\right) + R \ln\left( \frac{\nu_{2}}{\nu_{1}}\right)$
#card 
- It's just an equation that was derived to describe entropy changes in a simple model of a system
- It assumes a perfect gas
- $s$ is specific entropy
- $c_{V}$ is constant volume specific heat
- $R$ is specific gas constant of the thing
- $\nu$ is specific volume
- Note: This is derived simply using the second TdS equation and ideal gas law. 



Briefly state what assumptions go into the following equation and state variable names and the use of the equation: $s_{2}-s_{1} = c_{V} \ln\left(\frac{P_{2}}{P_{1}}\right) + c_{P} \ln\left( \frac{\nu_{2}}{\nu_{1}}\right)$
#card 
- It's just an equation that was derived to describe entropy changes in a simple model of a system
- It assumes a perfect gas
- $s$ is specific entropy
- $c_{V}$ is constant volume specific heat
- $c_{P}$ is constant pressure specific heat 
- $\nu$ is specific volume
- Note: This is derived simply using the second TdS equation and ideal gas law. 



On a TS diagram how does a isentropic process differ from a real process? How does this relate to a jet engine?
#card 
- By definition an isentropic process is one in which there is no increase in entropy. On a TS diagram this means that it will be a vertical line.
- By the second law of thermodynamics we know entropy will increase or stay the same
- Realistically entropy will always increase, hence it will not be a vertical line
- In a gas turbine we assume both the compressor and turbine are isentropic, in reality this isn't the case. In both cases it's clear that there is an increase in entropy which reduces the useful work of the system and hence efficiency
- ![[Pasted image 20230401155646.png]]



Define isentropic efficiency factor.
#card 
- Isentropic efficiency factor is commonly used when dealing with compressors/turbines, it is a measure of the difference between actual work and idealised isentropic work
- For work extracted it is $\eta = \frac{w_{real}}{w_{isentropic}}$, for work input it is $\eta = \frac{w_{isentropic}}{w_{real}}$. To avoid confusion all that's really needed is to keep in mind that $\eta<1$ (second law of thermodynamics)

