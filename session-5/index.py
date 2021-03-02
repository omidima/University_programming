from math import sqrt

# 1
month,day = int(input("month:")),int(input("day:"))
if (month and day) > 0:
    if month>6:
        print(day+((month-7)*30) + 186)
    elif month == 12:
        if (day>29):
            print("day input invalide")
        else:
            print(day+((month-7)*30) + 186)
    else:
        if month == 1:
            print(day)
        else:
            print(day+(month*31))
else:
    print("input invalide")

# 2
n =int(input("n:"))
if len(str(n)) == 3 and (n//100) < 8 and ((n%100)//10) < 8 and ((n%100)%10) < 8:
    a = (n//100)*8**2 + ((n%100)//10)*8**1 + ((n%100)%10)*8**0
    print(a)
else:
    print("input invalide")

# 3
a,b,c =int(input("a:")),int(input("b:")),int(input("c:"))
if a+b>c and a+c>b and b+c>a:
    s =(a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("area: ",area)
else:
    print("not correct")

# 4
n =int(input("n: "))*10000
n -= (n*9/100)
if n<1500000:
    n-=(n*5/100)
elif 1500000 <= n < 3000000:
    n-=(n*10/100)
else :
    n-=(n*15/100)
print("dastmozd: ",n)


# 5
n =int(input("n: "))
m =int(input("m: "))

if n%2==0 and m%2==0:
    print(n+m)
elif n%2!=0 and m%2!=0:
    print(n-m)
else:
    print(n*m)

# 6
number =int(input("n: "))
year = number // 10**8
dore = (number%10**8) // 10**7
daneshKade = (number%10**7) // 10**6

if len(str(number))==10 and 94 <= year  <=99 and (dore==1 or dore==2) and (daneshKade==1 or daneshKade==2 or daneshKade==3) :
    print("vorody: {} dore: {} danesh kade: {}".format(year,dore,daneshKade))
else:
    print("invalide")

    



