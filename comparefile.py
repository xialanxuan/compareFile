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
		head = origf.readline().strip('\n')
		origHead = head.split(',')
		origArray =[[]]
		TEST_origArray = [[]]
		for line in origf.readlines():
			origCurLine = line.strip('\n').strip(' ').split(',')
			origArray.append(origCurLine)


		TEST_origf = open(Path+TEST_origfn)
		TEST_origArray =[[]]
		TEST_origArray = [[]]
		for TEST_line in TEST_origf.readlines():
			TEST_origCurLine = TEST_line.strip('\n').strip(' ').split(',')
			TEST_origArray.append(TEST_origCurLine)			
		
#		print(origHead)
#		print(origArray)
#		result = os.popen('diff -w -u %s %s' %(Path+Dash+origfn, Path+Dash+TEST_origfn))
		
#		cur_file = open(openfile, 'w')
#		cur_file.write(result.read())
#		cur_file.close()
	else:
		DictOrig["%s" %origfn] = "error"
