TARGET_DECK: Advanced Astronautics::AA 1

--------

START_CARD
Basic

Sketch the rough voltage bands, state standard bands. What is the max bare conductor before you get space plasma issues?

Back: 
![[Pasted image 20240120144238.png]]
- Standard bands 28, 50, 70, 100, 120, 160, 200
- Above 160V it becomes an issue
<!--ID: 1705761876613-->
END_CARD



--------

START_CARD
Basic

What's the optimum voltage equation?


Back: 


(for spacecraft)
![[Pasted image 20240119123324.png]]
<!--ID: 1705670932732-->
END_CARD


--------

START_CARD
Basic

State the power required based on mass equation

Back: 

A ballpark estimator for spacecraft.
![[Pasted image 20240119123519.png]]
<!--ID: 1705670932741-->
END_CARD



--------

START_CARD
Basic

Sketch the voltage of a battery that's gone from 100% -> 0% -> 100%

Explain why we only use batteries within a certain %range.

Back: 
![[Pasted image 20240119123630.png]]

Most batteries degrade significantly faster when you use them outside of the range 10-90% (or 20% to 80%), some can even become unrechargable if they drop to 0%. So to extend their lifetime and to have it act like a psudo-constant voltage source we generally operate them in that 10-90% range. 
<!--ID: 1705670932747-->
END_CARD


--------

START_CARD
Basic

Sketch the voltage chart for a fuel cell

Back: 
![[Pasted image 20240119123803.png]]
<!--ID: 1705670932755-->
END_CARD


--------

START_CARD
Basic

Sketch the voltage-current relation for a solar cell and the power output. Labelling:
- Open circuit voltage 
- Short circuit current 

Back: 
![[Pasted image 20240119123909.png]]
<!--ID: 1705670932762-->
END_CARD



--------

START_CARD
Basic

Sketch the effect of angle on solar cell power output.

Back: 

(Very) Approximately cos
![[Pasted image 20240119124209.png]]
<!--ID: 1705670932770-->
END_CARD


--------

START_CARD
Basic

Kelly

Back: 
![[Pasted image 20240121145941.png]]
<!--ID: 1705849185368-->
END_CARD



--------

START_CARD
Basic

Sketch how a BOL vs EOL solar cell voltage-current graph looks

Back: 
![[Pasted image 20240119124256.png]]
<!--ID: 1705670932779-->
END_CARD


--------

START_CARD
Basic

Explain unregulated bus DET

Back: 
![[Pasted image 20240119125155.png]]
<!--ID: 1705670932787-->
END_CARD


--------

START_CARD
Basic

Explain fully regulated bus DET

Back: 
![[Pasted image 20240119125236.png]]
<!--ID: 1705670932793-->
END_CARD



--------

START_CARD
Basic

Explain sunlight regulated bus 

Back: 
A sunlight regulated bus optimizes power generation by adjusting solar panels and dynamically managing power consumption based on changing sunlight conditions. Maximizes energy harvesting, making it ideal for missions with variable sunlight exposure.

This is kind of in-between unregulated and fully regulated.
<!--ID: 1705670932801-->
END_CARD





--------

START_CARD
Basic

State the 4 types of DET: 

Back: 
- sunlight regulated bus 
- fully regulated bus
- unregulated bus
- Peak power tracker
<!--ID: 1705670932807-->
END_CARD


--------

START_CARD
Basic

What is PPT and state how transformers effect bus power?

Back: 
![[Pasted image 20240119125513.png]]
<!--ID: 1705670932812-->
END_CARD



--------

START_CARD
Basic

Sketch how the solar cell IV graph changes with decreasing solar intensity

Back: 
![[Pasted image 20240119125651.png]]
<!--ID: 1705670932819-->
END_CARD



--------

START_CARD
Basic

Sketch how photovoltaic efficiency varies with sun intensity, state how this effects design. State the approximate flux for LEO.

Back: 
![[Pasted image 20240119125750.png]]

- Once you pass ~300W/m^2 the reduction in efficiency means extreme losses
- Since this is on top of already reduced output (the lower intensity) the viability of solar is significantly effected
- LEO ~$1400W/m^2$
<!--ID: 1705670932824-->
END_CARD



--------

START_CARD
Basic

State the current for a solar cell at angle $\alpha$, at approximately what angle is it zero? 

Back: 
To achieve greater accuracy a Kelly cosine should be used:
- Beyond $85\degree$ no power is produced
- Beyond $50\degree$ a standard $\cos$ approximation becomes impractical

 $$\begin{align*} I_{s}  &= I_{0} \: \text{KellyCos} (\theta) \approx I_{0} \: \text{cos} (\theta)  \end{align*}$$

- $I_{s}=$ Current at current angle
- $I_{0}=$ Reference current when cell is normal to the sun ($\theta=0$)
- $\theta=$ Angle between cell normal and incident light
<!--ID: 1705670932830-->
END_CARD



--------

START_CARD
Basic

Sketch how increasing temperature effects IV chart for solar cells.

Back: 
![[Pasted image 20240119130411.png]]
<!--ID: 1705670932837-->
END_CARD


--------

START_CARD
Basic

State the relationships used for the current and voltage change due to temp. Comment on how they change with increasing temp.

Back: 
 $$\begin{align*} I_{sc}  &= I_{0} + \alpha \Delta T  \end{align*}$$
 $$\begin{align*} V_{oc}  &= V_{0} + \beta \Delta T  \end{align*}$$
- $I_{sc}=$ [[solar cell terms|cell short circuit current]] at target temp
- $V_{oc}=$ [[solar cell terms|cell open circuit voltage]] at target temp
- $I_{0}=$ [[solar cell terms|cell short circuit current]] at reference temp
- $V_{0}=$ [[solar cell terms|cell open circuit voltage]] at reference temp
- $\alpha=$ temperature coefficient for current
- $\beta=$ temperature coefficient for voltage
- $\Delta T=$ difference from reference to target temp

Generally $\alpha$ and $\beta$ are given by the manufacturer, a common reference temperature is 21C

Increasing temperatures:
- Significantly decrease voltage output
- Slightly increase current output
- Decrease potential max power
<!--ID: 1705670932843-->
END_CARD



--------

START_CARD
Basic

What is the useful effect of eclipses for solar power? Sketch a relevant temp-time chart.

Back: 
Eclipses lead to solar cells cooling down, which means there power output is higher for the short duration after the eclipse ends. This helps to recharge the probably depleated batteries.

![[Pasted image 20240119130811.png]]
<!--ID: 1705670932849-->
END_CARD


--------

START_CARD
Basic

How do we reduce problems caused by local shadows on solar strings? How does it effect the strings IV chart? What's the likely cause of the shadow?

Back: 
- Using bypass diodes a shaded string can still produce the same current (at a reduced voltage)
![[Pasted image 20240119131313.png]]
![[Pasted image 20240119131402.png]]
- Small shadows are likely the result of the spacecraft's own structure casting shadows on itself.
<!--ID: 1705670932856-->
END_CARD


--------

START_CARD
Basic

Sketch how power output from a solar-cell may change over 20 years comparing a high and low rad resistant cell. Commenting on implications.

Back: 
![[Pasted image 20240119132145.png]]
- Generally an equivalent price high resistant cell will have lower output, but given enough exposure it's output might be higher
- Hence depending on mission lifetime we may go for a lower power higher resistance cell
<!--ID: 1705670932863-->
END_CARD






--------

START_CARD
Basic

State the voltage-current equations for solar cell arrangement. State how the values must be rounded.

Back: 

![[Pasted image 20240119132553.png]]

![[Pasted image 20240119132650.png]]
<!--ID: 1705670932870-->
END_CARD




--------

START_CARD
Basic

What is DOD? Given a craft needs 8000 Wh of storage and has a DOD of 0.3, how much capacity does it actually need? How much power does it take to charge them assuming perfect charging efficiency?

Back: 
- DOD -  Depth of Discharge is a measure of the amount of energy that has been taken out of a battery compared to its total capacity.

$$ \begin{align}
\text{Total cell energy} \times \text{DoD} &= \text{Avaliable capacity} &&\to& \frac{\text{Avaliable capacity}}{\text{DoD}} &=\text{Total cell energy} &&\to& \frac{8000}{0.3} &= 26666 \text{Wh}
\end{align} $$
- It only takes 8000 Wh to charge them, since that is the avaliable capacity we use. (Note that if the question says FULLY then it means 0% to 100% aka: talking about TOTAL cell energy not available energy)
<!--ID: 1705674934535-->
END_CARD




--------

START_CARD
Basic

What is solar packing efficiency, what's it's optimal value and effect on power output?

Back: 

$$ \begin{align}
\text{Power output} &= \text{Area} \times \text{Power per cell area} \times \text{Packing efficiency}
\end{align} $$

- This is the fraction of the panel surface that can actually generate energy, since some will have to be taken up by wires, regulators and structural stuff
- We want a packing efficiency of 1 (not really possible)
<!--ID: 1705674934548-->
END_CARD




--------

START_CARD
Basic

State absolute zero.

Back: 
$$ \begin{align}
0\:^{o}K &= -273.15\:^{o}C
\end{align} $$
<!--ID: 1705674934556-->
END_CARD





