#assignment 2
###############################################################
num1=int(input("please input your first number.\n").strip())
num2=int(input("please input your second number.\n").strip())
operation=input("please input youroperation.\n").strip()
print(f"the operation is ({num1}{operation}{num2})")
if operation =="+":
    print(f"answer is : {num1+num2}")
elif operation=="-" :
          print(f"answer is : {num1-num2}")

elif operation=="*" :
          print(f"answer is : {num1*num2}")
elif operation=="/" :
          print(f"answer is : {num1/num2}")
elif operation=="%" :
          print(f"answer is : {num1%num2}")
else:
    print("you entered a rong operation ")
print("@"*80)
############################################################################
#assignment 2
############################################################################
age =int(input("please enter your age : "))
if age > 16 : print("App Is Suitable For You")    ##Ternary Conditional Operator
else: print("App Is Not Suitable For You")
print("@"*80)
################################################################################
#assignment 3
################################################################################
age =int(input("please enter your age : "))
if age >10 and age <100 :
    months=int(age)*12
    weeks=months*4
    days=int(age)*365
    mintes=days*60
    seconds=mintes*60
    print(f"Your Age In Months Is {months} Months")
    print(f"Your Age In Weeks Is {weeks} weeks")
    print(f"Your Age In Days Is {days} days")
    print(f"Your Age In mintes Is {mintes} mintes")
    print(f"Your Age In seconds Is {seconds} seconds")
else:
    print("the age you entered is out of range .")
print("@"*80)
#####################################################################################
#assignment 4
#####################################################################################
country = input("Input Your Country : \n ").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries :
    print (f"Your Country Eligible For Discount And The Price After Discount Is ${price-30}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
print("@"*80)
#######################################################################################
