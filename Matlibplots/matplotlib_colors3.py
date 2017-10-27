#  Created by Bogdan Trif on 09-10-2017 , 9:33 PM.
import matplotlib
COLORS = {}
COL = []
for name, hex in matplotlib.colors.cnames.items():
    print(name, hex)
    COLORS[name] = hex
    COL.append(name)

print(COLORS)
print(COL)



