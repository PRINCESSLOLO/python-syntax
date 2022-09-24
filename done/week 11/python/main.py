#assignment 1
import random
from sqlite3 import DateFromTicks
print(f"Random Number Between 10 And 50 =>{random.randint(10,50)}")
print("*"*50)
from random import randint
print(f"Random Even Number Between 2 And 10 =>{randint(1,5)*2}")
print("*"*50)
print(f"Random Odd Number Between 1 And 9 =>{randint(1,3)*2-1}")
print("*"*50)
##############################################   #assignment 2
import my_mod                        
print(dir(my_mod))
my_mod.say_hello ("aliaa")
my_mod.say_hello ("ali")
my_mod.say_hello ("alaa")
print("*"*50)
my_mod.say_welcome ("aliaa")
my_mod.say_welcome ("ali")
my_mod.say_welcome ("alaa")
print("*"*50)###################################    #assignment 3
from my_mod import say_welcome          
say_welcome("Aliaa")
print("*"*50)###################################    #assignment 4
from my_mod import say_welcome as new_welcome   
new_welcome("Aliaa")
##########################################################################
#assignment 1 part 2
print("*"*50)
import datetime
Date = datetime.datetime(2021, 6, 25)
dateNow = datetime.datetime.now()
print(f"Days From 2021-06-25 To 2022-09-23 Is => {(dateNow - Date).days} Days.")
print("*"*50)
########################################################################
#assignment 2 part 2
dateNow = datetime.datetime.now()
print(dateNow.strftime("%d %B %Y"))
print(dateNow.strftime("%d, %B, %Y"))
print(dateNow.strftime("%d/%B/%Y"))
print(dateNow.strftime("%d - %B - %Y"))
print(dateNow.strftime("%B - %Y"))
##########################################################################
#assignment 1 part 3
def reverse_string(my_str):
    my_str = reversed(my_str)
    for letter in my_str:
        yield letter


for c in reverse_string("Elzero"):
    print(c)
############################################################
#assignment 2 part 3
def make_sugar(funname):
    def nestedfun():
        print("Sugar Added From Decorators")
        funname()
        print("#"*50)
    return nestedfun
@make_sugar
def make_tea():
  print("Tea Created")
@make_sugar
def make_coffe():
  print("Coffe Created")
make_tea()
make_coffe()
