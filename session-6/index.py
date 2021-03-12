# 1
n = int(input("your number: "))
if n%2 != 0:
    print("invalid input")
elif n%4 == 0:
    print("bakhsh pazir bar : 4")
elif n%6 == 0:
    print("bakhsh pazir bar : 6")
else:
    print("addad zoj ama br 4 ya 6 bakhsh pazir nist")

# 2
x,y,z = int(input("1: ")),int(input("2: ")),int(input("3: "))
if x>0 and y>0 and z>0 and (x+y>z and x+z>y and z+y>x):
    if (x==y or x==z or z==y) :
        print("mosalas ghaem alzaviye hast")
    else:
        print("mosalas hast valy ghaem alzaviye nist")
else:
    print("mosalas nist")

# 3
x = int(input("1: "))
temp = x%10
if temp%2==0 :
    x+= (4-(x%4))
    print(x)
    x+= (4-(x%4))
    print(x)
    x+= (4-(x%4))
    print(x)
    x+= (4-(x%4))
    print(x)
else :
    x+= (3-(x%3))
    print(x)
    x+= (3-(x%3))
    print(x)
    x+= (3-(x%3))
    print(x)
    x+= (3-(x%3))
    print(x)

# 4
x = int(input("a: "))
w = int(input("w: "))
t = float(input("t: "))
if x>20:
    print(w/t**2)
else:
    print("sen shoma kame")

# 5
x,y,z = int(input("1: ")),int(input("2: ")),int(input("3: "))
if x<0 and y<0 and z<0:
    x,y,z= -x,-y,-z
    max = x
    if y>max:
        max =y
    if z>max:
        max =z
    print(max)
elif 0 <= x <= 20 and 0 <= y <= 20 and 0 <= z <= 20 :
    print(x+y+z)
elif x>20 and y>20 and z>20:
    min = x
    if y<min:
        min =y
    if z<min:
        min =z
    print(min)

# 6
print(  "ر صورتی که هر کدام از پارامتر ها را داشتید عدد1"+"\n"
        "و در غیر اینصورت 0 را وارد کنید"                     )
g = input("اگر مرد1 اگز زن0 :")
if g == "1":
    sen = int(input("سن: "))
    if sen>60:
        f_b =input("فشار خون:")
        ch_b =input("چربی خون:")
        d_b =input(" دیابت:")
        if f_b == "1" and ch_b =="1" and d_b == "1":
            print("very high")
        elif f_b == "1" and ch_b =="1" :
            print("high")
        elif d_b == "1":
            print("medium")
        else:
            print("easy")
    else:
        w = int(input("w: "))
        t = float(input("t: "))
        r = w/t**2
        if r<25:
            print("easy")
        elif 25 <= r < 40:
            print("medium")
        elif r <= 40:
            print("very high")
else:
    ch = int(input("تعداد فرزند: "))
    if ch == 0:
        a = int(input("age: "))
        t = int(input("متاهل 1 و مجرد 0: "))
        if (a>=50 and t == 0) or (a>=40 and t == 1):
            print("very high")
        elif (50 > a >= 40 and t == 0) or (40>= a >=30 and t == 1):
            print("medium")
        else:
            print("easy")
    else:
        f_b =input("فشار خون:")
        ch_b =input("چربی خون:")
        d_b =input(" دیابت:")
        if (f_b == "1" and ch_b =="1") or  (f_b == "1" and d_b == "1") or (ch_b =="1" and d_b == "1"):
            print("very high")
        elif f_b == "1" or ch_b =="1" or d_b == "1":
            print("medium")
        else:
            print("easy")
        







