TARGET_DECK: Propulsion::10 Turbomachinery part 2




START_CARD
Basic

State the equation and variable names for the flow coefficient. (turbomachines)

Back: 
$$ \begin{align}
\phi &= \frac{V_{x}}{U}
\end{align} $$

- $\phi$ is the flow coefficient
- $V_{x}$ is the axial flow velocity
- $U$ is the blade speed
<!--ID: 1685355946848-->
END_CARD


--------

START_CARD
Basic

What does flow coefficient tell us about how staggered the blades are?

Back: 
- A stage designed with a low value of 𝜙 generally implies highly staggered blades with the relative flow angles close to tangential. 
- High values imply low stagger and flow angles closer to axial.

$$ \begin{align}
\phi &= \frac{V_{x}}{U}
\end{align} $$

- Low value $\to$ near axial flow
- High value $\to$ near tangential flow

![[Pasted image 20230527181855.png]]
<!--ID: 1685355946862-->
END_CARD


--------

START_CARD
Basic

Why do we need to operate turbomachinery over a narrow range of flow coefficients?

Back: 
- For blades to operate effectively the flow incidence angle on the leading edge should be near zero
- The flow coefficient measures to some extent the angle of the flow
- If the flow coefficient is changing from it's design value then the turbomachinery is probably not going to have good incidence on it's flow and loose efficiency
<!--ID: 1685355946875-->
END_CARD


--------

START_CARD
Basic

Using the context of flow coefficient, why do we narrow the cross section of the compressor?

Back: 
- In a multistage axial flow compressor flow radius is constant(ish), so blade speed ($U$) is constant(ish) for the same spool
- To keep the flow coefficient at it's design value we therefor need to keep $V_{x}$ constant
- Between stages the flow density increases (compressed, duh), which if cross section is constant then axial velocity will drop
- To compensate for this we reduce the cross section, meaning $V_{x}$ is constant(ish) and flow coefficient is constant(ish)
- Since area drops blade height will obviously also drop.
<!--ID: 1685355946888-->
END_CARD



--------

START_CARD
Basic

State the equation and variable names for the stage loading coefficient. (turbomachines)

Back: 
$$ \begin{align}
\psi &= \frac{\Delta h_{0}}{U^{2}}
\end{align} $$

- $\psi$ is stage loading coefficient
- $\Delta h_{0}$ is stagnation enthalpy
- $U$ is blade speed
<!--ID: 1685355946900-->
END_CARD


--------

START_CARD
Basic

What does the following equation tell you about the meaning of stage loading coefficient?

$$ \begin{align}
\Delta h_{0}= U V_{x} ( &\tan \alpha_{3} - \tan \alpha_{2}) & &\to & \frac{\Delta h_{0}}{U^{2}}=  \frac{V_{x}}{U} ( &\tan \alpha_{3} - \tan \alpha_{2})
\end{align} $$

Back: 
$$ \begin{align}
\frac{\Delta h_{0}}{U^{2}} &=  \frac{V_{x}}{U} (  \tan \alpha_{3} - \tan \alpha_{2})\\
\psi &=  \phi (  \tan \alpha_{3} - \tan \alpha_{2})
\end{align} $$
- We know that $\phi$ is flow coefficient (a measure of how tangential the flow is)
- The magnitude of $(  \tan \alpha_{3} - \tan \alpha_{2})$ will increase as the exit angles from the blades increases
- So $\psi$ describes the indidence angle times the deflection angle, which is a measure of how much the blades are deflecting the flow
- Hence low stage loading implies low deflection of flow and the blades extracting/inputting little energy
- High stage loading would imply the opposite
<!--ID: 1685355946912-->
END_CARD


--------

START_CARD
Basic

Write a simple expression for stage loading coefficient. Describe how it's derived. Then describe what it implies about stage loading.

Back: 
- This equation is derived using the defenition of stage loading and eulers equation
$$ \begin{align}
\psi = \frac{\Delta V_{\theta}}{U}
\end{align} $$
- This equation shows that high loading implies a high Δ𝑉𝜃, and hence blades with a large amount of flow turning
- High stage loading means doing more with less machinery and is desirable
<!--ID: 1685355946927-->
END_CARD



--------

START_CARD
Basic

Where is the highest Mach number in a compressor?  How does this influence design?

Back: 
$$ \begin{align}
c &= \sqrt{k R T}
\end{align} $$

- We know that (for a perfect gas) speed of sound increases with temperature (this is also the case for real gases)
- Speed of sound will be increasing through the compressor.
- Since the max speed of the gas can be approximated to be constant, the highest mach numbers will be seen at the intake.
- Supersonic effects set an upper limit on flow rates related to choking fan blades.
- For practical reasons the relative mach number onto the fan tip is kept below Mach 1.6, with axial mach number about 0.6:
	- Bird strikes
	- Limiting noise
<!--ID: 1685355946941-->
END_CARD



--------

START_CARD
Basic

Consider a turbojet engine in flight at sea level (T=288 K, p=1.01 bar) and Mach 0.8. Due to flow divergence in the engine inlet, the flow enters the first compressor rotor at Mach 0.6. Assume there is no inlet guide vane and therefore no swirl in the flow entering the first rotor. If the designer has specified a mid-span flow coefficient of 0.55 for the first stage, determine the mid-span blade speed.

Back: 
![[Pasted image 20230529104340.png]]

- Assume a perfect gas, assume isentropic compression, find the temperature before the fan then using a mach number relation:
$$ \begin{align}
T_{02} &= T_{atm} \left( 1 + \frac{\gamma-1}{2} M^{2} \right) & &\to & T_{02} &=288 \left( 1 + \frac{1.4-1}{2} 0.6^{2} \right) = 324.9K
\end{align} $$
- Note that all velocity is axial $V=V_{x}$ since there is no swirl. So then we can use the following mach relation:
$$ \begin{align}
\frac{V}{\sqrt{c_{p} T_{0}}} &= \sqrt{\gamma -1}  M \left( 1 + \frac{\gamma-1}{2} M^{2} \right)^{-\frac{1}{2}} & &\to & V_{x}   &= \sqrt{c_{p} T_{02}(\gamma -1)}  M \left( 1 + \frac{\gamma-1}{2} M^{2} \right)^{-\frac{1}{2}}\\
&& && &= \sqrt{1005\times 324.9\times(1.4-1)} 0.6 \left( 1 + \frac{1.4-1}{2} 0.6^{2} \right)^{- \frac{1}{2} }\\
&& && &= 209.4\: m/s
\end{align} $$
- Now to get mid-span blade speed ($U$) we can make use of $\phi$ which we've been given:
$$ \begin{align}
\phi &= \frac{V_{x}}{U} & &\to & U &= \frac{V_{x}}{\phi} \\
&& && &= \frac{209.4}{0.55}=\underline{380.8\: m/s}
\end{align} $$
<!--ID: 1685355946955-->
END_CARD


--------

START_CARD
Basic

Consider a turbojet engine in flight at sea level, with mid-span blade speed of 380.8 m/s and inlet temperature of 324.9K, the multi-stage compressor has an overall total pressure ratio of 10:1. Assuming that the designer has decided that the upper limit for the mid-span stage loading coefficient should be 0.4, determine the minimum number of stages required.

Back: 
- Loading coefficient should maximum 0.4:
$$ \begin{align}
\psi &= \frac{\Delta h_{0,stage}}{U^{2}} \leq 0.4 & &\to & \psi U^{2} = \Delta h_{0,stage}  &\leq 0.4 U^{2}\\
&& &&  \Delta h_{0,stage}  &\leq 0.4 \times 380.8^{2}\\
&& &&  \Delta h_{0,stage}  &\leq 58003 \:J/kg
\end{align} $$
- Deriving a formula for temperature change interms of pressure ratio of isentropic compression of a perfect gas:
$$ \begin{align}
  \frac{T}{p^{\frac{\gamma-1}{\gamma}}} &= k &&\to& \frac{T_{02}}{p_{02}^{\frac{\gamma-1}{\gamma}}} &= \frac{T_{03}}{p_{03}^{\frac{\gamma-1}{\gamma}}}   &&\to& \frac{p_{03}}{p_{02}}^{\frac{\gamma-1}{\gamma}} &= \frac{T_{03}}{T_{02}}    \\&&&&&&&& T_{02}\text{PR}^{\frac{\gamma-1}{\gamma}} &= T_{03} 
\end{align} $$

- Deriving a formula for isentropic static entropy change using pressure ratio:

$$ \begin{align} 
\Delta h_{0,total} &= c_{p} (T_{03} - T_{02}) & &\to & \Delta h_{0,total} &= c_{p}T_{02} \left( \text{PR}^{\frac{\gamma-1}{\gamma}} - 1\right)\\
&& && &= 1005 \times 324.9\times \left( 10^{\frac{1.4-1}{1.4}} - 1 \right)\\
&& && &= 303895 \: J/kg
\end{align} $$

- Then determining the number of stages needed to get this change:
 $$ \begin{align}
\frac{\Delta h_{0,total}}{\Delta h_{0,stage}} = \frac{303895}{58003} = &5.23\\
&\therefore \text{need 6 compression stages}
\end{align} $$
<!--ID: 1685355946967-->
END_CARD

 






