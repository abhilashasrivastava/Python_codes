l=[1,5,3,7]
print("original list=",l)
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j] < l[j+1]:
         l[j] ,l[j+1]=l[j+1],l[j]
print(l)
        
#insertion sot
l=[1,9,6,5343,2]
print("original=",l)
for i in range (1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and k<l[j]:
       l[j+1]=l[j]
       j=j-1
    else:
        l[j+1]=k
print(l)
