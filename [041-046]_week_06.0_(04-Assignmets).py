################################################
## << Mastring Python -- Elzero Web School >> ##
#########    WEEK #06.0 Assignments    #########
## ----------- From #041  to #046 ----------- ##
print("############ Starting ############\n") ##
################################################




#######################################
#        <<<<< task #01 >>>>>        ##
print("\n<<<<< task #01 >>>>>")      ##
#######################################
operation = input('''From ("+" Or "-" Or "*" Or "/" Or "%"),
Choose the operation you want to apply:   ''').strip()
num1 = int(input("Enter the first number please..   ").strip())
num2 = int(input("Enter the second number please..   ").strip())
operations = ["+", "-", "*", "/", "%"]

if operation in operations:
    if operation == operations[0]:
        result = num1 + num2
    elif operation == operations[1]:
        result = num1 - num2
    elif operation == operations[2]:
        result = num1 * num2
    elif operation == operations[3]:
        result = num1 / num2
    elif operation == operations[4]:
        result = num1 % num2
    print(f"\nAccording to the given inputs,\nThe result of {num1} {operation} {num2} is: {result}")   
else: print("Invalid choice!!")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
age = int(input("Enter your age plz!   "))
print(f"App Is Suitabl For You" if age > 16 else "App Is Not Suitable For You")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
age = int(input("Enter your age in years please!   "))
ageInMonths = age * 12
ageInWeeks = age * 52
ageInDays = age * 365
ageInHours = ageInDays * 24
ageInMinutes = ageInHours * 60
ageInSeconds = ageInMinutes * 60
if 10 <= age <= 100:
    print(f"Your age in months is {ageInMonths} months.")
    print(f"Your age in weeks is {ageInWeeks} weeks.")
    print(f"Your age in days is {ageInDays} days.")
    print(f"Your age in hours is {ageInHours} hours.")
    print(f"Your age in minutes is {ageInMinutes} minutes.")
    print(f"Your age in seconds is {ageInSeconds} seconds.")
else: print("Age is out of the range")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
country = input(f"Hi! The original price is: {price}$\n"+
                "To check for discounts,"+
                "Please enter your country..   ").capitalize().strip()

print(f"Great! You have a discount!\nThe price now is: {price}$"
      if country in countries else
      f"There's no discount for you,\nThe price is: {price}$")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")