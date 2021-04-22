#!/usr/bin/env python
# coding: utf-8

# # session 10
# create by omid Hadidy

# ## question 1
# برنامه ای بنویسید که یک عدد اعشاری در مبنای ده دریافت کرده و در مبنای دو به کاربر نمایش دهد.

# In[82]:


def changeNumber(n):
    temp = int(n)
    tavan = 0
    result = 0
    while temp>0:
        ba = temp%2
        temp //= 2
        result += ba * (10**tavan)
        tavan+=1
    return str(result)
        


# In[80]:


def spel(n):
    arr =[]
    temp = ""
    for i in range(len(n)):
        if n[i] == "." :
            arr.append(temp)
            temp=""
        elif i==len(n)-1:
            temp+=n[i]
            arr.append(temp)
        else:
            temp+=n[i]
    return arr


# In[77]:


n = spel(input("n: "))


# In[87]:


result = float(changeNumber(n[0])+"."+changeNumber(n[1]))
result


# ## question 2
# برنامه ای بنویسید که سه عدد در مبنای 6 دریافت و حاصل جمع آنها را نمایش دهد

# In[104]:


def summer(n,m):
    temp = 0
    sum = 0
    tavan =0
    for i in range(max(len(str(n)),len(str(m)))):
        sum += (((n%10)+(m%10)+temp) % 6) * (10**tavan)
        temp += ((n%10)+(m%10)+temp) // 6 
        n //= 10
        m //= 10
        tavan+=1
    sum+= temp *(10**tavan)
    return sum


# In[108]:


def valide(n):
    temp = str(n)
    for i in range(len(temp)):
        if int(temp[i]) >6:
            return False
    return True


# In[110]:


n = int(input("n: "))
m = int(input("n: "))
z = int(input("n: "))
while not valide(n) and not valide(m) and not valide(z):
    n = int(input("again n: "))
    m = int(input("again n: "))
    z = int(input("again n: "))
result = summer(n,m)
result = summer(result,z)


# In[103]:


result


# ## question 3
# برنامه ای بنویسید که دو عدد اول دریافت و سپس حساب کند که مجموع آنها اول میباشد یا خیر

# In[119]:


def valide(n):
    for i in range(2,n):
        if n%i == 0 and n>2:
            return False
    return True


# In[120]:


n = int(input("n:"))
m = int(input("m:"))
while not valide(n) and not valide(m):
    n = int(input("again n:"))
    m = int(input("again m:"))


# In[121]:


if valide(n+m):
    print("Mian numebr")
else:
    print("not Main number")


# ## qustion 4
# برنامه ای بنویسید که دو عدد با تعداد ارقام برابر گرفته و حاصلضرب و تعداد ارقام آنرا اعلام نماید

# In[122]:


n = int(input("n:"))
m = int(input("m:"))
while len(str(n)) != len(str(m)):
    n = int(input("again n:"))
    m = int(input("again m:"))


# In[123]:


result = m*n
print(result,len(str(result)))


# ## qustion 5
# برنامه ای بنویسید که یک عدد از کاربر دریفات و اعداد اول موجود در آنرا نمایش و همچنین کل ارقام را نشان دهد

# In[126]:


n = int(input("n: "))
mainCount = 0
count = 0


# In[129]:


while n > 0:
    num = n%10
    if num%2 == 0 or num%3 ==0 or num%5 ==0 or num%7 ==0:
        mainCount+=1
    count+=1
    n//=10
print("Main: {} , count: {}".format(mainCount,count))


# In[ ]:




