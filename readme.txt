solresol text editor v0.1 by CUBE, 05/01/2020

all the source code is in the source folder, along with the script to convert the filenames
for misolsi misido's stenographs and remove the accents so it'll work.
run main.py to run the program

to add more stenographs, just put them into the glyphs_renamed folder and then run the script
you might need to change the folder it uses in the script but it's a tiny thing and just a variable at the top

the compiled folder contains a compiled version of the program (compiled using pyinstaller),
it should run on any machine regardless if python is installed though i have only tested it on windows 10
just run solresol_text_editor.exe


keybindings for the program
1-7 is the standard notes, so do through to si. no accents
the row below, q-u is the same but the accented versions
to make a word plural, press p and it'll change the last note and end the word
use the up and down arrow keys to adjust the text scaling
the spacebar adds a space and the enter key makes a newline, that scales with the tallest character in the previous line
backspace deletes things one note at a time and will also delete spaces and new lines
there is no word wrap, so lines can go off the edge of the window,
and there is no limit on number of lines, but there is no scroll bar, they'll just go off the window

be sensitive with the keys and don't hold any of them down as it'll just repeat it a lot,
it might be common for there to be acciedental double presses even if you didn't intend it

if a stenograpgh does not exist for what you have typed, it will break up into it's component characters
if you go over the limit of 4 notes in a word, it'll automatically do a space and go to the next word. 5 note words are not supported
also there is no cursor yet, so you can't go and delete certain sections. just backspace from the end

this is the first version and i have bug tested it but there are probably still some more,
please tell me if there is any unexpected beheaviour that is not outlined in this readme.
also please suggest features you want for the next version,
there will be updates to this but also the functionallity will grow by adding more stenographs
contact me through the coding channel of the la lasiresa discord server