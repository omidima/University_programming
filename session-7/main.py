"""
# create by omidima
# data: 1400/01/09
# 
"""

# 1
n = int(input(": "))
result=1
if n%2 > 0 :
    for i in range(3,n+1):
        if n%i == 0:
            result += i
else:
    while n > 0:
        result *= n
        n-=1
print(result)

# 2
a=6765
b=4181
n=0
while n<15:
    a+=b
    b=a-b
    print(a,end=" ")
    n+=1
    
# 3
a=0
b=1
n=0
while n<15:
    a+=b
    b=a-b
    if 200< a <400:
        print(a,end=" ")
    n+=1

# 4
sum=0
count=0
for i in range(21,100,21):
    sum+=i
    if i%2==0:
        count+=1
print("sum: {} & count: {}".format(sum,count))

# 5
student = []
for i in range(5):
    a=int(input("grade: ")) 
    if 0<= a <= 20:
        student.append(a)
    else:
        print("value incorrect")

temp={"low":0,"med":0,"high":0}
for i in student:
    if i<10:
        temp["low"]+=1
    elif 10 <= i <15:
        temp["med"]+=1
    else:
        temp["high"]+=1

print("high level: {} & medium level: {} & low level: {}".format(temp["high"],temp["med"],temp["low"]))

# 6
arr=[]
for i in range(5):
    arr.append(int(input("grade: ")))
max_index=0
temp=0
for i in range(len(arr)):
    if arr[i]>temp:
        temp=arr[i]
        max_index=i
print(max_index+1)

# 7
for i in range(1000,10000):
    if ( (i%10)%2>0 and (i//10%10)%2>0 ) and ( (i//100%10)%2==0 and (i//1000)%2==0):
        print(i,end=", ")

# 8
for i in range(100,1000):
    if i%10 == i//100:
        print(i,end=", ")