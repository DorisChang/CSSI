#Getting input
'''first_name = raw_input("What is your first name? ") #some  use input() instead of raw_input()
last_name = raw_input("What is your last name? ") #raw input returns a string
print(first_name + " " + last_name)

word = raw_input("Enter a word: ")
print(word*5)'''

#type() function tells you what data type something is

#Casting 
'''num_1 = int(raw_input("Enter the first number: "))
num_2 = int(raw_input("Enter the second number: "))
print("The sum is: " + str(num_1 + num_2)) #casting sum from int to str'''

#Control Flow
    #Conditionals: use booleans and boolean operators to determine IF something should happen
    #Loops: while & for loops
    '''for i in range(your_age):
        print("Happy Birthday!")'''
    '''for letter in "hello":
        print(letter.upper())'''
    '''range(5) --> [0,1,2,3,4]
    range(2,5) --> [2,3,4]
    range(0,10,2) --> [0,2,4,6,8]'''

#String Formatting
'''print("%s sang %s, %s and %s" % (name, song1, song2, song3))'''

#Functions
''' - another type of control Flow
    - used to organize code
    - keeps commonly run blocks of code together
    - allows code reuse
    def greetAgent(): 

def greetAgent(first_name, last_name): # function header
    print("%s. %s %s." % (last_name, first_name, last_name))    

def createAgentGreeting(first_name, last_name):
    return("%s. %s %s." % (last_name, first_name, last_name))
greeting = createAgentGreeting("James", "Bond")
print(greeting)'''

#Lists
'''fruits = []
marks = list()
names = ["Drake", "Eminem", "Jay-Z"]
names.append("Kanye")
names.insert(1, "Drake") #adds Drake to index 1
del names[0]
marks.sort() #sorts list from smallest to biggest
"Drake" in names  #Boolean '''
'''mutable, can change size'''

