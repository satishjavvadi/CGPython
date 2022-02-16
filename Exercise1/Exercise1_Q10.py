Name = str(input("Enter the Name:"))
Age = int(input("Enter the Age:"))
Roll_Number = int(input("Enter the Roll_Number:"))
Subjects = []
n = int(input("Enter number of Subjects : "))

for i in range(0, n):
    Subjects.append(input("Enter Subject{}: ".format(i+1)))

print("Name: {}".format(Name))
print("Age: {}".format(Age))
print("Roll Number: {}".format(Roll_Number))
print("Subjects: {}".format(Subjects))