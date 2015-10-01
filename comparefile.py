import string
import os


Path = 'D:/work/diff/'
Filenames = os.listdir(Path)
DictOrig = {}
DictTest = {}

if(len(Filenames)>0):
	for fn in Filenames:
		if "Test_" in fn:
			DictTest["%s" %fn] = ''
		else:
			DictOrig["%s" %fn] = ''

			
			
for origfn in DictOrig:
	index = origfn.find('_', 0) +1
	TEST_origfn = origfn[0:index] + "Test_" + origfn[index:]
	if TEST_origfn in DictTest:
		origHead = []
		origf = open(Path+origfn)
		head = origf.readline()
		origHead = head.split(',')
		for line in origf.readlines()
			
		
#		print(origHead)
	
	
#		result = os.popen('diff -w -u %s %s' %(Path+Dash+origfn, Path+Dash+TEST_origfn))
		
#		cur_file = open(openfile, 'w')
#		cur_file.write(result.read())
#		cur_file.close()
	else:
		DictOrig["%s" %origfn] = "error"
