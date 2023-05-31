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
name = input("Please enter your name\n").strip().capitalize()
print(f"Hello Mr/Mrs {name}! could you please eat shit!")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
# This task cannot be solved without using Control
# Flows, which is not studied yet.
# otherwise.. it's just a regular input field, and
# two print masseges.
age = int(input("Enter your age please!\n"))
print("Hello Your Age Is Under 16, Some Articles Are Not Suitable For You")
print(f"Hello Your Age Is {age}, All Articles Are Suitable For You")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
first_name = input("Enter you first name please!\n").strip().capitalize()
last_name = input("Enter you last name please!\n").strip().capitalize()
print(f"Hello {first_name} {last_name:.1s}.")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
email = input("Enter you E-mail please!\n").strip().lower()

username         = email[:email.index("@")].capitalize()
service_provider = email[email.index("@")+1:email.index(".")]
domain           = email[email.index(".")+1:]

print(f"Your Name Is {username}")
print(f"Email Service Provider Is {service_provider}")
print(f"Top Level Domain Is {domain}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")