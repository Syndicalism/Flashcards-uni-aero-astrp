---
cards-deck: Propulsion::Thermodynamics
---


How do you find the total mass and total number of moles in a mixture?
#card 
- If you get this wrong, drop out of uni, you sum up the contributions of each constituent part of the mixture.
- $m=\sum\limits m_{i}$ and $n=\sum\limits n_{i}$
- Here $m_{i}$ is the mass of a component of the mixture and $n_{i}$ is the number of moles of a component of the mixture.
^1680351377949


What is molar fraction and what is mass fraction. What are their symbols and why are they different.
#card 
- Mass fraction is simply the fraction that some constituent component of a mixture contributes to the total mixture mass: $x_{i}= \frac{m_{i}}{m}$
- Molar fraction is simply the fraction that some constituent component of a mixture contributes to the total molecule count: $y_{i}= \frac{n_{i}}{n}$
- They are obviously going to be (almost always) different because for any particular substance $m$ and $n$ are related by molar mass which varies between substances. ($M= \frac{m}{n}$)
^1680351377954



How can you relate mass fraction to molar fraction.
#card 
- Using the definition of mass fraction ($x_{i}= \frac{m_{i}}{m}$) and molar fraction ($y_{i}= \frac{n_{i}}{n}$) along side the definition of molar mass ($m=nM$ aka $m_{i}=n_{i}M_{i}$).
- $x_{i}= \frac{m_{i}}{m} \:\to\: x_{i}= \frac{n_{i}M_{i}}{n M} \:\to\: x_{i}= \frac{M_{i}}{M} \frac{n_{i}}{n}\:\to\: x_{i}= \frac{M_{i}}{M} y_{i}$
- Here $M$ is the molar mass of the mixture (aka average molar mass)
^1680351377959




How can we express the individual contributions of components to the overall intensive properties of a mixture?
#card 
- For an ideal gas we assume that all particles are behaving independently, hence we can just sum their contributions to get net intensive properties. Since intensive properties are not mass dependent we use molecule count: $P=\sum\limits P_{i}$ 
- This is because we can link these properties to the ideal gas law $P_{i}= \frac{n_{i}\bar{R}T}{V}$, so for pressure $\frac{P_{i}}{P} = \frac{n_{i}\bar{R}T}{V}/\frac{n\bar{R}T}{V} = \frac{n_{i}}{n} = y_{i}$
- Note it's trivial to also get the form $P_{i} = y_{i} P$
- Also note that although $P$ is used this would also work for other intensive properties such as internal energy, enthalpy ect.
^1680351377965




How do extensive properties contribute to mixture properties? How can intensive properties be linked to mass fraction?
#card 
- Extensive properties are the totals of things (quantity dependent), so they can be easily found by summing eg: $m=\sum\limits m_{i}$ and $n=\sum\limits n_{i}$, or alternatively something like internal energy $U=\sum\limits U_{i}$
- Specific and extensive properties can be easily linked using mass (by definition) hence  $U=\sum\limits U_{i} \:\to\: \frac{U}{m} =\sum\limits \frac{U_{i}}{m_{i}}\:\to\: u =\sum\limits u_{i} x_{i}$
^1680351377970


How could you find the specific volume heat for some mixture?
#card 
- Use the relationship for intensive properties in mixtures
- $c_{V} = \sum\limits x_{i} c_{V,i}$
- $x_{i}=$ mass fraction of component substance
- $c_{V,i}=$ specific volume heat of component substance
^1680351377977

