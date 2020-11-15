"""
 **Important to read Comment**
 *
 * Comment:
 * Sorting a List of student number
 * you need to index of data to use a Sorting of List in MainList
 * 
 * Element:
 * arr[index][0] Output => name of student
 * arr[index][1] Output => number of student
 * arr[index][2] Output => location of student
 *
"""

def sorting(ary):
    arr=ary
    #todo: Change index of arr 
    for i in range(len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j][1]>arr[j+1][1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr


arr_name=[] #MainList

try:
    count=int(input("please insert a count of student => ")) #@input
    print("*"*60)
    for i in range(count):
        person=[] #@input
        name=input("nanme => ")
        person.append(name) #append to person list
        number=input("number => ")
        person.append(number) #append to person list
        location=input("location => ")
        person.append(location) #append to person list
        print("*"*65)
        arr_name.append(person) #append to main list
    
    print("sorted: ",sorting(arr_name)) #Output

except ValueError:
    print("error of: ",ValueError)
    print("*"*60)

