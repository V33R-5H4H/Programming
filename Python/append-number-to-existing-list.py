#write a program that asks the user to input a number a list to be appended to a existing list. whether the user enters a single number or alist of numbers, the program should append the list accordingly
myl=[2,4,6]
print("existing list is:",myl)
n=eval(input("enter a number or a list to be appended:"))
if type(n)==type([]):
    myl.extend(n)
elif type(n)==type(1):
    myl.append(n)
else:
    print("please enter either an integer or a list.")
print("appended list is:",myl)
