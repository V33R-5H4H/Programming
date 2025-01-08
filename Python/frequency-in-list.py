lst=eval(input("enter list:"))
length=len(lst)
element=int(input("enter elemt:"))
count=0
for i in range(0,length):
    if element==lst[i]:
        count+=1
if count==0:
    print(element,"not found")
else:
    print(element,"has frequency as:",count,"in given list")
