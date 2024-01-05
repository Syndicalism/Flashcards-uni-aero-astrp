TARGET_DECK: Aerothermodynamics::4



START_CARD
Basic

Proof the Prantdtl-Glauert transform for velocity potential and pressure coefficient, starting from the linearized velocity potential equation:
$$ \begin{align}
0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}} 
\end{align} $$

Back: 
Here we make use of $\beta = \sqrt{1 - M^{2}_{\infty}}$ as a constant for applying the transform:
$$\begin{align*}
 & & \beta &= \sqrt{1 - M^{2}_{\infty}} \\
 & & \phi_{0} &= \beta \phi \\
 & & x_{0} &= x \\
 & & y_{0} &= \beta y \\
0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}} & &\to & 0  &=   (1-1+\beta^{2})  \frac{\partial^{2} \left(\frac{\phi_{0}}{\beta}\right) }{\partial x_{0}^{2}} + \frac{\partial^{2} \left(\frac{\phi_{0}}{\beta}\right)}{\partial \left(\frac{y_{0}}{\beta}\right)^{2}}
& &\to & 0  &=    \beta^{2}   \frac{\partial^{2} \phi_{0} }{\partial x_{0}^{2}} \frac{1}{\beta^{2}}+ \frac{\partial^{2} \phi_{0} }{\partial y_{0}^{2}} \frac{\beta^{2}}{\beta^{2}}
& &\to & 0  &= \frac{\partial^{2} \phi_{0} }{\partial x_{0}^{2}}  + \frac{\partial^{2} \phi_{0} }{\partial y_{0}^{2}} 
\end{align*}$$

Note that clearly for a real $\beta$ value to exist $M_{\infty}$ must be less than 1. Hence this works in the subsonic regime ($M<0.8$)

$$\begin{align*}
 & & \beta &= \sqrt{1 - M^{2}_{\infty}} \\
 & & \phi_{0} &= \beta \phi \\
 & & x_{0} &= x \\
 & & y_{0} &= \beta y \\
 && u' &= \frac{\partial\phi}{\partial x}= \frac{1}{\beta} \frac{\partial\phi_{0}}{\partial x} &&& C_{p0} &= -2 \frac{u_{0}'}{U_{\infty}}  \\
 C_{p} &= -2 \frac{u'}{U_{\infty}} & &\to & 
  C_{p} &= -  \frac{2}{U_{\infty}\beta} \frac{\partial\phi_{0}}{\partial x} & &\to & 
  C_{p} &=  \frac{C_{p0}}{\beta}   & &\to & 
  C_{p} &=  \frac{C_{p0}}{\sqrt{1-M_{\infty}^{2}}}  
\end{align*}$$
<!--ID: 1703587317252-->
END_CARD


--------

START_CARD
Basic

What is the usefulness of the Prandtl-Glauert transformation?

Back: 
$$\begin{align*} 
0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}}  
& &\to & 0  &= \frac{\partial^{2} \phi_{0} }{\partial x_{0}^{2}}  + \frac{\partial^{2} \phi_{0} }{\partial y_{0}^{2}} 
\end{align*}$$
- The Prandtl-Glauert transformation provides a method for converting transonic flow problems into an equivalent low speed incompressible version
- which allows for calculation of values in the incompressible potential flow domain, which is significantly simpler
- results can then be transformed back into the transonic domain to achieve a reasonable approximation of the true behaviour
<!--ID: 1703587317264-->
END_CARD


--------

START_CARD
Basic

State the equations for compressible pressure and temperature relations, stating differences in applicability.

Back: 
$$ \begin{align}
\frac{p_{0}}{p} &= \left(1 + \frac{\gamma-1}{2} M^{2}\right)^{\frac{\gamma}{\gamma-1} }&\frac{T_{0}}{T} &= 1 + \frac{\gamma-1}{2} M^{2}
\end{align} $$
- Temperature one just assumes perfect gas
- Pressure one has additional Isentropic assumption
<!--ID: 1703587317277-->
END_CARD


--------

START_CARD
Basic


How can I find the critical Mach number for a transonic regime? Comment on use for analysing a real airfoil. Then find the critical Mach number given $C_{p,min}=-0.4$.

Back: 
-  Critical Mach number is the Mach at which some point on the airfoil reaches Mach 1, this will of course occur at the location of lowest pressure and hence lowest pressure coefficient
- To find this minimum pressure coefficient ($C_{p,min}$) we can determine that in the incompressible regime, utilizing well established incompressible Laplacian methods
- Since this value is in the incompressible regime we caawdawdawd
- First a equation for pressure interms of free stream conditions needs to be found, this can use standard isentropic relations:
$$\begin{align*}
 &&\frac{p_{0}}{p} &= \left(1 + \frac{\gamma-1}{2} Ma^{2}\right)^\frac{\gamma}{\gamma-1} \\
\frac{p}{p_{\infty}} &= \frac{\frac{p_{0}}{p_{\infty}}}{\frac{p_{0}}{p} } 
& &\to & \frac{p}{p_{\infty}} &= \frac{ \left(1 + \frac{\gamma-1}{2} Ma_{\infty}^{2}\right)^\frac{\gamma}{\gamma-1} }{  \left(1 + \frac{\gamma-1}{2} Ma^{2}\right)^\frac{\gamma}{\gamma-1}  } 
& &\to & \frac{p}{p_{\infty}} &= \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{\infty}^{2} }{   1 + \frac{\gamma-1}{2} Ma^{2}  }   \right)^\frac{\gamma}{\gamma-1}
\end{align*}$$
- Then we can sub that into the equation for pressure coefficient after considering that by defenition of critical Mach number, this is where the local pressure $p$ has a Mach of 1 ($M=1$), the free stream is therefor critical $M_{\infty}=M_{crit}$.
$$\begin{align*}
&&\frac{p}{p_{crit}} &= \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{crit}^{2} }{   1 + \frac{\gamma-1}{2}   }   \right)^\frac{\gamma}{\gamma-1}\\
C_{p} &=   \frac{2}{\gamma M^{2}_{\infty}} \left(\frac{p}{p_{\infty}} - 1\right) & &\to &
C_{p} &=   \frac{2}{\gamma M^{2}_{crit}} \left(  \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{crit}^{2} }{   1 + \frac{\gamma-1}{2}   }   \right)^\frac{\gamma}{\gamma-1} - 1\right)
\end{align*}$$
- This is the compressible pressure coefficient, so we want to apply the Prantdtl-Glaurert transform:
$$\begin{align*}
C_{p} &=  \frac{C_{p0}}{\sqrt{1-M_{\infty}^{2}}} 
& &\to & \frac{2}{\gamma M^{2}_{crit}} \left(  \left( \frac{ 1 + \frac{\gamma-1}{2} Ma_{crit}^{2} }{   1 + \frac{\gamma-1}{2}   }   \right)^\frac{\gamma}{\gamma-1} - 1\right) &=  \frac{C_{p0}}{\sqrt{1-M_{crit}^{2}}} 
\end{align*}$$
- Here $C_{p0}=C_{p,min}$ since they both come from the incompressible regime, utilizing some iterative method we can now find what $M_{\infty}$ will make that pressure coefficient reach $M=1$, and hence $M_{crit}$
- For this case $M_{crit}=0.747$
<!--ID: 1703587317288-->
END_CARD


--------

START_CARD
Basic

What is the Karman-Tsien correction?

Back: 
![[Pasted image 20231220182300.png]]

- This is to get [[pressure coefficient]] more accurately by including some non-linear stuff. Comparing the two transformed pressure coefficient relationships:

$$\begin{align*}
\text{Prandtl-Glauret: }& &C_{p} &=  \frac{C_{p0}}{\sqrt{1-M_{\infty}^{2}}}\\
\text{Karman-Tsien: }& &C_{p} &=  \frac{ C_{p0} }{ \sqrt{1-M_{\infty}^{2}} + \frac{C_{p0}}{2} \left[ \frac{M_{\infty}^{2}}{\sqrt{1-M_{\infty}^{2}}}  \right] }
\end{align*}$$

- (Second equation not needed for passing this flashcard)
<!--ID: 1703587317298-->
END_CARD





