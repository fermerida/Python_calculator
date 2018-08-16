print("this is a python calculator file for python3")
print("Ingrese el primer número")
num1 = int(input())
print("Ingrese el segundo número")
num2 = int (input())
print("Seleccione una de las opciones colocando el número")
def switch_demo(argument):
    switcher = {
        1: "Resultado: " +str((num1 + num2)),
        2: "Resultado: " +str((num1 - num2)),
        3: "Resultado: " +str((num1 * num2)),
        4: "Resultado: " +str((num1 * num2)),
        5: "Resultado: " +str((num1 ** num2)),

    }
    return switcher.get(argument, "No existe esa opcion")

print("")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.División")
print("3.Potencia")
opt = int(input())
print("\n")

print(switch_demo(opt))
