TARGET_DECK: Spacecraft systems engineering and design::3 - Taguchi Method



START_CARD
Basic

Explain, using a diagram, why a high quality product can be considered to be one that is insensitive to environmental factors.

Back: 
![[Pasted image 20231223184228.png]]
-  We want to have a product that maintains the level of quality even when the parameters are not nominal. (robust product)
- In the diagram, we can choose a value of x (a design parameter) such that we maximise the quality, but it is sensitive to noise and the quality can be very low even though x is still close to the nominal value. 
- Alternatively, for the same noise/drift in the parameter x, we can have a product where the quality changes only slightly, this is a more robust design parameter

<!--ID: 1703407852175-->
END_CARD


--------

START_CARD
Basic

For a system with seven design parameters at four different levels, and four noise factors at three different levels. 
- what is the minimum number of experiments needed to find the parameters giving the highest quality? 
- If a Design of Experiments approach is not followed, what is the total number of combinations of design parameters and noise factors that would need to be tested?

Back: 
$$\begin{align*} \text{Total unique combos}  &= s^{m} &&& \text{Min exp combos}  &= 1 + m(s-1)  \end{align*}$$
- $s=$ parameter level count
- $m=$ number of parameters
- For this question:
$$ \begin{align}
s_{d} &= 4 & m_{d} &= 7  &&&s_{n} &= 3 & m_{n} &= 4 
\end{align} $$
- So then:
$$ \begin{align}
\text{Total unique combos}  &= (s_{d})^{m_{d}}\times (s_{n})^{m_{n}} &&& \text{Min exp combos}  &= [1 + m_{d}(s_{d}-1)]\times[1 + m_{n}(s_{n}-1)]\\
1327104&= 4^{7} 3^{4}  &&& 198 &=  [1 + 7(4-1)]\times[1 + 4(3-1)]
\end{align} $$
<!--ID: 1703407852185-->
END_CARD


--------

START_CARD
Basic

What is a signal to noise ratio? Why average it?

Back: 
- This is a value from the Taguchi method which signifies the performance of a certain configuration, it can be individual (where it's for one set of noise factors and design parameters) or averaged for a specific design condition
- By averaging it for a specific design condition we can find the most* robust design condition by what has the highest (or lowest, depending) average noise factor
<!--ID: 1703407852194-->
END_CARD



--------

START_CARD
Basic

What are the main limitations of Taguchi?

Back: 
- Inner and outer array structure assumes no interaction between design parameters and noise factors
- It is possible that the "most robust" combination chosen has a terrible S/N value as assumption of independent performance is unlikely to hold
- Only accounts for one performance characteristic
<!--ID: 1703407852204-->
END_CARD



--------

START_CARD
Basic

Draw the orthogonal matrix for four design parameters (A, B, C, D) at three different levels (L = Low, M = Medium, H = High)

Back: 
![[Pasted image 20231223190124.png]]
- Something like this (Note that at the very least each row is unique!!!)
<!--ID: 1703407852213-->
END_CARD


--------

START_CARD
Basic
Draw the orthogonal matrix for three noise factors:
• In-plane angle: 0° and 15°
• Out-of-plane angle: 0° and 15°
• Solar array degradation factor: 0.1 and 0.3

Back: 
![[Pasted image 20231223190301.png]]
- Something like this (Note that at the very least each row is unique!!!)
<!--ID: 1703407852222-->
END_CARD

 

--------

START_CARD
Basic

State the signal to noise ratio equations for both min and maxing.

Back: 
$$\begin{align*} \text{Min equation}& & S/N_{i}  &= -10 \log_{10} \left( \frac{1}{n_{T}} \sum\limits^{n_{T}}_{j=1} Q_{ij}^{2} \right) \\\\ \text{Max equation}& & S/N_{i}  &= -10 \log_{10} \left( \frac{1}{n_{T}} \sum\limits^{n_{T}}_{j=1} \frac{1}{Q_{ij}^{2}} \right)  \end{align*}$$


- $S/N_{i}=$ Signal to noise ratio for a row
- $n_{T}=$ Number of experiments per [[design parameters and noise factors|design parameter]] combination
- $Q_{ij}=$ The performance metric result for a particular [[design parameters and noise factors|noise factor]] and [[design parameters and noise factors|design parameter]] combinations experiment

END_CARD









