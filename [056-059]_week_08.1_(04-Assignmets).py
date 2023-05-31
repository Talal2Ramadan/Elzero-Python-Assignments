################################################
## << Mastring Python -- Elzero Web School >> ##
#########    WEEK #00.0 Assignments    #########
## ----------- From #000  to #000 ----------- ##
print("############ Starting ############\n") ##
################################################




#######################################
#        <<<<< task #01 >>>>>        ##
print("\n<<<<< task #01 >>>>>")      ##
#######################################  
def calculate(num1, num2, operation = "+"):
    if operation.strip().lower() in ("+", "a", "add"):
        print( num1 + num2)
    elif operation.strip().lower() in ("-", "s", "subtarct"):
        print( num1 - num2)
    elif operation.strip().lower() in ("*", "m", "mutliply"):
        print( num1 * num2)
    elif operation.strip().lower() in ("/", "d", "division"):
        print( num1 / num2)
    elif operation.strip().lower() in ("//", "f", "floor", "floor_division"):
        print( num1 // num2)
    elif operation.strip().lower() in ("%", "mo","mod", "modulas"):
        print( num1 % num2)
    else: print("Invalid Operation!!")

calculate(4, 5)              # defult addition
calculate(65, 5, "floor")    # floor division
calculate(4, 5, "Wrong")     # wrong operation
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
def addition(*args):
    counter = 0
    for number in args:
        if number == 10:
            continue
        elif number == 5:
            counter -= number
        else: counter += number
    print(counter)

addition(7, 4, 10, 5, 11)            # 22 - 5 # 10 ignored
addition(10, 20, 30, 10, 15)         # 65
addition(10, 20, 30, 10, 15, 5, 100) # 160
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
def show_skills(name, *skills):
    if len(skills) != 0:
        print(f"Hello {name.title()}! Your skills are:")
        for skill in skills:
            print(f"- {skill.upper()}")
    else: print(f"Hello {name.title()}! You got no skills to show.")
show_skills("shaapan abdelreheem", "html", "css", "js", "python")
show_skills("khaled bo tayeb")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
def say_hello(name="Talal", age=24, country="Egypt"):
    print(f"Hello {name}! Your age is {age}, and you live in {country}")
say_hello()
say_hello("Shadi", 22, "Helwan")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")