n=int(input("enter a no."))
s=0
while n>0:
    r=n%10
    s=r+s*10
    n=int(n/10)
print("reverse no.=",s)
