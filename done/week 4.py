#---------------------------------------
#set
#---------------------------------------
#Assignment 1
#my_list = [1, 2, 3, 3, 4, 5, 1]
#unique_list =set(my_list)           # i do this becouse set is unique 
#unique_list =list(unique_list)         
#print(unique_list)
#print(type(unique_list))
#unique_list.pop(-1)
#print(unique_list)
#----------------------------------------
#Assignment 2
#nums = {1, 2, 3}
#letters = {"A", "B", "C"}
#print(nums|letters)        #first way
#print(nums.union(letters)) #second way
#nums.update(letters)       third way
#print(nums)
#------------------------------------------
#Assignment 3
#my_set = {1, 2, 3}
#letters = {"A", "B", "C"}
#print(my_set )
#my_set .clear()
#print(my_set )
#my_set .add("A")
#my_set .add("B")
#my_set .discard("C")
#print(my_set )
#--------------------------------------------
#Assignment 4
#set_one = {1, 2, 3}
#set_two = {1, 2, 3, 4, 5, 6}
#print(set_one.issubset(set_two ))    #True
#------------------------------------------
#Dictionary
#------------------------------------------
#Assignment 5
languages={
    "one":{  
    "name":"html",
    "progress":"80%"
},
"two":{
    "name":"css",
    "progress":"90%"
},
"three":{
    "name":"python",
    "progress":"90%"
},
}
print(languages['one'])
print(languages['two'])
print(languages['three'])
languages.update({"four":{
    "name":"AI",
    "progress":"70%"
}})
print(languages['four'])


