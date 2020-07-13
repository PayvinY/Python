n=int(input("Какой длины вывести ряд чисел Фибоначи?\n"))
f=[0]
if n<0:
    z=-1
else:
    z=1
n*=z
f.append(z)
j=2
while j<=n:
 f.append(f[-2]+f[-1])
 j+=1
print("Элементов ряда Фибоначи ",n," получаем\n",f)
