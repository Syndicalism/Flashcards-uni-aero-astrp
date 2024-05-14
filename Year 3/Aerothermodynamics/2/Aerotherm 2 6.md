TARGET_DECK: Aerothermodynamics::2



START_CARD
Basic

What is the significance of this equation?
$$ \begin{align}
\frac{dA}{A}  &= (M^{2} - 1) \frac{dV}{V} 
\end{align} $$

Back: 
![[Pasted image 20231218135901.png]]

- So if we break down the implications of the equation when Mach is less than 1, it tells us that for subsonic flows velocity decreases with area increase.
- But the moment Mach number exceeds 1 we get something truly insane, increased area leads to increasing flow speed. 
- This process gives us a mechanism to convert pressure and temperature into velocity which is an incredibly useful form of energy! Opening up a huge realm of [[hell yeah fuck entropy|possibilities]], a critical one being the converging diverging nozzle.

<!--ID: 1703587215130-->
END_CARD


--------

START_CARD
Basic

What does this equation mean? Name it's terms.

$$\begin{align*} \frac{A}{A*}  &= \frac{1}{M} \left[ \frac{2}{\gamma+1} \left(1+ \frac{\gamma-1}{2} M^{2}\right) \right]^{\frac{\gamma+1}{2(\gamma-1)}} \end{align*}$$

Back: 
- $A=$ Area at some point
- $A*=$ critical area (area at nozzle throat, where $M=1$)
- $M=$ Mach number at some point
- $\gamma=$ [[specific heat ratio]]
- This equation relates throat area to nozzle area, predicting the area needed to get a desired Mach value
- It assumes that this is downstream of a supersonic choked nozzle
<!--ID: 1703587215144-->
END_CARD


--------

START_CARD
Basic

How can you find the Mach number downstream of a choked nozzle of area $A$, given the throat area $A^*$?

Back: 
- First calculate $A/A^*$ 
- Then find the Mach number related to that from the isentropic flow table
<!--ID: 1703587215158-->
END_CARD



--------

START_CARD
Basic

Sketch the pressure change and Mach change for the nozzle:

![[Pasted image 20231218140622.png]]

Back: 
![[Pasted image 20231218140638.png]]
<!--ID: 1703587215171-->
END_CARD



--------

START_CARD
Basic

What is this equation, name it's terms and usage.

$$\begin{align*} \dot{m}  &= p_{0}  A^{*} \sqrt{\frac{\gamma}{RT_{0}}} \left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}} \end{align*}$$

Back: 
- $\dot{m} =$ mass flow rate
- $p_{0}=$ [[stagnation pressure]]
- $T_{0}=$ [[stagnation points in a compressible flow|stagnation temp]]
- $A*=$ throat area
- $\gamma=$ [[specific heat ratio]]
- This is the equation for mass flowrate though a choked throat
- It is derived from perfect gas assumptions (speed of sound is a function of only stagnation temp)
- Additionally we assume isentropic relations, hence mass flow at $M=1$ is a function of initial stagnation density (pressure) and stagnation  temperature only
<!--ID: 1703587215183-->
END_CARD


--------

START_CARD
Basic

Explain flow state 1.

![[Pasted image 20231218141055.png]]

Back: 
- Zero flow
- Since there is no flow through the nozzle, the pressures don't change hence the flat line for pressure across the nozzles length.
<!--ID: 1703587215196-->
END_CARD


--------

START_CARD
Basic

Explain flow state 2.

![[Pasted image 20231218141055.png]]

Back: 
- Completely subsonic flow
- The flow doesn't exceed Mach 1 at any point in the nozzle, assuming some friction we can expect the output pressure to be slightly lower due to losses.
<!--ID: 1703587215205-->
END_CARD



--------

START_CARD
Basic

Explain flow state 3.

![[Pasted image 20231218141055.png]]

Back: 
- Only supersonic at throat
- For this to occur the back pressure must equal the critical pressure. In which case since the Mach number is 1, the "[[normal shock properties equations|normal shock]]" which occurs is barely a true shock (since there is no/negligible entropy increase). This results in a similar result to what's seen in 2.
<!--ID: 1703587215213-->
END_CARD


--------

START_CARD
Basic

Explain flow state 4.

![[Pasted image 20231218141055.png]]

Back: 
- Normal shock within diverging region
- Here the back pressure exceeds the flow pressure within the diverging region. Here Mach number has exceeded 1 so the entropy increase will be significant across the corresponding [[normal shock properties equations|normal shock]]. This results in terrible loss of efficiency.
<!--ID: 1703587215221-->
END_CARD




--------

START_CARD
Basic

Explain flow state 5.

![[Pasted image 20231218141055.png]]

Back: 
- Normal shock within diverging region
- Here the back pressure exceeds the flow pressure within the diverging region. Here Mach number has exceeded 1 so the entropy increase will be significant across the corresponding [[normal shock properties equations|normal shock]]. This results in terrible loss of efficiency. 
<!--ID: 1703587215229-->
END_CARD

--------

START_CARD
Basic

Explain flow state 5.

![[Pasted image 20231218141055.png]]

Back: 
- Normal shock at exit
- Although nearly ideal, the consequences are basically identical to what was seen in point 4. It's actually worse considering the higher Mach number will mean even greater entropy increases.

END_CARD





--------

START_CARD
Basic

Explain flow state 6.

![[Pasted image 20231218141055.png]]

Back: 
- Over expanded exhaust
- Here we have supersonic flow exiting the nozzle, but as it exits it falls below ambient pressure leading to a complex series of shocks and expansions. Although generally still practical it is still sub optimal as the excessive shocks lead to loss of useful energy.
<!--ID: 1703587215241-->
END_CARD



--------

START_CARD
Basic

Explain flow state 7.

![[Pasted image 20231218141055.png]]

Back: 
- At design condition
- Here supersonic flow is once again exiting the nozzle, in this case it continues in the supersonic regime and "smoothly" mixes with the atmosphere. Here we reach optimal efficiency as the lack of shock formation minimises entropy.
<!--ID: 1703587215250-->
END_CARD



--------

START_CARD
Basic

Explain flow state 8.

![[Pasted image 20231218141055.png]]

Back: 
- Under expanded exhaust
- Here we have supersonic flow exiting the nozzle, but as it exits it falls above ambient pressure leading to a complex series of shocks and expansions. Although generally still practical it is still sub optimal as the excessive shocks lead to loss of useful energy.
<!--ID: 1703587215258-->
END_CARD




--------

START_CARD
Basic

Why is there efficiency losses in 6 and 8, since information can't back propagate in supersonic flows there should be no effect on upstream performance?

![[Pasted image 20231218141055.png]]

Back: 
- consider what was described with subsonic boundary layers in [[simple observation of oblique shocks in viscous flows]]. 
- This is the mechanism for information back propagation in cases 6 and 8. 
- The subsonic boundary layer allows inefficiency causing phenomena to negatively effect performance within the nozzle.
- Viscosity must be considered for this effect to manifest
<!--ID: 1703587215266-->
END_CARD






