import pickle
sdata={}
slist=[]
file=open("student.dat","wb")
num=int(input("Enter No of Students? :"))
for i in range(num):
    Name=input("Enter the Name of the Student :")
    RollNo=int(input("Enter the Roll Number of the Student "))
    sdata[RollNo]=Name
    slist.append(sdata)
    sdata={}
pickle.dump(slist,file)
file.close()
x=open("student.dat","rb")
sdata=pickle.load(x)
print(sdata)
count=0
RollNo=int(input("enter the roll number you want to search for:"))
for line in sdata:
    if RollNo in line:
        print(line)
        count+=1
    else:
        count=0
if count==0:
    print("not found")