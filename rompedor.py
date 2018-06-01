#!/usr/bin/python
import zipfile
import argparse

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print "Encontrada= " + password
		return True
	except:
		return False

def main():
	parser = argparse.ArgumentParser("%prog -f <zipfile> -d <dictionary>")
	parser.add_argument("-f", dest="zip", help="ruta del zip")
	parser.add_argument("-d", dest="dic", help="ruta del dic")
	args = parser.parse_args()

	if (args.zip == None) or (args.dic == None):
		print parser.usage
		exit(0)
	else:
		zip = args.zip
		dic = args.dic

	zFile = zipfile.ZipFile(zip)
	passFile = open(dic)

	for line in passFile.readlines():
		password = line.strip("\n")
		found = extractFile(zFile, password)
		if found == True:
			exit(0)

	print 'No encontrada probar otro dic'

if __name__ == "__main__":
	main()