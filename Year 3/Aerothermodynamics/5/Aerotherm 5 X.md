TARGET_DECK: Aerothermodynamics::5

---

START_CARD
Basic

Define Nusselt number, Reynolds number and Prandtl number and specify how they are related in Reynolds analogy.

Back: 

$$\begin{align*}\text{Nu}  &=  \text{St} \cdot \text{Re} \cdot\text{Pr}&&& \text{Re}  &= \frac{VL}{\nu} &&& \text{Nu}  &= \frac{hL}{k} &&& \text{St}  &= \frac{h}{\rho V c_{p}} &&& \text{Pr}  &= \frac{c_{p} \mu}{k}\end{align*}$$

- The Nusselt number (Nu), Reynolds number (Re), and Prandtl number (Pr) are dimensionless quantities used in fluid mechanics and heat transfer. 
- They are related in the context of the Reynolds analogy, which is an empirical correlation that relates heat transfer and momentum transfer in a fluid flow. Giving Nu as a function of Re, St and Pr.
<!--ID: 1704396485191-->
END_CARD


--------

START_CARD
Basic

State reynolds number.

Back: 
$$ \begin{align}
Re &= \frac{VL}{\nu} = \frac{VL\rho}{\mu}
\end{align} $$
<!--ID: 1704434916003-->
END_CARD


--------

START_CARD
Basic

State nusselt number

Back: 
$$ \begin{align}
Nu &= \frac{hL}{k}
\end{align} $$
<!--ID: 1704436012474-->
END_CARD



--------

START_CARD
Basic

Define Prantyl number

Back: 
$$ \begin{align}
Pr &= \frac{c_{p}\mu}{k}
\end{align} $$
<!--ID: 1704436012484-->
END_CARD


--------

START_CARD
Basic

State Fourier number and use it in a 1D discretised unsteady system

Back: 

Start from:
![[Pasted image 20240112165035.png]]
Subbing in everything we get:
![[Pasted image 20240112165113.png]]
<!--ID: 1705093453637-->
END_CARD


--------

START_CARD
Basic

State the stability criteria for the 1D unsteady system

Back: 
Stable if:
![[Pasted image 20240112165154.png]]
<!--ID: 1705093453646-->
END_CARD


--------

START_CARD
Basic

State the 3 forms of 1D heat conduction

Back: 
$$ \begin{align}
\dot{Q} &= (\Delta T) \frac{kA}{L} =(\Delta T) \frac{1}{R}  &&& \dot{q} &= (\Delta T) \frac{k}{L} =(\Delta T) \frac{1}{AR}    
\end{align} $$
<!--ID: 1705093453653-->
END_CARD


--------

START_CARD
Basic

State conductive resistance

Back: 
$$ \begin{align}
R &= \frac{L}{kA}
\end{align} $$
<!--ID: 1705093453662-->
END_CARD


--------

START_CARD
Basic

State the convection heat transfer equation and resistance

Back: 
$$ \begin{align}
\dot{Q}  &= hA \:\Delta T &&& \dot{q}  &= h \:\Delta T &&& R &= \frac{1}{hA}
\end{align} $$
<!--ID: 1705093453669-->
END_CARD


--------

START_CARD
Basic

State the emissivity equation

Back: 
$$ \begin{align}
\dot{Q} &= \varepsilon \sigma T^{4} A &&& \dot{q} &= \varepsilon \sigma T^{4} 
\end{align} $$
<!--ID: 1705093587775-->
END_CARD




--------

START_CARD
Basic

State the general form of Reynolds analogy.

Back: 
![[Pasted image 20240113140848.png]]
<!--ID: 1705154935803-->
END_CARD









