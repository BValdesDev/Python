from db import crear_tablas
from models import agregar_categoria, obtener_categorias, agregar_tarea, obtener_tareas, actualizar_tarea, eliminar_tarea

def menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar categoría")
    print("2. Agregar tarea")
    print("3. Ver tareas")
    print("4. Editar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

# Muestra todas las tareas en consola
def mostrar_tareas():
    tareas = obtener_tareas()
    for t in tareas:
        print(f"ID: {t[0]}, Título: {t[1]}, Prioridad: {t[4]}, Categoría: {t[5]}")
        print(f"Descripción: {t[2]} | Fecha Límite: {t[3]}\n")

# Ejecutar la aplicación y responder a la entrada del usuario 
def ejecutar():
    crear_tablas()

    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la categoría: ")
            agregar_categoria(nombre)
        
        elif opcion == "2":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            prioridad = input("Prioridad (Alta, Media, Baja): ")
            # Mostrar categorias disponibles
            categorias = obtener_categorias()
            for cat in categorias:
                print(f"{cat[0]} - {cat[1]}") # Muestra el ID y el nombre de cada categoría en el formato: "1 - Trabajo"


            cat_id = int(input("ID de la categoría: "))
            agregar_tarea(titulo, descripcion, fecha, prioridad, cat_id)
        
        elif opcion == "3":
            mostrar_tareas()
        
        elif opcion == "4":
            mostrar_tareas()
            id_tarea = int(input("ID de la tarea a editar: "))
            titulo = input("Nuevo título: ")
            descripcion = input("Nueva descripción: ")
            fecha = input("Nueva fecha límite: ")
            prioridad = input("Nueva prioridad: ")
            categorias = obtener_categorias()
            for cat in categorias:
                print(f"{cat[0]} - {cat[1]}")
            cat_id = int(input("Nuevo ID de categoría: "))
            actualizar_tarea(id_tarea, titulo, descripcion, fecha, prioridad, cat_id)
        
        elif opcion == "5":
            mostrar_tareas()
            id_tarea = int(input("ID de la tarea a eliminar: "))
            eliminar_tarea(id_tarea)

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()
