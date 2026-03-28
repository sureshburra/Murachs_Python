"""
Write a Python function that takes a list of dictionaries, each representing a student's information (name, age, grade). The function should sort the list first by grade (ascending) and then by age (descending), filtering out any student who has a grade lower than 50.
"""


def filter_sort_students(students):
    filtered = [student for student in students if student['grade'] >=50]
    
    #print(filtered)

    sorted_students = sorted(filtered, key=lambda x: x['grade'], reverse=True)
    return sorted_students
    


students = [
    
    {"name": 'AA', 'age': 20, 'grade': 85},
    {"name": 'BB', 'age': 21, 'grade': 45},
    {"name": 'CC', 'age': 22, 'grade': 94},
    {"name": 'DD', 'age': 23, 'grade': 66},
    {"name": 'EE', 'age': 24, 'grade': 75},
]

result = filter_sort_students(students)
print(result)