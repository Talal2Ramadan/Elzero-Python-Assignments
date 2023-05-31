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
my_nums = [15, 81, 5, 17, 20, 21, 13]
counter = 1
for num in my_nums:
    if (num % 5) == 0:
        print(f"{counter} => {num}")
        counter += 1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
for num in range(1, 20):
    if num not in (6, 8, 12):
        print(str(num).zfill(2))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
my_ranks = {
  'Math': 'A',
  'Science': 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
grades_values = {
    'A': 100,
    'B': 80,
    'C': 40
}
for key, value in my_ranks.items():
    print(f"My rank in {key} is {value} and that equals {grades_values[value]} points.")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #04 >>>>>        ##
print("\n<<<<< task #04 >>>>>")      ##
####################################### 
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
grades_values = {
    'A': 100,
    'B': 80,
    'C': 40,
    'D': 20
}

for name, grades in students.items():
    print("------------------------------")
    print(f"-- Student Name => {name}")
    print("------------------------------")
    total_points = 0
    for course, grade in grades.items():
        course_grade = grades_values[grade]
        print(f"- {course} => {grades_values[grade]}")
        total_points += course_grade
    print(f"Total points for {name} is {total_points}")    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")