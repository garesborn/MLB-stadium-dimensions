# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:49:56 2021

@author: Gar
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# =============================================================================
#       A plotting of mlb stadium dimensions based on piecewise functions found
#   here: https://community.fangraphs.com/complete-outfield-dimensions/.
# 
#
#  NOTE: PLEASE SKIP TO LINE 255 FOR EXPLANTION
#
# =============================================================================

dARZ = [(-389.4194,-1.1624467,0,4.9),(423.5471,1.085346,4.9,6.6),(6211.3885,17.49789,6.6,31.7),#(427.9667,.630552,31.7,32.9),(1197.8397,2.9286229,32.9,34),
       (559.10919,1.0073058,31.7,38.9),(-91.557622,-1.10398598,38.9,39.1),
       (571.92441,1.0070058,39.1,50.5),(114.59269,-.76826977,50.5,50.8),(557.962,1.0031979,50.8,57.7),#(403.8808,.3213439,55.7,56.7),(775.17044,1.924966,56.7,57.7),
       (353.793768,.06108017,57.7,82.5),(395.0241,.9533913,82.5,84.2),(327,-.9060869,84.2,90)]

hARZ = [(8,0,0,4.9),(8,1,4.9,6.6),(7.5,0,6.6,31.7),
       (25,0,31.7,57.7),(7.5,0,57.7,82.5),(7.5,1,82.5,84.2),(8,0,84.2,90)]

#==============================================================================

dBAL = [[-1789.977, -5.61943, 0, 25.5], [801.702, 1.83, 25.5, 49], 
       [359.7761, 0.187168, 49, 82], [331, -.396914, 82, 90]]

hBAL = [[21,0,0,16.2],[7,0,16.2,90]]

#==============================================================================

dBOS = [(-119.0423, -.3941798, 0, 3.8),(-402.289, -1.17404, 3.8, 4.9),(-808.953, -2.274195, 4.9, 6),
         (-2332.79083,-6.3601456,6,7.1),(-20759.85313,-55.616,7.1,8.1),(1129.33168,2.875435,8.1,31),
         (-417.143116,-1.8849057,31,33.8),(431.2604,.587157,33.8,52.2),(2077.8716,7.7513156,52.2,53.1),
         (306,.00577087,53.1,90)]
        
hBOS = [(5, 0, 0, 4.9),(5, 1, 4.9, 6),
         (3,0,6,7.1),(3,0,7.1,8.1),(5,0,8.1,31),
         (5,0,31,33.8),(18,0,33.8,53.1),
         (37,0,53.1,90)]

#==============================================================================

dCHC = [[-4499.413, -12.7462, 0, 10.9], [297.1748, 0.636566, 10.9, 13.1], [18363.859, 53.4839, 13.1, 29.4], 
        [[9353823.75, 33.2, 2540504.25, 146.8, 33526.25, 9105.75, 180], [22815.51, 155682], 29.4, 49.2],
        [357.8732, 0.245827, 49.2, 73.2], [496.86435, 1.62768, 73.2, 74.8], [355, 0.112061, 74.8, 90]]

hCHC = [[15,0,0,10.9],[15,1,10.9,13.1],[11.5,0,13.1,73.2],[11.5,1,73.2,74.8],[15,0,74.8,90]]

#==============================================================================

dCLE = [(-1609.844,-4.98404,0,20.3),(906.183,2.2274,20.3,48.2),
        (356.7465,.197554,48.2,78.2),(321,-.303978,78.2,90)] 

hCLE = [(14,0,0,2),(8,0,2,48.2),
        (19,0,48.2,90)]

#==============================================================================

dCWS = [[-7014.6043, -20.939117, 0, 24.1], [1495.6997, 3.92207, 24.1, 30.6], [820.61, 1.88324, 30.6, 36.6], 
       [1969.1759, 5.562717, 36.6, 39.1], [561.4967, 1.00525, 39.1, 50.6], [363.2118, 0.2203438, 50.6, 54], 
       [426.18439, 0.49718, 54, 58.7], [378.8179, 0.259128, 58.7, 63.4], [340.82399, 0.03285, 63.4, 79], [327, -0.177146, 79, 90]]

hCWS = [[8,0,0.0,90.0]]

#==============================================================================

dCIN = [[[11951552.5, 25.2, 8986447.5, 164.8, 41212.25, 30987.75, 190], 
         [19212.09, 168200], 0, 44.7],[436.311, 0.52231577, 44.7, 60.3], [336.435, 0.0014347, 60.3, 86.6], 
        [326, -0.5206991, 86.6, 90]]

hCIN = [[12,0,0,1],[8,0,1,44.7],[12,0,44.7,90]]

#==============================================================================

dCOL = [[-551.417, -1.57548, 0, 1.2], [4061.537, 11.422, 1.2, 37.5], 
        [536.536, 0.84288, 37.5, 60.2], [345, -0.08135, 60.2, 90]]

hCOL = [[17,0,0,17.3],[8,0,17.3,90]]

#==============================================================================

dDET = [[-410, -1.23813, 0, 1.3], [337.21, 'cos', 1.3, 22.5], [-430.4868, -1.6908, 22.5, 24.6], 
        [347.675, 'cos', 24.6, 35.3], [593.97, 1, 35.3, 54], [345, 'sin', 54, 90]]

hDET = [[9,0,0,22.5],[9,1,22.5,24.6],[15,0,24.6,35.3],[9,0,35.3,54],[7,0,54,90]]

#==============================================================================

dHOU = [[-2738.7177, -8.400974, 0, 23], [315.172, 0.493462, 23, 24.1], [-2943.702, -9.23423, 24.1, 35.2], #[310.475, 0.23668, 33.7, 35.2],
        [522,.81,35.2,51.2], 
        [347.579, 0.120368, 51.2, 67.7], [42.673422, -2.124119, 67.7, 67.9], [315, 0.0366002, 67.9, 90]]

hHOU = [[7,0,0,23],[9,0,23,53.6],[25,0,53.6,67.7],[25,1,67.7,67.9],[21,0,67.9,90]]

#==============================================================================

dKC = [[[1738857, 10.1, 495945, 169.9, 5417, 1545, 180], [3671.3, 206082], 0, 5.9],[25650.376, 71.503534, 5.9, 22.1],
       [[19759218, 50.9, 1837968, -76.9, 111634, 10384, -26], [78594.9, 62658], 22.1, 59],
       [[5643864, 68.7, 4885920, -80.7, 16218, 14040, -12], [5740.3, 242208], 59, 76.9],
       [361.884, 0.01803985, 76.9, 82.7], [[958907, 82.6, 322725, -44.6, 2897, 975, 38], [1929, 219122], 82.7, 90]]

hKC = [[8,0,0,90]]

#==============================================================================

dLAA =[[-352.2388, -1.06739, 0, 1.6], [-496.7696, -1.493901, 1.6, 3.2], [-641.02615, -1.9114787, 3.2, 4.8], 
       [-1020.3203, -2.9928111, 4.8, 6.6], [6919.533, 19.3875915, 6.6, 11.2], [1240.50705, 3.314747, 11.2, 42.6], 
       [437.37565, 0.5733725, 42.6, 68], [351.0005, -0.0286525, 68, 84], [340.789, -0.3046164, 84, 85.6], 
       [329.5441, -0.72339596, 85.6, 87], [324.50638, -1.0040283, 87, 88.4], [328, -0.629411, 88.4, 90]]

hLAA = [[5,0,0,6.6],[8,0,6.6,84],[5,0,84,90]]

#==============================================================================

dLAD = [[-443.8081, -1.344873, 0, 4.2], [-829.5118, -2.44985, 4.2, 7.8], [-10942.3745, -30.646819, 7.8, 9.5], 
        [1719.756, 4.622957, 9.5, 25.1], [1115.073, 2.83277, 25.1, 31.1], [928.868, 2.258998, 31.1, 42.6], 
        [742.26267, 1.620443, 42.6, 44], [562.6864, 0.9947777, 44, 46.3], [472.8006, 0.66870534, 46.3, 49.2], 
        [423.6147, 0.478618, 49.2, 55.3], [395.11776, 0.349269, 55.3, 59], [392.2193, 0.3344991, 59, 63.1], 
        [381.7462, 0.2729345, 63.1, 69.2], [372.8431, 0.2051737, 69.2, 74.7], [368.8506, 0.163833, 74.7, 80.5], 
        [362.23, 0.053704, 80.5, 82.1], [353.007, -0.131245, 82.1, 83.3], [334.774, -0.564136, 83.3, 85.6], 
        [333.006, -0.629807, 85.6, 87.2], [328.317, -0.90885, 87.2, 88.4], [330, -0.729958, 88.4, 90]]

hLAD = [[4,0,0,7.8],[4,1,7.8,10.6],[8,0,10.6,80.5],[8,1,80.5,83.3],[4,0,83.3,90]]

#==============================================================================

dMIA = [[-3285.092, -9.80624, 0, 23.7], [5130.955, 14.1917, 23.7, 27.1], [1260.2215, 3.099602, 27.1, 33.1], 
        [928.6866, 2.112672, 33.1, 37.2], [822.69397, 1.78492, 37.2, 41.2], [697.69, 1.380693, 41.2, 44.6], 
        [624.24997, 1.1315557, 44.6, 47.9], [567.2531, 0.927191, 47.9, 51.2], [123.3194, -0.7717922, 51.2, 51.3], 
        [163.1114, -0.618006, 51.3, 51.6], [263.849, -0.2205658, 51.6, 52.3], [333.1776, 0.061447, 52.3, 53.6],
        [333.94836, 0.06472688, 53.6, 55], [391.363, 0.32139203, 55, 56.5], [457.485, 0.630953, 56.5, 59], 
        [389.587, 0.2903055, 59, 60.8], [387.8902, 0.281246, 60.8, 63.6], [367.932, 0.163124, 63.6, 68.2], 
        [360.9411, 0.112519, 68.2, 72.1], [349.332, 0.00931917, 72.1, 79.2], [339.562, -0.137541, 79.2, 84.3], 
        [337, -0.212114, 84.3, 90]] #THESE ARE THE OLD DIMENSIONS

hMIA = [[8.5,0,0,9.8],[11.5,0,9.8,16],[8.5,0,16,53.3],[11.5,0,53.3,65.1],[7,0,65.1,84.9],[11.5,0,84.9,90]]

#==============================================================================

dMIN = [[-2731.998, -8.3292, 0, 20], [1691.285, 4.5671, 20, 38.5], [629.3765, 1.2001, 38.5, 51.2], 
        [382.741, 0.24243, 51.2, 67], [339, -0.05651, 67, 90]]

hMIN = [[23,0,0,38.5],[8,0,38.5,90]]

#==============================================================================

dMIL = [[4068.1011, 11.7916, 0, 16.5], [-60.8626, -0.47706, 16.5, 16.8], [3834.475, 10.73232, 16.8, 23.3], 
        [1042.985, 2.60569, 23.3, 35.5], [-1107.4106, -4.237288, 35.5, 37.7], [566.71123, 1, 37.7, 52.3], 
        [287.52, -0.130068, 52.3, 56.2], [393.82239, 0.374126, 56.2, 74], [358.50448, 0.027826, 74, 85], 
        [344, -0.435742, 85, 90]]

hMIL = [[8,0,0,90]]

#==============================================================================

dNYM = [[-2766.825, -8.3843195, 0, 5.2], [-371.523921, -1.204617, 5.2, 7], [-1855.73071, -5.52645, 7, 18.8], 
        [682.2307, 1.566132, 18.8, 23.3], [-40721.387, -119.6616683, 23.3, 29.5], [1281.67692, 3.1812751, 29.5, 38.2], 
        [575.86589, 0.9960149, 38.2, 49.1], [358.6125, 0.1847292, 49.1, 82.1],[335,-.30194697,82.1,90]]

hNYM = [[8,0,0,90]]

#==============================================================================

dNYY = [[-752.7416, -2.397266, 0, 3.2], [-1341.4764, -4.22849, 3.2, 4.9], [323.639, 'cos', 4.9, 30.6], 
        [2683.6147, 7.700602, 30.6, 36.1], [913.27186, 2.139572, 36.1, 40.4], [707.36801, 1.4643105, 40.4, 44.4], 
        [600.6388, 1.096466, 44.4, 48.4], [496.311752, 0.7103813, 48.4, 52.1], [445.2994, 0.5053365, 52.1, 56.7], 
        [390.30014, 0.2548946, 56.7, 62.8], [345.39856, 0.001719809, 62.8, 80.6], [324.4985, -0.3638949, 80.6, 84.8], 
        [316, -0.6421425, 84.8, 90]]

hNYY = [[8,0,0,90]]

#==============================================================================

dOAK = [[-868.87639, -2.632959, 0, 12], [911.9339, 2.32779, 12, 22.3], [1753.07386, 4.853163, 22.3, 33.8], 
        [1043.552, 2.617999, 33.8, 40.8], [558.5246, 1, 40.8, 49.2], [398.6068, 0.381971, 49.2, 56.2], 
        [361.22296, 0.2060512, 56.2, 67.7], [391.759586, 0.429592, 67.7, 78], [330, -0.3798, 78, 90]]

hOAK = [[8, 0, 0, 12], [15, 0, 12, 33.8],
        [8, 0, 33.8, 56.2], [15, 0, 56.2, 78], [8, 0, 78, 90]]

#==============================================================================

dPHI = [[330, 'cos', 0, 34.3], [644.15, 1.277017, 34.3, 50.7], [308.591, -0.02468, 50.7, 55.9], 
        [543.4657, 1.08071, 55.9, 59.3], [331, 'sin', 59.3, 88.3], [325, -0.596191, 88.3, 90]]

hPHI = [[13,0,0,34.3],[6,0,34.3,50.7],[19,0,50.7,53.2], [19,1,53.2,55.9],[11,0,55.9,90]]

#==============================================================================

dPIT = [[-1759.947, -5.4827, 0, 22.3], [1120.146, 2.8184, 22.3, 34.1], [716.884, 1.56, 34.1, 44.3], 
        [478.809, 0.71785, 44.3, 58.5], [-4560.837, -24.0136, 58.5, 59.6], [366.846, 0.089958, 59.6, 81.5], 
        [321, -0.75751, 81.5, 90]]

hPIT = [[21, 0, 0, 22.3], [10, 0, 22.3, 59.6], [6, 0, 59.6, 90]]

#==============================================================================

dSDP = [[321.433, 'cos', 0, 3.4], [-311.7359, -1.029242, 3.4, 7.2], [346.87116, 'cos', 7.2, 27.8], 
        [1425.7353, 3.59492, 27.8, 31.8], [740.2202, 1.568309, 31.8, 38.3], [543.05468, 0.9402139, 38.3, 49.2], 
        [318.3662, 0.0718681, 49.2, 50.4], [539.44852, 0.9611939, 50.4, 56.2], [393.566469, 0.2972994, 56.2, 63.5], 
        [344.316, 0.0091096, 63.5, 83.8], [336, -0.2134522, 83.8, 90]]

hSDP = [[11,1,0,3.4],[8,0,3.4,90]]

#==============================================================================

dSFG = [[-697.339, -2.25676, 0, 15], [946.0859, 2.4155, 15, 18], [-712.5915, -2.389, 18, 26], 
       [565, 1.025, 26, 55], [347.526, 0.07905, 55, 86.5], [335, -0.513097, 86.5, 90]]

hSFG = [[25, 0, 0, 15], [25, 1, 15, 18], [20, 0, 18, 26], 
       [8, 0, 26, 90]]

#==============================================================================

dSEA = [[-3502.437, -10.74367, 0, 26.5], [825.224, 1.9153, 26.5, 47], [414.291, 0.427476, 47, 59.6], 
        [377.4922, 0.2382, 59.6, 66.5], [336.559, -0.037016, 66.5, 88.5], [331, -0.6671, 88.5, 90]]

hSEA = [[8,0,0,90]]

#==============================================================================

dSTL = [[-436.689, -1.3173, 0, 3.3], [346.303, 'cos', 3.3, 25.6], [857.076, 1.995805, 25.6, 39.9], 
       [569.534, 1.04571, 39.9, 50], [434.192, 0.514, 50, 64], [346.76, 'sin', 64, 88.4], [330, -1.73033, 88.4, 90]]

hSTL = [[8,0,0,90]]

#==============================================================================

dTEXold = [[-432.031, -1.3252, 0, 4], [343.5, 'cos', 4, 24], [543.706, 1.1376, 24, 26.1], [336.22, 'cos', 26.1, 34.3], [565.81, 1, 34.3, 53.1], [416.6997, 0.38598, 53.1, 64.3], [349.203, 'sin', 64.3, 84.2], [331, -0.51319, 84.2, 90]]

#==============================================================================

dTB = [[-357.101, -1.109, 0, 1.7], [331, 'cos', 1.7, 33.7], [1678.156, 4.403, 33.7, 36.2], [596.756, 1.09406, 36.2, 55], 
       [275.103, -0.2654, 55, 56.4], [477.013, 0.6444, 56.4, 58], [342.43, 0.011121, 58, 86], [315, -1.13533, 86, 90]]

hTB = [[9,0,0,1.7],[11.5,0,1.7,33.7],[9,0,33.7,58],[11.5,0,58,86],[5,0,86,90]]

#==============================================================================

dTOR = [[-1725.1974, -5.2597, 0, 20], [2160.354, 5.7667, 20, 32.5], [400, 'con', 32.5, 57.5], 
        [374.6429, 0.17341, 57.5, 70], [328, -0.19012, 70, 90]]

hTOR = [[10,0,0,90]]

#==============================================================================

dWSN = [[-1192.9, -3.56091, 0, 13.1], [1018.837, 2.609847, 13.1, 46.5], [372.8599, 0.286983, 46.5, 57.9], 
        [1089.6378, 3.903208, 57.9, 59], [383.87617, 0.297133, 59, 74.1], [163.401, -1.88975, 74.1, 74.2], 
        [377.1893, 0.261412, 74.2, 76.5], [336, -0.221987, 76.5, 90]]

hWSN = [[16, 0, 0, 2],[9, 0, 2, 13.1], [14, 0, 13.1, 40.0], [9, 0, 40, 46.8], [10, 0, 46.8,59], 
        [9, 0, 59, 90]]


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

#the following is a dictionary compiling each team's stadium, piecewise fncts
#for both wall distance and wall height, and the format code for wall height subeqs.

teams = {
    #key    Stadium name            dis functs hei functs  dform     graph colors
    'ARZ':('Chase Field',               dARZ,    hARZ,       0, 'lightgray', 'red'), 
    'BAL':('Camden Yards',              dBAL,    hBAL,       0, 'lightgray', 'lightgray'),
    'BOS':('Fenway Park',               dBOS,    hBOS,       0, 'green',     'green'),
    'CHC':('Wrigley Field',             dCHC,    hCHC,       1, 'lightgray', 'lightgray'), 
    'CWS':('US Cellular Field',         dCWS,    hCWS,       0, 'lightgray', 'lightgray'), # 5
    'CIN':('Great American Ballpark',   dCIN,    hCIN,       1, 'lightgray', 'lightgray'),
    'CLE':('Progressive Field',         dCLE,    hCLE,       0, 'lightgray', 'lightgray'),
    'COL':('Coors Field',               dCOL,    hCOL,       0, 'purple',    'lightgray'),
    'DET':('Comerica Park',             dDET,    hDET,       2, 'blue',      'lightgray'),
    'HOU':('Minute Maid Park',          dHOU,    hHOU,       1, 'lightgray', 'lightgray'), # 10
    'KC' :('Kauffman Stadium',          dKC,     hKC,        1, 'lightgray', 'lightgray'),
    'LAA':('Angel Stadium',             dLAA,    hLAA,       0, 'lightgray', 'lightgray'),
    'LAD':('Dodger Stadium',            dLAD,    hLAD,       0, 'lightgray', 'blue'),
    'MIA':('Marlins Park',              dMIA,    hMIA,       0, 'lightgray', 'lightgray'),
    'MIL':('Miller Park',               dMIL,    hMIL,       0, 'lightgray', 'lightgray'), #15
    'MIN':('Target Field',              dMIN,    hMIN,       0, 'lightgray', 'lightgray'),
    'NYM':('Citi Field',                dNYM,    hNYM,       0, 'lightgray', 'lightgray'),
    'NYY':('Yankee Stadium',            dNYY,    hNYY,       2, 'black',     'lightgray'),
    'OAK':('RingCentral Coliseum',      dOAK,    hOAK,       0, 'lightgray', 'lightgray'),
    'PHI':('Citizens Bank Park',        dPHI,    hPHI,       2, 'lightgray', 'black'), #20
    'PIT':('PNC Park',                  dPIT,    hPIT,       0, 'lightgray', 'lightgray'),
    'SDP':('Petco Park',                dSDP,    hSDP,       2, 'lightgray', 'lightgray'),
    'SFG':('Oracle Park',               dSFG,    hSFG,       0, 'orange',    'orange'),
    'SEA':('Safeco Field',              dSEA,    hSEA,       0, 'lightgray', 'lightgray'), 
    'STL':('Busch Stadium',             dSTL,    hSTL,       2, 'lightgray', 'lightgray'), #25
    'TB' :('Tropicana Field',           dTB,     hTB,        2, 'lightgray', 'lightgray'),
    'TOR':('Rogers Centre',             dTOR,    hTOR,       2, 'lightgray', 'lightgray'),
    'WSN':('Nationals Park',            dWSN,    hWSN,       0, 'red',       'lightgray')
    }

stads = []

# =============================================================================
#  Function plotting distance of outfield wall at any given angle through polar coordinates
# =============================================================================
def dim_plot(wall_distance, dform, title, plot = False):

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
    fig.savefig(teams[var][0])

# =============================================================================
# plot_type = 'dis' #'dis' or 'hei'
# for i in teams:
#     var = i
#     if plot_type == 'dis':
#         
#         if teams[var][4] == 'lightgray':
#             dim = dim_plot(teams[var][1], teams[var][3], teams[var][0])
#             stads.append((i, teams[var][0], dim, teams[var][4]))
#             
#     elif plot_type == 'hei':
#         if teams[var][5] == 'lightgray':
#             hei = height_plot(teams[var][2], teams[var][0])
#             stads.append((i, teams[var][0], hei, teams[var][5]))
#             #model(dim, hei, teams[var][0])
#     
# for i in teams:
#     var = i
#     if plot_type == 'dis':
#         
#         if teams[var][4] != 'lightgray':
#             dim = dim_plot(teams[var][1], teams[var][3], teams[var][0])
#             stads.append((i, teams[var][0], dim, teams[var][4]))
#             plt.figure(figsize=(10,10)) 
#     elif plot_type == 'hei':
#         if teams[var][5] != 'lightgray':
#             hei = height_plot(teams[var][2], teams[var][0])
#             stads.append((i, teams[var][0], hei, teams[var][5]))
#             plt.figure(figsize=(12,4)) 
#             #model(dim, hei, teams[var][0])
# 
# 
# patches = []
# for i in stads:
#     rad = i[2][0]
#     
#     #plots 2D image of wall dimensions
#     if i[3] != 'lightgray':
#         patches.append(mpatches.Patch(color = i[3], label = i[0]))
#     if plot_type == 'dis':
#         y = i[2][1]
#         plt.polar(rad, y, color = i[3])
#     elif plot_type == 'hei':
#         h = i[2][1]
#         plt.plot(rad,h, color = i[3])
# ax = plt.gca()
# #plots piecewise subeqs bounds
# plt.title('MLB Outfield Dimensions')
# plt.legend(handles=patches, loc = 'upper right')
# 
# if plot_type == 'dis':
#     plt.ylim(0,450)
#     plt.xlim(0,np.pi/2)
#     plt.grid(False)
# 
# elif plot_type == 'hei':  
#     plt.ylim(0,60)
#     plt.xlim(-45,45)
#     plt.xlabel('Distance from Centerfield (degrees)')
#     plt.ylabel('Height (ft)')
# =============================================================================
    
# =============================================================================
# for i in teams:
#     var = i
#     dim = dim_plot(teams[var][1], teams[var][3], teams[var][0])
#     hei = height_plot(teams[var][2], teams[var][0])
#     fig = model(dim, hei, teams[var][0])
# =============================================================================
    

