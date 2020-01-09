file = open("key_codes.txt", "r")
lines = file.read()
lines = lines.split("\n")

for y in range(133):
    lines[y] = lines[y].split(":")

mainstring = '{'

for x in range(133):
    linestring = str('"'+lines[x][1]+'"'+": "+"pygame."+lines[x][0]+",\n")
    mainstring+=linestring

mainstring+="}"

print(mainstring)
