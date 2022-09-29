# #assignment 1 
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []
# final_string=""
# for data in zip(my_list, my_tuple):
#     final_string+=data[0]+data[1]
#     print(final_string)
#     print(data)
###############################################
# #assignment 2 ٍ
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []
# final_string=""
# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     if item1 ==1 or item2==1 or item3==1  :
#         break
#     else:
#         # final_string+=item2[1]+item3[1]
#         # my_data.append(item1)
#         final_string="".join (my_data)
#         print(final_string)
################################################
# #assignment 3
# from PIL import Image
# import os 
# print(os.path.abspath(__file__))
# file = Image.open(r"C:\Users\fagr\Desktop\python work\week 12\elzero-pillow.png")
# myImage=file
# myImage.show()
# myBox = (400,0,800,400)
# myNewImage = myImage.crop(myBox)
# myNewImage.show()
# myConverted = myNewImage.convert("L")
# myConverted.show()
# myNewImage.save(r"C:\Users\fagr\Desktop\python work\week 12\img3.png")
# #######################
# myImage=Image.open(r"C:\Users\fagr\Desktop\python work\week 12\elzero-pillow.png")
# myBox2 = (0,400,1200,800)
# myNewImage2 = myImage.crop(myBox2)
# myNewImage2.show()
# myConverted = myNewImage2.convert("L").rotate(180)
# myConverted.show()
# myNewImage2.save(r"C:\Users\fagr\Desktop\python work\week 12\img4.png")
# myNewImage2 =myNewImage2.rotate(180)
# myNewImage2.show()
# myNewImage2.save(r"C:\Users\fagr\Desktop\python work\week 12\img2.png")
##################################################################################
#assignment 4
# def say_hello_to(name):
#  """parameter(someone) => Person Name
# Function To Say Hello To Anyone"""
#  print(f"Hello {name}") # "Hello Osama"
# say_hello_to("Aliaa")
# #print(say_hello_to.__doc__)
# help(say_hello_to)
#########################################################
#assignment 5   #install pylint
# ''' Function To Say Hello To Anyone'''
# my_Friends = ["Ahmed", "Osama", "Sayed"]
# def say_Hello(Some_Peoples) -> list:
#   for Some_one in Some_Peoples:
#     print(f"Hello {Some_one}.")
# say_Hello(my_Friends)
###########################################################
# #assignment 1 part 2
# NUM = input("Add Your Number ")
# if len(NUM) != 1:
#     raise IndexError("Only one character allowed.")
# elif NUM =="0":
#     raise ValueError(f"Number Must Be Larger Than {NUM}")
# elif type(NUM)!=int:
#      raise Exception("Only Numbers Allowed")  
# # elif NUM.isalpha():
# #     raise Exception("Only numbers allowed")
# else:
#      print("corect entered.")
#      print(f"The Number Is {NUM}")
##############################################################
#assignment 2
# try:
#     LETTER = input("Add Letter From A to Z : ".strip())
#     if len(LETTER)!=1:
#      raise ValueError
#     elif LETTER .islower() :
#         raise TypeError
# except ValueError:
#     print("You Must Write One Character Only")
# except TypeError:
#     print("The Letter Not In A - Z")
# else:
#     print(f"You Typed {LETTER}")
####################################################
#assignment 3
# def calculate(num1, num2)->int:        #Type Hinting
#   return num1 + num2

# print(calculate(20, 30))
######################################################