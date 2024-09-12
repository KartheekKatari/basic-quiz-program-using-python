
q1='''Which of the following is used to iterate over a sequence (such as a list) in Python?
a) for loop
b) foreach loop
c) while loop
d) iterate loop'''
q2='''What is the purpose of the __init__ method in a Python class?
a) To initialize the class variables
b) To define the constructor
c) To create a new object of the class
d) To destroy an object of the class'''
q3='''How can you open a file named "example.txt" in read mode in Python?
a) file = open("example.txt", "r")
b) file = open("example.txt", "w")
c) file = open("example.txt", "a")
d) file = open("example.txt", "x")'''
q4='''What is the output of the following code snippet?
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares)
a) [1, 4, 9, 16, 25]
b) [1, 2, 3, 4, 5]
c) [2, 4, 6, 8, 10]
d) [0, 1, 4, 9, 16]'''
q5='''What is the purpose of the pass statement in Python?
a) To create an empty class
b) To do nothing or create a placeholder
c) To exit a loop
d) To skip the current iteration of a loop'''
q6='''How do you check the length of a list in Python?
a) size(list)
b) length(list)
c) len(list)
d) count(list)'''
q7='''What does the __str__ method do in Python?
a) Converts an object to a string
b) Prints the object's memory address
c) Deletes an object
d) Initializes an object'''
q8='''In Python, what is the purpose of the __name__ variable?
a) Holds the name of the module
b) Holds the name of the class
c) Holds the name of the function
d) Holds the name of the variable'''
q9='''What is the correct way to comment multiple lines in Python?
a) // This is a comment
b) /* This is a comment */
c) # This is a comment
d) <!-- This is a comment -->'''
q10=''' What is the output of the following code snippet?
x = [1, 2, 3]
y = x
y[0] = 100
print(x[0])
a) 1
b) 100
c) 2
d) 3'''
questions={q1:"a",q2:"b",q3:"a",q4:"a",q5:"B",q6:"c",q7:"a",q8:"a",q9:"c",q10:"b"}
name=input("Enter your name:")
print("Hello",name,"Welcome to the quiz")
score=0
for i,j in questions.items():
 print()
 print(i)
 option=input("Do you want to skip this question(Yes/No):")\
 if option=="Yes":
     continue
 ans=input("Enter your answer(a/b/c/d):")
 if ans==questions[i]:
     print("Correct answer,you got 1 point")
     score=score+1
     print("Current score is:",score)
     print("Current score is:",score)
else:
     print("Wrong answer you lost 1 point")
     print("Current score is:",score)
 print("Final score is:",score)