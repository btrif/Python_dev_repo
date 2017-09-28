import re



m = re.search("Your number is <b>(\d+)</b>",
      "xxx Your number is <b>123</b>  fdjsk")
if m:
    print (m.groups()[0])