# #bilt in functions
# #assignment 1
# ##############################
# values = (0, 1, 2)

# if any(values):

#   my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#   print("Good")

# else:

#   print("Bad")
# #####################################
# #output
# #true      #first condition
# #true
# #false
# #false     #or need one condition at lest true
# #Good      # result
#################################################################################################
# #assignment 2
# v = 40                                  #v=40
# my_range = list(range(v))
# print(sum(my_range, v) + pow(v, v, v))  # 820
##################################################################################################
# #assignment3
# n =20              # 200/20=10 ,210/21=10.0 is true also becouse he need round of the number
                     #sum(0 to n)=n*(n+1)/2
# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
#   print("Good")
# #print(sum(l)/n)   for testing
# #the result must be equal 10
####################################################################################################
##assignment 4
# my_all=all
# print(my_all([1, 2, 3]))    # True
# print(my_all([1, 2, 3, []]))  # False
# #################################
# print("%"*50)
# my_any=any
# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False])) # False
# ##################################
# print("%"*50)
# my_min=min
# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100
# ##################################
# print("%"*50)
# my_max=max
# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700
#########################################################################################################
# #assignment 1 from 72 to 75
# def remove_chars(character):
#     return character[1:-1]
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# cleand_list=map(remove_chars,friends_map )
# for name in cleand_list:
#     print(name)
# print("%"*100)
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# cleand_list=map(lambda character:character[1:-1],friends_map )
# for name in cleand_list:
#     print(name)
#############################################################################################################
# #assignment 2
# from tkinter import N


# def get_name(name):
#     return name.endswith("m")
# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# names=filter(get_name,friends_filter)
# for name in names:
#     print(name)
# print("%"*100)
# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# names=filter(lambda name:name.endswith("m"),friends_filter)
# for name in names:
#     print(name)
#################################################################################################################
# #assignment 3
# from functools import reduce


# def mul(num1,num2):
#     return num1*num2
# nums = [2, 4, 6, 2]
# result=reduce(mul,nums)
# print(result)
# print("%"*100)
# nums = [2, 4, 6, 2]
# result=reduce(lambda num1,num2:num1*num2,nums)
# print(result)
#######################################################################
# #assignment 4               (1)
# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
# reverse_skiills=reversed(skills)
# myskillwithcounter=enumerate(reverse_skiills,50)
# for c,s in myskillwithcounter:
#     if type(s)==int:
#         continue
#     else:
#         print(f"{c}-{s}")
# print("%"*100)           #(2)
# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
# reverse_skiills=reversed(skills)
# myskillwithcounter=enumerate(reverse_skiills,50)
# for c, s in myskillwithcounter:
#     if type(s)==int:
#       continue
#     else:
#         print(c,s)
# print("%"*100)           #(3)
# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
# reverse_skiills=reversed(skills)
# c=50
# for skill in reverse_skiills:
#     if type(skill)==int:
#         continue
#     else:
#         c+=1
#         print(f"{c}_{skill}")
#######################################################################################