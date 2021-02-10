# MLB-stadium-dimensions
Modeling the dimensions of MLB stadiums using matplotlib

[Here](https://community.fangraphs.com/complete-outfield-dimensions/) is a list of piecewise functions created by Fangraphs user Andrew Fox where each subfunction describes the distance of the outfield wall of an mlb stadium from an angle θ1 to another angle θ2 relative to the left field foul pole.

There are 3 different formats to these subfunctions which are as follows:

![eqs](https://user-images.githubusercontent.com/65193347/107449801-38b68080-6b12-11eb-999e-48251c6c9f51.png)

Knowing these formats allowed me to simply (yet tediously!) collect the constants used in each subequation, append them to a list of all subequations for each park's piecewise function, and parse through each subfunction to plot the outfield walls of each stadium.
The following plot shows 28 of the current 30 MLB parks overlayed on one another. 
The radial axis represents the distance of the outfield wall from homeplate in feet.

![mlb_outfield_dims](https://user-images.githubusercontent.com/65193347/107464126-93110a80-6b2d-11eb-8766-198d62dfb1fb.png)

Using data from [this article written by Sam Vickars](https://thedataface.com/2019/04/sports/baseballs-irregular-outfields) as well as [Andrew Clem's extensive database of stadium data](http://www.andrewclem.com/Baseball/Stadium_statistics.html), I was able to use the same methodology to plot the heights of the same 28 outfield walls.

![mlb_outfield_wall_height](https://user-images.githubusercontent.com/65193347/107464130-94dace00-6b2d-11eb-8a76-e4d4dd9d1480.png)




