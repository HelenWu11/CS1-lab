def add(m,n):
    if n == 0:
        return m
    else:
        n -= 1
        m += 1
        return add(m,n)
    
print(add(5,3))
print(add(6,4))

def mult(a,b,val=0):
    if b == 0:
        return val 
    else:
        return mult(a,b-1,add(val,a))

def mult1(a,b):
    if b == 1:
        return a
    else:
        return add(mult1(a,b-1), a) 

print(mult1(8,3))
print(mult1(5,4))

def power(x,n,val=1):
    if n == 0:
        return val
    else:
        return power(x,n-1,mult(val,x))

print(power(6,4))
print(power(2,3))
     