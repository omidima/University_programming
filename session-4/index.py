from math import sqrt

# 1
maximum = int(input("max: "))
minimum = int(input("min: "))
rootFee = maximum*950 + minimum*750
rootFee += (5*rootFee/100) + (2*rootFee/100)
rootFee += 3*rootFee/100
print("tota:",rootFee)

# 2
n = 101101
t=(n//10**5)*2**5
t+=((n%10**5)//10**4)*2**4
t+=((n%10**4)//10**3)*2**3
t+=((n%10**3)//10**2)*2**2
t+=((n%10**2)//10**1)*2**1
t+=(n%10**1)*2**0
print(1*bool(-1))

# 3
n = 5746.234
t=(n//10**3)*8**3
t+=((n%10**3)//10**2)*8**2
t+=((n%10**2)//10**1)*8**1
t+=(n%10**1)*8**0
t+=((n%10**-1)//10**0)*8**-1
t+=((n%10**-1)//10**-2)*8**-2
t+=((n%10**-2)//10**-2)*8**-3
print(t)

# 4
n= int(input("n: "))
box = n//(6*24)
jin = n%(6*24)//6
jorab = (n%24)%6
print("box: {} jin: {} jorab: {}".format(box,jin,jorab))

# 5
x = int(input("x: "))
y = int(input("y: "))
t = (x+y)%12/12
print(t)

# 6
x1= 8 + 26 *((10+int(input("random number: ")))%12/12)
print("day 1:",x1)
x2= 8 + 26 *((10+int(input("random number: ")))%12/12)
print("day 2:",x2)
x3= 8 + 26 *((10+int(input("random number: ")))%12/12)
print("day 3:",x3)
x4= x1+x2+x3
print("total:",x4)

# 7
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
s =(a+b+c)/2
A = sqrt(s*(s-a)*(s-b)*(s-c))
print(A)

# 8
n = int(input("n: "))
h = n//3600
m = n%3600//60
s = n%3600%60
print("h: {} m: {} s:{}".format(h,m,s))

# 9
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print((a==b-c) and (bool(c)) or (not (b<=c)))
print((a==b-c) and ((bool(c)) or (not (b<=c))))
print((a!=c) or (b>a) or (a<=c) and (c!=b-a) or ( bool(a)))
print((a!=c) or ((b>a) or (a<=c)) and ((c!=b-a) or ( bool(a))))
print((a!=c) or (b>a) or ((a<=c) and (c!=b-a)) or ( bool(a)))