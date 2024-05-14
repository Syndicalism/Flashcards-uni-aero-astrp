TARGET_DECK: Aero systems control::Topic 6

---

START_CARD
Basic

What is the controllability pole finding formula thing? Apply it to stabilise the following state space form thingy:

$$ \begin{align}
\pmb{A}&=\begin{bmatrix}  1 & 5 \\ -4  &  2 \end{bmatrix} &&& \pmb{B}&=\begin{bmatrix}  1  \\ 0 \end{bmatrix}  &&& \pmb{C}&=\begin{bmatrix}  0  \\ 1 \end{bmatrix}
\end{align} $$ 

Back:  


$$ \begin{align}
|\lambda\pmb{I} -  (\pmb{A} - \pmb{B}\pmb{K})|  &= \left|\begin{bmatrix}  \lambda & 0 \\ 0  &  \lambda \end{bmatrix}   -   \left(\begin{bmatrix}  1 & 5 \\ -4  &  2 \end{bmatrix} - \begin{bmatrix}  1  \\ 0 \end{bmatrix} \begin{bmatrix}  k_{1}  & k_{2} \end{bmatrix} \right) \right| &&\to&  

&\left|\begin{bmatrix}  \lambda & 0 \\ 0  &  \lambda \end{bmatrix}   -   \left(\begin{bmatrix}  1 & 5 \\ -4  &  2 \end{bmatrix} - \begin{bmatrix}  k_{1} & k_{2}  \\ 0 & 0 \end{bmatrix} \right) \right|&&\to&  

&\left|\begin{bmatrix}  \lambda-1+k_{1} & k_{2}-5 \\ 4  &  \lambda - 2 \end{bmatrix}    \right|
\end{align} $$

Then expanding:
$$ \begin{align}
\left|\begin{bmatrix}  \lambda-1+k_{1} & k_{2}-5 \\ 4  &  \lambda - 2 \end{bmatrix}    \right| &= \lambda^{2} + \lambda(k_{1}-3) + (2 - 2k_{1}) + 4k_{2} - 20 &&\to& \lambda^{2} + \lambda(k_{1}-3) +  (2k_{1} + 4k_{2} - 18)
\end{align} $$

Now to ensure stability we want values of $\lambda$ that ensure stability, let's use $\lambda = -1 \pm i$:

$$ \begin{align}
\lambda = -1 \pm i &= \frac{ - (k_{1} - 3) \pm \sqrt{ (k_{1} - 3)^{2} - 4 (2k_{1} + 4k_{2} - 18) } }{2} &&\to& 
-2 \pm 2i &=  - (k_{1} - 3) \pm \sqrt{ (k_{1} - 3)^{2} - 4 (2k_{1} + 4k_{2} - 18) } 
\end{align} $$

Splitting into parts:
$$ \begin{align}
-2 &= - (k_{1} - 3) &&\to& k_{1} &= 5\\
&&2i &= \sqrt{ (k_{1} - 3)^{2} - 4 (2k_{1} + 4k_{2} - 18) } &&\to& -4 &= (5 - 3)^{2} - 4 (10 + 4k_{2} - 18) &&\to& -40 &= -16k_{2} &&\to&  k_{2} &= \frac{5}{2}
\end{align} $$

<!--ID: 1704396530685-->
END_CARD



--------

START_CARD
Basic

State how you can get the open and closed loop poles given $\pmb{A}$, $\pmb{B}$ and $\pmb{K}$. Name these matrices.

Back: 
- The matrices relate to a state space form system, here $\pmb{A}$ and $\pmb{B}$ from the state and control relationships ($x=$state variable, $u=$ control variable):
$$ \begin{align}
\dot{\pmb{x}} &= \pmb{A} \pmb{x} + \pmb{B} \pmb{u}
\end{align} $$
- Then $\pmb{K}$ represents the controller (in a closed loop)
- The open loop poles will simply be the eigenvalues of $\pmb{A}$ hence:
$$ \begin{align}
0 &= |\pmb{I}\lambda - \pmb{A}| &&\to& \lambda_{1} , \lambda_{2} ... &= \text{solved}(0 = |\pmb{I}\lambda - \pmb{A}|)
\end{align} $$
- The closed loop poles are the eigenvalues of $\pmb{A}-\pmb{B}\pmb{K}$ hence:
$$ \begin{align}
0 &= |\pmb{I}\lambda - (\pmb{A}-\pmb{B}\pmb{K})| &&\to& \lambda_{1} , \lambda_{2} ... &= \text{solved}(0 = |\pmb{I}\lambda - (\pmb{A}-\pmb{B}\pmb{K}) |) 
\end{align} $$

<!--ID: 1704396530691-->
END_CARD



