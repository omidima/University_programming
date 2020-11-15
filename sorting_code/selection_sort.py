arr=[64,8,24,25,37,94,12,0,7,6,49,82,0,42]

for i in range(len(arr)):
    min=arr[i]
    min_index=i
    for j in range(i,len(arr)):
        if min>arr[j]:
            min=arr[j]
            min_index=j
    temp=arr[i]
    arr[i]=min
    arr[min_index]=temp
print(arr)