# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:28:53 2019

@author: YS15101711
"""
import numpy as np

class Mouse:
    
    # Pond radius
    radius = 1
    speed = 1
    
    def __init__(self, r, th):
        assert r < Mouse.radius, 'position must be within pond radius'
        self.r = r
        self.th = th % (2 * np.pi)
        self.speed = Mouse.speed
        
    def calcRelAngle(self, catTheta):
        angle = (self.theta - catTheta) % (2 * np.pi)
        return angle
    
    def angleAwayFromCat(self, catTheta):
        angle = (np.pi + catTheta) % (2 * np.pi)
        return angle
    
    def moveAwayFromCat(self, catTheta, dt):
        angle = self.angleAwayFromCat(catTheta)
        dr = dr
        dTheta = dTheta
        pass
    
    
def main():
    myMouse = Mouse(0.5, 5)
    angle = myMouse.angleAwayFromCat(5.5)
    print(angle)
    
if __name__ == '__main__':
    main()
    
    