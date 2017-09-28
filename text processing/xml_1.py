# rexml is the XML string read from a URL

from xml.etree import ElementTree as ET
tree = ET.fromstring(rexml)



ef print_page(node, depth):
    print "%s" % depth
    url = node.find("url")
    if url is not None:
        print url.text
    title = node.find("title")
    if title is not None:
        print title.text
    print '-' * 30

def find_pages(node, depth=0):
    for page in sub(node, "page"):
        print_page(page, depth)
        subpage = page.find("subpages")
        if subpage is not None:
            find_pages(subpage, depth + 1)

