arr=[64,8,24,25,37,94,12,0,7,6,49,82,0,42]

for i in range(len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            i=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=i
print(arr)