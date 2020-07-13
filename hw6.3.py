def strtolist(a):
 x=[]
 for i in a.split(" "):
    x.append(i)
 return x

def listtostr(a):
 for i in a:
    x=str(i) + " "
 return x

INPUT=open('pxelinux.txt',"r")
OUTPUT=open('list2.txt',"a")
for s in INPUT:
 s=str(INPUT.readline())
 a=strtolist(s)
 a.reverse()
 OUTPUT.writelines(listtostr(a))
INPUT.close()
OUTPUT.close()
