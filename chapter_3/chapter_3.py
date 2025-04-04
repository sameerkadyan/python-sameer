# Question 1 :-
'''
write a python program to display a user entered name followed by Good Afternoon using input() function? 
'''
# There is two method to solve of this question
# 1st method (Old Method)
'''
name = input("Enter your name is here")
print("Good Afternoon ", name)

'''
# 2nd methos (Modern Method)
'''

name = input("Enter Your name is here \n")
print(f"Good Afternoon {name}")'

'''
# Question 2 :-
'''
write a program to fill in a letter template given below with name and date
letter = "
            Dear <|Name|>
            you are selected
            <|Date|>
            "
'''
# Answer 2 :-

'''

letter = 
            Dear <|Name|>
            you are selected
            <|Date|>
            
nxtLetter = letter.replace("<|Name|>", "Sameer kadyan").replace("<|Date|>","5 April")

print(nxtLetter)

'''

# Queation 3 :-
'''
Write a program to detect double space in a string 
'''
# Answer 3 :-
'''
str = "Hi I am Sameer kadyan  and what's your name "
print(str.find("  "))
'''

# Question 4 :-
'''
Replace the double space from problem 3 with single sapce
'''
# Answer 4 :-
'''
str = "Hi I am Sameer kadyan  and what's your name "
print(str.replace("  ", " "))
'''

# Question 5 :-
'''
write a program to format the following letter using escape sequence characters.

letter = " Sameer Bhai sahab aap great ho aapke jaisa koi nahi hai "
'''
# Answer 5 :-
'''
letter = " Sameer Bhai saha\t aap great ho\n aapke \"jaisa\" koi nahi hai "
print(letter)
'''

