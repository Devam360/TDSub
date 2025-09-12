def fact(s):
    if(s==1):
        return 1
    else:
        return s*fact(s-1)
e=5
f=fact(e)
print(f)