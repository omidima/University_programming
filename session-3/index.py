# 1
r = int(input("r: "))
print((r*2)**2)

# 2
h=int(input("h: "))
print("w: ",h//168)
print("d: ",(h%168)

# 3
n=int(input("h: "))
m=int(input("h: "))
print("before: ",n,m)
x=n
n=m
m=x
print("after: ",n,m)

# 4
n=input("name: ")
nw=int(input("wight: "))
m=input("name,wight: ")
mw=int(input("wight: "))
z=input("name,wight: ")
zw=int(input("wight: "))
print("average wight of {} {} {} equal to {}".format(n,m,z,"%3.2f"%((nw+mw+zw)/3)))

# 5
n=input("name: ")
print((n+"\n")*len(n))

# 6
k=int(input("k: "))
a=int(input("a: "))
print((4*k)**(1/3) + (5-(2*k)) / (3*a) - (1/(3+k**2)))
print(a/1 + (a**2)/2 + (a**3)/6 - (a**4)/24)
print((a+1)**((2*a)-1)**(3/((3*a)+2)))