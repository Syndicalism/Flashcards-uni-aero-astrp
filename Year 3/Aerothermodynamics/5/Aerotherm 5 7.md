TARGET_DECK: Aerothermodynamics::5

---

START_CARD
Basic

Assuming it's steady state. Derive the equation for $T_{i,j}$

![[Pasted image 20231224134406.png]]

Back: 
$$ \begin{align}
0= \frac{d^{2}T}{dx^{2}} + \frac{d^{2}T}{dy^{2}} &= \frac{  \left.\frac{dT}{dx}\right|_{ \frac{1}{2}0} - \left.\frac{dT}{dx}\right|_{ -\frac{1}{2}0}  }{\Delta x} +  \frac{  \left.\frac{dT}{dy}\right|_{0 \frac{1}{2}} - \left.\frac{dT}{dy}\right|_{0 -\frac{1}{2}}  }{\Delta y} &&\to&
0 &= \frac{   \frac{T_{01} - T_{00}}{\Delta x} - \frac{T_{00} - T_{0-1}}{\Delta x}   }{\Delta x} +  \frac{  \frac{T_{10} - T_{00}}{\Delta y} - \frac{T_{00} - T_{-10}}{\Delta y}  }{\Delta y}
\end{align} $$

Then collecting terms:

$$ \begin{align}
0 &= \frac{   \frac{T_{01} - T_{00}}{\Delta x} - \frac{T_{00} - T_{0-1}}{\Delta x}   }{\Delta x} +  \frac{  \frac{T_{10} - T_{00}}{\Delta y} - \frac{T_{00} - T_{-10}}{\Delta y}  }{\Delta y}&&\to&
0 &= \frac{  T_{01}   -  2T_{00} + T_{0-1}    }{\Delta x^{2}} +  \frac{   T_{10} -2T_{00} + T_{-10}   }{\Delta y^{2}}&&\to&
0 &= \frac{  T_{01}  + T_{0-1}    }{\Delta x^{2}} +  \frac{   T_{10}  + T_{-10}   }{\Delta y^{2}} - 2T_{00} \left(\frac{  1}{\Delta x^{2}}+\frac{  1}{\Delta y^{2}}\right)
\end{align} $$

END_CARD


--------

START_CARD
Basic

State the steady state surface convection condition for 1D $x=0$ and $x=L$.

Back: 
$$ \begin{align}
-k \left.\frac{dT}{dx}\right|_{x=0} &= h(T_{\infty} - T_{0}) &&&  -k \left.\frac{dT}{dx}\right|_{x=L} &= h(T_{L}-T_{\infty}) \\
 \left.\frac{dT}{dx}\right|_{x=0} &= -\frac{h}{k}(T_{\infty} - T_{0}) &&&   \left.\frac{dT}{dx}\right|_{x=L} &= - \frac{h}{k}(T_{L}-T_{\infty}) \\
\end{align} $$

END_CARD


--------

START_CARD
Basic

For a discretised 2D system, state the equations of $\frac{\Delta T}{\Delta x}$ and $\frac{\Delta T}{\Delta y}$.

Back: 
$$ \begin{align}
\left. \frac{dT}{dy} \right|_{x=i}  &= \frac{1}{\Delta x} ( T_{i+\frac{1}{2},j} - T_{i- \frac{1}{2},j} ) &&& \left. \frac{dT}{dy} \right|_{y=j}  &= \frac{1}{\Delta y} ( T_{i,j+\frac{1}{2}} - T_{i,j- \frac{1}{2}} )
\end{align} $$

END_CARD


--------
 

START_CARD
Basic

Assuming it's steady state. Derive the equation for $T_{i,j}$

![[Pasted image 20231224140735.png]]

Back: 
$$ \begin{align}
  -k \left.\frac{dT}{dx}\right|_{x=L} &= h(T_{L}-T_{\infty}) &&\to& \left.\frac{dT}{dx}\right|_{x=L} &= - \frac{h}{k}(T_{L}-T_{\infty})\\ 
\end{align} $$
We use the identity above to fix the convection condition
$$ \begin{align}
0= \frac{d^{2}T}{dx^{2}} + \frac{d^{2}T}{dy^{2}} &= \frac{  \left.\frac{dT}{dx}\right|_{ \frac{1}{2}0} - \left.\frac{dT}{dx}\right|_{ 00}  }{0.5\Delta x} +  \frac{  \left.\frac{dT}{dy}\right|_{0 \frac{1}{2}} - \left.\frac{dT}{dy}\right|_{0 -\frac{1}{2}}  }{\Delta y} &&\to&
0 &= \frac{   - \frac{h}{k} (T_{00} - T_{\infty}) - \frac{T_{00} - T_{0-1}}{\Delta x}   }{0.5\Delta x} +  \frac{  \frac{T_{10} - T_{00}}{\Delta y} - \frac{T_{00} - T_{-10}}{\Delta y}  }{\Delta y}
\end{align} $$

Then collecting terms:

$$ \begin{align}
0 &= \frac{   - \frac{h}{k} (T_{00} - T_{\infty}) - \frac{T_{00} - T_{0-1}}{\Delta x}   }{0.5\Delta x} +  \frac{  \frac{T_{10} - T_{00}}{\Delta y} - \frac{T_{00} - T_{-10}}{\Delta y}  }{\Delta y}&&\to&
- \frac{2h}{k \Delta x} T_{\infty} &= \frac{2 }{\Delta x^{2}} T_{0-1}+ \frac{1}{\Delta y^{2}} (T_{10} + T_{-10}) -2T_{00} \left(\frac{h}{k\Delta x} + \frac{1}{\Delta x^{2}} + \frac{1}{\Delta y^{2}} \right)
\end{align} $$

END_CARD





