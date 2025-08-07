import sqlite3

# Función para conectar con la base de datos SQLite

def conectar():
    return sqlite3.connect("tareas.db")

# Función para crear las tablas 
def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    # Crear tabla de categorías
    cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL)''')
    
    
    # Crear tabla de tareas con clave foránea hacia categorías
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        descripcion TEXT,
                        fecha_limite TEXT,
                        prioridad TEXT,
                        categoria_id INTEGER,
                        FOREIGN KEY(categoria_id) REFERENCES categorias(id))''')
    conexion.commit()
    conexion.close()
