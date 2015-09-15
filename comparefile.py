import os

def cmpstr(str1, str2):
    col = 0
    for c1, c2 in zip(str1, str2):
        if c1 == c2:
            col += 1
            continue
        else :
            break
        
    #exit when length different
    if c1 != c2 or len(str1) != len(str2):
        return col+1
    else :
        return 0
    
file1 = open('D:/work/diff/a.txt','r')
file2 = open("D:/work/diff/b.txt",'r')

fa = file1.readlines()
fb = file2.readlines()
file1.close()
file2.close()


row = 0
col = 0

#start compare
for str1, str2 in zip(fa, fb):
    col = cmpstr(str1,str2)
    # if equals, col = 0
    if col == 0 :
        row += 1
        continue
    else:
        break

#if different
if str1 != str2 or len(fa) != len(fb):
    
    print ("row:", row+1, "col:", col)
    print ("file a is:\n", fa[row-1],fa[row][:col+1], "\n")
    print ("file b is:\n", fb[row-1],fb[row][:col+1], "\n")
else :
    print ("All are same!")

#get input  
#raw_input("Press Enter to exit.")   

