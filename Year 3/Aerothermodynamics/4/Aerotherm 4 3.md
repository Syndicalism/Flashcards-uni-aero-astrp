TARGET_DECK: Aerothermodynamics::4



START_CARD
Basic

What is the linearized pressure coefficient for supersonic flows? State it's variables and limitations

Back: 
$$\begin{align*}  C_{p} &= -2 \frac{u'}{U_{\infty}}   \end{align*}$$ 
- $C_{p}=$ linearized [[pressure coefficient]]
- $u'=\frac{\partial\phi}{\partial x}=$ velocity perturbation in $x$
- $U_{\infty}=$ free stream velocity
- (All the usual assumptions)
- Key limitation is it can't be used near $M=1$ ($0.8<M<1.2$), as well as failing above $M>5$
- This acts as the start point for Ackeret and Prantdl-Glauert linerization

END_CARD


--------

START_CARD
Basic

What is the significance and applicability of, comment on it's relationship to low speed flows:
$$\begin{align*}   0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}}  \end{align*}$$

Back: 
- $M_{\infty}=$ [[Mach number]] free stream
- $\phi=$ [[velocity potential]]
- This is a linearized compressible flow, velocity potential equation
- Key limitation is it can't be used near $M=1$ ($0.8<M<1.2$), as well as failing above $M>5$
- This acts as the start point for Ackeret and Prantdl-Glauert linerization
- We can see that for a small free stream Mach number, the equation reduces to an incompressible potential flow equation (Laplace equation in incompressible flow)

END_CARD


