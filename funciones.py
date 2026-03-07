import json
from datetime import datetime

def registro_tareas ():
    try:
      with open('registro de tareas' , 'r') as archivo:
        return json.load(archivo)
    except(FileNotFoundError,json.JSONDecodeError):
       return []
def opcion_menu():
  print('1. Ingrese 1 para agregar tareas : ')
  print('2. Ingrese 2 para moatrar tareas : ')
  print('3. Ingrese 3 para eliminar tarea : ')
  print('4. Ingrese 4 para salir : ')
  print('-------------------------------------')

def agragar_tarea(nombre,id,categoria):
    tarea = registro_tareas()
    fecha_actual = datetime.now().strftime("%d/%m/%y")
    nueva_tarea = {
    'nombre' : nombre,
    'id': id,
    'categoria': categoria,
    'fecha': fecha_actual
    }

    tarea.append(nueva_tarea)

    with open('registro de tareas' , 'w') as archivo:
      json.dump(tarea,archivo,indent=4)
      print('Tarea Guardada con exito')

def mostrar_tarea():
  tareas = registro_tareas()

  if not tareas :
    print('Aun no hay registro de tareas')
    return

  for tarea in tareas:
      print(f" ID: {tarea['id']} |  {tarea['nombre'].upper()}")
      print(f"  Cat: {tarea['categoria']} | ")




def eliminar_tarea(id_eliminar):
  tareas_actuales = mostrar_tarea()
  lista_nueva = []
  encontrada = false

  for tarea in tareas_actuales:
    if tarea.get('id') == id_eliminar:
      encontrada == True


