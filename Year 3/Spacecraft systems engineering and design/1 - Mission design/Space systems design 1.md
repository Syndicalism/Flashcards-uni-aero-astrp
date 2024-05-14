TARGET_DECK: Spacecraft systems engineering and design::1 - Mission design


---

START_CARD
Basic

Define:
- Spatial resolution 
- Spectral resolution 
- Radiometric resolution 
- Temporal resolution 
- Swath width 


Back: 
- Spatial resolution, the spacing between pixel samples on the Earth
- Spectral resolution, measurement of ability to resolve spectral features
- Radiometric resolution, the number of bits per pixel
- Temporal resolution, time between re-imaging of target (revisit time)
- Swath width, the width of the area being scanned
<!--ID: 1703407834587-->
END_CARD


--------

START_CARD
Basic

What is the relationship between spatial and spectral resolution? Why?

Back: 
- Spatial resolution, the spacing between pixel samples on the Earth
- Spectral resolution, measurement of ability to resolve spectral features
- Bandwidth limitations, having both large spatial and spectral resolutions leads to significant increases in the data size of the scan. With the limited data transfer methods from earth to space it may not be possible to parse the huge quantity of data faster than it is scanned
- Hence as one increases it becomes expensive to maintain/scale the other
<!--ID: 1703407834598-->
END_CARD


--------

START_CARD
Basic

Explain passive and active sensors.

Back: 
- Passive sensor's just measure their environment without actively sending out the relevant waves for reflection detection
- Active sensors measure the result of their transmission
<!--ID: 1703407834608-->
END_CARD


--------

START_CARD
Basic

State advantages/disadvantages of active sensors.

Back: 
- Expensive
- High energy intensity
- Reliable
- Controllable output level
- Lower noise (due to control over source)
<!--ID: 1703407834619-->
END_CARD




--------

START_CARD
Basic

Sketch the scanning profile of the scanning methods, labelling the terms:
- FOV
- GFOV
- in/cross track

Back: 
![[Pasted image 20231223162551.png]]
<!--ID: 1703407834626-->
END_CARD



--------

START_CARD
Basic

State the equation for ground velocity for a push broom scanner.

Back: 
$$ \begin{align}
V_{gd}  &= V_{orb} \frac{R_{E}}{r_{orb}}
\end{align} $$
<!--ID: 1703407834633-->
END_CARD


--------

START_CARD
Basic

State the equation for push broom sample rate

Back: 
 $$\begin{align*} d_{s} &= t V_{orb} &&& d_{g}= GSI&= t V_{gd}  \end{align*}$$
 
- $V_{orb}=$ velocity of satellite
- $V_{gd}=$ velocity of ground relative to satellite   
- $d_{s}=$ [[remote sensing (aerospace)|Spatial]] sample rate (space)
- $d_{g}=$ [[remote sensing (aerospace)|Spatial]] sample rate (ground)
- GSI$=$ Ground-projected Sample Interval
- $t=$ array sample rate (time between samples)
<!--ID: 1703407834641-->
END_CARD


--------

START_CARD
Basic

What are scanner ghosts?

Back: 
![[Pasted image 20231223162924.png]]

- Scanner ghosts are these things
- This is especially bad when using multiple sensors and aggregating their data to produce one image. Here RGB scanners are used to create a image with colour, but it can be seen that the tiny differences in scan time lead to the place being scattered.
- These issues can potentially be fixed with data processing but are still annoying, and especially problematic with fast moving targets.
<!--ID: 1703407834649-->
END_CARD


--------


START_CARD
Basic

Identify four microwave remote sensing techniques that can be used by instruments on an Earth- orbiting satellite and describe power requirements and state requirements

Back: 
- Radar - imaging
- Radiometer - passively receives EM radiation
- Altimeter - actively uses radio to get distance measurements (or uses ground stations)
- Scatterometer - measures properties of gas through scattering/diffusion can be used for wind
- Synthetic Aperture Radar -  form of radar that is used to create two-dimensional images or three-dimensional reconstructions of objects
- All of these (except Radiometers) are active systems and have a high power requirement.  (detecting emitted microwave radiation – e.g. SMOS mission) and so have a relatively low power requirement. 
- The instruments are high spatial resolution (except perhaps the Radiometer, which can be low spatial resolution) and need fine pointing control (e.g. reaction wheels)
<!--ID: 1703407834654-->
END_CARD


--------

START_CARD
Basic

A satellite in a dawn dusk Sun-synchronous 720 km circular orbit is to be used to measure the extent and characteristics of ice extent over the poles. Propose a suitable payload for this orbit and application and give reasons for your choice.

Back: 
- A dawn dusk orbit would be suitable for a payload that was not concerned about the sun illumination angle i.e. a microwave payload. A microwave payload would be ideal because it can observe the earth at all times and is unaffected by cloud. Possible microwave payloads can be active or passive
- The synthetic aperture radar would be able to provide high resolution imagery that would be able to map the extent of the ice
- An altimeter would be able to map the extent of ice if it was similar to Cryosat. This instrument would require additional instrumentation in order to track the orbit accurately. The sun-synchronous orbit is not ideal for this instrument.
- A passive microwave radiometer would be able to measure the characteristics of the ice.
<!--ID: 1703407834660-->
END_CARD


--------

START_CARD
Basic

Sketch the relationship between $f$ and $H$ for remote sensing. Then briefly state definitions of parts. Describe how height effects resolution.

Back: 
![[Pasted image 20231223174310.png]]
- Instantaneous field of view (IFOV) - represents the minor angle in a projection of the sensor's view after exiting the lens or optical system. It defines the angular size of an individual pixel or detector element in the sensor array. IFOV is crucial in determining the level of detail that the sensor can capture, and it influences the spatial resolution of the resulting images.
- Ground-projected instantaneous field of view (GIFOV) - the IFOV that has been projected onto the Earth's surface. It accounts for the effect of the satellite's altitude and viewing angle, indicating the area on the ground corresponding to one pixel after considering the satellite's position and orientation.
- Swadth width (GFOV) Basically just GIFOV times by pixel count. (the total width of a swath for pushbroom)
- Focal length - the distance between the lens (or the mirror) and the image sensor in the satellite sensor system. It determines how much the sensor can zoom in or out and affects the field of view. A shorter focal length results in a wider field of view, while a longer focal length provides a narrower, more zoomed-in view.
- Altitude - The height of the satellite above the Earth's surface. It is a crucial parameter as it directly influences the spatial resolution of the satellite imagery. (Satellites at higher altitudes tend to have coarser spatial resolution (larger pixels) because they cover larger areas, while satellites at lower altitudes provide finer spatial resolution (smaller pixels) because they can distinguish smaller details on the Earth's surface due to the closer proximity.)
<!--ID: 1703407834667-->
END_CARD


--------

START_CARD
Basic

Sketch the difference between GSI and GIFOV, state the equation of GSI and GIFOV. Explain the difference, what happens if GSI << GIFOV.

Back: 
![[Pasted image 20231223174736.png]]
- GSI is the d
$$ \begin{align}
GIFOV &= w \frac{H}{f} & GSI &= d \frac{H}{f}
\end{align} $$
- $w=$ inter-detector spacing
- $d=$ spatial sample rate (distance travelled by the sensor in between samples)

Generally GSI and GIFOV are the same, but in some cases the GIFOV may be larger or smaller than GSI, if it is smaller then it would lead to gaps in between the pixels that aren't sampled from. In the event that GIFOV was much much larger than GSI the image would be blurry.
<!--ID: 1703407834673-->
END_CARD



--------

START_CARD
Basic

State the equation for data rate for a push broom scanner.

Back: 
$$ \begin{align}
Q N \omega &= bits/sec
\end{align} $$
- $\omega=$ samples per second
- $Q=$ pixel bits (spectral resolution)
- $N=$ number of pixel scanners
<!--ID: 1703407834680-->
END_CARD



--------

START_CARD
Basic

Given a sample has a bit size of $8$ how many potential states does it have?

Back: 
$$ \begin{align}
2^{Q}&= n &&&2^{8} &= 256
\end{align} $$
<!--ID: 1703407834688-->
END_CARD







