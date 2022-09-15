# Assignment1
name="Aliaa"
age= "20"
country= "Egypt"
print("Hello \'"+name+" \', How You Doing \\ \"\"\" Your Age Is \""+age+"\" + And Your Country Is :"+country)

#Assignment2
name="Aliaa"
age= "20"
country= "Egypt"
print("Hello \'"+name+" \', How You Doing \\\n \"\"\" Your Age Is \""+age+"\" +\n And Your Country Is :"+country)

#Assignment 3
name = 'Elzero'
print("The secand lettre is:\""+name[1]+"\"" "\n" "the thired litter is :\""+name[2]+"\"" "\n"  "the last litter is :\""+name[5]+"\"" ) 

#ASSIGNMENT4
name = 'Elzero'
print(name[1:4])
print(name[0:1]+name[2:3]+name[4:5])   #Way with concatenation
print(name[: :2])       #another way[start:end:staps]
print(name[-2:-7:-2])     #لما باجى ادى النهايه بالعكس بزود النهايه واحد عن القيمه الاصليه

#Assignment 5
name = "#@#@Elzero#@#@"
print(name.replace("#@#@","    " ,2))     #replace(old,new,count)

#Assignment 6
num1= "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

#Assignment 7
name_one = "Aliaa"
name_two = "Aliaa_Nabil"
print(name_one.rjust(20,"@"))
print(name_two.rjust(19,"@"))

#Assignment 8
name_one = "Aliaa"
name_two = "aliAA"
print(name_one.swapcase())
print(name_two.swapcase())

#Assignment 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

#Assignment 10
name = "Elzero"
print(name.index("z",0,6))

#Assignment 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1))

#Assignment 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",2))

#Assignnment13
name = "Aliaa"
age = 20
country = "Egypt"
print(f"My name is :{name} and my age is :{age} and my country is :{country}")






