# constants
# solresol text editor v0.1. released 5/1/2020 (dd/mm/yyyy)
# all code by CUBE
# all stenograph images by misolsi misido, owner of the la lasiresa discord server

import pygame

numbers_table = {
    # normal
    "1": "do",
    "2": "re",
    "3": "mi",
    "4": "fa",
    "5": "sol",
    "6": "la",
    "7": "si",

    # accented
    "q": "d1",
    "w": "r1",
    "e": "m1",
    "r": "f1",
    "t": "s1l",
    "y": "l1",
    "u": "s1",

    # plural normal
    "a": "ddo",
    "s": "rre",
    "d": "mmi",
    "f": "ffa",
    "g": "ssol",
    "h": "lla",
    "j": "ssi",

    # plural accented
    "z": "dd1",
    "x": "rr1",
    "c": "mm1",
    "v": "ff1",
    "b": "ss1l",
    "n": "ll1",
    "m": "ss1"
}

plural_table = {
    # normal
    "1": "a",
    "2": "s",
    "3": "d",
    "4": "f",
    "5": "g",
    "6": "h",
    "7": "j",

    # accented
    "q": "z",
    "w": "x",
    "e": "c",
    "r": "v",
    "t": "b",
    "y": "n",
    "u": "m"
}

controlchars = ["S", "R"]

letterchars = ["1", "2", "3", "4", "5", "6", "7",
               "q", "w", "e", "r", "t", "y", "u"]

inputmap = {
    # normal
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",

    # accented
    pygame.K_q: "q",
    pygame.K_w: "w",
    pygame.K_e: "e",
    pygame.K_r: "r",
    pygame.K_t: "t",
    pygame.K_y: "y",
    pygame.K_u: "u",

    # controls
    pygame.K_SPACE: "S",
    pygame.K_RETURN: "R",

    pygame.K_p: "P",
    pygame.K_BACKSPACE: "B",

    pygame.K_UP: "U",
    pygame.K_DOWN: "D"
}
