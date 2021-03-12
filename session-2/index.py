# 1
province = input("province name: ")
cityOne = input("name of a city in this province: ")
cityTwo = input("name of a another city in this province: ")
print("Question 1=> province: {} city: {} and city: {} ".format(province, cityOne, cityTwo))

# 2
print(eval(input(": ")))

# 3
inp = input("numebr: ")
checker = inp.split(".")
number = float(inp)
if len(checker[1]) == 6:
    print("you number convert to: %3.3f" %number)
else:
    print("your number incorrect")

# 4
name1 = input("1:")
name2 = input("2:")
name3 = input("3:")
print(name1, "-"*len(name1), name2, "-"*len(name2), name3, "-"*len(name3))

# 5
space= int(input("space: "))
num1 = int(input("1:"))
num2 = int(input("2:"))
num3 = int(input("3:"))
num4 = int(input("4:"))
num5 = int(input("5:"))
if num1 > 9 and num2 > 9 and num3 > 9 and num4 > 9 and num5 > 9:
    print("{}{}{}".format(num1, "-"*space,num2))
    print("{}{}{}".format("-"*((space//2)+1), num3, "-"*((space//2)+1)))
    print("{}{}{}".format(num4, "-"*space, num5))
else:
    print("numbers incorrect")


