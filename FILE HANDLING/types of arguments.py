def add(a,b):
    c=a+b
    print(c)
add(100,100)    
#default
def add(a,b=2):
    c=a+b
    print(c)
add(2)
#kleyword
def add(a,b):
    c=a+b
    print(c)
add(a=2,b=2)
add(a=2,b=3)
add(b=6,a=1)
#udf without argument and return
def add():
    a=int(input("enter1:"))
    b=int(input("enter2:"))
    c=a+b
    print(c)
add()
#udf without return and with argument
def add(a,b):
    c=a+b
    print(c)
a=int(input("enter1:"))
b=int(input("enter2:"))
add(a,b)
#with return
def add (a,b):
    c=a+b
    return c
a=int(input("enter"))
b=int(input("entr"))
o=add(a,b)
print(o)
#multiple
def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return (add, sub,mul,div)
a=int(input("enter"))
b=int(input("entert"))
result=cal(a,b)
print(result)
for i in result:
    print(i)
