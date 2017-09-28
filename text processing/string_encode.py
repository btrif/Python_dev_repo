#!/usr/bin/python

import base64
encoded = base64.b64encode(b'Let me show you how I love you')
print(encoded)

data = base64.b64decode(encoded)
print(data)
print(data.strip()[3])
