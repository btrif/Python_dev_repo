from xml.dom import minidom

filename = 'pricefx-config.xml.template'

xmldoc = minidom.parse(filename)

itemlist = xmldoc.getElementsByTagName('nodeName') 

print(len(itemlist))
# print(itemlist[0].attributes['name'].value)

for s in itemlist :
    print(s.attributes['nodeName'].value)
