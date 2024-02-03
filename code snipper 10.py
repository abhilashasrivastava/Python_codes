myfile=open("E:\\Abhilasha\\dik.txt","w")
list1=[]
for i in range(5):
    name=input("enyter your name:")
    
    list1.append(name+"\n")
myfile.writelines( list1)
myfile.close()
