# define the scores attrubutes 
score = int(input("score: "))
# categorise scoes according to grades
if score >= 70 and score <=100:
    print("Grade: A")
elif score >=60 and score <= 69:
    print("Grade: B")
elif score >=50 and score <= 59:
    print("Grade: C")
elif score  >=40 and score <= 49:
    print("Grade: D")
else:
    print("Grade: F")