# Question 4 We have a list given below. Add an item 200 to the list, after the item 100.
# myList = [2, 8, [10, 20, [40, 60, [90, 100], 30, 70], 80], 50]
myList = [2, 8, [10, 20, [40, 60, [90, 100], 30, 70], 80], 50]
myList[2][2][2]=[90,100,200]
print(myList)
