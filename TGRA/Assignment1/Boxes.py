from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL

import random
from random import *

from math import sqrt

from Constants import *

class Box:
    def __init__(self, pos, scale, color):
        self.pos = pos # A (x, y) positional tuple for bottom-left corner of box.
        self.scale = scale # A (width, height) tuple.
        self.color = color # A (R, G, B) triple.
    
    def Draw(self): # Draw the box onto the screen.
        glColor3f(*self.color) # Set color.
        glBegin(GL_TRIANGLE_FAN)
        # 4 corners of the box, in correct order.
        glVertex2f(*self.pos)
        glVertex2f(self.pos[0] + self.scale[0], self.pos[1])
        glVertex2f(self.pos[0] + self.scale[0], self.pos[1] + self.scale[1])
        glVertex2f(self.pos[0], self.pos[1] + self.scale[1])
        glEnd()
    
    def RandomColor(self):
        self.color = (random(), random(), random()) # Random RGB color.

class RoamingBox(Box): # Box which moves on its own.
    def __init__(self, pos, scale, color, vel):
        self.vel = vel # A [vel_x, vel_y] list.
        Box.__init__(self, pos, scale, color) # Otherwise init Box as normal.
    
    def Move(self):
        self.pos = [self.pos[0]  +  self.vel[0], self.pos[1] + self.vel[1]] # Move the box accoring to the velocity.
        for i in range(2): # x, then y.
            if self.pos[i] <= 0 or self.pos[i] + self.scale[i] >= [WINDOW_WIDTH, WINDOW_HEIGHT][i]: # Check whether the box is on or outside the bounds of the screen.
                self.vel[i] = - self.vel[i] # Flip the direction of the velocity.
                self.RandomColor() # Flip color when wall is hit.

class ControlBox(Box): # Box which the player controls.
    def __init__(self, pos, scale, color, speed):
        self.speed = speed # The speed of the box.
        self.dir = [0, 0] # The direction the box want to move. [0, 0] by default.
        Box.__init__(self, pos, scale, color) # Otherwise init Box as normal.

    def Move(self):
        slowdown = self.dir[0] != 0 and self.dir[1] != 0 # True is box is attempting to move in both axes at once.
        newx = self.pos[0] + (self.dir[0] * self.speed / (sqrt(2) if slowdown else 1)) # Get the new cordinates and normalize the speed if slowdown = true, so diagonal speed = horizontal speed.
        newy = self.pos[1] + (self.dir[1] * self.speed / (sqrt(2) if slowdown else 1)) # (also gives the feeling of "scraping" against the wall if moving towards it).
        self.pos = (
            0 if newx < 0 else WINDOW_WIDTH - self.scale[0] if newx + self.scale[0] > WINDOW_WIDTH else newx, # Don't move box outside of bounds.
            0 if newy < 0 else WINDOW_HEIGHT - self.scale[1] if newy + self.scale[1] > WINDOW_HEIGHT else newy,
        )