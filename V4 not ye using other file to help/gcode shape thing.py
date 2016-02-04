# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:03:46 2015

@author: Conor
"""

def gcodeMaker(number,origin):
    output = "G1 X{0} Y{1} Z{2} F{3}"
    counter = 0
    z = 0.1
    fn = "produced tab gcodes.txt"
#    print "Boundary points"
#    print "1: {0}, {1}".format(edge,(edge + origin))
#    print "2: {0}, {1}".format(edge,((-1 * edge)+origin))
#    print "3: {0}, {1}".format((-1 * edge),(edge + origin))
#    print "4: {0}, {1}".format((-1 * edge),((-1 * edge)+origin))
    with open(fn, 'w') as out:
        out.write('\n')

    for i in range (0, 3):
        #draw outline
        #Make outline here
        with open(fn, 'a+') as out:
            x = xoutline1[0]
            y = youtline1[0]
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(x,y,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
        #M101 turns it on, G1 = move
            for i in range(0, len(xoutline1)):
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xoutline1[i],youtline1[i],z))
            out.write("\nG1 F1200.0 \nG1 F1080.0 \nM103")
            x = xoutline2[0]
            y = youtline2[0]
            out.write( "\nG1 X{0} Y{1} Z{2} F3360.0".format(x,y,z))
            out.write("\nG1 F1200.0  \nG1 F3360.0 \nM101")
        #M101 turns it on, G1 = move
            out.write( "\nG1 X{0} Y{1} Z{2} F2100.0".format(x,y,z))
            for i in range(0, len(xoutline2)):
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xoutline2[i],youtline2[i],z))
            out.write("\nG1 F1200.0  \nG1 F1080.0 \nM103")
            for i in range (0, 1):
                n = 2 * i
                m = n + 1
                out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xInfill1[(n)],yInfill1[(n)],z))
                out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill1[m],yInfill1[m],z))
                out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            pos = 0
            for i in range (0, len(xMove2)):
                out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove2[i],yMove2[i],z))
                out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill2[pos],yInfill2[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill2[pos],yInfill2[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill2[pos],yInfill2[pos],z))
                pos += 1
                out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
                
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove3,yMove3,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            for i in range (0, len(xInfill3)):
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill3[i],yInfill3[i],z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            pos = 0
            for i in range (0, len(xMove4)):
                out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove4[i],yMove4[i],z))
                out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill4[pos],yInfill4[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill4[pos],yInfill4[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill4[pos],yInfill4[pos],z))
                pos += 1
                out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove5,yMove5,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill5,yInfill5,z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove6,yMove6,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill6[0],yInfill6[0],z))
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill6[1],yInfill6[1],z))
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill6[2],yInfill6[2],z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove7,yMove7,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            for i in range (0, len(xInfill7)):
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill7[i],yInfill7[i],z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            pos = 0
            for i in range (0, len(xMove8)):
                out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove8[i],yMove8[i],z))
                out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill8[pos],yInfill8[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill8[pos],yInfill8[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill8[pos],yInfill8[pos],z))
                pos += 1
                out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
                
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove9,yMove9,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            for i in range (0, len(xInfill9)):
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill9[i],yInfill9[i],z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            
            pos = 0
            for i in range (0, len(xMove10)):
                out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove10[i],yMove10[i],z))
                out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill10[pos],yInfill10[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill10[pos],yInfill10[pos],z))
                pos += 1
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill10[pos],yInfill10[pos],z))
                pos += 1
                out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove11,yMove11,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill11,yInfill11,z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            
            pos = 0
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove12,yMove12,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill12[pos],yInfill12[pos],z))
            pos += 1
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill12[pos],yInfill12[pos],z))
            pos += 1
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill12[pos],yInfill12[pos],z))
            pos += 1
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
                
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove13,yMove13,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            for i in range (0, len(xInfill13)):
                out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill13[i],yInfill13[i],z))
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            
            pos = 0
            out.write("\nG1 X{0} Y{1} Z{2} F3360.0".format(xMove14,yMove14,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill14[pos],yInfill14[pos],z))
            pos += 1
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill14[pos],yInfill14[pos],z))
            pos += 1
            out.write("\nG1 X{0} Y{1} Z{2} F2100.0".format(xInfill14[pos],yInfill14[pos],z))
            pos += 1
            out.write("\nG1 F1200.0  \nG1 F2100.0 \nM103")
            out.write("\nG4 P3000")
            
                
        z += 0.2

xoutline1 = [-57.21,-37.51,-35.8,-34.09,-32.41,-30.75,-29.13,
             -27.55,-24.74,-24.18,-22.63,-20.97,-19.25,-18.37,
             -17.04,16.51,18.28,20.03,21.72,23.34,26.13,27.66,29.25,
             30.87,32.53,34.22,35.92,37.64,57.21,57.21,36.76,35.05,
             33.35,31.68,30.03,28.43,26.87,23.12,21.49,19.79,18.91,
             17.58,-16.5,-18.6,-20.34,-22.03,-23.62,-24.73,-27.37,
             -28.94,-30.56,-32.21,-33.9,-35.6,-37.31,-57.21,-57.21]
             
youtline1 = [-9.29,-9.29,-9.19,-8.97,-8.64,-8.19,-7.63,-6.96,
             -5.43,-5.05,-4.18,-3.52,-3.06,-2.92,-2.8,-2.79,-2.9,
             -3.26,-3.81,-4.57,-6.25,-7.03,-7.69,-8.25,-8.69,-9.01,
             -9.22,-9.31,-9.31,9.2,9.26,9.11,8.84,8.46,7.96,7.35,
             6.63,4.43,3.7,3.18,3,2.84,2.81,2.97,3.35,3.94,4.74,
             5.45,6.89,7.58,8.15,8.62,8.96,9.19,9.3,9.31,-9.29]
             
xoutline2 = [-56.81,-35.84,-34.16,-32.5,-30.87,-29.27,-27.73,
             -22.8,-21.1,-19.34,-17.05,16.53,18.33,20.13,21.87,23.52,
             26.33,27.83,29.39,30.99,32.62,34.28,35.96,56.81,56.81,
             36.77,35.09,33.43,30.16,27.06,23.3,21.63,19.89,17.61,
             -16.52,-18.66,-20.45,-22.18,-27.55,-29.09,-30.68,-32.31,
             -33.96,-35.64,-56.81,-56.81]
             
youtline2 = [-8.89,-8.79,-8.58,-8.25,-7.81,-7.25,-6.59,-3.82,-3.14,
             -2.67,-2.4,-2.39,-2.53,-2.87,-3.44,-4.22,-5.9,-6.66,
             -7.32,-7.86,-8.3,-8.62,-8.82,-8.91,8.89,8.86,8.71,8.45,
             7.58,6.27,4.08,3.33,2.79,2.44,2.41,2.58,2.96,3.57,6.53,
             7.21,7.77,8.23,8.57,8.79,8.91,-8.89]
             
xInfill1 = [-34.98,-56.52,-56.53,-19.39]
#move to first position, turn on, move to second, turn off, repeat.
yInfill1 = [-8.4,-8.4,-2.4,-2.4]

xInfill2 = [-56.53,-56.53,-22.0,-56.53,-56.53,-23.68,
            -56.53,-56.53,-25.1,-56.53,-56.53,-26.52,
            -56.53,-56.53,-27.99,-56.53,-56.53,-29.97,
            -56.53,-56.53,-32.68]
#move, do three points, turn off, move to a point, turn back on and do 3 more
yInfill2 = [-2.8,-3.2,-3.2,-3.6,-4.0,-4.0,
            -4.4,-4.8,-4.8,-5.2,-5.6,-5.6,
            -6.0,-6.4,-6.4,-6.8,-7.2,-7.2,
            -7.6,-8.0,-8.0]

xMove2 = [-20.92,-22.97,-24.39,-25.81,-27.24,-28.92,-31.18]
yMove2 = [-2.8,-3.6,-4.4,-5.2,-6.0,-6.8,-7.6]
          
#turn on, print the following points and then tune off at the end
xMove3 = -22.87
yMove3 = 3.6
xInfill3 = [-56.53,-56.53,-23.7,-24.37,-56.53,
            -56.53,-25.04,-25.7,-56.53,-56.53,-26.37]

yInfill3 = [3.6,4.0,4.0,4.4,4.4,4.8,4.8,5.2,5.2,5.6,5.6]

#go to point, then 3 at  time again

xMove4 = [-27.13,-28.88,-31.09]

yMove4 = [6.0,6.8,7.6]

xInfill4 = [-56.53,-56.53,-27.94,-56.53,-56.53,-29.89,-56.53,-56.53,-32.6]

yInfill4 = [6.0,6.4,6.4,6.8,7.2,7.2,7.6,8.0,8.0]
xMove5 = -34.78
yMove5 = 8.4
xInfill5 = -56.53
yInfill5 = 8.4

xMove6 = -20.8
yMove6 = 2.8
xInfill6 = [-56.53,-56.53,-22.01]
yInfill6 = [2.8,3.2,3.2]

xMove7 = 19.21
yMove7 = -2.4
xInfill7 = [56.53,56.53,-56.53,-56.53,56.53,56.53,
            -56.53,-56.53,56.53,56.53,-56.53,-56.53,
            56.53,56.53,-56.53,-56.53,56.53,56.53,
            -56.53,-56.53,56.53,56.53,-56.53,-56.53,
            -19.14]
yInfill7 = [-2.4,-2.0,-2.0,-1.6,-1.6,-1.2,-1.2,
            -0.8,-0.8,-0.4,-0.4,0.0,0.0,0.4,0.4,
            0.8,0.8,1.2,1.2,1.6,1.6,2.0,2.0,2.4,2.4]
            
#back to threes
xMove8 = [19.25,22.05]
yMove8 = [2.4,3.2]
xInfill8 = [56.53,56.53,20.87,56.53,56.53,22.91]
yInfill8 = [2.4,2.8,2.8,3.2,3.6,3.6]       

xMove9 = 23.73
yMove9 = 4.0
xInfill9 = [56.53,56.53,24.37,25.0,56.53,56.53,25.72]
yInfill9 = [4.0,4.4,4.4,4.8,4.8,5.2,5.2]
xMove10 = [26.45,28.0,29.97,32.71,28.88,31.12]
yMove10 = [5.6,6.4,7.2,8.0,-6.8,-7.6]
xInfill10 = [56.53,56.53,27.18,56.53,56.53,28.9,
            56.53,56.53,31.19,56.53,56.51,34.96,
            56.53,56.53,29.88,56.53,56.53,32.63]
yInfill10 = [5.6,6.0,6.0,6.4,6.8,6.8,
            7.2,7.6,7.6,8.0,8.4,8.4,
            -6.8,-7.2,-7.2,-7.6,-8.0,-8.0]
            
            

xMove11 = 34.73
yMove11 = -8.4
xInfill11 = 56.53
yInfill11 = -8.4

xMove12 = 27.13
yMove12 = -6.0
xInfill12 = [56.53,56.53,27.96]
yInfill12 = [-6.0,-6.4,-6.4]

xMove13 = 22.92
yMove13 = -3.6
xInfill13 = [56.53,56.53,23.68,24.36,56.53,56.53,
             25.04,25.72,56.53,56.53,26.4]
yInfill13 = [-3.6,-4.0,-4.0,-4.4,-4.4,-4.8,-4.8,
             -5.2,-5.2,-5.6,-5.6]

xMove14 = 20.87
yMove14 = -2.8
xInfill14 = [56.53,56.53,21.96]
yInfill14 = [-2.8,-3.2,-3.2]

            
            
            
gcodeMaker(1,0)
