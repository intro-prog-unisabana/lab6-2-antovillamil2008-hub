#Ejemplo de Diccionario
student_grades = {
    "Alice": {
        "Math": 90.5,
        "English": 85.0,
        "Science": 92.0
    },
    "Bob": {
        "Math": 78.0,
        "English": 82.5,
        "History": 88.0
    },
    "Charlie": {
        "Science": 95.0,
        "English": 89.5
    }
}

#Parte 1
def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

#Partre 2
def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    name_input = input("Enter student name: ")
    student_name = name_input.title()
    subjects_dict = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ")
        if entry.lower() == 'exit':
            break
        if "," in entry:
            parts = entry.split(',')
            subject = parts[0].strip().title()
            grade_str = parts[1].strip()
            if grade_str.replace('.', '', 1).isdigit():
                subjects_dict[subject] = float(grade_str)
            else:
                print("Invalid grade. Please enter a number.")
        else:
            print("Invalid format. Please use: Subject,Grade")
    student_grades[student_name] = subjects_dict
    print(f"Student {student_name} successfully added to the grades management system.")
    return student_grades