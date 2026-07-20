age = 22
has_id = False

if age >= 18 and has_id:
    print("Can enter")
else:
    print("Access denied")

    temperature = 22

    if temperature >=30 or temperature <10:
        print("Extreme weather.")
    else:
        print("Normal weather.")

logged_in = True

if not logged_in:
    print("Please log in.")
else:
    print("Welcome.")

print("-----------------Movie TV-------------------")

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and has_ticket == "yes":
    print("Welcome and enjoy.")
else:
    print("You are not allowed.")

print("--------------------------------------------")

marks = int(input("Enter your marks: "))
sport = input("Did you participate in sports? (Yes or No)" )

print("--------------------Scholarship Eligibility--------------------")

if marks >= 75 or sport == "Yes":
    print("You are eligible. ")
else:
    print("Regrets. ")

print("----------------------------------------------------------------")


print("-----------Login System--------------------")

logged_in = True
if not logged_in:
    print("Please log in first. ")
else:
    print("Welcome! ")

    print("-------------------------------------------")

    print("---------------------Driver's License------------------------")

    age = int(input("Enter your age: "))
    has_license = input("Do you have access to driver's license? (Yes/No) ").lower()

    if age >= 18 and has_license == "yes":
        print("You can drive. ")
    else:
        print("You cannot drive. ")


        print("------------------------------------------------")


        print("----------------------Stadium Access------------------------")

    age = int(input("Enter your age: "))
    has_ticket = input("Do you have ticket? (yes/no)").lower()

    if age >= 18 and has_ticket == "yes":
            print("Access granted. ")
    else:
            print("Access denied! ")


            print("----------------------------------------------------")