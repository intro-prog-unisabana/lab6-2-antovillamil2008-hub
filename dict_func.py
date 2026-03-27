# Write your code here!
def employee_print(employee_info):
    datos = employee_info.copy()
    nombre = datos.pop("Name", "N/A")
    salario = datos.pop("Salary", "N/A")
    rol = datos.pop("Role", "N/A")
    print(f"Name: {nombre}")
    print(f"Salary: {salario}")
    print(f"Role: {rol}")
    if not datos:
        print("No other info!")
    else:
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

employee_info = {
    "Name": "Diego",
    "Salary": 5000000,
    "Role": "Janitor",
    "Years at company": 9001,
    "Hours per week": 2
}
employee_print(employee_info)
