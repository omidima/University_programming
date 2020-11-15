arr=[64,8,24,25,37,94,12,0,7,6,49,82,0,42]
for i in range(len(arr)):
    temp=arr[i]
    index=i
    for j in range(i,-1,-1):
        if arr[j]<temp:
            arr[j+1] = arr[j]
            index=j
    arr[index]=temp
print(arr)
