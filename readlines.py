myfile=open(r"F:\ABHILASHA SRIVASTAVA\IMAGES\fish.txt","r")
#file=myfile.readline(4)
#print(file,end="")
file=myfile.readline()
print(file,end="")
file=myfile.readline()
print(file,end="")
file=myfile.readline()
print(file,end="")
myfile.close()
# complete file in a list use readlines()
myfile=open(r"F:\ABHILASHA SRIVASTAVA\IMAGES\fish.txt","r")
d=myfile.readlines()
print(d)
#size of bytes

myfile=open(r"F:\ABHILASHA SRIVASTAVA\IMAGES\fish.txt","r")
t=myfile.read()
size=len(t)
print(size)
myfile.close()
#
myfile=open(r"F:\ABHILASHA SRIVASTAVA\IMAGES\fish.txt","r")
y=myfile.readlines()
length=len(y)
print(length)
myfile.close()
