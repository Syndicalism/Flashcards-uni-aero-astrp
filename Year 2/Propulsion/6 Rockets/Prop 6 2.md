TARGET_DECK: Propulsion::6 Rockets



START_CARD
Basic

How is the exhaust manipulated in a rocket engine to accelerate it to supersonic speeds?

Back: 
![[Pasted image 20230404143355.png]]
$$\frac{1}{A} \frac{dA}{dx} = \frac{1}{U} \frac{dU}{dx} (Ma^{2} - 1)$$
- The use of a converging diverging nozzle allows for supersonic acceleration of the exhaust (with the working principle behined that nozzle being shown in the equation above)
- This nozzle converts the thermal and pressure energy in the gas into useful KE
END_CARD



--------

START_CARD
Basic

$$ \begin{align}
V_{j} = \sqrt{2 c_{p} T_{0c} \left[1 - \left(\frac{P_{e}}{P_{0c}}\right)^\frac{\gamma-1}{\gamma} \right]}
\end{align} $$
For the equation above:
- Name it's variables
- Describe it's meaning
- State limitiations and applicability
Back: 
- This is the equation for the exhaust velocity out of a rocket engine using an isentropic nozzle and perfect gas
- It shows how exahust velocity can be increased by
	- Maximising temperature
	- MAximising chamber pressure

- $T_{0c}$ is stagnation temperature from the combustion chamger
- $P_{0c}$ is stagnation pressure from the combustion chamger
- $P_{e}$ is environmental pressure
- $V_{j}$ is the exhaust velocity
- $\gamma$ is the specific heat ratio of the exhaust
- $c_{p}$ is the constant pressure specific heat of the exhaust
END_CARD



--------

START_CARD
Basic

How is the following equation derived:
$$ \begin{align}
V_{j} = \sqrt{2 c_{p} T_{0c} \left[1 - \left(\frac{P_{e}}{P_{0c}}\right)^\frac{\gamma-1}{\gamma} \right]}
\end{align} $$

Back: 
![[Pasted image 20230404143355.png]]
- Starting with the following assumptions
	- All processes are isentropic
	- We are using a perfect gas
	- The exhaust is fully expanded such that $P_{e}=P_{A}$
	- The KE of the gas exiting the combustion chamber is negligible
- Using the SFEE we can note that $q=0,w=0$ so it can be rearranged and simplified:
$$ \begin{align}
q-w &= \left(h_{out} + \frac{1}{2} V^{2}_{out}\right) - \left(h_{in} + \frac{1}{2} V^{2}_{in}\right) &&\to &h_{in} - h_{out} &=   \frac{1}{2} (V^{2}_{out} - V^{2}_{in} )\\
&& && h_{c} - h_{e} &=   \frac{1}{2} (V^{2}_{e} - V^{2}_{c} )
\end{align} $$
- Then using the perfect gas relation $\Delta h = c_{p} \Delta T$ we can get an expression for exhaust velocity, note that since the exit velocity from the combustion chamber is negligible $T_{c} = T_{0,c}$ and $V^{2}_{c}=0$:
$$ \begin{align}
h_{c} - h_{e} &=   \frac{1}{2} (V^{2}_{e} - V^{2}_{c} ) &\to&& c_{p} (T_{c} - T_{e}) &=   \frac{1}{2} (V^{2}_{e} - V^{2}_{c} ) &\to&& \sqrt{2c_{p} (T_{0,c} - T_{e})} &= V_{e}
\end{align} $$
- Finally since it is a isentropic nozzle we can use the isentropic relation $T_{e} = T_{0c} \left(\frac{P_{e}}{P_{0c}}\right)^{\frac{\gamma-1}{\gamma}}$ in the equation above:
$$ \begin{align}
V_{e} & =\sqrt{2c_{p} \left(T_{0,c} - T_{0c} \left(\frac{P_{e}}{P_{0c}}\right)^{\frac{\gamma-1}{\gamma}}\right)} & &\to & V_{j} &= \sqrt{2 c_{p} T_{0c} \left[1 - \left(\frac{P_{e}}{P_{0c}}\right)^\frac{\gamma-1}{\gamma} \right]}
\end{align} $$
END_CARD



--------

START_CARD
Basic

Define $I_{sp}$:
- Standard defenition
- Steady state defenition

Back: 
- Specific impulse, it is the total impulse of a mass of propellant divided by the weight of that propellant in the standard acceleration of the earths gravity:
$$ \begin{align}
I_{sp} &= \frac{I_{T}}{g_{0} m_{p}} 
\end{align} $$
- In the steady state where $F$ and $\dot{m}$ are constant:
$$ \begin{align}
I_{sp} &= \frac{F}{g_{0} \dot{m}} 
\end{align} $$
END_CARD



--------

START_CARD
Basic

What does$I_{sp}$ of an engine tell you about it's performance?

Back: 
- It shows how much force can be generated per mass of propleant acting as a sort of efficiency metric
END_CARD



--------

START_CARD
Basic

What is the better version of ISP?

Back: 
- Effective exhaust velocity
- Because why the fuck do we divide by $g_{0}$, it's just an unneeeded earth centric step that is dumb and stupid
- Screw ISP
END_CARD



--------

START_CARD
Basic

Define effective exhaust velocity

Back: 
- This is the exhaust velocity required to give the actual thrust assuming it was uniform (because in reality exhaust velocity will vary for a variety of reasons)
$$ \begin{align}
c_{e} &= \frac{F}{\dot{m}}
\end{align} $$
END_CARD



--------

START_CARD
Basic

What is the relationship between effective exhaust velocity and specific impulse?

Back: 
$$ \begin{align}
c_{e} &= \frac{F}{\dot{m}} & & & I_{sp} &= \frac{F}{g_{0} \dot{m}}\\
&& \therefore c_{e} &= \frac{I_{sp}}{g_{0}}
\end{align} $$
END_CARD



--------

START_CARD
Basic

What is the following equation and name it's variables:
$$ \begin{align}
C^{*} &= \frac{P_{c}A_{t}}{\dot{m}} 
\end{align} $$

Back: 
- It is the equation of characteristic velocity. This is a measure of velocity through the throat of the nozzle (note it isn't equivalent to the velocity through the nozzle)
- $C^{*}$ is the characteristic velocity
- $P_{c}$ is combustion chamber exit temperature
- $A_{t}$ is the are of the throat
- $\dot{m}$ is the mass flow rate though the throat
END_CARD



--------

START_CARD
Basic

Can down stream conditions effect the characteristic velocity of a rocket?

Back: 
- If the nozzle is operating correctly it is choked
- Since it is supersonic past the throat downstream information cannot propagate backwards
- Downstream conditions cannot effect characteristic velocity of a correctly functioning rocket
- Note that in the event it does  not achieve supersonic flow then it can be influenced by downstream conditions
END_CARD



--------

START_CARD
Basic

What is the following equation and name it's variables:
$$ \begin{align}
C_{F} &= \frac{F}{P_{c} A_{t}} 
\end{align} $$

Back: 
- This is the equation for nozzle thrust coefficient which is a measure of nozzle performance
- $C_{F}=$  nozzle thrust coefficient
- $F=$  nozzle thrust coefficient
- $P_{c}$ is combustion chamber exit temperature
- $A_{t}$ is the are of the throat
END_CARD


--------

START_CARD
Basic

How can effective exhaust velocity be calculated from characteristic velocity and nozzle thrust coefficient?

Back: 
- Simply multiply them together:
$$ \begin{align}
C_{F} &= \frac{F}{P_{c} A_{t}} & & & C^{*} &= \frac{P_{c}A_{t}}{\dot{m}} \\
&&  C_{F}  C^{*} &= \frac{F}{P_{c} A_{t}}\frac{P_{c}A_{t}}{\dot{m}}\\
&&  &=  \frac{F}{\dot{m}}\\
&& C_{F}  C^{*}  &=  c_{e}
\end{align} $$
END_CARD


--------

START_CARD
Basic

What is the symbol for:
-  characteristic velocity
- nozzle thrust coefficient

Back: 
-  characteristic velocity is $C^{*}$
- nozzle thrust coefficient is $C_{F}$
END_CARD




