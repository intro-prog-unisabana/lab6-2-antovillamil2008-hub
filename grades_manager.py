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
    entrada_usuario = input("Enter student name: ")
    nombre_formateado = entrada_usuario.title()
    materias_y_notas = {}
    while True:
        linea_ingresada = input("Enter subject and grade (or 'exit' to finish): ")  
        if linea_ingresada.lower() == 'exit':
            break
        if "," in linea_ingresada:
            partes = linea_ingresada.split(',')
            materia = partes[0].strip().title()
            nota_texto = partes[1].strip()
            if nota_texto.replace('.', '', 1).isdigit():
                materias_y_notas[materia] = float(nota_texto)
            else:
                print("Invalid grade. Please enter a number.")
        else:
            print("Invalid format. Please use: Subject,Grade")
    student_grades[nombre_formateado] = materias_y_notas
    print(f"Student {nombre_formateado} successfully added to the grades management system.")
    return student_grades

#Parte 3
def get_students(student_grades, keys):
    estudiantes_encontrados = {}
    buscador_minusculas = {n.lower(): n for n in student_grades.keys()}
    for llave in keys:
        busqueda_limpia = llave.strip()
        termino_busqueda = busqueda_limpia.lower()
        if termino_busqueda in buscador_minusculas:
            nombre_real = buscador_minusculas[termino_busqueda]
            estudiantes_encontrados[nombre_real] = student_grades[nombre_real]
        else:
            print(f"{busqueda_limpia.title()} not found!")
    return estudiantes_encontrados

#Partre 4
def avg_by_student(student_grades, keys=None):
    diccionario_a_revisar = student_grades if keys is None else get_students(student_grades, keys) 
    for estudiante, materias in diccionario_a_revisar.items():
        if materias:
            suma_notas = sum(materias.values())
            cantidad = len(materias)
            promedio_final = suma_notas / cantidad
            print(f"{estudiante}: {promedio_final:.1f}")