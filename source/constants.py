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
    "do": "1",
    "re": "2",
    "mi": "3",
    "fa": "4",
    "sol": "5",
    "la": "6",
    "si": "7",

    # accented
    "d1": "q",
    "r1": "w",
    "m1": "e",
    "f1": "r",
    "s1l": "t",
    "l1": "y",
    "s1": "u",

    # controls
    "SPACE": "S",
    "NEWLINE": "R",

    "PLURAL": "P",
    "BACKSPACE": "B",

    "UPSIZE": "U",
    "DOWNSIZE": "D"
}

allinputs = ["do",
             "re",
             "mi",
             "fa",
             "sol",
             "la",
             "si",

             # accented
             "d1",
             "r1",
             "m1",
             "f1",
             "s1l",
             "l1",
             "s1",

             # controls
             "SPACE",
             "NEWLINE",

             "PLURAL",
             "BACKSPACE",

             "UPSIZE",
             "DOWNSIZE"
             ]

wordlengthlimit = 5

pygame_key_map = {
    "backspace": pygame.K_BACKSPACE,
    "tab": pygame.K_TAB,
    "clear": pygame.K_CLEAR,
    "return": pygame.K_RETURN,
    "pause": pygame.K_PAUSE,
    "escape": pygame.K_ESCAPE,
    "space": pygame.K_SPACE,
    "exclaim": pygame.K_EXCLAIM,
    "quotedbl": pygame.K_QUOTEDBL,
    "hash": pygame.K_HASH,
    "dollar": pygame.K_DOLLAR,
    "ampersand": pygame.K_AMPERSAND,
    "quote": pygame.K_QUOTE,
    "left parenthesis": pygame.K_LEFTPAREN,
    "right parenthesis": pygame.K_RIGHTPAREN,
    "asterisk": pygame.K_ASTERISK,
    "plus sign": pygame.K_PLUS,
    "comma": pygame.K_COMMA,
    "minus sign": pygame.K_MINUS,
    "period": pygame.K_PERIOD,
    "forward slash": pygame.K_SLASH,
    "0": pygame.K_0,
    "1": pygame.K_1,
    "2": pygame.K_2,
    "3": pygame.K_3,
    "4": pygame.K_4,
    "5": pygame.K_5,
    "6": pygame.K_6,
    "7": pygame.K_7,
    "8": pygame.K_8,
    "9": pygame.K_9,
    "colon": pygame.K_COLON,
    "semicolon": pygame.K_SEMICOLON,
    "less-than sign": pygame.K_LESS,
    "equals sign": pygame.K_EQUALS,
    "greater-than sign": pygame.K_GREATER,
    "question mark": pygame.K_QUESTION,
    "at": pygame.K_AT,
    "left bracket": pygame.K_LEFTBRACKET,
    "backslash": pygame.K_BACKSLASH,
    "right bracket": pygame.K_RIGHTBRACKET,
    "caret": pygame.K_CARET,
    "underscore": pygame.K_UNDERSCORE,
    "grave": pygame.K_BACKQUOTE,
    "a": pygame.K_a,
    "b": pygame.K_b,
    "c": pygame.K_c,
    "d": pygame.K_d,
    "e": pygame.K_e,
    "f": pygame.K_f,
    "g": pygame.K_g,
    "h": pygame.K_h,
    "i": pygame.K_i,
    "j": pygame.K_j,
    "k": pygame.K_k,
    "l": pygame.K_l,
    "m": pygame.K_m,
    "n": pygame.K_n,
    "o": pygame.K_o,
    "p": pygame.K_p,
    "q": pygame.K_q,
    "r": pygame.K_r,
    "s": pygame.K_s,
    "t": pygame.K_t,
    "u": pygame.K_u,
    "v": pygame.K_v,
    "w": pygame.K_w,
    "x": pygame.K_x,
    "y": pygame.K_y,
    "z": pygame.K_z,
    "delete": pygame.K_DELETE,
    "keypad 0": pygame.K_KP0,
    "keypad 1": pygame.K_KP1,
    "keypad 2": pygame.K_KP2,
    "keypad 3": pygame.K_KP3,
    "keypad 4": pygame.K_KP4,
    "keypad 5": pygame.K_KP5,
    "keypad 6": pygame.K_KP6,
    "keypad 7": pygame.K_KP7,
    "keypad 8": pygame.K_KP8,
    "keypad 9": pygame.K_KP9,
    "keypad period": pygame.K_KP_PERIOD,
    "keypad divide": pygame.K_KP_DIVIDE,
    "keypad multiply": pygame.K_KP_MULTIPLY,
    "keypad minus": pygame.K_KP_MINUS,
    "keypad plus": pygame.K_KP_PLUS,
    "keypad enter": pygame.K_KP_ENTER,
    "keypad equals": pygame.K_KP_EQUALS,
    "up arrow": pygame.K_UP,
    "down arrow": pygame.K_DOWN,
    "right arrow": pygame.K_RIGHT,
    "left arrow": pygame.K_LEFT,
    "insert": pygame.K_INSERT,
    "home": pygame.K_HOME,
    "end": pygame.K_END,
    "page up": pygame.K_PAGEUP,
    "page down": pygame.K_PAGEDOWN,
    "F1": pygame.K_F1,
    "F2": pygame.K_F2,
    "F3": pygame.K_F3,
    "F4": pygame.K_F4,
    "F5": pygame.K_F5,
    "F6": pygame.K_F6,
    "F7": pygame.K_F7,
    "F8": pygame.K_F8,
    "F9": pygame.K_F9,
    "F10": pygame.K_F10,
    "F11": pygame.K_F11,
    "F12": pygame.K_F12,
    "F13": pygame.K_F13,
    "F14": pygame.K_F14,
    "F15": pygame.K_F15,
    "numlock": pygame.K_NUMLOCK,
    "capslock": pygame.K_CAPSLOCK,
    "scrollock": pygame.K_SCROLLOCK,
    "right shift": pygame.K_RSHIFT,
    "left shift": pygame.K_LSHIFT,
    "right control": pygame.K_RCTRL,
    "left control": pygame.K_LCTRL,
    "right alt": pygame.K_RALT,
    "left alt": pygame.K_LALT,
    "right meta": pygame.K_RMETA,
    "left meta": pygame.K_LMETA,
    "left Windows key": pygame.K_LSUPER,
    "right Windows key": pygame.K_RSUPER,
    "mode shift": pygame.K_MODE,
    "help": pygame.K_HELP,
    "print screen": pygame.K_PRINT,
    "sysrq": pygame.K_SYSREQ,
    "break": pygame.K_BREAK,
    "menu": pygame.K_MENU,
    "power": pygame.K_POWER,
    "Euro": pygame.K_EURO
}
