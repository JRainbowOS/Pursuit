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
        # Resorting to Cartesians...
        dx = - self.speed * dt * np.sin(angle) - self.r * np.sin(self.th)
        dy = self.speed * dt * np.cos(angle) + self.r * np.cos(self.th)
        
        newTh = np.arctan2(dx, dy) % (2 * np.pi)
        newR = np.sqrt(dx ** 2 + dy ** 2)
        return newTh, newR
    
    
def main():
    myMouse = Mouse(0.5, 3 * np.pi / 2)
    angle = myMouse.angleAwayFromCat(0)
    newTh, newR = myMouse.moveAwayFromCat(np.pi, 0.1)
    print(angle)
    print(newTh, newR)

    
if __name__ == '__main__':
    main()
    
    