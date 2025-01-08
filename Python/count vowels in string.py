def count(str):
    vowels=["a","A","e","E","i","I","o","O","u","U"] 
    x=list(str)
    count=0
    for i in range(len(x)):
        if x[i] in vowels:
            count+=1
    if count==0:
        print("No Vowels Found")
    else:
        print("No. of Vowels :",count)

str=input("Enter a String :")
count(str)