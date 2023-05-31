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
num = int(input("Enter a number bigger than 0:   "))
counter = 0
if num > 0:
    while num > 0:
        num -= 1
        if num == 6 or num == 0:
            continue
        else: 
            print(num)
            counter += 1
    if counter > 0:        
        print(f"{counter} Numbers Printed Successfully.")
    else: print("No numbers to print")    
else: print(f"Number {num} Is Not Larger Than 0")    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
counter = 0
while counter < len(friends):
    if str(friends[counter]).istitle():
        print(friends[counter])
    counter += 1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0)) 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
my_friends = []
while len(my_friends) < 4:
    new_friend = input("Enter the new friend's name:   ").strip()
    if new_friend.isupper():
        print("invalid name, use lower case!")
    elif new_friend.islower():
        print(f"Successfully added {new_friend}")
        print(f"Automatically: {new_friend} changed to: "+
              f"{new_friend.capitalize()}")
        my_friends.append(new_friend.capitalize())
        print(f"Places left in the list: {4- len(my_friends)}") 
    elif new_friend.istitle():
        print(f"Successfully added {new_friend}")
        my_friends.append(new_friend)
        print(f"Places left in the list: {4- len(my_friends)}")
    else:
        print(f"Successfully added {new_friend},"+
              "\nand will be automatically capitalized!")
        my_friends.append(new_friend.capitalize())
        print(f"Places left in the list: {4- len(my_friends)}") 
else: print(my_friends)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")