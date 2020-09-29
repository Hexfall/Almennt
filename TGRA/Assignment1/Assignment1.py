import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL

import random
from random import *

from Constants import WINDOW_HEIGHT, WINDOW_WIDTH

from Boxes import Box, RoamingBox, ControlBox

def init_game():
    pygame.display.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def update(): # Called once every frame
    RoamBox.Move() # Move the roaming box.
    ContBox.Move() # Move the controlled box.

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    
    for box in clickboxes + boxes: # Draw all boxes. Mouse boxes first (Since the other two are more "important").
        box.Draw()

    pygame.display.flip()

def game_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            parse_input(event.key, True)
        elif event.type == pygame.KEYUP:
            parse_input(event.key, False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                spawn_box(pygame.mouse.get_pos()) # Spawn box on click.

    update()
    display()

def spawn_box(pos):
    pos = (
        pos[0],
        WINDOW_HEIGHT - pos[1],
    ) # Screen is measured bottom-up, mouse position is top-down. Compensating for this difference.
    length = 50
    b = Box((pos[0] - length / 2, pos[1] - length / 2), (length, length), ())
    b.RandomColor() # Give the new box a random colour.
    clickboxes.append(b) # Keep a reference to the box.

def quit_game():
    pygame.quit()
    quit()

def parse_input(key, down = True):
    if key == K_ESCAPE:
        quit_game()
    elif key == K_UP: # Begin moving in direction if button is down, undo if button is up.
        ContBox.dir[1] += 1 if down else -1
    elif key == K_DOWN:
        ContBox.dir[1] += -1 if down else 1
    elif key == K_RIGHT:
        ContBox.dir[0] += 1 if down else -1
    elif key == K_LEFT:
        ContBox.dir[0] += -1 if down else 1

RoamBox = RoamingBox((WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50), (100, 100), (0.0, 1.0, 0.0), [0.5, 0.5])
ContBox = ControlBox((WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50), (100, 100), (0.0, 0.0, 1.0), 1)
boxes = [RoamBox, ContBox]
clickboxes = []

if __name__ == "__main__":
    init_game()
    while True:
        game_loop()