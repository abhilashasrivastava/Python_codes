def display_oddline():
    myfile=open("E:\\Abhilasha\\abhi.txt","r")
    count=0
    for line in myfile:
        count+=1
        if count%2!=0:
            print("no of line:",count)
    myfile.close()
display_oddline()
