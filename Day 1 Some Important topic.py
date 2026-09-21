import keyword
print(keyword.kwlist,end="\n")


a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10]
print(a==b)
print(a is b)
print(a is not b)

result=None
if result is not None:
    print("We have a result")
else:
    print("Nothing is true")


result=None
if result is None:
    print("We have a result")
else:
    print("Nothing is true")