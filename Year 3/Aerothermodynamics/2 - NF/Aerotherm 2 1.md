TARGET_DECK: Aerothermodynamics::2 - NF



START_CARD
Basic

What are oblique shocks?

Back: 
- Shocks that occur at an angle to flow direction
- They are compressive shocks

END_CARD


--------

START_CARD
Basic

Draw a diagram showing a oblique shock on the tip of a cone in a supersonic flow. Labelling key angles and flow features.

Back: 
![[Pasted image 20231117000519.png]]

END_CARD


--------

START_CARD
Basic

In the context of oblique shocks define:
- Turning angle
- Shock angle

Giving their symbols

Back: 

![[Pasted image 20231117000519.png]]

 here:
 $\theta=$ Shock angle, the path of the streamline for most problems we take this as the angle of the objects surface
 $\beta=$ Turning angle ,the angle of the oblique shock

END_CARD


--------

START_CARD
Basic

What does the following equation describe, what name each of it's variables:

$$\begin{align*}   \tan\theta&= 2 \frac{1}{\tan\beta} \left[\frac{M_{1}^{2} \sin^{2}\beta - 1 }{M_{1}^{2}(\gamma + \cos 2\beta)+2}\right]   \end{align*}$$

Back: 
- This equation describes the relationship between an oblique shocks turning angle and shock's angle. Both angles are taken tangentially to $M_{1}$.

- $M=$ Mach number before and after shock 
- $\theta=$ oblique shock turning angle
- $\beta=$ oblique shock shock angle

END_CARD


--------

START_CARD
Basic

What does the following equation describe, what name each of it's variables:
$$ \begin{align}
 M^{2}_{2}  &= \frac{1}{\sin^{2}(\beta-\theta)}   \frac{(\gamma - 1) M^{2}_{1} \sin^{2} \beta + 2}{2\gamma M^{2}_{1} \sin^{2} \beta - (\gamma - 1)}
\end{align} $$

Back: 
- This equation describes how the Mach number changes across a oblique shock

- $M=$ Mach number before and after shock 
- $\theta=$ oblique shock turning angle
- $\beta=$ oblique shock shock angle

END_CARD


--------

START_CARD
Basic

How do you find the $\beta$ of an oblique shock?

Back: 
- You don't try and use the equation since it cant be inversed, instead use a method involving the NST
- You instead interpolate from the Oblique shock chart, finding the shock-wave angle $(\beta)$ which corresponds to your known deflection angle and Mach

![[Pasted image 20231117001641.png]]

END_CARD


--------

START_CARD
Basic

How do you find the Mach across a normal shock, given you know shock angle, turning angle and initial Mach number?

Back: 
- First you get the NORMAL component of the incident Mach velocity vector
$$ \begin{align}
M_{n1} &= M_{1} \sin \beta
\end{align} $$
- Then look up the NORMAL component in the normal shock table, noting the $M_{2}$ (interpolating if needed) this $M_{2}$ will be your $M_{n2}$
- Get the actual $M_{2}$ using geometric relationships:
$$ \begin{align}
M _{2} &= \frac{M _{n2}}{\sin (\beta-\theta)}
\end{align} $$

END_CARD


--------

START_CARD
Basic

How do you find the Mach across a normal shock, given you know turning angle and initial Mach number?

Back: 
- You don't try and use the equation since it cant be inversed, instead use a method involving the NST
- You instead interpolate from the Oblique shock chart, finding the shock-wave angle $(\beta)$ which corresponds to your known deflection angle and Mach

![[Pasted image 20231117001641.png]]

- With the shock angle found we can get Mach change, get the NORMAL component of the incident Mach velocity vector:
$$ \begin{align}
M_{n1} &= M_{1} \sin \beta
\end{align} $$
- Then look up the NORMAL component in the normal shock table, noting the $M_{2}$ (interpolating if needed) this $M_{2}$ will be your $M_{n2}$
- Get the actual $M_{2}$ using geometric relationships:
$$ \begin{align}
M _{2} &= \frac{M _{n2}}{\sin (\beta-\theta)}
\end{align} $$

END_CARD


--------

START_CARD
Basic

Draw a diagram for the geometric relationships for incident and exit Mach vectors on a oblique shock. Labelling ALL key variables.

Back: 
![[Pasted image 20231117002209.png]]

END_CARD


--------

START_CARD
Basic

What is this chart called, state the obvious 4 key observations:

![[Pasted image 20231117003111.png]]

Back: 
This is the oblique shock chart.

- If $\theta<\theta_{max}$ there area 2 solutions for any valid turning angle
- At zero turning angle they have a normal shock solution as well as some $\beta\neq90\degree$ solution.
- The maximum turning angle (at $M=\infty$) is $45\degree$ with high Mach numbers tending towards this value
- There exists a maximum possible turning angle for any Mach number $\theta_{max}$

END_CARD


--------

START_CARD
Basic

What do the coloured lines mean?

![[Pasted image 20231117002729.png]]

Back: 
- The red line describes where we have strong or weak solutions, with those that have $\beta$ angles above $\theta_{max}$ being strong solutions and those below being weak solutions
- The dotted blue line separates where oblique shocks will cause subsonic flow transition, those above will have $M_{2}<1$ while those below will have $M_{2}>1$

END_CARD




--------

START_CARD
Basic

State the equation for the $\beta$ and $\theta$ at the red marks:

![[Pasted image 20231117003208.png]]

Back: 

$$ \begin{align}
\theta &= 0 & \sin\beta &= \sin M_{1}
\end{align} $$

END_CARD


--------

START_CARD
Basic

State the Mach cone equation, name it's variables, draw it's actual meaning.

Back: 
$$ \begin{align}
\sin \mu &= \frac{1}{M}
\end{align} $$
- $\mu=$ Mach angle
- $M=$ Mach number

![[Pasted image 20231117003519.png]]

END_CARD


--------

START_CARD
Basic

What is the tan equation for Mach angle?

Back: 

![[Pasted image 20231117003539.png]]
- From this diagram it can be easily derived:
$$ \begin{align}
\tan \mu &= \frac{1}{\sqrt{M^{2}-1}}
\end{align} $$

END_CARD



--------

START_CARD
Basic

Derive the equation for Mach angle, state it's relationship it oblique shocks.

Back: 
![[Pasted image 20231117003729.png]]

- From this diagram:
$$ \begin{align}
\sin\mu &= \frac{3a\Delta t}{3V\Delta t} = \frac{1}{M}
\end{align} $$

- It can be seen that in this derivation the velocity remains straight to the freestream, hence $\theta_{0}=\theta_{1}=0$
- Recalling the implications for oblique shocks:
$$ \begin{align}
\sin\beta  = \frac{1}{M}
\end{align} $$

END_CARD













