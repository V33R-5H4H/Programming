def update(y):
    updated=[]
    for i in range(len(y)):
        if y[i]%2==0:
            updated.append(int(y[i]/2))
        else:
            updated.append(int(y[i]*2))
    print(updated)
y=eval(input("Enter a List of Numbers :"))
update(y)