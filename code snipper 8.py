myfile=open("E:\\Abhilasha\\dik.txt","w")
for i in range(5):
    name=input("enyter your name:")
    myfile.write(name)
    myfile.write("\n")
myfile.close()
