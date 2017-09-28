import re


ss = open('ghost.xml', 'r')

regx = re.compile('^(.*)\r?\n(.*?error.*)\r?\n(.*)', re.MULTILINE)

print (regx.search(ss).groups())
