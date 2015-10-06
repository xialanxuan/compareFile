import string
import os


Path = 'D:/work/1002data/'
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
		sechead = origf.readline().strip('\n')
		origHead = sechead.split(',')
		origArray =[[]]
		TEST_origArray = [[]]
		for line in origf.readlines():
			origCurLine = line.strip('\n').strip(' ').split(',')
			origArray.append(origCurLine)


		TEST_origf = open(Path+TEST_origfn)
		TEST_head = TEST_origf.readline()
		TEST_origArray =[[]]
		TEST_origArray = [[]]
		TEST_sechead = TEST_origf.readline().strip('\n')
		for TEST_line in TEST_origf.readlines():
			TEST_origCurLine = TEST_line.strip('\n').strip(' ').split(',')
			TEST_origArray.append(TEST_origCurLine)			
		
		origlen = len(origArray)
		TEST_origlen = len(TEST_origArray)
		writePath = 'D:/work/diff_result/'+origfn
		writeFile = open(writePath, 'w+')		
		
		
		if(origlen == TEST_origlen):
			for i in range(0, origlen):
				if (len(origArray[i]) == len(TEST_origArray[i]) and len(origArray[i]) == len(origHead)):
					for j in range (0, len(origHead)):
						if (origArray[i][j] == TEST_origArray[i][j]):
							pass
						else:
							if (origArray[i][j] == ' ' or TEST_origArray[i][j] == ' '):
								pass
							else:
								
								writeFile.write('%d line: %d column, head name: %s \n' %(i+2, j, origHead[j]))							
								writeFile.write('orig: %s\n' %origArray[i][j])
								writeFile.write('test: %s\n' %TEST_origArray[i][j])
								writeFile.write('\n')
				else:
					if (len(origArray[i]) > len(TEST_origArray[i])):
						diffElement =  list(set(origArray[i]).difference(set(TEST_origArray[i])))
						writeFile.write('%d line: missing element in orign %s \n' %(i+2,diffElement))
						#writeFile.write('head %s' %(origHead))
						writeFile.write('origin %s\n' %(origArray[i]))
						writeFile.write('intest %s\n' %(TEST_origArray[i]))							
						writeFile.write('\n\n')
					else: 
						diffElement =  list(set(TEST_origArray[i]).difference(set(origArray[i])))
						
						writeFile.write('%d line: missing element in orign %s\n' %(i+2,diffElement))
						#writeFile.write('head %s' %(origHead))
						writeFile.write('origin %s\n' %(origArray[i]))
						writeFile.write('intest %s\n' %(TEST_origArray[i]))							
						writeFile.write('\n\n')
		else:
			writeFile.write('missing lines %d - %d' %(TEST_origlen, origlen))
			writeFile.write('\n')
		
		
		
		
		
		
#		print(origHead)
#		print(TEST_origArray)
#		result = os.popen('diff -w -u %s %s' %(Path+Dash+origfn, Path+Dash+TEST_origfn))
		
#		cur_file = open(openfile, 'w')
#		cur_file.write(result.read())
#		cur_file.close()
	else:
		DictOrig["%s" %origfn] = "error"
