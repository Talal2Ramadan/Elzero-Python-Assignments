################################################
## << Mastring Python -- Elzero Web School >> ##
#########    WEEK #10.1 Assignments    #########
## ----------- From #069  to #071 ----------- ##
print("############ Starting ############\n") ##
################################################

# only the first task is solved, others are need
# more study.

#######################################
#        <<<<< task #01 >>>>>        ##
print("\n<<<<< task #01 >>>>>")      ##
#######################################  
values = (0, 1, 2)
# delclaring a tuple of numbers.
if any(values):
# the condition checks if any item is true (which is right), then:
# declare a new variable my_var and assign it to 0 value.
  my_var = 0
# declare a new list my_list and assign it to maltiple values.
my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
# as appears, the list contains 5 True values, and 1 False value.
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
# this condition checks if any of the conditions mintions is True,
# the three check each a part of the list, as the False item is the
# last item of the list, with the index [5], so whenever the iteration
# don't contain it, the code will work.
# the first condition at least is true so the code will work.
  print("Good")

else:

  print("Bad")
# output is "Good"
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
print(pow(5,5,5))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
#  code
#  to
#  be
#  run
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")