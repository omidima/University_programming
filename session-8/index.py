#!/usr/bin/env python
# coding: utf-8

# # code of session 8
# create by omid Hadidy

# ## qustion 1
# برنامه ی بنویسید که یک رشته از ورودی دریافت و کلمات مستتر در این رشته را مستخرج و چاپ نماید
# 
# ---

# In[1]:


n= input("input: ")


# In[2]:


arr=[]
temp = ""
for i in n:
    if i != " ":
        temp += i
    else:
        arr.append(temp)
        temp = ""        


# In[3]:


arr


# ## qustion 2
#  .برنامه ی بنویسید که بااستفاده از دستورات break و continue اعداد اول چهاررقمی زوج از دنباله فیبوناتچی را چاپ نماید.
#  
#  ---

# In[5]:


def isMain(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
        


# In[8]:


def isEven(n):
    if n%2 == 0:
        return True
    return False


# In[19]:


arr= []
a=0
b=1
while True:
    a=a+b
    b=a-b
    if a<999:
        continue
    elif a>10000:
        break
    else:
        if isMain(a) and isEven(a):
            arr.append(a)
arr


# ## qustion 3
# برنامه ی بنویسید که اسامی دانشجویانی که معدل باالتر از 15 دارند را از لیستهای از قبل ثبت شده ذیل استخراج و چاپ نماید.
# 
# ---
# > name = [Ali, Mohsen, Sara, Amir, Maryam, Saam, Karim, Majid, Hassan, Rahim]
# <br>
# > score = [19, 14.5, 13.25, 16.75, 15.25, 17.25, 11.75, 13.93, 14.81, 16.09]

# In[21]:


name  = ["Ali", "Mohsen", "Sara", "Amir", "Maryam", "Saam", "Karim", "Majid", "Hassan", "Rahim"]
score = [19, 14.5, 13.25, 16.75, 15.25, 17.25, 11.75, 13.93, 14.81, 16.09]


# In[22]:


for i in range(len(name)):
    if score[i] > 15:
        print("{} have score more than 15. {} scores: {}".format(name[i],name[i],score[i]))


# ## qustion 4
# برنامه ی بنویسید که اولین مض رب 7 یا 3 ذخیره شده در متغیر دیتا را پیدا و آنرا چاپ نماید. در صورت عدم وجود عدد مذکور پیام مناسب را
# چاپ نماید )از یکی از دستورات continue و یا break استفاده شود(.
# 
# ---
# > Data = [ 13, 16, 19, 25, 29, 31, 20, 10, 24, 8, 41, 53]
# 

# In[28]:


data =  [ 13, 16, 19, 25, 29, 31, 20, 10, 24, 8, 41, 53]


# In[29]:


temp = "invalid"
for i in data:
    if i%7 == 0 or i%3 == 0:
        temp = i
        break
temp


# ## qustion 5
# برنامه ی بنویسید که اسامی دانشجویان، رشته تحصیلی و معدل آنها را به ترتیب از متغیر دیتا استخراج و چاپ نماید. 
# 
# ---
# > Data = Ali, civil, 15.34, Ahmad, computer, 17.04, Sara, Mechanics, 15.84, Mohammad, computer, 16.99 <br>
# ,Javad, civil, 17.21, Majid, civil, 14.87, Saman, Mechanics, 16.55
# 

# In[30]:


arr = ["Ali", "civil", 15.34, "Ahmad", "computer", 17.04, "Sara", "Mechanics", 15.84, "Mohammad", "computer", 16.99,"Javad", "civil", 17.21, "Majid", "civil", 14.87, "Saman", "Mechanics", 16.55]


# In[35]:


counter = 0
for i in range(1,(len(arr)//3)+1):
    for j in range(counter,counter+3):
        print(arr[j],end=" ")
        counter+=1
    print()   


# In[ ]:





# 
