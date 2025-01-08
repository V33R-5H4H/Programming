#Write a program to create Lpush() and Lpop() function to do push and pop operation on a stack using a list.
def isEmpty(s):
    if len(s)==0:
        return True
    else:
        return False
def Push(s,item):
    s.append(item)
    top=len(s)-1
def Pop(s):
    if isEmpty(s):
        return 'Underflow'
    else:
        val=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1
        return val
s=[]
top=None
while True:
    print('*Stack Demonstration*')
    print('1.Push')
    print('2.Pop')
    print('3.Exit')
    ch=int(input('Enter Choice :'))
    if ch==1:
        val=int(input('Enter Item to Push :'))
        Push(s,val)
        print("Stack : ",s)
    elif ch==2:
        val=Pop(s)
        if val=='Underflow':
            print('Stack is Empty :')
            print("Stack : ",s)
        else:
            print('Deleted Item was :',val)
            print("Stack : ",s)
    elif ch==3:
        print('Thank You')
        break