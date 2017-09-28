from xml.etree import ElementTree as ET


def main():
	infile = 'c:/Util/TEST/pricefx-config.xml'
	tomcat_users = ET.parse(infile)

	for user in [e for e in tomcat_users.findall('./user') if e.get('name') == 'tomcat']:
		print (user.tag)

if __name__ == "__main__": main()
