import funciones

print('---GESTOR DE TAREAS---')

while True:
    funciones.opcion_menu()
    
    try:
        opcion = int(input('Ingrese una opcion: '))
    except ValueError:
        print('Error: Por favor ingrese un número válido.')
        continue

    match opcion:
        case 1 : 
            funciones.agregar_tarea()
        case 2 :
            funciones.mostrar_tarea()
        case 3:
            funciones.eliminar_tarea()
        case 4 :
            funciones.completado()
        case 5:
            funciones.buscar_categoria()
        case 6:
            print('--- FIN DEL PROGRAMA ---')
            break
        case _:
            print('Opción no válida. Por favor, ingrese un número del 1 al 6.')

            




