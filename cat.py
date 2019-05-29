# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:58:59 2019

@author: YS15101711
"""

import numpy as np

class Cat:
    
#    WLOG
    radius = 1
    
    speed = 4
    
    def __init__(self, theta):
        """
        define 0 angle to be North Pole, angles running anticlockwise 
        """
        self.theta = theta % (2 * np.pi)
        self.radius = Cat.radius
        self.speed = Cat.speed
        
    def calcRelAngle(self, mouseTheta):
        """
        Calculates the relative angle between the cat and the mouse, mod 2 * pi
        """
        angle = (self.theta - mouseTheta) % (2 * np.pi)
        return angle
    
    def calcDirection(self, mouseTheta):
        """
        Calculates the sign of the direction of cat movement:
            +1: Anticlockwise
            -1: Clockwise
        """
        angle = self.calcRelAngle(mouseTheta)
        if angle > 0 and angle < np.pi:
            direction = -1
        else:
            direction = 1
        return direction
    
    def chaseMouse(self, mouseTheta, dt):
        """
        Returns new theta position of cat after time interval dt
        """
        direction = self.calcDirection(mouseTheta)
        dTheta = (dt * self.speed ) / self.radius
        newTheta = self.theta + direction * dTheta
        return newTheta
    
def main():
    
    catTheta = 6
    myCat = Cat(catTheta)
    mouseTheta = 4
    dt = 0.01
    iters = 0
    originalDirection = myCat.calcDirection(mouseTheta)
    direction = originalDirection
    while direction == originalDirection:
        print('iter: {}'.format(iters))
        print('Cat Theta: {}'.format(myCat.theta))
        direction = myCat.calcDirection(mouseTheta)
        newTheta = myCat.chaseMouse(mouseTheta, dt)
        myCat = Cat(newTheta)
        iters += 1
        if iters > 100:
            break
        
    
if __name__ == '__main__':
    main()