def frequency(x,y):
    index=[]
    count=0
    for i in range(len(y)):
        if y[i]==x:
            count+=1
            index.append(i)
    if count==0:
        print("Element",x,"is not in the list")
    else:
        print("Element",x,"Has Freq. :",count)
        print("Found at index :",index)
abc=eval(input("Enter List :"))
x=eval(input("Element to be searched :"))
frequency(x,abc)