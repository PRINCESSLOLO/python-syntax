##loop
##assignment1
##################################
num = int(input("Please enter a +ve number.\n"))
while num <= 0:
  num=int(input("Number is not larger than 0.\n"))          #if it wasnot a variable it will print infinite loop (print only is rong)
else:
    print("the number you entered is correct .")
    count= 0                #we use the counter started with 0 to prevent printing 0      
while num >1:             #we start with 1 to prevent print the number we are entered .
    num -= 1
    if(num == 6):
        continue
    print(num)
    count+= 1             #update
else:
    print (f"{count} Numbers was Printed ")
#######################################
#assignment2
#######################################
counter =0
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
while counter <5:
    counter += 1
counter2 = 0
Ignored = 0
while counter2 < 5:
    if friends[counter2].islower():
        counter2 += 1
        Ignored += 1
        continue
    else:
        print(friends[counter2])
    counter2 += 1
print(f"Friends Printed And Ignored Names Count Is {Ignored}")
######################################################
#Assignment3
######################################################
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop(0))                                                    #done

print(skills.pop(-1))  #start from end
######################################################
#Assignment4
######################################################
count=0
my_friends=[]
while count<4:
   num=input(f"please enter your friends names :{count+1}\n").strip()
   #my_friends.append(num)
   #count+=1
   if num.isupper():
    print("Invalid Name")
    continue
   elif num[0].islower():
        print(f"Friend {num} Added => 1st Letter Become Capital \n ")
        #num=num.capitalize()
        my_friends.append(num.capitalize())
        count+=1
        continue
   else:
        my_friends.append(num)
        print("name is added .\n")
        count+=1
else:
    print(f"{count} friends is added.")
    print(my_friends)


############################################
#assignment 1 from 51 to 55
###################################                         
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 1
for number in my_nums:
    if number % 5 == 0:
        print(f"{count} => {number} ")
        count += 1

print("All Numbers Printed.\n")
#######################################
# assignment 2 from 51 to 55                        #done
####################################  
# my_range=range(1,21)  
my_range=range(1,21)
for num in my_range:
    num=str(num)
    if num=="6"or num=="8"or num=="12" :
        continue
    else:    
        print(num.zfill(2))
print("All Numbers Printed")
######################################
#assignment 3 from 51 to 55                    #done
#####################################
my_ranks = { 'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
values={
    "A":"100",
    "B":"80",
    "C":"40"
}
sum=0
for main_key ,main_value in my_ranks.items() :
    print(f"My Rank in {main_key} Is {main_value} And This Equal {values[main_value]} Point")
#######################################
# assignment 4 from 51 to 55                    #done
######################################
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

progress_value={
  "A":100,
  "B":80,
  "C":40,
  "D":20
}
print("@@@@@@@@@@@@@@@@ first way @@@@@@@@@@@@@@@@@@@@@")
for main_key, main_value in students.items():
  sum = 0
  print("------------------------------")
  print(f"-------student name =>{main_key}")
  print("------------------------------")
  for key, value in students[main_key].items():
    print(f" {key} => {progress_value[value]} points.")
    sum += progress_value[value]
  print(f"Total points for {main_key} is {sum}")          #solved
      
print("@@@@@@@@@@@@@@@@@ second way @@@@@@@@@@@@@@@@@@@")
for names in students:
    sum = 0
    print("------------------------------")
    print(f"-- Student Name => {names}")
    print("------------------------------")
    for value in students[names]:
        print(f"{value} => {progress_value[students[names][value]]} points.")
        sum += progress_value[students[names][value]]
    print(f"Total points for {names} is {sum}")

