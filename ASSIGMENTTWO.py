"""
@author: Adilhan Koçak 
"""
#This function be able to convert one coordinate system to another one when changed the ax input(RİGHT HANDED)
#input1:[vec] = [1x3]or [3x1]
#input2:[ang] = [angle with degree format]
#input3:[ax] = (1 = x,2 = y,3 = z)
#Adilhan Koçak
import math
def rotation(vec,ang,ax):
    
    #I check the input values to correct values 
    if (len(vec) ==3) and ang>=0 and ang<=360 and ax == 1 or ax == 2 or ax == 3:
        # for convert z axis 
        if ax == 3:
            
            #formulas of z axis to convert
            xp = vec[0]*math.cos(math.radians(ang)) + vec[1]*math.sin(math.radians(ang)) + vec[2]*0
            yp = -vec[0]*math.sin(math.radians(ang)) + vec[1]*math.cos(math.radians(ang)) + vec[2]*0
            zp = vec[0]*0 + vec[1]*0 + vec[2]*1
            
        # for convert y axis
        if ax == 2:
            
            #formulas of x axis to convert
            xp = vec[0]*math.cos(math.radians(ang)) + vec[1]*0 - vec[2]*math.sin(math.radians(ang))
            yp = vec[0]*0 + vec[1]*1 + vec[2]*0
            zp = vec[0]*math.sin(math.radians(ang)) + vec[1]*0 + vec[2]*math.cos(math.radians(ang))
        # for convert x axis
        if ax == 1:
            
            #formulas of x axis to convert
            xp = vec[0]*1 + vec[1]*0 + vec[2]*0
            yp = vec[0]*0 + vec[1]*math.cos(math.radians(ang)) + vec[2]*math.sin(math.radians(ang))
            zp = vec[0]*0 - vec[1]*math.sin(math.radians(ang)) + vec[2]*math.cos(math.radians(ang))
        
        return [xp,yp,zp]
    
    # if angle values -360<angle<0 formulas will be changed so ı change the formulas.
    elif (len(vec) ==3) and 0>=ang and ang>=-360 and ax == 1 or ax == 2 or ax == 3:
        
        #for z axis
        if ax == 3:
            
            #formulas of z axis to convert
            xp = vec[0]*math.cos(math.radians(ang)) + vec[1]*math.sin(math.radians(ang)) + vec[2]*0
            yp = -vec[0]*math.sin(math.radians(ang)) + vec[1]*math.cos(math.radians(ang)) + vec[2]*0
            zp = vec[0]*0 + vec[1]*0 + vec[2]*1
        #for y axis
        
        if ax == 2:
            
            #formulas of y axis to convert
            xp = vec[0]*math.cos(math.radians(ang)) + vec[1]*0 - vec[2]*math.sin(math.radians(ang))
            yp = vec[0]*0 + vec[1]*1 + vec[2]*0
            zp = +vec[0]*math.sin(math.radians(ang)) + vec[1]*0 + vec[2]*math.cos(math.radians(ang))
        #for x axis
        
        if ax == 1:
            
            #formulas of x axis to convert
            xp = vec[0]*1 + vec[1]*0 + vec[2]*0
            yp = vec[0]*0 + vec[1]*math.cos(math.radians(ang)) + vec[2]*math.sin(math.radians(ang))
            zp = vec[0]*0 - vec[1]*math.sin(math.radians(ang)) + vec[2]*math.cos(math.radians(ang))
        return [xp,yp,zp]
    #if user entered wrong input ı should send error messages.
    else:
        print("Check input again ! ")

a = rotation([197.8743692166875, 40.135016557167916, 153.7365098246148],7,2)
print(a)
