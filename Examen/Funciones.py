import random
import csv
import statistics
from math import prod

lista_empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernandez", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
mapasalarios = {}

def asignar_sueldos_aleatorios():
    mapa_salarios = {}
    for empleado in lista_empleados:
        salario_aleatorio = random.randint(300000, 2500000)
        mapa_salarios[empleado] = salario_aleatorio
    print("")
    print("")
    return mapa_salarios
     
def clasificar_por_sueldo(mapa_salarios):
    if not mapa_salarios:
        print("")
        print("")
        print("Aún no se han asignado sueldos.")
        return
    
    salarios_bajos = []
    salarios_medios = []
    salarios_altos = []

    for empleado, salario in mapa_salarios.items():
        if salario < 800000:
            salarios_bajos.append((empleado, salario))
        elif 800000 <= salario <= 2000000:
            salarios_medios.append((empleado, salario))
        else:
            salarios_altos.append((empleado, salario))

    print(f"Sueldos menores a 800.000 ({len(salarios_bajos)} Total):\n")
    for empleado, salario in salarios_bajos:
        print(f"{empleado}: ${salario}\n")

    print(f"Sueldos entre 800.000 y 2.000.000 ({len(salarios_medios)} Total):\n")
    for empleado, salario in salarios_medios:
        print(f"{empleado}: ${salario}\n")

    print(f"Sueldos mayores a 2.000.000 ({len(salarios_altos)} Total):\n")
    for empleado, salario in salarios_altos:
        print(f"{empleado}: ${salario}\n")     

def ver_estadisticas(mapa_salarios):
    try: 
        lista_salarios = list(mapa_salarios.values())
        salario_maximo = max(lista_salarios)
        salario_minimo = min(lista_salarios)
        promedio_salarios = statistics.mean(lista_salarios)
        media_geo_salarios = prod(lista_salarios) ** (1 / len(lista_salarios))
        return salario_maximo, salario_minimo, promedio_salarios, media_geo_salarios
    except(TypeError) and (ValueError):
        print("Asigna el sueldo primero")
def reporte_sueldo(mapa_salarios):
    mapa_salarios_netos = {}
    for empleado, salario in mapa_salarios.items():
        salario_neto = salario * (1 - 0.07 - 0.12)
        mapa_salarios_netos[empleado] = salario_neto
    for empleado , salario in mapa_salarios.items():
        salariosalud = salario * 0.12
        salarioafp = salario * 0.07
        print("\nNombre empleado:",empleado,"\nSueldo Base:", salario,"\nDescuento salud:", salariosalud, "\nDescuento afp:", salarioafp, "\nSueldo Liquido:",salario_neto)
    print("_____________________________________")
    print("")           
    print("reporte de sueldos creado")
    return mapa_salarios_netos

def escribir_reporte_csv(mapa_salarios):
    with open("reportesueldos.csv", "w", newline="",encoding="utf-8") as archivo:
        archivosueldo = csv.writer(archivo)
        archivosueldo.writerow(['Nombre empleado'," ",'Sueldo'])
        for empleado, salario in mapa_salarios.items():
            salariosalud = salario * 0.12
            salarioafp = salario * 0.07
            salario_neto = salario * (1 - 0.07 - 0.12)
            archivosueldo.writerow([empleado,  " $",salario," Pesos","Descuento salud",salariosalud, "Descuento AFP", salarioafp, "Sueldo Liquido:",salario_neto])

def menu(titulo, lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i = 1
        for elem in lista:
            print(i, '.-', elem)
            i += 1
        print(i, '.- Salir')
        opc = input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int = int(opc)
            if opc_int >= 1 and opc_int <= i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y', i)
        else:
            print('Ingrese Sólo Números')

