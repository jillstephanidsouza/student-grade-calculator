print("Student Grade Calculator")

name = input("Enter student name: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Result ---")
print("Student:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
