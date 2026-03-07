import funciones
print('---GESTOR DE TAREAS---')

while True:
    funciones.opcion_menu()
    
    opcion = int(input('Ingrese una opcion'))
    match opcion:
        case 1 : 
            agregar_tarea = input('Desea agregar una nuvea tarea  S/N? :').lower()
            if agregar_tarea == 's':
                nombre = input("Nombre : ").lower()
                id = int(input("id : ").lower())
                categoria = input("Categoria : ").lower()            
                funciones.agragar_tarea(nombre,id,categoria)
            else:
                print('opcion invalida')
        case 2 :
            funciones.mostrar_tarea()
        case 4:
            print('Fin del programa')
            break
            
            




