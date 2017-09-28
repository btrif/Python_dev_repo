#!/usr/bin/python

import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print('The correct syntax is: test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('\nA little help for you little boy. See the syntax from bellow:')	
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print('Input file is "', inputfile)
	print('Output file is "', outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])
