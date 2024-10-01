import datetime

def calcular_edad(fecha_nacimiento):
    """Calcula la edad a partir de una fecha de nacimiento.

    args:
        fecha_nacimiento: Una cadena de texto en formato 'dd/mm/yyyy'.

    return:
        Un entero representando la edad en años.
    """
    
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/yyyy): ")
edad = calcular_edad(fecha_nacimiento)
print(f"Tienes {edad} años.")
