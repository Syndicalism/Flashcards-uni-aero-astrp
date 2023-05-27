TARGET_DECK: Propulsion::9 Turbomachinery part 1




START_CARD
Basic

Derive the Euler work equation. (Turbomachines)

Back: 
![[Pasted image 20230527135534.png]]
- Consider the change in angular momentum of the fluid between the input and output along a streamline:
$$ \begin{align}
 \dot{m} r_{2} V_{\theta 2} - \dot{m} r_{1} V_{\theta 1} & &\to & & \dot{m} (r_{2} V_{\theta 2} -  r_{1} V_{\theta 1})
\end{align} $$
- This will require a amount of torque to impart (conservation of energy):
$$ \begin{align}
T &= \dot{m} (r_{2} V_{\theta 2} -  r_{1} V_{\theta 1})
\end{align} $$
- The equation relating power and torque is $P=T \omega$, applying that:
$$ \begin{align}
\dot{W}_{x} &= T\Omega & U &=\Omega r \\
&= \dot{m} (r_{2} V_{\theta 2} -  r_{1} V_{\theta 1})\Omega & &\to & \dot{W}_{x} &= \dot{m} (U_{2} V_{\theta 2} -  U_{1} V_{\theta 1}) \\

\end{align} $$

- Noting that $U$ is equal to the speed of the rotor. Then take SFEE and apply it to this situation:
$$ \begin{align}
\dot{Q} - \dot{W}_{out} &= \Delta H_{0} & \text{Ad}&\text{iabatic}\\ &= \dot{m}(\Delta h_{0}) & &\to & \dot{W}_{in}&= \dot{m}(\Delta h_{0})
\end{align} $$

- Finally combining get's the thing interms of stagnation enthalpy:
$$ \begin{align}
 \dot{m}(\Delta h_{0}) &= \dot{m} (U_{2} V_{\theta 2} -  U_{1} V_{\theta 1}) & &\to & \Delta h_{0}  &= U_{2} V_{\theta 2} -  U_{1} V_{\theta 1} 
\end{align} $$
<!--ID: 1685200388379-->
END_CARD


--------


START_CARD
Basic

What is the equation relating torque and power?

Back: 
$$ \begin{align}
P &= T\omega
\end{align} $$
<!--ID: 1685200388391-->
END_CARD

--------

START_CARD
Basic

What is swirl velocity and it's symbol?

Back: 
- It is the velocity of a gas in the direction of rotation ($V_{\theta}$), aka it's tangential velocity component.
<!--ID: 1685200388404-->
END_CARD




--------

START_CARD
Basic

Simplify this equation using an assumption:
$$ \begin{align}
\Delta h_{0}  &= U_{2} V_{\theta 2} -  U_{1} V_{\theta 1}
\end{align} $$ 
Back: 
- Assume no change in radius ($r_{1} = r_{2}$):
$$ \begin{align}
\Delta h_{0}  &= U_{2} V_{\theta 2} -  U_{1} V_{\theta 1} & &\to &  \Delta h_{0}  &= U( V_{\theta 2} -   V_{\theta 1} )
\end{align} $$
<!--ID: 1685200388416-->
END_CARD




--------

START_CARD
Basic

Sketch the key velocity vectors on an impeller diagram. Then briefly describe them.

Back: 
![[Pasted image 20230527142214.png]]

- $V_{\theta2}$ is the velocity imparted on the exit gas in the direction of rotation (swirl velocity)
- $V_{2}$ is the exit velocity vector
- $V_{2}^{rel}$ is the exit velocity in the impellers reference frame, which is equivalent to the $V_{r2}$ (radial velocity) assuming no axial velocity
<!--ID: 1685200388429-->
END_CARD


--------

START_CARD
Basic

What is the expression for swirl velocity of an impeller? 

Derive an expression for work required.

Back: 
$$ \begin{align}
V_{\theta\:out} &= r \Omega
\end{align} $$

- Starting with the equation for shaft torque, then applying the context.
$$ \begin{align}
&&V_{\theta 1}&=0&&& \dot{W}&=\Omega T&&& V_{\theta\:out} &= r \Omega\\
T &= \dot{m} (r_{2} V_{\theta 2} -  r_{1} V_{\theta 1}) & &\to &  T &= \dot{m} rV_{\theta\:out}  & &\to &   \dot{W} &= \dot{m}r \Omega V_{\theta\:out}   & &\to &   \dot{W} &= \dot{m} r^{2} \Omega^{2}   
\end{align} $$



![[Pasted image 20230527142214.png]]
<!--ID: 1685200388442-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20230527145535.png]]

Using this diagram label:
- $V$
- $V^{rel}$
- $V_{x}$
- $V_{\theta}$
- $V_{\theta}^{rel}$
- $\alpha$
- $\alpha_{rel}$

For both entering the rotor and exiting the rotor (assume flow comes from the left).

Back: 
![[Pasted image 20230527145831.png]]
<!--ID: 1685200388454-->
END_CARD



--------

START_CARD
Basic

In the context of a axial flow compressor, what is a compressor stage?

Back: 
- A rotor-stator pair responsible for compressing the gas is a compressor stage
<!--ID: 1685200388465-->
END_CARD


--------

START_CARD
Basic

What is the practical max limit on the pressure ratio that can be achieved across a single compressor stage in a axial flow compressor? Why is it that?

Back: 
- Maximum pressure ratio across a single compressor stage is less than 2
- This is due to flow separation occurring on the airfoils as pressure ratio increases
<!--ID: 1685200388477-->
END_CARD


--------

START_CARD
Basic

What is the practical max limit on the pressure ratio that can be achieved across a single compressor stage in a axial flow turbine? Why is it that?

Back: 
- Maximum pressure ratio across a single compressor stage is about 4
- This is due to flow separation occurring on the airfoils as pressure ratio increases
- Since the pressure gradient is favorable (high -> low) the risk of flow speration is reduced allowing greater pressure ratios than in the compressor
<!--ID: 1685200388491-->
END_CARD


--------

START_CARD
Basic

Using a diagram describe the mounting of a stator vs a rotor.

Back: 
Stators are fixed (top), rotors are attached to the shaft.
![[Pasted image 20230527150510.png]]
<!--ID: 1685200388502-->
END_CARD






