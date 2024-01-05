TARGET_DECK: Aerothermodynamics::4



START_CARD
Basic

Derive Ackeret’s formula, starting from:

$$ \begin{align}
(1-M^{2}_{\infty}) \frac{\partial^{2} \phi}{\partial x^{2}} +  \frac{\partial^{2} \phi}{\partial y^{2}} &= 0
\end{align} $$

Back: 

$$ \begin{align}
(1-M^{2}_{\infty}) \frac{\partial^{2} \phi}{\partial x^{2}} +  \frac{\partial^{2} \phi}{\partial y^{2}} &= 0 &&\to& \lambda^{2} \frac{\partial^{2} \phi}{\partial x^{2}} +  \frac{\partial^{2} \phi}{\partial y^{2}} &= 0
\end{align} $$

Assume that $\lambda = \sqrt{ M^{2}_{\infty} - 1 }$  and $\eta$ is constant along lines of gradient $\lambda$ (aka $\eta = x - \lambda y$). This can be proved, first we can guess that $\eta$ is some function of the velocity potential $\phi$:
$$\begin{align*}
 & & \lambda &= \sqrt{ M^{2}_{\infty} - 1} \\
 & & \phi &= \phi(\eta) &&& \frac{\partial \eta }{\partial y}&=  -\lambda  \\
 & & \eta &= x - \lambda y &&& \frac{\partial \eta }{\partial x}&=  1 \\ 

u' &=  \frac{\partial \phi}{\partial x} & &\to & u' &= \frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial x} & &\to & u' &= \frac{\partial \phi}{\partial \eta}  &&\searrow&

\\ 

v' &=  \frac{\partial \phi}{\partial y} & &\to & v' &= \frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial y} & &\to & v' &= -\frac{\partial \phi}{\partial \eta}\lambda  
& &\to& u' &= - \frac{v'}{\lambda}\\\\\\

& & & & \frac{\partial^{2} \phi}{\partial x^{2} } &=  \frac{\partial }{\partial \eta} \left(\frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial x}\right) & 
&\to & \frac{\partial^{2} \phi}{\partial x^{2} } &=    \frac{\partial^{2} \phi}{\partial \eta^{2}}   &&\searrow&

\\ 


& & & & \frac{\partial^{2} \phi}{\partial y^{2} } &=   \frac{\partial }{\partial \eta}  \left(\frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial y}\right) & 
&\to & \frac{\partial^{2} \phi}{\partial y^{2} } &=   \lambda^{2}   \frac{\partial^{2} \phi}{\partial \eta^{2}}   &&\to& \lambda^{2} \frac{\partial^{2} \phi}{\partial x^{2} } &= \frac{\partial^{2} \phi}{\partial y^{2} }

\end{align*}$$
 
This provides a relationship between perturbations in y and x velocities. Then recalling the tan Mach angle relation we can demonstrate that $\lambda$ which defines characteristic lines is a function of just free stream Mach number.

$$ \begin{align}
&&&&&&&&&&\tan\mu &= \frac{1}{\sqrt{M^{2}-1 }}\\
\eta &= x - \lambda y &&\to& y &= \frac{x}{\lambda} + c &&\to& \frac{dy}{dx} &= \frac{1}{\lambda}= \frac{1}{\sqrt{M_{\infty}^{2} -1}} &&\to& \frac{dy}{dx} &= \tan\mu_{\infty}
\end{align} $$

If we take a streamline of small angle $\theta$, then we can imagine it's path on the surface:

![[Pasted image 20231231162532.png]]

Then utilising the previous velocity relation we can sub into linear $C_{p}$ to get the Ackeret formula.

$$\begin{align*}
&& u' &= - \frac{v'}{\lambda}& && \tan \theta= \frac{v'}{U_{\infty}} &\approx\theta && & \lambda &= \sqrt{ M^{2}_{\infty} - 1}\\
 C_{p} &= -2 \frac{u'}{U_{\infty}} & &\to &  C_{p} &=   \frac{2}{\lambda} \frac{v'}{U_{\infty}}   & &\to &  C_{p} &=   \frac{2}{\lambda}\theta  & &\to &  C_{p} &=   \frac{2\theta}{\sqrt{ M^{2}_{\infty} - 1}}
\end{align*}$$

<!--ID: 1704033732168-->
END_CARD


--------

START_CARD
Basic

For a flat plate at 10 degrees incidence in a stream at Mach 2, find Ackeret predictions of lift and drag coefficients.



Back: 
![[Pasted image 20231231162922.png]]
<!--ID: 1704033732176-->
END_CARD



--------

START_CARD
Basic

What is the sign convention for using Ackeret?

Back: 
![[Pasted image 20231231164144.png]]
<!--ID: 1704033732183-->
END_CARD


