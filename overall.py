def student_averages(data):
    #promedio de calificaciones por cada estudiante.
    averages = {}
    for student, assignments in data.items():
        # Obtenemos todas las notas del estudiante actual
        grades = assignments.values()
        if grades:
            avg = sum(grades) / len(grades)
            averages[student] = round(avg)
    return averages

def assignment_averages(data):
    first_student = list(data.keys())[0]
    assignment_names = data[first_student].keys()
    averages = {}
    total_students = len(data)
    for task in assignment_names:
        total_score = 0
        for student in data.values():
            total_score += student.get(task, 0)
        avg = total_score / total_students
        averages[task] = round(avg) 
    return averages

# --- Datos de Prueba ---
students = {
  "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
  "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
  "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}

print("Promedios por Estudiante:", student_averages(students))
print("Promedios por Tarea:", assignment_averages(students))