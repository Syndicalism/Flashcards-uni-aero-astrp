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
\text{Adiabatic+zero work entropy:}& & h_{0} &= h + \frac{1}{2}V^{2} & &\to & V_{jb} &= \sqrt{ 2 c_{p} ( T_{013} - T_{19} ) }\\
\text{Isentropic relation:}&& \frac{T}{P^{\frac{\gamma-1}{\gamma}}} &= k & &\to & \frac{P_{02}}{P_{a}} &= \left(\frac{T_{02}}{T_{a}}\right)^{\frac{\gamma}{\gamma -1}}
\end{align} $$

Using maths magic all of these combine into:
$$ \begin{align}
V_{jb} &= \sqrt{2 c_{p} T_{013} \left(1 - \frac{P_{a}}{P_{013}}^{\frac{\gamma-1}{\gamma}}\right)} \\&= \sqrt{2 c_{p} T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right) \left(1 - \frac{P_{a} }{P_{02}(\text{fpr})}^{\frac{\gamma-1}{\gamma}}\right)}
\end{align} $$

Which essentially tells us that the bypass exit velocity is purely a function of fan pressure ratio

END_CARD


--------

START_CARD
Basic

![[Pasted image 20230508131525.png]]

How can the following equation be determined, and how does it relate to finding bypass ratio?

$$ \begin{align}
V_{jc} &= \sqrt{ 2 c_{p} T_{05} \left( 1 - \frac{P_{9}}{P_{05}}^{\frac{\gamma-1}{\gamma}}\right) }
\end{align} $$

Back: 
$$ \begin{align}
\text{Isentropic relation:}&& \frac{T}{P^{\frac{\gamma-1}{\gamma}}} &= k & &\to & \frac{T_{9}}{T_{5}} &= \left(\frac{P_{9}}{P_{5}}\right)^{\frac{\gamma-1}{\gamma}}\\
\text{Adiabatic+zero work entropy:}& & h_{0} &= h + \frac{1}{2}V^{2}\\
\text{Low KE at 5:}& & V_{5}^{2} &\approx 0, & &\therefore h_{05} \approx h_{5},\:\:T_{05} \approx T_{5}\\
\end{align} $$
- This can all be combined together

$$ \begin{align}
h_{05} - h_{09} &= h_{5} - h_{9} + \frac{1}{2}(V_{5}^{2} - V_{9}^{2})\\
0 &= h_{05} - h_{9} + \frac{1}{2}( - V_{9}^{2})\\
V_{9} &= \sqrt{ 2c_{p} (T_{05} - T_{9}) } \\
 &= \sqrt{ 2c_{p} \left(T_{05} - T_{05} \left(\frac{P_{9}}{P_{05}}\right)^{\frac{\gamma-1}{\gamma}} \right) } \\
V_{jc} &= \sqrt{ 2c_{p} T_{05} \left(1 - \frac{P_{9}}{P_{05}}^{\frac{\gamma-1}{\gamma}} \right) } \\
\end{align} $$
- It shows us that by varying the pressure loss across the turbine we can change the jet output velocity, which makes perfect sense
- So if we want to maximise efficiency aka $V_{jc} \approx V_{jb}$ we can use this to find the work that needs to be extracted through the turbine and hence bypass ratio


END_CARD


--------

START_CARD
Basic

Name all the variables in the following equation and state what the equation describes:

$$ \begin{align}
\dot{m}_{c} c_{p} (T_{045} - T_{05}) &= \dot{m}_{c} c_{p} (T_{023} - T_{02}) + \text{bpr} \:\dot{m}_{c} c_{p} (T_{013} - T_{02})
\end{align} $$

Then give a basic outline of how it's derived

Back: 
- 

$$ \begin{align}
m_{c} c_{p} (T_{04} - T_{05}) &= m_{c} c_{p} (T_{03} - T_{02}) + m_{b} c_{p} (T_{013} - T_{02})
\end{align} $$

END_CARD





