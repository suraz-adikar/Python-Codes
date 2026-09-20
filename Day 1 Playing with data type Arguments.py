# There is a conversion of int()extra argument for base
#int("Anything but string",base(like 2,10,16))
a=int("101",2)
print(a)
# so it works like 101 is 1*2^0=1,0*2^1=0,1*2^2=4 so 1+4=5

a=int("FF",16)
print(a)
# so it works like f=15   15*16^1 and 15*16^0
# 240+15=255


a=bin(5)
print(a)
#converts converting integer to binary
#where 0b tells it is binary and 101 is its binary number

a=hex(3)
print(a)
#here 0x tells it is hexadecimal and 3 is its hex value



#Print also has hidden Parameters in it
'''print(*objects, sep=' ', end='\n', file=None, flush=False)'''
#Use flush=True when you actually care about seeing the output immediately.
#file is used when we need to send output to the specific file
a=10
print(a,flush=True)


'''for input()it has prompt= means input(prompt=) means input("") is valid'''