import json
import datetime

def registro_tareas ():
    try:
      with open('registro de tareas' , 'r') as archivo:
        return json.load(archivo)
    except(FileNotFoundError,json.JSONDecodeError):
       return []
#MENU
def opcion_menu():
  print('1. Ingrese 1 para agregar tareas : ')
  print('2. Ingrese 2 para mostrar tareas : ')
  print('3. Ingrese 3 para eliminar tarea : ')
  print('4. Ingrese 4 para maracar completada : ')
  print('5. Ingrese 5  para filtrar por categoria : ')
  print('6. Ingrese 6 para salir : ')
  print('-------------------------------------')

#AGREGAR
def agregar_tarea():
  nombre = input('Nombre : ').lower()
  try:
    id_tarea = int(input('ID : '))
  except ValueError:
    print('ERROR : El ID debe ser un número')
    return 
    
  categoria = input('Categoria : ').lower()
  estado = 'pendiente'

  tareas = registro_tareas()
  fecha_actual = datetime.datetime.now().strftime("%d/%m/%y")
  nueva_tarea = {
    'nombre': nombre,
    'id': id_tarea,
    'categoria': categoria,
    'fecha': fecha_actual,
    'estado': estado
  }

  tareas.append(nueva_tarea)

  with open('registro de tareas', 'w') as archivo:
    json.dump(tareas, archivo, indent=4)
    print('Tarea Guardada con éxito')

#MOSTRAR
def mostrar_tarea():
  tareas = registro_tareas()

  if not tareas :
    print('Aun no hay registro de tareas')
    return

  for tarea in tareas:
      print(f" ID: {tarea.get('id')} |  {tarea.get('nombre')} | Categoria: {tarea.get('categoria')} | Estado: {tarea.get('estado')}")

#COMPLETADO     
def completado ():
  tareas = registro_tareas()
  try:
    terminado = int(input('Ingesa ID de tarea completada: '))
  except ValueError:
    print('ID invalido')
    return
  encontrada = False
  for tarea in tareas:
      if tarea['id'] == terminado:
        tarea['estado'] = 'completada'
        encontrada = True
  with open('registro de tareas', 'w') as archivo:
     json.dump(tareas, archivo, indent=4)
     print('Tarea Marcada como completada')

#ELIMINAR
def eliminar_tarea ():
    print('--TAREAS ACTUALES--')
    mostrar_tarea()
    
    tareas = registro_tareas()
    if not tareas:
      print(' No hay registros guardados')
      return
    try:
      eliminar = int(input(' Ingrese ID  a eliminar : '))
    except ValueError:
      print("El ID debe ser un número.")
      return

    encontrada = False
    for tarea in tareas:
       if tarea['id'] == eliminar :
         tareas.remove(tarea)
         encontrada = True
         break
    if encontrada:
        with open ('registro de tareas' , 'w') as archivo:
          json.dump(tareas,archivo,indent=4)
          print('Tarea elimanada exitosamente')
          
    else:
        print('No se encontro tareas con ese ID')

#BUSCAR
def buscar_categoria():
  tareas = registro_tareas()
  categoria = input('Ingresa categoria de tareas: ').lower()
  encontrada = False

  for tarea in tareas:
    if tarea['categoria'] == categoria:
      print (tarea)
      encontrada = True




