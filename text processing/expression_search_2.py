import re

# Define the search term:
pattern = '>.*<'

# Create an empty list:

fh = open('pricefx-config.xml.template', 'r')

def main():
    
    for line in fh:
	    if re.findall(pattern, line):
                # print(line.group(1))
					print(line)

if __name__ == "__main__": main()

'''
def main():
    fh = open('pricefx-config.xml.template', 'r')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()
'''
