def student_averages(data):
    """Calcula el promedio de calificaciones por cada estudiante."""
    # Manejo de caso vacío
    if not data:
        return {}
    averages = {}
    for student, assignments in data.items():
        grades = assignments.values()
        if grades:
            avg = sum(grades) / len(grades)
            averages[student] = round(avg)
        else:
            averages[student] = 0  
    return averages

def assignment_averages(data):
    if not data:
        return {}
    all_students = list(data.keys())
    first_student = all_students[0]
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
