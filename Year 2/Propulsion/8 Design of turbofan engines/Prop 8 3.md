TARGET_DECK: Propulsion::8 Design of turbofan engines



START_CARD
Basic

What is bypass ratio?

Back: 
- The mass flow bypassing the engine core over the mass flow through the engine core

END_CARD


--------

START_CARD
Basic

What is the fan pressure ratio?

Back: 
- The ratio of the pressure before the fan vs after the fan

END_CARD


--------

START_CARD
Basic

For a fixed thrust how does the fan pressure ratio and bypass ratio relate?

Back: 
- A higher fan pressure ratio means that the velocity at the outlet will be greater, hence to keep a constant thrust you'd have to decrease mass flow rate and hence bypass ratio
  
![[Pasted image 20230507203928.png]]

END_CARD



--------

START_CARD
Basic

Explain the following graph and it's implications in turbofan design. 
![[Pasted image 20230507211044.png]]

Back: 
- This shows how specific thrust and specific fuel consumption vary with fan pressure ratio
- Specific thrust is effectively just the speed of the air exiting the jet
- (Bare) Specific fuel consumption is the fuel needed per unit thrust
- It can be seen that a higher fan pressure ratio results in reduced efficiency

END_CARD


--------

START_CARD
Basic

What is the equation for fpr?

Back: 
- fpr is fan pressure ratio:
$$ \begin{align}
\text{fpr} &= \frac{P_{013}}{P_{02}}
\end{align} $$

- This is the ratio of stagnation pressures across the fan (after fan divided by before fan)

![[Pasted image 20230508131525.png]]

END_CARD


--------

START_CARD
Basic

How can fan pressure ratio be used to determine $T_{013}$ for the isentropic and realistic case?
![[Pasted image 20230508131525.png]]

Back: 
$$ \begin{align}
\text{Fan pressure ratio:}&&\text{fpr} &= \frac{P_{013}}{P_{02}}\\
\text{Isentropic relation:}&& \frac{T}{P^{\frac{\gamma-1}{\gamma}}} &= k & &\to & \frac{T_{013s}}{T_{02}} &= \left(\frac{P_{013}}{P_{02}}\right)^{\frac{\gamma-1}{\gamma}} \\
&& && && &= (\text{fpr})^{\frac{\gamma-1}{\gamma}}\\
&& && && T_{013s} &= T_{02} (\text{fpr})^{\frac{\gamma-1}{\gamma}}
\end{align} $$
- This assumes perfect gas relations and no entropy change, to account for entropy we use isentropic efficiency factor $\eta_{f}$:

$$ \begin{align}
\eta_{f} &= \frac{\Delta T_{0s}}{\Delta T_{0}} = \frac{T_{013s} - T_{02}}{T_{013} - T_{02}} & &\to & \eta_{f}(T_{013} - T_{02}) = T_{013s} - T_{02}\\
&& && \eta_{f}T_{013} = T_{013s} + T_{02} (\eta_{f} - 1)\\
&& && \eta_{f}T_{013} = T_{02} (\text{fpr})^{\frac{\gamma-1}{\gamma}} + T_{02} (\eta_{f} - 1)\\
&& && T_{013} = \frac{T_{02}}{\eta_{f}} \left( (\text{fpr})^{\frac{\gamma-1}{\gamma}} + \eta_{f} - 1 \right)\\
&& && T_{013} = T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right)\\
\end{align} $$


--------

START_CARD
Basic

Starting with the equation:
$$ \begin{align}
T_{013} = T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right)
\end{align} $$
What else is needed to derive fan velocity? What does the final equation tell us about the properties of fan exit velocity?

Back: 
$$ \begin{align}
\text{Temperature across fan:}& & T_{013} &= T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right)\\
\text{Adiabatic - zero work:}& & h_{0} &= h + \frac{1}{2}V^{2}
\end{align} $$

END_CARD



