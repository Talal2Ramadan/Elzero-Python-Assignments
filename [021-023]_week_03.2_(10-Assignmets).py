################################################
## << Mastring Python -- Elzero Web School >> ##
#########    WEEK #03.2 Assignments    #########
## ----------- From #021  to #023 ----------- ##
print("############ Starting ############\n") ##
################################################




#######################################
#        <<<<< task #01 >>>>>        ##
print("\n<<<<< task #01 >>>>>")      ##
#######################################  
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0::2])
print(friends[1::2])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends.pop(-1)
friends.pop(-1)
friends.extend(["Elzero", "Elzero"])
print(friends)
# better one
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2] = friends[-1] = "Elzero"
print(friends)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #05 >>>>>        ##
print("\n<<<<< task #05 >>>>>")      ##
####################################### 
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #06 >>>>>        ##
print("\n<<<<< task #06 >>>>>")      ##
####################################### 
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.pop(0)
friends.pop(0)
print(friends)
friends.pop(-1)
print(friends)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #07 >>>>>        ##
print("\n<<<<< task #07 >>>>>")      ##
####################################### 
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
all = []
all.extend(friends)
all.extend(employees)
all.extend(school)
print(all)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #08 >>>>>        ##
print("\n<<<<< task #08 >>>>>")      ##
####################################### 
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #09 >>>>>        ##
print("\n<<<<< task #09 >>>>>")      ##
####################################### 
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #10 >>>>>        ##
print("\n<<<<< task #10 >>>>>")      ##
####################################### 
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")