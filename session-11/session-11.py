#!/usr/bin/env python
# coding: utf-8

# # session 11
# create by omid Hadidy

# ## question 1
# <p style="direction:rtl">برنامه ای بنویسید که k کاربر دریافت و جمع آنها را به کاربر نمایش دهد عدد را ا</p>

# In[1]:


def convertToDecimal(n):
    temp = n
    result = 0
    tavan = 0
    while temp>0:
        result += (temp%10)*(2**tavan)
        temp//=10
        tavan+=1
    return result      


# In[2]:


def convertToBinery(n):
    temp = n
    result = 0
    tavan =0
    while temp>0:
        result += (temp%2)*(10**tavan)
        temp//=2
        tavan+=1
    return result


# In[3]:


def valide(n):
    temp = str(n)
    for i in range(len(temp)):
        if int(temp[i])>1:
            return False
    return True


# In[4]:


arr =[]
sum=0


# In[5]:


while True:
    n = int(input("0 for end input:"))
    if n==0:
        inp=False
        break
    elif not valide(n):
        print("invalid number try again")
        continue
        
    arr.append(n)

for i in arr:
    sum += convertToDecimal(i)
convertToBinery(sum)


# ## question 2
# برنامه ای بنویسید که دو عدد در مبنای 6 دریافت و حاصل ضرب آن دو را نمایش دهد

# In[6]:


def convertToDecimal(n):
    temp = n
    result = 0
    tavan = 0
    while temp>0:
        result += (temp%10)*(6**tavan)
        temp//=10
        tavan+=1
    return result 


# In[7]:


def convertToHex(n):
    temp = n
    result = 0
    tavan =0
    while temp>0:
        result += (temp%6)*(10**tavan)
        temp//=6
        tavan+=1
    return result


# In[8]:


def valide(n):
    temp = str(n)
    for i in range(len(temp)):
        if int(temp[i])>5:
            return False
    return True


# In[9]:


n= int(input("n:"))
m= int(input("m:"))

while  not valide(n) or not valide(m):
    n= int(input("again n:"))
    m= int(input("again m:"))


# In[10]:


result = convertToDecimal(n) + convertToDecimal(m)
result = convertToHex(result)
result


# ## question 3
# برنامه ای بنویسی که دو عدد در مبنای 2دریافت و تفاضل آنها را حساب کند

# In[11]:


def newNumber(n):
    temp_n = n
    tavan=1
    temp = n//(10**tavan)%10
    while temp == 0:
        tavan+=1
        temp = temp_n//(10**tavan)%10
    while tavan>0:
        temp_n-=(10**tavan)
        tavan-=1
        temp_n+=2*(10**tavan)
    return temp_n


# In[12]:


n = 1101
m = 111
tavan = 0
result = 0
while n>0:
    n_temp = n%10 
    m_temp = m%10
    if n_temp>=m_temp:
        n_temp = n%10 
        m_temp = m%10
        result += (n_temp-m_temp)*(10**tavan)
        tavan+=1
        n//=10
        m//=10
    else:
        n = newNumber(n)
result  


# ## question 3
# برنامه ای بنویسید که k عدد از ورودی دریافت و
# تعداد ارقام زوج و فرد و صفر آنرا نمایش دهد

# In[13]:


arr = []
while True:
    n= int(input("0 for stop input:"))
    if n==0:
        break
    else:
        arr.append(n)


# In[18]:


def counter(n):
    temp = n
    even,notEven,ziro = 0,0,0
    while temp>0 :
        temp_num = temp%10
        if temp_num==0:
            ziro+=1
        elif temp_num%2 == 0:
            even+=1
        else:
            notEven += 1
        temp //= 10
    return [even,notEven,ziro]


# In[19]:


for i in arr:
    temp_arr = counter(i)
    print("for {}, Even: {} , notEven: {} , Zire: {}".format(i,temp_arr[0],temp_arr[1],temp_arr[2]))
    


# ## question 5
# برنامه ای بنویسید که اشکال خواسته شده را نمایش دهد

# In[20]:


n=19


# In[21]:


for i in range(n):
    for j in range(n):
        if (j==n//2 and (i==0 or i==n-1)) or (i==n//2 and (j==0 or j==n-1) ):
            print("*",end=" ")
        elif i+j==n//2 or i-j==n//2  or j-i==n//2 or i+j - (n//2)==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# In[22]:


for i in range(n//2+1):
    for j in range(n):
        if (j==n//2 and i==0) or (i==n//2 and (j==0 or j==n-1) ) :
            print("*",end=" ")
        elif i+j==n//2 or j-i==n//2:
            print("*",end=" ")
        elif i==n//2:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()


# In[ ]:




