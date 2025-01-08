def updater(dict,key,value):
    dict[key]=value
    print(dict)
dict={}
Num=int(input("Enter No of Records :"))
for i in range(Num):
    key=input("Enter Key :")
    value=input("Enter Value :")
    dict[key]=value
print(dict)
key=input("Enter Key of Value to be updated :")
value=input("Enetr New Value :")
updater(dict,key,value)