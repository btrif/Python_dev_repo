import re


ss = '''qhvfgbhgozr
yytuuuyuyuuuyuyuuyy
jhfg tryy error  jjfkhdjhfjh ttrtr
aaaeeedddeedaeaeeaeeea
jhzdgcoiua zfaozifh cohfgdyg fuo'''

regx = re.compile('^(.*)\r?\n(.*?error.*)\r?\n(.*)', re.MULTILINE)

print (regx.search(ss).groups())
