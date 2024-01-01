#writing in files
myfile=open("abhi.txt","w")
for i in range(5):
    name=input("enter your name:")    
    myfile.write(name)
myfile.close()
#
myfile=open("diksha.txt","w")
myfile.write("MY NAM IS ABHILASHA SRIVASTAVA.\n")
myfile.write("YO YO MAN\n")
myfile.write("my another name is diksha srivastava.\n")
myfile.close()
#
myfile=open("yoyo.txt","w")
for i in range(0,5):
    name=input("enter a name:")
    myfile.write(name)
    myfile.write("\n")
myfile.close()
