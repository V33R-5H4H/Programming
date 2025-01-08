line=input("enter a line:")
lowercount=uppercount=0
digitcount=alphacount=symcount=0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    elif a.isalpha():
        alphacount+=1
    elif a.isalnum ()!=True and a!=' ':
        symcount+=1
print("number of uppercase letters:",uppercount)
print("number of lowercase letters:",lowercount)
print("number of alphabets :",alphacount)
print("number of digits :",digitcount)
print("number of symbols :",symcount)
