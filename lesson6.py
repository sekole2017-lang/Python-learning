print("-----------Voting Checker---------------")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are elligible to vote")
else:
    print("You are not allowed to vote")

    print("----------------------------------------")


print("-------------Marks Gradings-------------")

marks = int(input("Enter your marks: "))
if marks >= 75:
    print("Grades:Distinction")
elif marks >= 50:
    print("Grades:Pass")
else:
    print("Grades:Fail")

print("----------------------------------------------")

print("--------------------Child's age & prints-------------------")

age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
elif age >=13 and age <=19:
    print("teenager")
else:
    print("Adult")

print("--------------------------------------------")