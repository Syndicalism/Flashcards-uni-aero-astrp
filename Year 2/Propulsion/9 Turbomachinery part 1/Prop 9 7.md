TARGET_DECK: Propulsion::9 Turbomachinery part 1




--------

START_CARD
Basic

![[Pasted image 20230527171738.png]]

Show the velocity vectors and angles at the exit of each blade:
- Relative velocities
- Absolute velocities
- Relative angles
- Absolute angles
- Translation between relative and absolute vectors

Back: 
![[Pasted image 20230527171911.png]]
<!--ID: 1685355931643-->
END_CARD


--------

START_CARD
Basic

What do we use as justification for drawing the exit velocities from turbine blades as parallel to their camber lines?

Back: 
 The Kutta condition:
 "A body with a sharp trailing edge which is moving through a fluid will create about itself a circulation of sufficient strength to hold the rear stagnation point at the trailing edge."

![[Pasted image 20230527172034.png]]
<!--ID: 1685355931667-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20230527172353.png]]

Show the velocity vectors and angles at the exit of each blade:
- Relative velocities
- Absolute velocities
- Relative angles
- Absolute angles
- Translation between relative and absolute vectors

Back: 
![[Pasted image 20230527172256.png]]
<!--ID: 1685355931680-->
END_CARD


--------

START_CARD
Basic

State the equation relating relative and absolute swirl out of:
- A compressor rotor blade
- A compressor stator blade
- A turbine rotor blade
- A turbine stator blade

Back: 
- A compressor rotor blade: $V_{\theta\:rel} = V_{\theta} - U$
- A compressor stator blade: $V_{\theta\:rel} = V_{\theta} - U$
- A turbine rotor blade: $V_{\theta\:rel} = V_{\theta} - U$
- A turbine stator blade: $V_{\theta\:rel} = V_{\theta} - U$

(They are all the same :trol:)
<!--ID: 1685355931693-->
END_CARD


--------

START_CARD
Basic

State the simplified form of Euler's work equation for a axial turbomachine.

Back: 
$$ \begin{align}
\Delta h_{0} &= U( V_{\theta2} - V_{\theta1} )
\end{align} $$
<!--ID: 1685355931704-->
END_CARD


--------

START_CARD
Basic

Derive this equation:
$$ \begin{align}
\Delta h_{0} &= U V_{x} (\tan \alpha_{3} - \tan \alpha_{2})
\end{align} $$

Back: 
![[Pasted image 20230527173209.png]]

- We start with eulers equation:
$$ \begin{align}
&&\Delta \alpha&=0\\
\Delta h_{0} &= U_{3} V_{\theta3} - U_{2} V_{\theta2} & &\to & \Delta h_{0} &= U(  V_{\theta3} -  V_{\theta2})
\end{align} $$
- Then we assume that the axial velocity is constant ($\Delta V_{x}=0$) and re write $V_{\theta}$ interms of it:
$$ \begin{align}
&& \Delta h_{0} = U(  &V_{\theta3} -  V_{\theta2})\\\\
V_{\theta2} &= V_{x} \tan\alpha_{2} &&\downarrow& V_{\theta3} &= V_{x} \tan\alpha_{3}\\\\
&& \Delta h_{0}= U V_{x} ( &\tan \alpha_{3} - \tan \alpha_{2})
\end{align} $$
<!--ID: 1685355931717-->
END_CARD







