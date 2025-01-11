TARGET_DECK: Adv Management::0 Exams

---

START_CARD
Basic

State the equation of variance and covariance for a likelihood function.

Back: 

> ### $$\begin{align*} I_{ij}  &=  -\frac{\partial^{2}l (t;\theta)}{\partial \theta_{i} \partial\theta_{j}}\end{align*}$$
> ### $$\begin{align*} I^{-1} &= \begin{pmatrix} \text{Var}(\theta_{1}) & \text{Cov}(\theta_{1},\theta_{2}) & ...  & \text{Cov}(\theta_{1},\theta_{k} ) \\ \text{Cov}(\theta_{2},\theta_{1}) & \text{Var}(\theta_{2}) & ... &  \text{Cov}(\theta_{2},\theta_{k} ) \\ ... & ... & ... & ... \\ \text{Cov}(\theta_{k},\theta_{1})  & \text{Cov}(\theta_{k},\theta_{2}) & ... & \text{Var}(\theta_{k})  \end{pmatrix}\end{align*}$$
>> where:
>> $l=$ [[maximum likelihood estimation#^6e1413|log likelihood estimation function]]
>> $\text{Var}(\theta_{i})=$ [[standard deviation for probabability functions|varience]] in the parameter $\theta_i$
>> $\text{Cov}(\theta_{i},\theta_{j})=$ the covariance of the parameters $\theta_i$ and $\theta_j$
>> $I=$ the [[maximum likelihood estimation confidence|Fisher information matrix]]
>> $I_{ij}=$ an element of the Fisher information matrix

END_CARD


--------

START_CARD
Basic

State the 95% confidence bounds for some parameter's estimated state based on its max likelihood estimate.

Back: 
> ### $$\begin{align*}  P(\theta_{l} \leq \hat{\theta}  \leq \theta_{u}) &= \gamma &&\overset{(95\%\text{ case})}{=} 0.95 \end{align*}$$
> ### $$\begin{align*} \theta_{l}&=  \hat{\theta} - Z_{\alpha/2} \sqrt{\text{Var}(\hat{\theta})}& &&\theta_{u}&=  \hat{\theta} + Z_{\alpha/2} \sqrt{\text{Var}(\hat{\theta})} \end{align*}$$
> ### $$\begin{align*} \alpha &= 1- \gamma &&& Z_{\alpha/2}=\begin{cases} 1.96&&& 95\%\text{ certainty}\\2.58&&& 99\%\text{ certainty} \end{cases} \end{align*}$$
>> where:
>> ${\theta}=$ some parameter of our target [[continuous distribution functions|distribution function]]
>> $\hat{\theta}=$ the most likely value of the parameter according to [[maximum likelihood estimation]]
>> $\theta_{l},\theta_{u}=$ the upper and lower bounds under the target certainty
>> $\text{Var}(\hat\theta)=$ the variance for the parameter in question ([[maximum likelihood estimation confidence#Information and Covariance Matrices]])
>> $Z_{\alpha/2}=$ the standard normal statistic (taken from lookup tables generally or calculated) (NOTE: values placed here might ONLY work for gaussians? unsure)
>> $\gamma=$ confidence that the true $\theta$ is in that range

END_CARD


--------

START_CARD
Basic

State the definition of $M(t)$ for an exponential distribution.

Back: 
- $M$ is the expected number of failures from $0\to t$
- For an exponential distribution, the hazard rate is constant. $\lambda$ being the chance per $t$ that failure occurs.
- Hence we can trivially state that the expected number of failures is simply $M(t)=t\:\lambda$

END_CARD



--------

START_CARD
Basic

State the equation for integration by parts

Back: 
$$ \int u \dot{v} \cdot dx = uv - \int \dot{u}v \cdot dx $$

END_CARD



--------

START_CARD
Basic

State the two equations for robust solutions and describe what they optimize for.

$$\begin{align*} F(x)  &=  \int f(x+\varepsilon) P(\varepsilon) \: d\varepsilon \end{align*}$$

$$\begin{align*} F(x)  &=  \int [f(x+\varepsilon)-f(x)]^{2} P(\varepsilon) \: d\varepsilon \end{align*}$$


Back: 
> ### $$\begin{align*} F(x)  &=  \int f(x+\varepsilon) P(\varepsilon) \: d\varepsilon \end{align*}$$
>> where:
>> This equation convolves the performance metric with the variance of $x$, to get the best mean solution.
>> $F(x)=$ the "effective fitness", how fit it is considering the inputs actually vary about the [[probability density function|PDF]]
>> $P(x)=$ the [[probability density function|PDF]] defining the variation of $x$ ([[convolution|kernel]])
>> $f(x)=$ our fitness function
>> ![[Pasted image 20250107161624.png]]

> ### $$\begin{align*} F(x)  &=  \int [f(x+\varepsilon)-f(x)]^{2} P(\varepsilon) \: d\varepsilon \end{align*}$$
>> where:
>> This equation measures the variation in the performance of $f$ under the variance of $x$ described in $P$. It is a measure of local "flatness".
>> $F(x)=$ the deviation experienced by $f(x)$ given some pdf
>> $P(x)=$ the [[probability density function|PDF]] defining the variation of $x$
>> $f(x)=$ our fitness function
>> ![[Pasted image 20250107161832.png]]

END_CARD



