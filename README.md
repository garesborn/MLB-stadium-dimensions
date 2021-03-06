# MLB-stadium-dimensions
Modeling the dimensions of MLB stadiums using matplotlib

[Here](https://community.fangraphs.com/complete-outfield-dimensions/) is a list of piecewise functions created by Fangraphs user Andrew Fox where each subfunction describes the distance of the outfield wall of an mlb stadium from an angle θ1 to another angle θ2 relative to the leftfield foul pole.

There are 3 different formats to these subfunctions which are as follows:

![eqs](https://user-images.githubusercontent.com/65193347/107449801-38b68080-6b12-11eb-999e-48251c6c9f51.png)

Knowing these formats allowed me to simply (yet tediously!) collect the constants used in each subequation into a tuple, append each tuple to a list for each park's piecewise function, and parse through each piecewise to plot the outfield walls of each stadium using [matplotlib's polar plot function](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.polar.html).
The following plot shows 28 of the current 30 MLB parks overlayed on one another. 
The radial axis represents the distance of the outfield wall from homeplate in feet.

![mlb_outfield_dims](https://user-images.githubusercontent.com/65193347/107464126-93110a80-6b2d-11eb-8766-198d62dfb1fb.png)

Using data from [Andrew Clem's extensive database of stadium data](http://www.andrewclem.com/Baseball/Stadium_statistics.html), I was able to use the same methodology to plot the heights of the same 28 outfield walls. Having this data will allow me to model each park in 3 dimensions. 

![mlb_outfield_wall_height](https://user-images.githubusercontent.com/65193347/107464130-94dace00-6b2d-11eb-8a76-e4d4dd9d1480.png)

Using [matplotlib's plot_surface](https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#surface-plots) function, I was able to convert these wall distances and heights into 3D surfaces. This requires 3 arrays of shape 901x901 to represent each of the lower and upper bounds of each dimension. (Please see code for more information)

First, was a list P (for greek letter phi) of 901 evenly spaced angles between 0 and π/2 repeated 901 times.

Next, was a list R of 901 values evenly spaced from 0 to the radial distance of the outfield wall at each of the 901 evenly spaced angles between 0 and π/2.

Lastly, was a list z of 901 values evenly spaced from 0 to the height of the outfield wall at each of the 901 evenly spaced angles between 0 and π/2.

Once this data was compiled into 3 arrays, I converted the data from arrays R and P from polar to cartesian coordinates to plot the final surface. 

ARZ

![Chase Field](https://user-images.githubusercontent.com/65193347/107466893-cf933500-6b32-11eb-8393-3f60bd1e9e70.png)

BAL

![Camden Yards](https://user-images.githubusercontent.com/65193347/107466892-cf933500-6b32-11eb-8ad9-c88122b699a8.png)

BOS

![Fenway Park](https://user-images.githubusercontent.com/65193347/107466902-d02bcb80-6b32-11eb-8355-d4f37914a7fb.png)

CHC

![Wrigley Field](https://user-images.githubusercontent.com/65193347/107466888-cf933500-6b32-11eb-836b-fca29ff1de0d.png)

CWS

![US Cellular Field](https://user-images.githubusercontent.com/65193347/107466887-cefa9e80-6b32-11eb-9bc8-076c59c8e317.png)

CIN

![Great American Ballpark](https://user-images.githubusercontent.com/65193347/107466903-d0c46200-6b32-11eb-8ce5-a9b03232a0d3.png)

CLE

![Progressive Field](https://user-images.githubusercontent.com/65193347/107466879-ce620800-6b32-11eb-8b42-c926bf6c9455.png)

COL

![Coors Field](https://user-images.githubusercontent.com/65193347/107466898-d02bcb80-6b32-11eb-832e-6c883e0fde32.png)

DET

![Comerica Park](https://user-images.githubusercontent.com/65193347/107466897-d02bcb80-6b32-11eb-9a79-ee57fbaaafb0.png)

HOU

![Minute Maid Park](https://user-images.githubusercontent.com/65193347/107466908-d15cf880-6b32-11eb-8e25-5da99111461f.png)

KC

![Kauffman Stadium](https://user-images.githubusercontent.com/65193347/107466904-d0c46200-6b32-11eb-927a-034b9a5a6c4d.png)

LAA

![Angel Stadium](https://user-images.githubusercontent.com/65193347/107466890-cf933500-6b32-11eb-9c9d-8e7e49aa58bc.png)

LAD

![Dodger Stadium](https://user-images.githubusercontent.com/65193347/107466899-d02bcb80-6b32-11eb-82ef-e584c801fd7b.png)

MIA

![Marlins Park](https://user-images.githubusercontent.com/65193347/107466905-d0c46200-6b32-11eb-8920-2996ac14963d.png)

MIL

![Miller Park](https://user-images.githubusercontent.com/65193347/107466907-d0c46200-6b32-11eb-98e5-b4343768a6ba.png)

MIN

![Target Field](https://user-images.githubusercontent.com/65193347/107466884-cefa9e80-6b32-11eb-8374-38be8b6fa9cd.png)

NYM

![Citi Field](https://user-images.githubusercontent.com/65193347/107466895-d02bcb80-6b32-11eb-8e1c-44dfd6ff0322.png)

NYY

![Yankee Stadium](https://user-images.githubusercontent.com/65193347/107466889-cf933500-6b32-11eb-9e66-f7028837754a.png)

OAK

![RingCentral Coliseum](https://user-images.githubusercontent.com/65193347/107466880-cefa9e80-6b32-11eb-82bf-360e5b54705b.png)

PHI

![Citizens Bank Park](https://user-images.githubusercontent.com/65193347/107466896-d02bcb80-6b32-11eb-994a-a584623e0338.png)

PIT

![PNC Park](https://user-images.githubusercontent.com/65193347/107466915-d15cf880-6b32-11eb-9131-f0b28ba8781b.png)

SDP

![Petco Park](https://user-images.githubusercontent.com/65193347/107466913-d15cf880-6b32-11eb-9fa3-9cec1916c1eb.png)

SFG

![Oracle Park](https://user-images.githubusercontent.com/65193347/107466912-d15cf880-6b32-11eb-8721-a687d9cbc64f.png)

SEA

![Safeco Field](https://user-images.githubusercontent.com/65193347/107466883-cefa9e80-6b32-11eb-900d-e1d716ac0d7c.png)

STL

![Busch Stadium](https://user-images.githubusercontent.com/65193347/107466891-cf933500-6b32-11eb-8058-d2842e4ef765.png)

TB

![Tropicana Field](https://user-images.githubusercontent.com/65193347/107466885-cefa9e80-6b32-11eb-9187-3a61ada7c4f9.png)

TOR

![Rogers Centre](https://user-images.githubusercontent.com/65193347/107466882-cefa9e80-6b32-11eb-9d32-b1b803916a5e.png)

WSN

![Nationals Park](https://user-images.githubusercontent.com/65193347/107466911-d15cf880-6b32-11eb-8b1a-5f77831a8ef7.png)


Conclusion: The RF Short Porch in Yankee Stadium (315' deep, 8' tall) is much easier to hit a ball over than the Green Monster (310' deep, 37' tall) so I never want to hear Yanks fans (dad) talk trash about Fenway's dimensions again.
