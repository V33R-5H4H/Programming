#program to create a copy of a list. in the lists copy, add 10 to its first and last elements. then display the lists
L1=[17,24,15,30,34,27]
L2=L1.copy()
print("original list:",L1)
print("Created copy of the list:",L2)
L2[0]+=10
L2[-1]+=10
print("copy of the list after changes:",L2)
print("original list:",L1)
