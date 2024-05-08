dietaryrestrictions = (input("Do you have any dietary restrictions? "))

if dietaryrestrictions == "yes":
    type = input("What kind? ")
else:
    print("Thank you.")
if type == "vegetarian":
    print("You can have a salad.")
elif type == "gluten-free":
    print("You can eat gluten-free pasta.")
elif type == "nut-free":
    print("You can eat a burger.")

meal = input("What meal would you like? ")
print("The meal fits your preference.")

payment = input("Do you have a payment plan? ")
if payment == "yes":
    print("It's been successfully paid.")
else:
    amount = input("Enter amount of payment. ")
    print("Your meal coordinators will set up a payment for you.")

question = input("Would you like to eat inside or outside? ")
outside = True

if outside:
    print("You can go out at a picnic table.")
else:
    print("Stay inside.")