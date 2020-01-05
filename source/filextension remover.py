import os

allfiles = os.listdir(path="glyphs_renamed/")

for x in range(len(allfiles)):
    allfiles[x] = allfiles[x][:-4]

print(allfiles)
