TARGET_DECK: Propulsion::7 Gas Turbine Engines



START_CARD
Basic

Sketch the TS diagram for the process across and ideal diffusor and a realistic diffusor.

Back: 

![[Pasted image 20230414155111.png]]

END_CARD


--------

START_CARD
Basic

What is the definition of isentropic efficiency? (for a compressor and turbine)

Back: 
- It is the change in stagnation enthalpy in the ideal case divided by the change in stagnation enthalpy in the real case. (for a compressor)
$$ \begin{align}
\eta_{c} &= \frac{\Delta h_{0s}}{\Delta h_{0}} = \frac{h_{03s} - h_{02}}{h_{03} - h_{02}}
\end{align} $$
- Since the real enthalpy change is greater than ideal it's clear this will be less than one.

- For a turbine you just flip it:
$$ \begin{align}
\eta_{c} &= \frac{\Delta h_{0}}{\Delta h_{0s}}  
\end{align} $$

END_CARD


--------

START_CARD
Basic

$$ \begin{align}
T_{03} &= T_{02} + \frac{T_{03s} - T_{02}}{\eta_{c}}
\end{align} $$

For this equation:
- State what it describes
- Name it's variables

Back: 
- This is the equation for the real temperature change across a compressor
- $T_{03}$ is the real temperature out of the compressor
- $T_{02}$ is the temperature into the compressor
- $T_{03s}$ is the temperature out of the compressor assuming isentropic compression
- $\eta_{c}$ is the isentropic efficiency of the compressor

END_CARD


--------

START_CARD
Basic

$$ \begin{align}
\dot{Q}_{23} - \dot{W}_{x,23} &= H_{2} - H_{3}
\end{align} $$

Starting with the SFEE, how can we determine specific work done across a real compressor? (Making use of isentropic efficiency factor)

Back:  
- We assume negligible KE, and $Q$ to be zero:
$$ \begin{align}
\dot{Q}_{23} - \dot{W}_{x,23} &= H_{2} - H_{3} & &\to & - \dot{W}_{x,23} &= (h_{2} - h_{3})\dot{m} _{air}
\end{align} $$
- Then we assume a perfect gas ($\Delta h = c_{p} \Delta T$):
$$ \begin{align}
 \dot{W}_{x,23} &= (h_{2} - h_{3})\dot{m}_{air}  & &\to & - \frac{\dot{W}_{x,23}}{\dot{m}_{air} } &= (T_{2} - T_{3}) c_{P}
\end{align} $$
- Now we can use old methods to calculate the temp change assuming isentropic efficiency, and use that with isentropic efficiency factor to get the real temp change:
$$ \begin{align}
\eta_{c} &= \frac{\Delta h_{0s}}{\Delta h_{0}} & &\to & T_{03} &= T_{02} + \frac{T_{03s} - T_{02}}{\eta_{c}}
\end{align} $$
- Done

END_CARD



--------

START_CARD
Basic



Back: 
- 

END_CARD




