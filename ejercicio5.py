def aniobisiesto():
    anio = int(input("Introduzca un año para saber si es o no bisiesto: "))
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print("El año: ", anio, "SI es bisiesto.")
    else:
        print("El año: ", anio, "NO es bisiesto.")

aniobisiesto()

