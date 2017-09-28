

import re
# Define the search term:
pattern = 'idleMaxAgeInMinutes'

# Create an empty list:
data = []
'''
def main():
    for line in open('pricefx-config.xml.template', 'r'):
#		if line !='':  		#<-- To make sure the whole file is read
		word = re.findall(pattern, line)
		data.append(str(word))  

if __name__ == "__main__": main()
'''

def main():
    fh = open('pricefx-config.xml.template', 'r')
#    exp = 
    for line in fh.readlines(3):
        print(line)

if __name__ == "__main__": main()
