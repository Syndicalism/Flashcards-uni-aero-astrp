TARGET_DECK: Propulsion::6 Rockets



START_CARD
Basic

Define:
- Payload mass
- Propellant mass
- Deadweight mass
- Initial mass
- Burnout mass

And state their symbols.

Back: 
- Payload mass - $m_{pl}$ - The mass of payload being delivered by this stage
- Propellant mass - $m_{p}$ - The mass of the propellant of the stage before any is used
- Deadweight mass - $m_{dw}$ - The mass of structure of the stage, also called structure mass
- Initial mass - $m_{0}$ - The total mass of the stage + payload before any propellant is used
- Burnout mass - $m_{bo}$ - The mass of the stage+payload once all propellant in the stage is used

END_CARD


--------

START_CARD
Basic

Define the following equation and name it's variables:
$$ \begin{align}
\text{MR} &= \frac{m_{0}}{m_{bo}}
\end{align} $$

Back: 
- This is the equation for a rockets mass ratio, which is the ratio of initial mass to burnout mass. It will always be greater than 1.
- $\text{MR}$ is rocket mass ratio
- $m_{0}$ is initial mass
- $m_{bo}$ is burnout mass

$$ \begin{align}
\text{MR} &= \frac{m_{0}}{m_{bo}}= \frac{m_{bo}+m_{p}}{m_{bo}}
\end{align} $$

END_CARD


--------

START_CARD
Basic

What is the equation for payload mass to initial mass ratio?

Back: 
$$ \begin{align}
{\lambda} &= \frac{m_{pl}}{m_{0}} = \frac{\text{payload mass}}{\text{initial mass}}
\end{align} $$
- ${\lambda}$ is the symbol for payload mass to initial mass

END_CARD


--------

START_CARD
Basic

What is the equation for deadweight mass to initial mass ratio?

Back: 
$$ \begin{align}
{\delta} &= \frac{m_{dw}}{m_{0}} = \frac{\text{deadweight mass}}{\text{initial mass}}
\end{align} $$
- ${\delta}$ is the symbol for deadweight mass to initial mass ratio

END_CARD



--------

START_CARD
Basic

$$ \begin{align}
\text{MR} = \frac{1}{\lambda + \delta}
\end{align} $$
Name the variables in the equation above
Back: 
- ${\delta}$ is the symbol for deadweight mass to initial mass ratio
- ${\lambda}$ is the symbol for payload mass to initial mass
- $\text{MR}$ is rocket mass ratio

END_CARD





--------

START_CARD
Basic

$$ \begin{align}
\Delta V_{\text{ideal}} = c_{e} \ln \left(\frac{m_{0}}{m_{bo}}\right) = c_{e} \ln \left(\frac{1}{\lambda + \delta}\right) = c_{e} \ln \left(\text{MR}\right)
\end{align} $$
For the equation above:
- Name it's variables
- Describe it's meaning
- State limitations and applicability
Back: 
- This is the rocket equation which gives velocity change as a function of mass change
- ${\delta}$ is  deadweight mass to initial mass ratio
- ${\lambda}$ is  payload mass to initial mass ratio
- $\text{MR}$ is rocket mass ratio
- $m_{0}$ is initial mass
- $m_{bo}$ is burnout mass
- $c_{e}$ is effective exhaust velocity
- $\Delta V_{\text{ideal}}$ is the ideal change in velocity due to thrust
- This equation assumes that there are no forces acting on the rocket other than thrust but apart from that makes no assumptions

END_CARD




--------

START_CARD
Basic

What are the variables in the following equation and what is it describing?
$$ \begin{align}
\Delta V &= c_{e} \ln\left(\frac{m_{0}}{m_{b0}}\right) - \int^{t}_{0} g \sin\psi \: dt - \int^{t}_{0} \frac{D}{m} \: dt
\end{align} $$
Back: 
- This is the rocket equation after accounting for gravity and drag losses
- $m_{0}$ is initial mass
- $m_{bo}$ is burnout mass
- $m$ is instantaneous mass of the rocket
- $c_{e}$ is effective exhaust velocity
- $\Delta V$ is the change in velocity due to thrust
- $g$ is local gravitational acceleration
- $\psi$ is the angle between the direction of thrust and the normal to the direction of gravity (upright it is $90\degree$)
- $D$ is the force of drag

END_CARD


--------

START_CARD
Basic

What can be done to minimise the effect of gravity drag?

Back: 
$$ \begin{align}
(\Delta V)_{g} &= \int^{t}_{0} g \sin\psi \: dt
\end{align} $$
To decrease it you can:
- Fly at a shallow angle
- Decreasing the time spent during a burn
- Decrease the period of the burn in high gravity area's (be high)

END_CARD



--------

START_CARD
Basic

What can be done to minimise the effect of drag drag?

Back: 
$$ \begin{align}
(\Delta V)_{D} &= \int^{t}_{0} \frac{D}{m} \: dt
\end{align} $$
To decrease it you can:
- Decreasing the time spent during a burn
- Fly slowly through regions of high density
	- To achieve this you may want to fly vertically for the fastest decrease in air density

END_CARD





--------

START_CARD
Basic

What is a gravity turn?

Back: 
- In practice, launches start vertically with relatively low speeds and accelerations, which occurs quite naturally because the mass is highest at lift-off. 
- After that, the angle ψ is reduced quite rapidly to reduce gravity losses in a manoeuvre called a gravity turn.

END_CARD



--------

START_CARD
Basic

Why don't we make everything an SSTO?

Back: 
$$ \begin{align}
\Delta V_{\text{ideal}} = c_{e} \ln \left(\frac{m_{0}}{m_{bo}}\right) 
\end{align} $$
- The rocket equation shows us that we get diminishing returns for just adding more fuel, in the context of gravity eventually "more fuel" just doesn't help
- By introducing staging and dumping unneeded components (empty tanks, engines ect) we can overcome this issue

END_CARD



--------

START_CARD
Basic

What is the following equation, name all it's variables.
$$ \begin{align}
\lambda_{i} &= \exp\left( - \frac{\Delta V_{i}}{c_{e,i}} \right) - \delta_{i}
\end{align} $$

Back: 
- This equation describes the payload mass to initial mass ratio that can be achieved for a specific non dimensionalised rocket.
- $\lambda_{i}$ is payload mass to initial mass ratio for stage $i$ 
- ${\delta_{i}}$ is  deadweight mass to initial mass ratio for stage $i$
- $\Delta V_{i}$ is the delta V that is achieved by stage i
- $c_{e,i}$ is the effective exhaust velocity for stage i

END_CARD


--------

START_CARD
Basic

Why don't we just keep adding stages forever? What number of stages provides the largest performance improvement?

Back: 
![[Pasted image 20230404164514.png]]
- Consecutive stages need to carry each other, so the first one must be larger than the second ect
- This results in an exponential relationship as stage size increases, which is how you get absolutely ridiculous rockets like the Saturn 5
- Additionally stages provide lots of added complexity
- The largest improvement in performance comes from going from 1 to 2 stages, as you'd expect due to diminishing returns with additional staging

END_CARD



--------

START_CARD
Basic

How can total payload to initial mass ratio be calculated using a the payload to initial mass ratio's of the rockets constituent stages?

Back: 
- By multiplying them together:
$$ \begin{align}
\lambda &= \lambda_{1} \times \lambda_{2} \times \lambda_{3} \times ... \times \lambda_{n}
\end{align} $$

END_CARD



