a=[]
def push_stack(item):
    a.append(item)
def pop_stack():
    if len(a)<=0:
        print("list id empty")
    else:
        return a.pop()
def display_stack():
    for i in range(len(a)-1,-1,-1):
         print(a[i])
push_stack(1)
push_stack(2)
push_stack(3)
push_stack(4)
push_stack(5)
push_stack(6)
display_stack()
