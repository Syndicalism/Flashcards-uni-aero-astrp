TARGET_DECK: Propulsion::8 Design of turbofan engines



START_CARD
Basic

What is bypass ratio?

Back: 
- The mass flow bypassing the engine core over the mass flow through the engine core
<!--ID: 1684940390917-->
END_CARD


--------

START_CARD
Basic

What is the fan pressure ratio?

Back: 
- The ratio of the pressure before the fan vs after the fan
<!--ID: 1684940390927-->
END_CARD


--------

START_CARD
Basic

For a fixed thrust how does the fan pressure ratio and bypass ratio relate?

Back: 
- A higher fan pressure ratio means that the velocity at the outlet will be greater, hence to keep a constant thrust you'd have to decrease mass flow rate and hence bypass ratio
  
![[Pasted image 20230507203928.png]]
<!--ID: 1684940390936-->
END_CARD



--------

START_CARD
Basic

Explain the following graph and it's implications in turbofan design. 
![[Pasted image 20230507211044.png]]

Back: 
- This shows how specific thrust and specific fuel consumption vary with fan pressure ratio
- Specific thrust is effectively just the speed of the air exiting the jet
- (Bare) Specific fuel consumption is the fuel needed per unit thrust
- It can be seen that a higher fan pressure ratio results in reduced efficiency
<!--ID: 1684940390943-->
END_CARD


--------

START_CARD
Basic

What is the equation for fpr?

Back: 
- fpr is fan pressure ratio:
$$ \begin{align}
\text{fpr} &= \frac{P_{013}}{P_{02}}
\end{align} $$

- This is the ratio of stagnation pressures across the fan (after fan divided by before fan)

![[Pasted image 20230508131525.png]]
<!--ID: 1684940390952-->
END_CARD


--------

START_CARD
Basic

How can fan pressure ratio be used to determine $T_{013}$ for the isentropic and realistic case?
![[Pasted image 20230508131525.png]]

Back: 
$$ \begin{align}
\text{Fan pressure ratio:}&&\text{fpr} &= \frac{P_{013}}{P_{02}}\\
\text{Isentropic relation:}&& \frac{T}{P^{\frac{\gamma-1}{\gamma}}} &= k & &\to & \frac{T_{013s}}{T_{02}} &= \left(\frac{P_{013}}{P_{02}}\right)^{\frac{\gamma-1}{\gamma}} \\
&& && && &= (\text{fpr})^{\frac{\gamma-1}{\gamma}}\\
&& && && T_{013s} &= T_{02} (\text{fpr})^{\frac{\gamma-1}{\gamma}}
\end{align} $$
- This assumes perfect gas relations and no entropy change, to account for entropy we use isentropic efficiency factor $\eta_{f}$:

$$ \begin{align}
\eta_{f} &= \frac{\Delta T_{0s}}{\Delta T_{0}} = \frac{T_{013s} - T_{02}}{T_{013} - T_{02}} & &\to & \eta_{f}(T_{013} - T_{02}) = T_{013s} - T_{02}\\
&& && \eta_{f}T_{013} = T_{013s} + T_{02} (\eta_{f} - 1)\\
&& && \eta_{f}T_{013} = T_{02} (\text{fpr})^{\frac{\gamma-1}{\gamma}} + T_{02} (\eta_{f} - 1)\\
&& && T_{013} = \frac{T_{02}}{\eta_{f}} \left( (\text{fpr})^{\frac{\gamma-1}{\gamma}} + \eta_{f} - 1 \right)\\
&& && T_{013} = T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right)\\
\end{align} $$


--------

START_CARD
Basic

Starting with the equation:
$$ \begin{align}
T_{013} = T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right)
\end{align} $$
What else is needed to derive fan velocity? What does the final equation tell us about the properties of fan exit velocity?

Back: 
$$ \begin{align}
\text{Temperature across fan:}& & T_{013} &= T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right)\\
\text{Adiabatic+zero work entropy:}& & h_{0} &= h + \frac{1}{2}V^{2} & &\to & V_{jb} &= \sqrt{ 2 c_{p} ( T_{013} - T_{19} ) }\\
\text{Isentropic relation:}&& \frac{T}{P^{\frac{\gamma-1}{\gamma}}} &= k & &\to & \frac{P_{02}}{P_{a}} &= \left(\frac{T_{02}}{T_{a}}\right)^{\frac{\gamma}{\gamma -1}}
\end{align} $$

Using maths magic all of these combine into:
$$ \begin{align}
V_{jb} &= \sqrt{2 c_{p} T_{013} \left(1 - \frac{P_{a}}{P_{013}}^{\frac{\gamma-1}{\gamma}}\right)} \\&= \sqrt{2 c_{p} T_{02} \left( 1 + \frac{(\text{fpr})^{\frac{\gamma-1}{\gamma}} - 1}{\eta_{f}} \right) \left(1 - \frac{P_{a} }{P_{02}(\text{fpr})}^{\frac{\gamma-1}{\gamma}}\right)}
\end{align} $$

Which essentially tells us that the bypass exit velocity is purely a function of fan pressure ratio
<!--ID: 1684940390959-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20230508131525.png]]

How can the following equation be determined, and how does it relate to finding bypass ratio?

$$ \begin{align}
V_{jc} &= \sqrt{ 2 c_{p} T_{05} \left( 1 - \frac{P_{9}}{P_{05}}^{\frac{\gamma-1}{\gamma}}\right) }
\end{align} $$

Back: 
$$ \begin{align}
\text{Isentropic relation:}&& \frac{T}{P^{\frac{\gamma-1}{\gamma}}} &= k & &\to & \frac{T_{9}}{T_{5}} &= \left(\frac{P_{9}}{P_{5}}\right)^{\frac{\gamma-1}{\gamma}}\\
\text{Adiabatic+zero work entropy change:}& & h_{0} &= h + \frac{1}{2}V^{2}\\
\text{Low KE at 5:}& & V_{5}^{2} &\approx 0, & &\therefore h_{05} \approx h_{5},\:\:T_{05} \approx T_{5}\\
\end{align} $$
- This can all be combined together

$$ \begin{align}
h_{05} - h_{09} &= h_{5} - h_{9} + \frac{1}{2}(V_{5}^{2} - V_{9}^{2})\\
0 &= h_{05} - h_{9} + \frac{1}{2}( - V_{9}^{2})\\
V_{9} &= \sqrt{ 2c_{p} (T_{05} - T_{9}) } \\
 &= \sqrt{ 2c_{p} \left(T_{05} - T_{05} \left(\frac{P_{9}}{P_{05}}\right)^{\frac{\gamma-1}{\gamma}} \right) } \\
V_{jc} &= \sqrt{ 2c_{p} T_{05} \left(1 - \frac{P_{9}}{P_{05}}^{\frac{\gamma-1}{\gamma}} \right) } \\
\end{align} $$
- It shows us that by varying the pressure loss across the turbine we can change the jet output velocity, which makes perfect sense
- So if we want to maximise efficiency aka $V_{jc} \approx V_{jb}$ we can use this to find the work that needs to be extracted through the turbine and hence bypass ratio
<!--ID: 1684940390969-->
END_CARD


--------

START_CARD
Basic

Name all the variables in the following equation and state what the equation describes:

$$ \begin{align}
\dot{m}_{c} c_{p} (T_{045} - T_{05}) &= \dot{m}_{c} c_{p} (T_{023} - T_{02}) + \text{bpr} \:\dot{m}_{c} c_{p} (T_{013} - T_{02})
\end{align} $$

Then derive it.

Back: 
- $\dot{m}_{c}$ is the mass flow through the turbine
- $c_{p}$ is the constant pressure specific temperature
- $T_{045}$ is stagnation temperature between the turbines
- $T_{05}$ is stagnation temperature out the last turbine
- $T_{023}$ is stagnation temperature between the compressors
- $T_{02}$ is stagnation temperature in the inlet
- $T_{013}$ is stagnation temperature out the fan
- $\text{bpr}$ is the fan bypass ratio (~12ish)

- To derive it, just apply SFEE to a SINGLE SPOOL, then simplify
$$ \begin{align}
\text{Energy extracted in turbine} &= \text{Energy used in compressor} + \text{Energy used in fan}\\
m_{c} c_{p} (T_{045} - T_{05}) &= m_{c} c_{p} (T_{023} - T_{02}) + m_{b} c_{p} (T_{013} - T_{02})\\
m_{c} c_{p} (T_{045} - T_{05}) &= m_{c} c_{p} (T_{023} - T_{02}) +  \text{bpr}\:m_{c} c_{p} (T_{013} - T_{02})\\
\end{align} $$
<!--ID: 1684940390977-->
END_CARD


--------

START_CARD
Basic

Why is fan pressure ratio a useful measure of engine performance?

Back: 
- It determines the force used to accelearte the bypassed air, effectively determining bypass air velocity
- A turbofan can have increased thrust by increasing pressure ratio even while keeping bypass ratio constant
<!--ID: 1685187307087-->
END_CARD


--------

START_CARD
Basic

State the equation for the specific thrust of a turbofan.

Back: 
$$ \begin{align}
\text{Specific thrust} &= \frac{F_{N}}{\dot{m}} \approx \frac{F_{N}}{\dot{m}_{air}} = V_{j} - V_{\infty}
\end{align} $$
<!--ID: 1685187307097-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20230527111859.png]]

By starting with a consistent jet core and a fan pressure ratio, other properties of the engine such as bypass and LP turbine pressure ratio was determined (Using the iterative procedure of changing thing's till $V_{jb}=V_{jc}$). What does this analysis show? Explain the findings. (analysis done for bare engine)

Back: 
Findings:
- Reducing fan pressure ratio allows for a higher bypass ratio. 
- Increasing bpr requires more work to be extracted from the low pressure turbine. 

Expleen:
- If fpr is lower then $V_{jb}$ will be lower and for $V_{jb}=V_{jc}$ the core must also extract a larger amount of KE from it's air. This larger KE must be distributed over more air leading to greater bypass ratio.
<!--ID: 1685187307104-->
END_CARD



--------

START_CARD
Basic

![[Pasted image 20230527113104.png]]

By starting with a consistent jet core and a fan pressure ratio, other properties of the engine such as bypass and LP turbine pressure ratio was determined (Using the iterative procedure of changing thing's till $V_{jb}=V_{jc}$). Using that measures of thrust where determined.  (analysis done for bare engine)

Given that for the same analysis it is shown that decreasing fan pressure ratio will lead to higher bypass ratio.

What does this analysis show? Explain the findings.

Back: 
- Note that the y axis shows thrust is divided by CORE mass flow, which will be constant.
- Decreasing fpr leads to increased bpr which intern increases gross thrust. This makes sense since not only is more KE extracted from the core but also more air is being worked on (bpr) hence momentum flux increases and so does gross thrust.
- Although gross thrust increases with decreasing fpr, there is actually not a huge improvement in net thrust. This is due to the increase in ram drag associated with increased fan cross section.
<!--ID: 1685187307112-->
END_CARD



--------

START_CARD
Basic

![[Pasted image 20230527113955.png]]

By starting with a consistent jet core and a fan pressure ratio, other properties of the engine such as bypass and LP turbine pressure ratio was determined (Using the iterative procedure of changing thing's till $V_{jb}=V_{jc}$). Using that measures of thrust where determined. (analysis done for bare engine)

Given that for the same analysis it is shown that decreasing fan pressure ratio will lead to higher bypass ratio.

What does this analysis show? Explain the findings.

Back: 
- Specific thrust ($F_{N}/\dot{m}_{air}$) increases with increasing fpr, which makes sense as fpr effectively increases the velocity of bypassed air. If the air is moving faster it's specific thrust decreases.
- The sfc improves by decreasing fan pressure ratio, considering that a lower fan pressure ratio leads to higher bpr and then more KE distrobuted over a larger mass of slower moving air... this ties in with things like propulsive efficiency, improving sfc.
<!--ID: 1685187307121-->
END_CARD



--------

START_CARD
Basic

What do we mean by doing analysis on a bare engine?

Back: 
- Only doing analysis on the stream tubes entering/exiting the engine
- This ignores the drag effects of the surrounding structure (nacelle)
<!--ID: 1685187307128-->
END_CARD




--------

START_CARD
Basic

What are the additional factors created by including the necelle on engine efficiency analysis?

Back: 
- Engine weight becomes a thing, increasing bpr will increase engine size and hence the weight of the necelle
- Engine size is also a driver of parasitic drag
- There are additional pressure losses inside the bypass duct as a result of the necelle
<!--ID: 1685187307136-->
END_CARD


--------

START_CARD
Basic

What does the following equation mean? What are it's variables? Explain it.

$$ \begin{align}
D_{nac} &\propto A_{w} \rho V^{2} 
\end{align} $$

Back: 
- This equation describes the drag on the necelle including inside and outside the bypass duct
- $D_{nac}$ is the drag caused
- $A_{w}$ engine wetted area
- $\rho$ air density
- $V^{2}$ air veloicty
- This equation is basically the same as what we've seen in mechanics of flight, but here $A_{w}$ is the main thing varying.
<!--ID: 1685187307144-->
END_CARD


--------

START_CARD
Basic

Starting with:
$$ \begin{align}
D_{nac} &\propto A_{w} \rho V^{2} 
\end{align} $$
Derive the expression:
$$ \begin{align}
D_{nac} &= k V (F_{N}/X) 
\end{align} $$

Back: 
- First we know that the wetted area of the engine will scale with some area measure, let's use cross section:
$$ \begin{align}
A_{w} &= k_{1} \pi\left(\frac{d}{2}\right)^{2} 
\end{align} $$
- Then we know that the mass flow rate through the engine is the stream line flow rate times cross section:
$$ \begin{align}
\dot{m} &= \rho V \times \pi\left(\frac{d}{2}\right)^{2} & &\to &  \frac{\dot{m}}{\rho V} &= \pi\left(\frac{d}{2}\right)^{2}  
\end{align} $$

- Specific thrust can be given as velocity flux:
$$ \begin{align}
\text{specific thrust} &= X = \frac{F_{N}}{\dot{m}} & &\to &  \dot{m} &= \frac{F_{N}}{X}
\end{align} $$
- Now combining all these together:
$$ \begin{align}
& & \text{Area}&\text{ eq}& && \text{Mass}&\text{ flow}& && \text{Specific}&\text{ thrust}\\
D_{nac} &= k_{2} A_{w} \rho V^{2} & &\to & D_{nac} &= k_{2} k_{1} \pi\left(\frac{d}{2}\right)^{2}  \rho V^{2} & &\to & D_{nac} &= k_{2} k_{1} \frac{\dot{m}}{\rho V}  \rho V^{2}\\
&&&&&&&& &= k_{2} k_{1} \dot{m}  V  & &\to & D_{nac}&= k V  \frac{F_{N}}{X}
\end{align} $$
<!--ID: 1685187307151-->
END_CARD




--------

START_CARD
Basic

For the following equation, what is a reasonable value for k?
$$ \begin{align}
D_{nac} &= k V (F_{N}/X) 
\end{align} $$

Back: 
0.04
<!--ID: 1685187307158-->
END_CARD


--------

START_CARD
Basic

Making use of:
$$ \begin{align}
D_{nac} &= k V (F_{N}/X) 
\end{align} $$
What is the equation for the effective thrust of a engine, relative to it's bare form?

Back: 
$$ \begin{align}
F_{N,effective} &= F_{N,bare} - D_{nac} & &\to & F_{N,effective} &= F_{N,bare} - k V (F_{N,bare}/X) \\
&& && &= F_{N,bare} \left(1 -  \frac{k V}{X}\right)
\end{align} $$
<!--ID: 1685187307166-->
END_CARD


--------

START_CARD
Basic

![[Pasted image 20230527121911.png]]

Explain why this makes sense. (only makes use of accounting for drag from nacelle)

Back: 
- Effective sfc will alwayse be greater than bare sfc (drag losses)
- Bare analysis shows that sfc will improve with decreating fan pressure ratio (which causes increased bpr)
- Once accounting for the drag associated with the increase in bpr the sfc gains reduce
<!--ID: 1685187307173-->
END_CARD



--------

START_CARD
Basic

What is the following equation, explain why it isn't cubic.

$$ \begin{align}
W_{engine} &\propto d^{2.4} 
\end{align} $$

Back: 
- This is showing that the weight of an engine increases exponentially with engine diameter
- You'd expect this to be cubic, but in practice upscaling provides weight reduction avenues which in practice lead to an exponent of ~2.4. 
<!--ID: 1685187307180-->
END_CARD


--------

START_CARD
Basic

Write an expression for corrected engine thrust. 


Back: 
$$ \begin{align}
F_{N,corrected} &= F_{N,effective}  - \text{thrust for lifting itself}\\
F_{N,corrected} &= F_{N,effective}  - \frac{W_{engine}}{L/D}\\
\end{align} $$
<!--ID: 1685187307188-->
END_CARD



--------

START_CARD
Basic

![[Pasted image 20230527122925.png]]

Why does this graph make sense (focus on corrected engine weight).

Back: 
- Decreasing fpr for the same core leads to increase bpr. Due to propulsive efficiency this should improve sfc. Which it does (in the bare case)
- Increasing bpr leads to the engine weighing more and the drag increasing
- This offsets the effiency gains making it more practical to not minimise fpr but instead apporach some optimum value
<!--ID: 1685187307196-->
END_CARD







