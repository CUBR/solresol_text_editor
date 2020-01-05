#solresol stenographs file renamer
import os

keychars = [
"ô",
"ê",
"î",
"â"]

folder = "glyphs_renamed/"

allfiles = os.listdir(path=folder)

for name in allfiles:
    origin = name
    print(origin)
    name = name[:-4]
    name = list(name)

    for x in range(len(name)):
        if name[x] in keychars:
            name[x]="1"

    name = "".join(name)
    name += ".png"

    print(name)

    os.rename(folder+origin, folder+name)
    print("")
