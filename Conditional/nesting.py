############################################################################### 
#                   NESTING IF-ELIF-ELSE STATEMENTS
###############################################################################


# Refer to and.py for AND operator

grade = int(input("Enter your grade: "))

if 90 <= grade <= 100:
    print("You got an A")
elif 80 <= grade < 90:
    print("You got a B")
elif 70 <= grade < 80:
    print("You got a C")
elif 60 <= grade < 70:
    print("You got a D")
else: 
    print("You got an F")    


# Improving the above code:
# We can remove the AND operator and just check the lower limit because if the code reaches that point, it means the previous conditions were false.
# For example, if the code reaches the elif grade >= 80, it means the grade is less than 90, so we only need to check if it's greater than or equal to 80.

score = int(input("Enter your score: ")) 

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else: 
    print("You got an F")     