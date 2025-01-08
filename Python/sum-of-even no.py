n=int(input("enter the number of terms:"))
tot = 0
for i in range(1, n+ 1):
   if (i % 2 == 0):
       tot = tot + n
print("The Sum of All Even Numbers from 1 to",n,"is",tot)
