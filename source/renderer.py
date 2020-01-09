# renderer

# solresol text editor v0.1. released 5/1/2020 (dd/mm/yyyy)
# all code by CUBE
# all stenograph images by misolsi misido, owner of the la lasiresa discord server

from constants import *

def numbers_to_text(word):
    numbers = list(word)

    for x in range(len(numbers)):
        numbers[x] = numbers_table[numbers[x]]

    newword = ""

    newword = newword.join(numbers)

    return newword


class renderer:
    def __init__(self, screen):
        self.screen = screen
        self.mainarray = []

        self.scale = 0.5

        self.cursorpos = 0
        self.cursorimg = pygame.image.load("ui_assets/cursor.png")

    def process_input(self, keypress):
        # print(keypress)
        if keypress != "":
            if keypress in controlchars:
                self.mainarray.append(keypress)

            elif len(self.mainarray) == 0 and keypress in letterchars:
                self.mainarray.append(keypress)

            elif keypress in letterchars:
                lastword = self.mainarray[-1]

                if lastword in controlchars:
                    self.mainarray.append(keypress)

                elif len(lastword) == wordlengthlimit:
                    self.mainarray.append("S")
                    self.mainarray.append(keypress)

                elif len(lastword) < wordlengthlimit:
                    self.mainarray[-1] += keypress

            elif keypress == "P":
                lastword = self.mainarray[-1]
                lastword = list(lastword)

                lastword[-1] = plural_table[lastword[-1]]

                final = ""

                for x in range(len(lastword)):
                    final += lastword[x]

                self.mainarray[-1] = final
                self.mainarray.append("S")

            elif keypress == "B" and len(self.mainarray) > 0:
                lastword = self.mainarray[-1]
                lastword = list(lastword)
                lastword = lastword[:-1]
                lastword = "".join(lastword)

                self.mainarray[-1] = lastword

                if self.mainarray[-1] == "":
                    del self.mainarray[-1]

            elif keypress == "U":
                self.scale += 0.1

            elif keypress == "D":
                self.scale += -0.1

    def main(self):
        xpos = 5
        ypos = 0

        height = 0

        words = self.mainarray

        size = len(words)

        x = 0

        while x < size != 0:

            # print(words)

            word = words[x]
            characters = []

            if word not in controlchars:
                # print(word)

                try:
                    characters = [pygame.image.load("glyphs_renamed/" + numbers_to_text(word) + ".png")]

                except pygame.error as message:
                    characters = []
                    letters = list(word)
                    for letter in letters:
                        characters.append(pygame.image.load("glyphs_renamed/" + numbers_to_text(letter) + ".png"))

                for character in characters:
                    # print(character)

                    character = pygame.transform.scale(character,
                                                       (int(self.scale*character.get_width()),
                                                        int(self.scale*character.get_height())))

                    if xpos + character.get_width() > self.screen.get_width():
                        ypos += (height + 5)
                        xpos = 5

                    self.screen.blit(character, (xpos, ypos))
                    xpos += (character.get_width() + 5)

                    if character.get_height() > height:
                        height = character.get_height()

            elif word in controlchars:
                if word == "S":
                    xpos += 20

                if word == "R":
                    ypos += (height + 5)
                    xpos = 5

            x += 1
