file1=open("string.txt","r")
x=file1.readlines()
for line in x:
    x=line.split()
    for y in x:
        print(y+"#",end=" ")
    print(" ")
file1.close()