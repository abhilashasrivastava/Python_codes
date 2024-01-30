def countline():
    myfile=open("E:\\Abhilasha\\abhi.txt","r")
    line=myfile.readlines()
    count=0
    for i in line:
       if i[0]=="a" or i[0]=="A":
         count+=1
    print(count)
    myfile.close()
countline()
