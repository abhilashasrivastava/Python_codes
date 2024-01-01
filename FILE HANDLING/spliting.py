myfile=open("F:\\ABHILASHA SRIVASTAVA\\YO.txt","r")
lines=myfile.readlines()
for line in lines:
    x=line.split()
    for y in x:
        print(y+"#",end="")
        
