# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:49:56 2021

@author: Gar
"""

from stad_data import stad_df as df
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# =============================================================================
#       A plotting of mlb stadium dimensions based on piecewise functions found
#   here: https://community.fangraphs.com/complete-outfield-dimensions/.
#
# =============================================================================
# =============================================================================
#
#                           WALL DISTANCE DIMENSIONS
#
#       These piecewise functions are described as a list of tuples where 
#       each tuple represents a subfunction of the overall piecewise.
#       there are 3 different formats of piecewise subfunctions used. 
#
#       See: https://github.com/garesborn/MLB-stadium-dimensions for a cleaner
#       record of these equations (NOTE: c values represent constants)
#
#  0: format is always c0/(sin(theta)-c1*cos(theta))
#  1: format is combo of format 0 and
#
#       c0*cos(theta - c1)-c2*cos(theta-c3)/d+
#       c7*sqrt(d - c8*sin^2(theta-c2))/d
#       where d = (c4-c5*cos(2*theta-c6))
#
#  2: format is combo of 0 and c0/sin(theta) or c0/cos(theta) or c0
#
#  These sub-equations are represented in tuples in the following formats:
#
#  0: [c0, c1, theta_min, theta_max]
#  1: [[c0,c1,c2,c3,c4,c5,c6],[c7,c8], theta_min, theta_max] formatted based on first and second term of eq
#  2: [c0, str, theta_min, theta_max] where str is one of 'sin', 'cos', or 'con'
# =============================================================================
# =============================================================================
#
#                       WALL HEIGHT DIMENSIONS
#
# There are 2 types of Wall height subequations, constant height and linearly sloped.
#
# These sub equations are represented in tuples in the following format:
#
#   [h, b, theta_min, theta_max] 
#   where h is the height at theta_min and b is 0 for constant height
#   or 1 for sloped
# =============================================================================


# =============================================================================
#  Function plotting distance of outfield wall at any given angle through polar coordinates
# =============================================================================
def dim_plot(wall_distance, dform, title, plot = False, rev = False):

    # wall_distance: list of tuples that provide piecewise constants and angle limits, ex. line 23
    # dform: format value of piecewise subfunctions as described on line 250
    # title: name of stadium
    # plot: True value will plot stadium dimension using matplotlib
    
    # create a list of deg where step = .1 from 0 deg = left field foul pole
    # to 90 deg = right field foul pole
    x = np.linspace(0,90,901)
    # create empty list for distances at each angle
    y =  []
    track = [] #trouble shooting list
    lines = [] #bounds to each distance equation
    output = [] #list of tuples including radians and distances
    #Convert constants and limits to list of data points
    for i in wall_distance:
        #grabs min and max angle index in list x for current eq in piecewise list
        # ex. index for 57.2 deg in x is 572 
        mn = np.where(abs(x - i[2]) < .01)[0]
        mx = np.where(abs(x - i[3]) < .01)[0]
        #adds the max angle for current piecewise subeq to list so we can plot the limits of each subeq on final graph
        lines.append(round(x[mx[0]],3))
        #iterate through indicies of list x for theta_min and theta_max of each sub eq
        for j in np.arange(mn[0],mx[0]):
            # debugging
            if x[j] not in track:
                track.append(round(x[j],3))
            # setting n as current angle
            n = x[j]
            
            # code for subeqs described in line 260
            if dform == 2 and isinstance(i[1], str):
                if i[1] == 'cos':
                    m =i[0]/(np.cos(np.deg2rad(n)))
                elif i[1] == 'sin':
                        m =i[0]/(np.sin(np.deg2rad(n)))
                elif i[1] == 'con':
                    m = i[0]
                    
            # code for the vast majority of subeqs, described in line 253
            
            elif dform == 0 or type(i[0]) is int or type(i[0]) is float:
                m = i[0]/(np.sin(np.deg2rad(n))+i[1]*np.cos(np.deg2rad(n)))
                
            # code for subeq format described in lines 256-258
            elif dform == 1:
                den = (i[0][4]-i[0][5]*np.cos(2*np.deg2rad(n)-np.deg2rad(i[0][6])))
                m1 = (i[0][0]*np.cos(np.deg2rad(n)-np.deg2rad(i[0][1]))-
                      i[0][2]*np.cos(np.deg2rad(n)-np.deg2rad(i[0][3])))/den
                s = np.power(np.sin(np.deg2rad(n)-np.deg2rad(i[0][1])),2)
                m2 = (i[1][0]*np.sqrt(den-i[1][1]*s))/den
                m = m1 + m2
            #add m to list of distances                
            y.append(m)
            # special case for last value in list
            # follows the same functions above
            if n == 89.9:
                if dform == 2 and isinstance(i[1], str):
                    if i[1] == 'cos':
                        m =i[0]/(np.cos(np.deg2rad(n)))
                    elif i[1] == 'sin':
                        m =i[0]/(np.sin(np.deg2rad(n)))
                    elif i[1] == 'con':
                        m = i[0]
                elif dform == 0 or type(i[0]) is int or type(i[0]) is float:
                    m = i[0]/(np.sin(np.deg2rad(90))+i[1]*np.cos(np.deg2rad(90)))
                elif dform == 1:
                    den = (i[0][4]-i[0][5]*np.cos(2*np.deg2rad(n)-np.deg2rad(i[0][6])))
                    m1 = (i[0][0]*np.cos(np.deg2rad(n)-np.deg2rad(i[0][1]))-
                      i[0][2]*np.cos(np.deg2rad(n)-np.deg2rad(i[0][3])))/den
                    s = np.power(np.sin(np.deg2rad(n)-np.deg2rad(i[0][1])),2)
                    m2 = (i[1][0]*np.sqrt(den-i[1][1]*s))/den
                    m = m1 + m2
                y.append(m)
                
    #convert list of degrees to list of radians
    #compile radians and distances into list of tuples

    rad = []
    for i in range(len(x)):
        rad.append(np.deg2rad(x[i]))
        # function returns 2 list of rad and y
        # where rad is angle in rad from LF pole, and d is distance of wall from homeplate
    
    if plot:
        plt.figure(figsize=(10,10))  
        #plots 2D image of wall dimensions
        if rev:
            plt.polar(rad, -y)
        else:
            plt.polar(rad, y)
        ax = plt.gca()
        #plots piecewise subeqs bounds
        for i in lines:
            ax.plot((0, np.deg2rad(i)), (0,550), c = 'lightgray')
        plt.title(str(title+ ' Outfield Dimensions'))
        plt.grid(False)
        plt.ylim(0,450)
        plt.xlim(0,np.pi/2)
        gridlines = ax.xaxis.get_gridlines()
    
    #see line 398
    return (rad,y)
        
def height_plot(wall_height, title, plot = False):
    
    # wall_height: list of tuples formatted as described in line 276
    # title: name of stadium
    # plot: oif True will plot wall height using matplotlib    
    
    x = np.linspace(0,90,901)
    h =  []
    track = []
    lines = []
    output = []
    for i in range(len(wall_height)):
                    
        mn = np.where(abs(x - wall_height[i][2]) < .01)[0]
        mx = np.where(abs(x - wall_height[i][3]) < .01)[0]
        lines.append(round(x[mx[0]],3))
        
        #if curent piecewise subeq is lineraly sloped wall
        if wall_height[i][1] == 1:
                #print(wall_height[i],wall_height[i+1])
                s = wall_height[i][0] #wall height at min_angle
                f = wall_height[i+1][0] #wall height at max_angle (or next subeqs min_angle)
                z = wall_height[i][2] #min angle for current subeq
                rise = f - s
                run = x[mx[0]]-x[mn[0]]
                slope = rise/run     #slope calculated from rise and run
                
                
        for j in np.arange(mn[0],mx[0]):
            #for debugging
            if x[j] not in track:
                    track.append(round(x[j],3))
            # set n as current working angle
            n = x[j]        
            # if curent piecewise is lineraly sloped wall
            if wall_height[i][1] == 1:
                #calculates height based on previously derived slope eq                
                m= slope*(n-z) + wall_height[i][0]
                h.append(m)
            else:
                #for constant height, h @ current angle x is just constant i[0] based on format described in line 276
                m=wall_height[i][0]
                h.append(m)
                if n == 89.9:
                    m=wall_height[i][0]
                    h.append(m)
    
    rad = []
    for i in range(len(x)):
        rad.append(np.tan(np.deg2rad(x[i])-np.pi/4)*45)
        # function returns 2 lists of rad and h
        # where rad is angle in rad from LF pole, and h is height of wall at that angle
    
    #plots wall height from angle 0-90deg
    if plot:    
        h.reverse()
        plt.figure(figsize=(12,4)) 
        plt.plot(x,h)
        plt.title(str(title + ' Outfield Wall Height'))
        plt.ylim(0,40)
    
    #see lines 469-470
    h.reverse()
    return (rad,h)

def model(distance, height, title):
    r = [] #radius
    p = [] #angle
    h = [] #height
    for i in range(len(distance[0])):
        #creates lists of:angles p (for phi)
        #                 radii r
        #                 heights h
        p.append(distance[0][i])
        r.append(distance[1][i])
        h.append(height[1][i])
    
    p.reverse()
    r.reverse()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    #to plot a plane in matplotlib in this case, an array of shape n*n is required
    z = np.zeros((901,901))
    R = np.zeros((901,901))
    P = np.zeros((901,901))
    for i in range(len(h)):
        #print(i)
        z[i] = np.linspace(0,h[i],901)
        P[i] = p
        R[i] = r
        
        
    #P is an array of length 901 where every entry is a list of angles from 0 to pi/2 incremented by pi/900
    #R is an array of length 901 where every entry is a list of the distance from home to the outfield wall
    #               (step = 900) at every angle 0 to pi/2 as listed in P
    #z is an array of length 901 where every entry is a list of points between 0 and the height of the wall
    #               and where the index of each entry corresponds to a angle from 0 to pi/2
    
           
    # convert from polar coordiates to cartesian
    X, Y = R*np.cos(P), R*np.sin(P)
    ax.plot_surface(-Y,X, np.transpose(z), color = "green")
    plt.xlim(-400, 0)
    plt.ylim(0,400)
    plt.xlabel('y (ft)')
    plt.ylabel('x (ft)')
    fig = plt.gcf()
    fig.set_size_inches(12,6)
    plt.grid(False)
    plt.title(str(title + ' Outfield Wall'))
    ax.set_zlim(0, 150)
    fig.savefig(title)

# =============================================================================
#                   Plotting Overlapped Outfield Walls
# =============================================================================

stads = []
plot_type = 'hei' #'dis' or 'hei'

# walls are plotted in order so we must plot lightgray lines first by adding them to beginning of list
for i in df.index:
    # if plotting outfield wall distance dimensions 
    if plot_type == 'dis':
        #if color of distance line is gray
        if df['dcolor'][i] == 'lightgray':
            #calculate polar coordinate array
            dim = dim_plot(df['distance'][i], df['dform'][i], df['stadium'][i])
            #compile data tuple and add to stad list
            stads.append((df['team'][i], df['stadium'][i], dim, df['dcolor'][i]))
            
    elif plot_type == 'hei':
        # if plotting outfield wall height dimensions 
        if df['hcolor'][i] == 'lightgray':
            # calculate cartesian height dims
            hei = height_plot(df['height'][i], df['stadium'][i])
            # compile height data into tuple and to stad list
            stads.append((df['team'][i], df['stadium'][i], hei, df['hcolor'][i]))

# next add the color lines so they are highlighted at the top
# Note: this alg is the same format as above
for i in df.index:
    if plot_type == 'dis':
        
        if df['dcolor'][i] != 'lightgray':
            dim = dim_plot(df['distance'][i], df['dform'][i], df['stadium'][i])
            stads.append((df['team'][i], df['stadium'][i], dim, df['dcolor'][i]))
            plt.figure(figsize=(10,10)) 
    elif plot_type == 'hei':
        if df['hcolor'][i] != 'lightgray':
            hei = height_plot(df['height'][i], df['stadium'][i])
            stads.append((df['team'][i], df['stadium'][i], hei, df['hcolor'][i]))
            plt.figure(figsize=(12,4)) 


patches = []
for i in stads:
    rad = i[2][0]
    #plots 2D image of wall dimensions
    if i[3] != 'lightgray':
        #add non-gray colors to a list for legend
        patches.append(mpatches.Patch(color = i[3], label = i[0]))
    if plot_type == 'dis':
        y = i[2][1]
        plt.polar(rad, y, color = i[3])
    elif plot_type == 'hei':
        h = i[2][1]
        plt.plot(rad, h, color = i[3])
ax = plt.gca()
#plots piecewise subeqs bounds
plt.title('MLB Outfield Dimensions')
plt.legend(handles=patches, loc = 'upper right')

if plot_type == 'dis':
    plt.ylim(0,450)
    plt.xlim(0,np.pi/2)
    plt.grid(False, axis='y')
    plt.grid(False, axis= 'x')

elif plot_type == 'hei':  
    plt.ylim(0,60)
    plt.xlim(-45,45)
    plt.xlabel('Distance from Centerfield (degrees)')
    plt.ylabel('Height (ft)')

# Modeling each stadium in 3D
for i in df.index:
    dim = dim_plot(df['distance'][i], df['dform'][i], df['stadium'][i])    
    hei = height_plot(df['height'][i], df['stadium'][i])
    fig = model(dim, hei, df['stadium'][i])
    

