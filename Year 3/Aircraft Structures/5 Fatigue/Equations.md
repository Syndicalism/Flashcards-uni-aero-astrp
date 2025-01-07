TARGET_DECK: Aircraft Structures::5 Fatigue

Goodman thin


--------

START_CARD
Basic

State the differential equation for gust integration

Back: 
![[Pasted image 20240516160211.png]]
- Note the $U_{f}$ is the minimum gust intensity at which there is no risk of failure
<!--ID: 1716056929388-->
END_CARD




--------

START_CARD
Basic

Write the equation for gust exceedance

Back: 
![[Pasted image 20240518163929.png]]
<!--ID: 1716056929396-->
END_CARD




--------

START_CARD
Basic

State goodmans equation.

Back: 
![[Pasted image 20240516135925.png]]
- $S_{a}$ stress amplitude
- $S_{a0}$ equivalent zero mean stress amplitude
- $S_{m}$ mean stress
- $S_{t}$ ultimate tensile stress
- $m$ some imperial constant, approximately 1
<!--ID: 1716056929404-->
END_CARD




---



START_CARD
Basic

What is that cringe equation to do with latitiude and gusts, how do you use it what does it take in? How do you change it for full load cycles.

Back: 

$$ \begin{align}
\frac{n}{l_{10}} R &= T_{gusts} &&& E= \frac{n}{2l_{10}}
\end{align} $$
- $n$ is the number of gusts above velocity $U$, relative to 10 feet per second (found from chart)
- $l_{10}$ the distance between 10 feet per second gusts encountered at altitude $H$ (found from chart)
- $R$ the total distance travelled
- $T_{gusts}$ the number of gusts encountered
- For fatigue calculations you divide by 2!
<!--ID: 1716056929411-->
END_CARD


--------

START_CARD
Basic

State miners rule and how to use it.

Back: 
![[Pasted image 20240516140426.png]]
- $N_{i}$ the total number of cycles at stress level $i$ to cause failure
- $n_{i}$ the current number of cycles at stress level $i$
- Summing these up, when the value is 1 the material will fail
- This permits estimating the life of a component considering stresses at different intensities
<!--ID: 1716056929418-->
END_CARD



--------

START_CARD
Basic

Aircraft component equation lifetime.

Back: 
![[Pasted image 20240516141725.png]]

- $S_{a}$ stress cycle amplitude
- $S_{\infty}$ the stress that can be resisted forever without failure
- $c$ a constant related to the component
- $N$ cycles till failure
- $k_{n}$ scatter factor, accounts for uncertainty from "insufficient" testing
<!--ID: 1716056929425-->
END_CARD


--------

START_CARD
Basic

Explain
![[Pasted image 20240516142022.png]]

Back: 
- Total damage to aircraft
- Damage due to ground->air->ground cycles
- Damage due to gusts
- Damage from other stuff, eg breaking, manovres
<!--ID: 1716056929433-->
END_CARD


--------

START_CARD
Basic

State the GAG cycle equations

Back: 
![[Pasted image 20240516142228.png]]
- $S_{a}$ stress cycle amplitude
- $S_{m}$ mean stress
- $S_{1g}$ the stress at normal loading (1g)
- $S_{TO}$ ground stress caused by wing weight, and includes possible dynamic effects during taxi
- These equations show the Ground air ground stresses in one cycle
<!--ID: 1716056929441-->
END_CARD


--------

START_CARD
Basic

Write the equation for stress sensativity

Back:
![[Pasted image 20240516143442.png]]

![[Pasted image 20240516143327.png]]
<!--ID: 1716056929447-->
END_CARD


--------

START_CARD
Basic

What is the GAG safety factor?

Back: 
![[Pasted image 20240516143842.png]]
<!--ID: 1716056929454-->
END_CARD


--------

START_CARD
Basic

Write the expanded form of the damage per flight equation

Back: 
![[Pasted image 20240516144636.png]]
- $N_{GAG}$ the theoretical number of GAG cycles to failure
- $D_{gust}$ the typical damage caused by gusting per unit range
- $R_{av}$ the average range per flight
- $D_{extra}$ unaccounted for stresses damage caused
- Obviously the number of flights
![[Pasted image 20240516144828.png]]
<!--ID: 1716056929460-->
END_CARD


--------

START_CARD
Basic

Because of insufficient testing the SN curve needs to be adjusted with a scatter factor of 1.45, how?
![[Pasted image 20240516173651.png]]

Back: 
![[Pasted image 20240516173710.png]]
<!--ID: 1716056929467-->
END_CARD


--------

START_CARD
Basic

Write down engineers bending theory

Back: 
![[Pasted image 20240516174912.png]]

- $M=$ anticlockwise moment about the [[neutral surface and neutral axis|neutral axis]]  
- $I_{zz}=I=\int \int y^{2} \cdot dy\cdot dz=$ The resistance to bending due to the geometry of the beams cross section
- $\sigma_{xx}=$ stress
- $y=$ displacement from [[neutral surface and neutral axis|neutral axis]]
- $E=$ [[modulus of elasticity]]
- $R=$ Radius of circle (For this beams bending curviture)

![[Pasted image 20240516174932.png]]
- 
<!--ID: 1716056929474-->
END_CARD



--------

START_CARD
Basic

State the $I$ for a rectangular cross section and the location of the neutral axis.

Back: 
![[Pasted image 20240516175310.png]]
- Neutral axis is through the centre
<!--ID: 1716056929480-->
END_CARD












