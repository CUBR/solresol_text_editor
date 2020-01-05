# key_input

# solresol text editor v0.1. released 5/1/2020 (dd/mm/yyyy)
# all code by CUBE
# all stenograph images by misolsi misido, owner of the la lasiresa discord server

import pygame
import constants as c

class input_processor:
    def __init__(self):
        self.character = ""

    def main(self, event):
        tempchar = ""
        if event.type == pygame.KEYDOWN:
            if event.key in c.inputmap:
                tempchar = c.inputmap[event.key]
            pygame.time.delay(150)

        if tempchar == self.character:
            self.character = ""
        else:
            self.character = tempchar

    def getcharacter(self):
        return self.character
