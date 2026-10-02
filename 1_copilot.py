# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.extend(["Sara", "Miko"])

# change Jon to John
students[0] = "John"

# function to print ‘Hi name’ for each student in the list
def greet_students(students):
    for student in students:
        print(f"Hi {student}")
    print(f"Total number of students: {len(students)}")

# call the function
greet_students(students)