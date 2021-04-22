#!/usr/bin/env python
# coding: utf-8

# # code of session 9
# create by omid Hadidy

# ## qustion 1
# محاسبه دو سری اعداد
# 
# ---

def fac_n(n):
    if n == 1: return 1
    else : return n*fac_n(n-1)

def t_n(n):
    if n == 1 :return n**2
    else: return (n**2)*(t_n(n-1))

def s_n(n):
    if n == 1: return 1
    else: return n+(s_n(n-1))


n = int(input("input n: "))
x = int(input("input x: "))
while n>=x:
    print("x should more than n")
    x = int(input("input x: "))
    
# g(x)
result = 0
for i in range(1,n+1):
    result += (s_n(i)+t_n(i)) / ((i*x) - fac_n(i))
result

#f(x)
result = x
for i in range(1,n+1):
    result += x**s_n(i) / fac_n(i)
result


# ## qustion2
#  .برنامه ی بنویسید که اعداد کامل چهار رقمی را محاسبه و چاپ نماید. 
#  
#  ---

temp = 2
while True:
    num = (2**(temp-1))*((2**temp)-1)
    if num<1000:
        temp +=1
        continue  
    elif num>10000:
        break
    else:
        print(num)
    temp +=1
    


# ## qustion 3
# برنامه ی بنویسید که تعداد اعداد اول، تعداد اعداد فرد و تعداد اعداد زوج عناصر بین 20 تا 40 از دنباله فیبوناتچی را محاسبه و چاپ نماید.
# 
# ---

def isEven(n):
    if n%2 == 0:
        return True
    return False


def isMain(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


a = 0
b = 1
even = 0
notEven = 0
main =0


# In[22]:


for i in range(41):
    if i>19:
        if isEven(a):
            even += 1
        else:
            if isMain(a):
                main+=1
            else:
                notEven += 1
            
    a=a+b
    b=a-b
print("Even: {} , notEven: {} , Main: {}".format(even,notEven,main))


# ## qustion 4
# برنامه ی بنویسید که حاصل تقسیم اعداد 1 تا 10 را بریکدیگر محاسبه و چاپ نماید.
# 
# ---


sum = 0
for i in range(1,11):
    for j in range(1,11):
        sum+=(i/j)
sum


# ## qustion 5
# برنامه ی بنویسید که نمرات امتحانی n دانشجو از k رشته را از ورودی دری افت کرده و نشان دهد برای هرکدام از رشته ها چند نفر ضعیف )زیر
# 10 ،)چند نفر متوسط )بین 10 تا 15 )و چند نفر خوب )بال ی 15 )گرفته اند. )راهنمایی: فرض کنید 3=k یعنی سه رشته مدنظر هستند و
# 10=n یعنی برای هر رشته، نمرات 10 دانشجو باید از ورودی دریافت شود و اعالم شود که برای هر رشته چه تعداد ضعیف، چه تعداد متوسط و
# چه تعداد خوب گرفته اند.(
# 
# ---

def spel(data = " ",n = 1000):
    arr = []
    count = 0
    temp = ""
    for i in range(len(data)):
        if count<n-1:
            if data[i] != " ":
                temp+=data[i]
            else:
                arr.append(temp)
                count+=1
                temp = ""
        else:
            return arr
        
        if i == len(data)-1:
            arr.append(temp)
            
    return arr


# In[24]:


k=int(input("k:"))
n=int(input("n:"))


# In[73]:


for i in range(k):
    arr = spel(input("n:"))
    low,medium,high=0,0,0
    for j in arr:
        if int(j)<10:
            low+=1
        elif 10<= int(j) <15:
            medium+=1
        else:
            high+=1
    print("low: {} , medium: {} , high: {}".format(low,medium,high))


# ## qustion 6
# برنامه ی بنویسید که اعداد سه رقمی که با مقلوبشان برابر بوده و عدد اول نیز هستند را محاسبه و چاپ نماید. )راهنمایی: منظور از مقلوب،
# همان معکوس رقمی می باشد. یعنی منظور اعدادی مانند 121 ،454 ،393 و ... هستند که خود عدد با معکوس رقمی آن یکی است.(
# 
# ---


def isMain(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


# In[78]:


for i in range(100,1000):
    if i//100 == i%10 and isMain(i):
        print(i,end=" , ")




