#Write a python program to remove all the lines that contain the character ‘a’ in a file and write it to another file.
fname=str(input('Enter File Path & Name:'))
myfile=fname+'.txt'
file=open(myfile,'r')
lines=file.readlines()
file.close()
file=open(myfile,'w')
fname1=str(input('Enter File Path & Name of second File:'))
myfile1=fname1+'.txt'
file1=open(myfile1,'w')
for line in lines:
    if 'a' in line:
        file1.write(line)
    else:
        file.write(line)
print("lines that contain a character are removed from",myfile)
print("lines that contain a character are added in",myfile1)