def calulator(n1,n2):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    return add(n1,n2),sub(n1,n2)

result=calulator(100,50)
print(result)



try:
    num=int('hcl')
    print(num)
except ValueError:
    print("give a valid number!")



def calculator(n1,n2):
    def add(a,b):
        return a+b
    def sub (a,b):
        return a-b
    return add(n1,n2),sub(n1,n2)
result=calculator(100,20)
a=result[0]
b=result[1]
print(a,b)
print(a==b)