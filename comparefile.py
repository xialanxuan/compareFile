import string
import os


Path = 'D:/work/diff/'
Filenames = os.listdir(Path)
DictOrig = {}
DictTest = {}

if(len(Filenames)>0):
	for fn in Filenames:
		if "TEST_" in fn:
			DictTest["%s" %fn] = ''
		else:
			DictOrig["%s" %fn] = ''

			
			
for origfn in DictOrig:
	TEST_origfn = "TEST_" + origfn
	if TEST_origfn in DictTest:
		result = os.system('diff %s %s' %(Path+origfn, Path+TEST_origfn));
		DictOrig["%s" %origfn] = result
	else:
		DictOrig["%s" %origfn] = "error"
			
			

for origfn in DictOrig:
	openfile = 'D:/work/diff_'+origfn
	cur_file = open(openfile, 'w')
	cur_diff = DictOrig["%s" %origfn]
	cur_file.write(str(cur_diff))
	cur_file.close()
	print (cur_diff)