e={"a":1,"b":2,"c":3}
print(len(e))
#
e={"a":1,"b":2,"c":3}
e.clear()
print(e)
#
#e={"a":1,"b":2,"c":3}
e#.get("a")
#print(e)
#
e={"a":1,"b":2,"c":3}
d=e.items()
for i in d:
    print(i)
#
e={"a":1,"b":2,"c":3}
print(e.keys())

#
e={"a":1,"b":2,"c":3}
print(e.values())

#
e={"a":1,"b":2,"c":3}
p={"j":6,"y":5,"g":2}
e.update(p)
print(e)
