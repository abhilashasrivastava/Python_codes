myfile=open("E:\\Abhilasha\\abhi.txt","r")
for line in myfile:
    word=line.split()
    for i in word:
        for letter in i:
            if(letter.isdigit()):
              print(letter)
