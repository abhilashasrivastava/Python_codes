n=int(input("enter"))
r=1
while n>0:
    d=n%10
    r=r*d
    n=int(n/10)
    print(r)
