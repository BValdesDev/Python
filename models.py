from db import conectar

# Agrega una nueva categoría

def agregar_categoria(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))
    conexion.commit()
    conexion.close()

# Devuelve todas las categorías existentes

def obtener_categorias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    conexion.close()
    return categorias

# Funcion para agregar una nueva tarea
def agregar_tarea(titulo, descripcion, fecha_limite, prioridad, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO tareas (titulo, descripcion, fecha_limite, prioridad, categoria_id)
                      VALUES (?, ?, ?, ?, ?)''',
                   (titulo, descripcion, fecha_limite, prioridad, categoria_id))
    conexion.commit()
    conexion.close()

# Devuelve todas las tareas unidas con su categoría

def obtener_tareas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''SELECT tareas.id, titulo, descripcion, fecha_limite, prioridad, categorias.nombre 
                      FROM tareas LEFT JOIN categorias ON tareas.categoria_id = categorias.id''')
    tareas = cursor.fetchall()
    conexion.close()
    return tareas

# Actualizar una tarea existente
def actualizar_tarea(id_tarea, titulo, descripcion, fecha_limite, prioridad, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''UPDATE tareas SET titulo=?, descripcion=?, fecha_limite=?, prioridad=?, categoria_id=? 
                      WHERE id=?''',
                   (titulo, descripcion, fecha_limite, prioridad, categoria_id, id_tarea))
    conexion.commit()
    conexion.close()

# Eliminar una tarea por su ID
def eliminar_tarea(id_tarea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE id=?", (id_tarea,))
    conexion.commit()
    conexion.close()
