import math
x=15
ans=0
while x<=15:
    ans=ans+(pow((0.2),x)*pow((0.8),100-x)*(math.factorial(100)/(math.factorial(x)*math.factorial(100-x))))
    x=x+1
print(ans)
