################################################
## << Mastring Python -- Elzero Web School >> ##
#########    WEEK #10.2 Assignments    #########
## ----------- From #072  to #075 ----------- ##
print("############ Starting ############\n") ##
################################################




#######################################
#        <<<<< task #01 >>>>>        ##
print("\n<<<<< task #01 >>>>>")      ##
#######################################  
def remove_chars(word):
    return word[1:-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars, friends_map)
for item in cleaned_list:
    print(item)

# with Lambda
cleanedWithLamda= map(lambda word: word[1:-1], friends_map)
for n in cleanedWithLamda:
    print(n)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
def get_names(name):
    return name.endswith("m")
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names, friends_filter)
for name in names:
    print(name)

# with Lambda
namesWithLamda= filter(lambda name: name.endswith("m"), friends_filter)
for n in namesWithLamda:
    print(n)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
nums = [2, 4, 6, 2]
from functools import reduce
def multiply(num1, num2):
    return num1 * num2
result = reduce(multiply, nums)
print(result)

# with Lambda
resultWithLambda = reduce(lambda n1, n2: n1 * n2, nums)
print(resultWithLambda)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
enumeratedSkills = enumerate(reversed(skills), 50)
for a, b in enumeratedSkills:
    if type(b) == int:
        pass
    else:
        print(f"{a} - {b}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")