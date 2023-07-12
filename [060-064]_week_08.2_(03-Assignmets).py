################################################
## << Mastring Python -- Elzero Web School >> ##
#########    WEEK #08.2 Assignments    #########
## ----------- From #060  to #064 ----------- ##
print("############ Starting ############\n") ##
################################################




#######################################
#        <<<<< task #01 >>>>>        ##
print("\n<<<<< task #01 >>>>>")      ##
#######################################  
def get_score(**args):
    for a, b in args.items():
        print(f"{a} => {b}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #02 >>>>>        ##
print("\n<<<<< task #02 >>>>>")      ##
#######################################  
## This answer was created by Bing AI chat :) 
def get_people_scores(name=None, **topics):
    if name is not None:
        if topics:
            print(f"Hello {name} your scores table is:")
            for topic, score in topics.items():
                print(f"{topic} => {score}")
        else:
            print(f"Hello {name} you have no scores to show.")
    else:
        for topic, score in topics.items():
                print(f"{topic} => {score}")
    
get_people_scores("Osama", Math=90, Science=80, Language=70)
print("===========")
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("===========")
get_people_scores(Logic=70, Problems=60)
print("===========")
get_people_scores("Ahmed")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#######################################
#        <<<<< task #03 >>>>>        ##
print("\n<<<<< task #03 >>>>>")      ##
####################################### 
scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}
def get_the_scores(name=None, **dictionary):
    if name is not None:
        if dictionary:
            print(f"Hello {name} This Is Your Score Table:")
            for subject, score in dictionary.items():
                print(f"{subject} => {score}")
        else:
            print(f"Hello {name} you have no scores to show.")
    else:
        for subject, score in dictionary.items():
                print(f"{subject} => {score}")
    
        
get_the_scores("Fatema", **scores_list)
print("===========")
get_the_scores("Fatema")
print("===========")
get_the_scores(**scores_list)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




###############################################
###############################################
print("\n############# Finished #############")