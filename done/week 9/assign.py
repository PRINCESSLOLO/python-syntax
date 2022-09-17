#import os          #assignment 1 (file handiling)
# count=1
# while count<=50:
#     #myfile=open(fr"C:\Users\fagr\Desktop\python\txt{count}.txt","x")       #first step to create 50 text
#     if count !=25:
#         myfile=open(fr"C:\Users\fagr\Desktop\python\txt{count}.txt","w")
#         myfile.write (f"Elzero Web School => {count}\n")
#         if count==25:
#             myfile=open(fr"C:\Users\fagr\Desktop\python\ special-text.txt","w")
#             myfile.write(None)
#     count+=1
# myfile=open(r"C:\Users\fagr\Desktop\python\txt1.txt","a")              #####assignment 2##########
# # myfile.write (f"Elzero Web School => 1\n")
# myfile.write ("Appended => Elzero Web School \n "*50) 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# print("%"*100)
# print(os.getcwd())
# print("%"*100)
# print(os.path.abspath(__file__))
# #print(__file__)
# print("%"*100)
# print(os.path.relpath(__file__))
# print("%"*100)
# print(len(os.getcwd()))
##############################################################################            #assignment 3
# myfile=open(r"C:\Users\fagr\Desktop\python\txt1.txt")
# read_data=myfile.read()
# myfile=open(r"C:\Users\fagr\Desktop\python\txt1.txt")
# lines=myfile.readlines()                     #back list 
# num_words=read_data.split()                 #take date and return it in a list (splite()\rsplite()\splite line())
# word=0
# char=0
# for items in lines:
#     for words in items:
#         if words:
#          word+=1
#         if words=="l":
#             char+=1
# print(f"Number Of Lines Is =>{len(lines)}")
# print(f"Number Of Words Is =>{len(num_words)}")     
# print(f"Number Of Chars Is =>{word}")               #????????????
# print(f"Number Of Word (I) Is =>{char}")
####################################################################################
#assignment 4                    #done
# counts=50
# while counts>40:
#    os.remove(fr"C:\Users\fagr\Desktop\python\txt{counts}.txt")
#     counts=counts-1

###############################    #assignment4 (2)
# my_range=range(41,51)
# for num in my_range:
#     if num>40:
#         os.remove(fr"C:\Users\fagr\Desktop\python\txt{num}.txt")      #in this code he remove from 41 to 49 
#                                                                       #text 50 not removed
