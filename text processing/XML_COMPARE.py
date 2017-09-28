from lxml import etree
import xmltodict  # pip install xmltodict

'''
    Recursively convert dict-like object (eg OrderedDict) into plain dict.
    Sorts list values.
'''

def normalise_dict(d):

    out = {}
    for k, v in dict(d).iteritems():
        if hasattr(v, 'iteritems'):
            out[k] = normalise_dict(v)
        elif isinstance(v, list):
            out[k] = []
            for item in sorted(v):
                if hasattr(item, 'iteritems'):
                    out[k].append(normalise_dict(item))
                else:
                    out[k].append(item)
        else:
            out[k] = v
    return out

"""
    Compares two XML documents (as string or etree)

    Does not care about element order
"""

def xml_compare(a, b):
    if not isinstance(a, basestring):
        a = etree.tostring(a)
    if not isinstance(b, basestring):
        b = etree.tostring(b)
        a = normalise_dict(xmltodict.parse(a))
        b = normalise_dict(xmltodict.parse(b))
    return a == b


a = 'module_input.xml'
b = 'template.xml'

xml_compare(a, b)