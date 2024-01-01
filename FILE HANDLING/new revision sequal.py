myfile=open("F:\\ABHILASHA SRIVASTAVA\\YO.txt","w")
L=[]
for i in range(5):
     name=input("enter")
     L.append(name+"\n")
myfile.writelines(L)     
myfile.close()

