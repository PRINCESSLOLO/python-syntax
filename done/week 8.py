# #Function
# #####################################
# #assignment1
# #####################################
# def calculate(num1,num2,operation="unknown"):
#     num1=int(num1)
#     num2=int(num2)
#     operation=str(operation).strip()
#     print(f"the operation is ({num1}{operation}{num2})")
#     if operation =="+":
#          print(f"answer is : {num1+num2}")
#     elif operation=="-" :
#           print(f"answer is : {num1-num2}")

#     elif operation=="*" :
#           print(f"answer is : {num1*num2}")
#     elif operation=="unknown" :
#           print(f"answer is : {num1+num2}")
#     else:
#        print("you entered a rong operation ")
# calculate(100,50, )
###########################################################
##assignment2
#########################################################
# def addition(*nums):
#     sum=0
#     for num in nums:
#         if num==10:
#             continue
#         if num==5:
#             sum-=5
#             continue
#         else:
#           sum+=num
#     return sum
# print(addition(10, 20, 30, 10, 15))  #65
# print(addition(10, 20, 30, 10, 15, 5, 100))   #160
###########################################################
##assignment3
##########################################################
# def show_skills(name,*skills):
#     if not skills:
#       print(f"Hello {name} You Have No Skills To Show")          #there is a problem in this place not solved yet  (solved)
#     else:
#         print(f"hello {name} your skills is:")
#         for skill in skills:
#             print(f"-{skill}")
# show_skills("Aliaa","HTML", "CSS", "JS", "Python")
# print("!"*80)
# show_skills("Aliaa")
#########################################################
##assignment4
##########################################################
# def say_hello(name="unknown",age="unknown",country="unknown"):
#     print(f"Hello {name} your age is {age} and your country is {country}".strip())
# say_hello("Aliaa","20","Egypt")
# print("*"*50)
# say_hello()
############################################################
##assignment 1 from 60 to 64
############################################################
# def get_score(**scores):
#     for main_key ,main_value in scores.items():
#         print(f"-{main_key}=>{main_value}")

# get_score(Math=90, Science=80, Language=70)
# print("+"*80)
# get_score(Logic=70, Problems=60)
############################################################
##assignment 2 from 60 to 64                                  #done
############################################################
# def get_people_scores(name=None,**skills):
#     if not skills :
#        print(f"Hello {name} You Have No Scores To Show".strip())
#        return
#     else:
#       if name:
#         print(f"Hello {name} This Is Your Score Table: ".strip())
#         for skill,score in skills.items():
#           print(f"-{skill}=>{score}")
#       else:
#         if not name:
#             for skill,score in skills.items():
#               print(f"-{skill}=>{score}")
#             return
#     return
# get_people_scores("aliaa", Math=90, Science=80, Language=70)
# print("*"*50)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# print("*"*50)
# get_people_scores(Logic=70, Problems=60)                          #not solved yet(solved)(for loop inside if condition + return )
# print("*"*50)
# get_people_scores("Ahmed")
# ############################################################
##assignment 3 from 60 to 64                                     #done
############################################################
# scores_list={
# "Math": "90",
# "Science": "80",
# "Language": "70"
# }
# def get_the_scores(name=None,**score_list):
#     if not score_list:
#         print(f"Hello {name} You Have No Scores To Show".strip())
#         return
#     else:
#         if name:
#           print(f"Hello {name} This Is Your Score Table: ".strip())
#           for skill,score in score_list.items():
#             print(f"-{skill}=>{score}")
#         else:
#            if not name :
#              for skill,score in score_list.items():
#                print(f"-{skill}=>{score}")
#              return
#     return
# get_the_scores("Osama", **scores_list)
# print("&"*90)
# get_the_scores("Osama")
# print("&"*90)
# get_the_scores(**scores_list)          #not solved yet(solved)(for loop inside if condition +return)