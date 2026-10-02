
import csv

students = []
gpas = []
majors = []

# Open the CSV file
file = open("students.csv", "r")

# Read the CSV file
reader = csv.reader(file)

# Skip the first row
next(reader)

# Store the data in lists
for row in reader:
    students.append(row[0])
    gpas.append(float(row[1]))
    majors.append(row[2])

file.close()

# Calculate the average GPA
total = sum(gpas)
average = total / len(gpas)

print("Average GPA:", round(average, 2))

# Print students above average
print("\nStudents above average:")

for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], gpas[i], majors[i])

# Predict scholarship students
print("\nPredicted scholarship students:")

for i in range(len(students)):
    if majors[i] == "Biology" and gpas[i] >= 2.75:
        print(students[i], gpas[i], majors[i])
    elif majors[i] == "Math" and gpas[i] >= 3.50:
        print(students[i], gpas[i], majors[i])

