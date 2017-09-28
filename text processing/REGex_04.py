# Acts like GREP acts in Linux
import re
f = open('pricefx-config.xml', 'r', encoding='ISO_8859-1', errors='surrogateescape')


#  Must use REGEXP below, re.blablabla

for line in f:
    if re.search('(\w\w)') in line:
        print (line)

'''
for line in f:
    if ">f" in line:
        print (line.split())



for line in f:
    if ">f" in line:
        print (line.split("><")[-0])

# Acts like GREP acts in Linux
for line in open("file"):
 if "search_string" in line:
   print line
   '''
