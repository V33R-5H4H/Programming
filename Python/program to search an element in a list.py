def search(x,y):
    if x in y:
        print("Index of Element ",x,"is",y.index(x))
    else:
        print("Element ",x,"does not exist in the given list")
abc=eval(input("Enter Elements of the list :"))
print(abc)
ele=eval(input("Enter Element to be searched :"))
search(ele,abc)