x=list(range(0,100))
def is_prime(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
             return False
    return True

y= list(filter(is_prime,x))
print(y)
z=list(map(lambda f: f%10,y))
print(list(filter(lambda f:f%3==0,z)))
print(len(list(filter(lambda a: a==3,z))))
print(len(list(filter(lambda a: a==9,z))))

