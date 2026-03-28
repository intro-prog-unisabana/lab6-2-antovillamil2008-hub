from grades_manager import *

def main():
    print("Welcome to the Student Grades Manager!")
    my_grades = {}
    
    while True:
        print("\nSelect an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")
        opcion_elegida = input().strip()
        if opcion_elegida == '1':
            my_grades = add_student(my_grades)
        elif opcion_elegida == '2':
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")
            sub_opcion = input().strip().lower()
            if sub_opcion == 'a':
                avg_by_student(my_grades)
            elif sub_opcion == 'b':
                nombres_crudos = input("Enter student names (comma-separated): ")
                lista_de_busqueda = nombres_crudos.split(',')
                avg_by_student(my_grades, lista_de_busqueda)
            else:
                print("Invalid option selected!")  
        elif opcion_elegida == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()