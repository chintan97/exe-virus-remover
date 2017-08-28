#Chintan Patel
#chintan97patel@gmail.com

import os, sys

dir = raw_input("Enter folder path: ")

def Test(rootDir):
	file = []
	rootDir_check = len(rootDir) - rootDir[::-1].find('\\')
	file.append(rootDir+'\\'+rootDir[rootDir_check:]+'.exe')
	count = 0
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		for d in dirs:
			file.append(os.path.join(root, d)+'\\'+d+'.exe')
		for f in files:
			if '.exe' in f and os.path.join(root, f) in file:
				print "Deleted from",os.path.join(root)
				os.remove(os.path.join(root, f))
				count += 1
	print count,"virus removed!!!"
Test(dir)