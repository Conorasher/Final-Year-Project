# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:03:46 2015

@author: Conor
"""

def gcodeMaker(length,height,origin):
    output = "G1 X{0} Y{1} Z{2} F{3}"
    edge = float(length / 2)
    edge -= 0.2
    counter = 0
    n = height * 5
    z = 0.1
    fn = "gcodes.txt"
    print "Boundary points"
    print "1: {0}, {1}".format(edge,(edge + origin))
    print "2: {0}, {1}".format(edge,((-1 * edge)+origin))
    print "3: {0}, {1}".format((-1 * edge),(edge + origin))
    print "4: {0}, {1}".format((-1 * edge),((-1 * edge)+origin))
    with open(fn, 'w') as out:
        out.write('\n')

    for i in range (0, 3):
        #draw outline
        x = (-1 * edge)
        y = (-1 * edge) + origin
        with open(fn, 'a+') as out:
            out.write("\n \nG1 X{0} Y{1} Z{2} F3360.0".format(x,y,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
        #M101 turns it on, G1 = move
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            x *= -1 
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            y *= -1
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            x *= -1 
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            y *= -1 
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            out.write("\nG1 F1200.0 \nG1 F1080.0 \nM103")
            x = (-1 * (edge - 0.4))
            y = (-1 * (edge - 0.4))
            out.write( "\n \nG1 X{0} Y{1} Z{2} F3360.0".format(x,y,z))
            out.write("\nG1 F1200.0  \nG1 F3360.0 \nM101")
        #M101 turns it on, G1 = move
            out.write( "\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            x *= -1 
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            y *= -1
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            x *= -1 
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            y *= -1 
            out.write("\nG1 X{0} Y{1} Z{2} F1080.0".format(x,y,z))
            out.write("\nG1 F1200.0  \nG1 F1080.0 \nM103")
        
            x = (edge - 0.8)
            y = (edge - 0.8)
            out.write("\n \nG1 X{0} Y{1} Z{2} F3360.0".format(x,y,z))
            out.write("\nG1 F1200.0 \nG1 F3360.0 \nM101")
            x *= -1 
            while x <= (edge - 0.8):
                out.write("\nG1 X{0} Y{1} Z{2} F2160.0".format(x,y,z))
                x += 0.2
                counter += 1
                if counter == 2:
                    counter = 0
                    y *= -1
            out.write("\nG1 F1200.0 \nG1 F2160.0 \nM103")
        z += 0.2
            
    
    
gcodeMaker(20,5,10)