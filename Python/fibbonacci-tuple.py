
def make_fibonacci(n):
    fib=[0]
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        fib.append(a)
    print(tuple(fib))
n=int(input("Enter the number of terms for fibonacci series:"))
make_fibonacci(n-1)
