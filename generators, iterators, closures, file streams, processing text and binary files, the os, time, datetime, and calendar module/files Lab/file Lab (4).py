class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

def read_and_sum(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        raise StudentsDataException("Error: File not found.")

    if not data:
        raise FileEmpty("Error: File is empty.")

    students = {}
    for line in data:
        line = line.strip().split()
        if len(line) != 3:
            raise BadLine("Error: Bad line found in the file.")
        try:
            points = float(line[2])
        except ValueError:
            raise BadLine("Error: Bad line found in the file.")

        if (line[0] + " " + line[1]) in students:
            students[line[0] + " " + line[1]] += points
        else:
            students[line[0] + " " + line[1]] = points

    for student in sorted(students):
        print(student + " " + str(students[student]))

file_name = input("Enter Prof. Jekyll's file name: ")

try:
    read_and_sum(file_name)
except StudentsDataException as e:
    print(e)
