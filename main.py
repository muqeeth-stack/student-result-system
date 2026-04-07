name = input("Enter student name: ")

marks1 = int(input("Enter marks in Subject 1: "))
marks2 = int(input("Enter marks in Subject 2: "))
marks3 = int(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n----- RESULT -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
