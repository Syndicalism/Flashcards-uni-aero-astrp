TARGET_DECK: Propulsion::2 Thermodynamics



START_CARD
Basic

What are state properties? What are the types of state properties? What notation is used for them?

Back: 
Properties that define the state of a system. The 3 types are:
- Intensive, properties that do not depend on the amount of material eg: Temperature. For things like temp and pressure which aren't specific quantity's they may be upper, so intensive doesn't really say much about the notation used.
- Extensive, properties do depend on the amount of material eg: Mass, kinetic energy. Denoted using upper case letters eg $C_{p}$ constant pressure heat. 
- Specific, a type of intensive property derived by dividing any extensive property by mass. Denoted using lower case letters eg $c_{p}$ constant pressure specific heat. 
![[Pasted image 20230401101743.png]]

END_CARD


--------

START_CARD
Basic


State and explain the two property rule.

Back: 
- “The state of a simple compressible system is completely specified by two independent, intensive properties.”
- Simple implies no electrical, magnetic, gravitational, motion or surface tension effects. Basically that the behaviour of the gas is not being influenced by fucky forces beyond the scope of basic gas dynamics. Note that this isn't assuming a perfect or even ideal gas.
- The 2 variables must be independent, for instance under the assumption of an ideal gas internal energy and enthalpy are NOT independent hence a different variable pair must be used (like pressure and specific volume).


END_CARD


--------

START_CARD
Basic 

What is a process and explain the importance of path.

Back: 
- A process is simply the change of some system from one equilibrium state to a different equilibrium state.
- The process can only be fully defined if: The first and final state is fully defined, the path is fully defined
- The path taken can drastically change heating requirements and work done

END_CARD


 
--------

START_CARD
Basic

How is the two property rule useful in defining a process?

Back: 
- The two property rule allows you to describe the state of a system using 2 independent variables (under certain requirements)
- This means that by showing a chart with 2 independent variables (eg: pressure, volume) the state of a system at all times during a process can be fully defined on a simple 2D diagram
- It then becomes much simpler to calculate things eg: work done
- In this example the end points are the same but it is clear that the work done is different!

![[Pasted image 20230401103635.png]]

END_CARD


 
--------

START_CARD
Basic

State and briefly describe the 6 types of process we generally use in this course.

Back: 
- Isothermal (constant temperature)
- Isobaric (constant pressure)
- Isochoric (constant volume)
- Adiabatic (no heat transfer)
- Isentropic (constant entropy, valid when a process is adiabatic and reversible)
- Isenthalpic (constant enthalpy)

END_CARD



--------

START_CARD
Basic


State the first law of thermodynamics and it's equation.

Back: 
- The total energy of an isolated system is constant, energy cannot be created or destroyed it can only change form.
- It is basically a strict rule that can be used to describe what work output is achievable for any process.
- $$ \Delta U  = Q - W  $$ 
- $\Delta U=$ internal energy change of system
- $Q=$ heat transfer into system
- $W=$ thermodynamic work done, extracting energy from the system

END_CARD


 
--------

START_CARD
Basic

What is the second law of thermodynamics and describe it with an equation.


Back: 
- "Entropy of a closed system cannot be reduced"
- The second law of thermodynamics is a general principle which places constraints upon the direction of heat transfer and the attainable efficiencies of heat engines. 
- As an equation it could just be stated that for a closed system $\frac{dS}{dt} \geq 0$ where $S$ is entropy.
- In perfect systems we may model that $\frac{dS}{dt}=0$ which is of course not possible in real life.

END_CARD



--------

START_CARD
Basic

What is the third law of thermodynamics? Explain it to some extent.

Back: 
- "The entropy of a system approaches a constant value when its temperature approaches absolute zero."
- This constant value cannot depend on any other parameters characterizing the closed system, such as pressure or applied magnetic field. At absolute zero (zero kelvins) the system must be in a state with the minimum possible energy.
- Entropy is related to the number of accessible microstates, and there is typically one unique state (called the ground state) with minimum energy. In such a case, the entropy at absolute zero will be exactly zero.
- If the system does not have a well-defined order, then there may remain some finite entropy as the system is brought to very low temperatures, either because the system becomes locked into a configuration with non-minimal energy or because the minimum energy state is non-unique. The constant value is called the residual entropy of the system.
- This stuff isn't really needed to be known for the course but it's nice to add in for completion.

END_CARD


 
--------

START_CARD
Basic

What is entropy, specific entropy and their symbols? 


Back: 
- The disorder of a system, it has relation to the number of accessible microstates of the system.
- A measure of how much unusable energy there is in a system.
- Specific entropy is just the specific version of entropy, hence has symbol $s$, normal entropy has symbol $S$

END_CARD


 
--------

START_CARD
Basic


What is enthalpy and states it's symbols. Then describe it's general practical use.

Back: 
- Symboles are $H$ and $h$ for specific entropy
- It is defined as the sum of the systems internal energy and the product of it's pressure and volume aka: $H=U+PV$ or $h=u + \frac{P}{\rho}$
- Since internal energy can't really be found we often work with changes instead: $\delta H = \delta U + \delta(PV) = \delta U + \delta W$

END_CARD


 
--------

START_CARD
Basic


Describe enthalpy in the case of an ideal and perfect gas. Explain the difference.

Back: 
- For an ideal gas enthalpy is independent of it's pressure or volume, depending only on temperature
- Ideal gas can use the equation $dh = c_{P} \:dT$
- For a perfect gas $c_{P}$ is constant (by definition) hence the equation can be simplified to $\Delta h = c_{p} \Delta T$ 

END_CARD

 
--------

START_CARD
Basic

What is the sign convention for $\Delta U=Q-W$, and what are the variables? Also where does this equation come from.


Back: 
- This equation states the first law of thermodynamics
- $\Delta U=$ increase in internal energy in the system
- $W=$ work output from the system
- $Q=$ heat added into the system

END_CARD


 
--------

START_CARD
Basic


State the following forms of the ideal gas equation and name their variables:
- The shit form
- The somewhat useful form
- The based form

Back: 
- The SHIT form is $PV=n\bar{R}T$
- $\bar{R}=$ the universal gas constant
- $n=$ number of moles of the gas
- The somewhat useful form is $PV=mRT$
- The based form is $P=\rho RT$ (sometimes in the form $P\nu = RT$, here $\nu=$ specific density)
- $R=$ specific gas constant

END_CARD


 
--------

START_CARD
Basic

What is the meaning of the equation: $R = \frac{\bar{R}}{M}$


Back: 
- This relates the specific gas constant of some substance to the universal gas constant
- $\bar{R}=$ the universal gas constant
- $R=$ specific gas constant
- $M=$ molar mass of the gas, the mass of 1 mol of a substance

END_CARD


 
--------

START_CARD
Basic


What is molar mass? What is it's typical symbol?

Back: 
- This is the mass of 1 mol of a substance, often given in grams/mol
- The molar mass of hydrogen is typically 1g/mol
- The molar mass of carbon-12 is 12g/mol
- It's kinda obvious how this works
- The symbol typically used for molar mass is $M$

END_CARD

 
--------

START_CARD
Basic

What are the 4 basic assumptions of the ideal gas model?


Back: 
- All collisions are elastic
- The volume occupied by the molecules is negligible relative to the empty space
- Intermolecular interactions/forces are negligible
- Molecules only carry translational kinetic energy, aka: no weird forms of KE storage like vibration or rotation, just linear momentum.

END_CARD


 
--------

START_CARD
Basic

Give a basic outline of the applicability of the ideal gas law, it's success' and explain limitations.


Back: 
- For typical temperatures, pressures, density's and many common gas compositions it's often quite accurate
- At high pressures and densities the volume of the molecules is not negligible and you get non negligible intermolecular interaction
- Near phase transitions it stops working due to the funky forces involved in phase transitions (intermolecular stuff)

![[Pasted image 20230401120952.png]]

END_CARD


 
--------

START_CARD
Basic

Define constant pressure and volume specific heat and briefly touch on $\gamma$. 


Back: 
- $c_{P}\equiv\left. \frac{\delta u}{\delta T} \right|_{P=const}$ Constant pressure specific heat ($u$ is internal energy)
- $c_{C}\equiv\left. \frac{\delta h}{\delta T} \right|_{V=const}$ Constant volume specific heat ($h$ is enthalpy)
- They can be used to relate temperature change and energy changes assuming some constant conditions, this form is universal with no assumptions.
- $\gamma\equiv \frac{c_{P}}{c_{V}}$, it is the ratio of specific heats (about 1.4 for air) and comes up often in various other equations

![[Pasted image 20230401122452.png]]

END_CARD


 
--------

START_CARD
Basic


Explain how specific heat changes when an ideal and perfect gas is assumed.

Back: 
- In real cases specific heat changes with various state properties (temp, pressure ect). 
- When we assume a ideal gas both internal energy and enthalpy can be shown to be functions of temperature only, hence we can show $c_{P}$ and $c_{V}$ to be ONLY functions of temperature.
- In the perfect gas gas we take these as constants ignoring the temp variable behaviour. (For basically all this modules content we will use perfect gases.)
- ![[Pasted image 20230401122657.png]]

END_CARD


 



