TARGET_DECK: Spacecraft systems engineering and design::4 - Spacecraft orbit design



START_CARD
Basic

For a geostationary spacecraft, write down the:
- semi-major axis
- eccentricity
- inclination

Back: 
- $a=42164$ km
- $e=0$
- $i=0$

END_CARD


--------

START_CARD
Basic

What are common features of highly eccentric orbits?

Back: 
- Common advantages of HEO is:
	- Short eclipses, which don't occur near apogee (often the main operating period for comms, so where most power is needed)
	- The flexibility allows for targeting specific latitudes, though additional consideration regarding stability is required
	- Can cover poles which aren't accessible by GEO
- Common disadvantages of HEO is:
	- Complex issues for signal transmission due to complex motion:
		- Ground stations do still require active tracking, unlike [[geostationary coverage|GEO]]
		- The ground stations must actively account for the [[doppler effect]] since the relative velocity of the satellite is changing in a complex manor
		- The intensity of the signal also varies as distance varies
		- Latency varies with distance
	- For [[highly eccentric orbit (year 3)|HEO]] that are not synced with Earths rotation, they can have constant change in ground coverage, this can be an advantage for some use cases
	- Orbital perturbations ([[space drag]]) with potential for significant interference from the moon due to high [[ellipse (year 2)|eccentricity]]
	- Passes through [[Van Allen radiation belts]], which can cause significant problems for the [[spacecraft maintenance problem]]
	- Generally requires quite large satellites (>1000kg) unlike LEO and has large power requirements

END_CARD



--------

START_CARD
Basic

Describe 2 types of HEO constellations. Sketch the orbital paths. How many needed to achieve 24 hour coverage? Then compare them.

Back: 
![[Pasted image 20231224093317.png]]
- Molniya orbit
	- Highly elliptical 12 hour orbit (strictly, half a [[sidereal day]] 11 h 58 m), inclined at 63.4° or 116.6° to the equator.
	- This type of orbit is particularly useful for communication satellites serving polar and high-latitude regions, where geostationary satellites may have limitations due to their positioning relative to the equator. Molniya orbits allow for longer dwell times over high-latitude areas, improving communication services in these regions
	- To achieve 24 hour coverage of the target region, 3 satellites spaced 120 degrees apart are needed.
- Tundra orbit
	- This is a Highly elliptical 24 hour (strictly, 23 h 56 m) orbit, inclined at 63.4°to the equator (a = RGEO = 42,164 km).
	- Basically the same as a normal Molniya orbit, but instead of having 2 regions it's just got 1, this requires a higher delta-V to reach but has more targeted coverage
	- To achieve 24 hour coverage of the target region, 3 satellites spaced 120 degrees apart are needed.
![[N0H7Q.gif]]

END_CARD


--------

START_CARD
Basic

A polar research station in the Antarctic requires 24-hour coverage in order to provide transmission of telemetry and science data. By discussing the advantages and disadvantages, compare and contrast two orbit options for this system.

Back: 
- LEO constellation v Molniya-type constellation with perigee in Northern hemisphere (GEO not an option for Antarctic coverage)
- LEO requires smaller less powerful satellites
- LEO has less variation in transmission signal and pointing, simpler ground station
- HEO requires fewer satellites for 24 hour coverage
- HEO has less complications caused by eclipses (with LEO these could occur during transmission periods)

END_CARD



--------

START_CARD
Basic

Describe the 2 types of global constellations we consider. State important equations, sketch path and describe coverage. What are the advantages of these arrangements? Which requires more satellites for global coverage, generally by how much?

Back: 
$$\begin{align*} I &= \left\{\begin{aligned} &\frac{180\degree}{p},&\text{Walker star}\\&\frac{360\degree}{p},&\text{Walker delta}   \end{aligned}\right. \end{align*}$$
- $p=$ number of planes
- $I=$ angle between consecutive orbital planes
- Advantages
	- Perturbations act similarly on all satellites, reducing inter satellite variation
	- Both allow for global coverage
- Walker delta requires more satellites for achieving global coverage, although not always the case it often requires double the number of satellites when compared to walker star.

![[Pasted image 20231224094928.png]]
![[Pasted image 20231224094847.png]]

END_CARD


--------

START_CARD
Basic

How many GEO satellites would be required for 24hour equatorial coverage, assuming min acceptable elevation is $30\degree$?

Back:
$$ \begin{align}
\alpha &= \arccos\left( \frac{R_{E}}{R_{E} + H} \right) - E =52.47\degree
\end{align} $$
- The are covered by 1 satellite is double this ($2\alpha=104.94\degree$)
$$ \begin{align}
n_{raw} &= \frac{360\degree}{2\alpha} = 3.43
\end{align} $$
- We need 4 satellites

END_CARD


--------

START_CARD
Basic

A low Earth orbit (LEO) constellation is used to achieve complete (24 hour) coverage of the Equator, such that the coverage of each satellite is required to span from the node of the next most westerly orbit plane to the node of the next most easterly plane (with a similar requirement for satellite separation in-plane) as in Figure 2. If the minimum acceptable elevation at the edge of coverage is 10°, and the orbital height of the constellation, H, is 5400 km, use the data provided to determine the minimum number of satellites in the constellation.

Back: 
$$ \begin{align}
\alpha &= \arccos\left( \frac{R_{E}}{R_{E} + H} \right) - E =47.77\degree
\end{align} $$
- The area covered by 1 satellite is $2\alpha$ but in this case we want double overlap along the equator so for in plane spacing:
$$ \begin{align}
s &= \frac{360\degree}{2\alpha} \times 2 =7.53 &&\to& s=8
\end{align} $$
- To achieve global coverage we can use either a walker star or walker delta configuration,  the same coverage properties applied above apply here, hence:
$$ \begin{align}
\text{Walker star}&& p &= \frac{180\degree}{2\alpha} \times 2 =3.77 &&\to& p&=4 &&\to&  t&= ps=32\\\\
\text{Walker delta}&& p &= \frac{360\degree}{2\alpha} \times 2 =7.53 &&\to& p&=8 &&\to&  t&= ps=64
\end{align} $$

END_CARD


--------

START_CARD
Basic

Compare latency of:
- HEO
- LEO
- MEO
- GEO

Back: 
- HEO - Medium latency, but changes significantly during operation
- LEO - Low latency, relatively consistent
- MEO - Medium latency, relatively consistent
- GEO - High latency, perfectly consistent

END_CARD


--------

START_CARD
Basic

Sketch a labelled diagram of single satellite coverage, naming terms.

Back: 
![[Pasted image 20231224102140.png]]
- $H=$ orbital height 
- $\theta=$ half antenna beam width
- $\theta_{max}=$ half antenna beam width if $E=0$ (max theoretical beam width)
- $\beta=$ coverage area diameter
- $\alpha=$ coverage angle
- $\alpha_{max}=$ coverage angle if $E=0$ (max theoretical coverage angle)
- $E=$ spacecraft elevation angle at edge of coverage
- $R=$ slant range at edge of coverage area
- $R_{E}=$ earth radius

END_CARD







