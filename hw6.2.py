def strtolist(a):
 x=[]
 for i in a.split(" "):
    i=int(i)
    x.append(i)
 return x

def odd(a):
 b=[]
 for i in a:
     if i%2==1:
        b.append(i)
 return b

def even(a):
 b=[]
 for i in a:
     if i%2==0:
        b.append(i)
 return b

INPUT=open('list1.txt',"r")
s=str(INPUT.readline())
INPUT.close()
a=strtolist(s)
b=str(even(a))+"\n"
OUTPUT=open('list1_1.txt',"w")
OUTPUT.write(b)
OUTPUT.close()
