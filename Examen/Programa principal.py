from math import prod
from Funciones import asignar_sueldos_aleatorios, clasificar_por_sueldo, ver_estadisticas, reporte_sueldo, escribir_reporte_csv, menu

mapa_salarios = {}
opciones_menu = ["Asignar sueldos aleatorios", "Clasificar sueldos", "Ver estadísticas", "Reporte de sueldos"]

while True:
    opcion_seleccionada = menu("Menú Principal", opciones_menu)

    if opcion_seleccionada == 1:
        mapa_salarios = asignar_sueldos_aleatorios()
        print("Personas y sueldos generados:")
        for nombre_empleado, salario in mapa_salarios.items():
            print(f"{nombre_empleado}: {salario}")
    
    if opcion_seleccionada == 2:
        clasificar_por_sueldo(mapa_salarios)
    
    if opcion_seleccionada == 3:
        salario_maximo, salario_minimo, promedio_salarios, media_geo_salarios = ver_estadisticas(mapa_salarios)
        print(f"Sueldo más alto: {salario_maximo}$")
        print(f"Sueldo más bajo: {salario_minimo}$")
        print(f"Promedio de sueldos: {promedio_salarios}$")
        print(f"Media geométrica de sueldos: {media_geo_salarios}$")
    
    if opcion_seleccionada == 4:
        reporte_sueldo(mapa_salarios)
        escribir_reporte_csv(mapa_salarios)
        
    if opcion_seleccionada == 5:
        print("Saliendo del programa")
        print("Jose Ignacio Espinoza Espinoza")
        print("21.317.707-9")
        break