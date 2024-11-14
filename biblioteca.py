#para inciar usar: biblioteca.py

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos import Base
import logging
engine = create_engine("mysql+mysqlconnector://axel:blackzone4+@localhost/biblioteca", echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session= Session()
sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
sqlalchemy_logger.setLevel(logging.WARNING)
for handler in sqlalchemy_logger.handlers:
    sqlalchemy_logger.removeHandler(handler)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
sqlalchemy_logger.addHandler(handler)

from crud import (
    crear_usuario, actualizar_usuario, borrar_usuario, agregar_libro,
    actualizar_libro, borrar_libro, agregar_genero, actualizar_genero,
    crear_prestamo, actualizar_prestamo, ver_libros, ver_generos, ver_prestamos, ver_usuarios
)

def menu():
    while True:
        print("\nGestor de Biblioteca")
        print("1. Crear Usuario")
        print("2. Actualizar Usuario")
        print("3. Borrar Usuario")
        print("4. Agregar Libro")
        print("5. Actualizar Libro")
        print("6. Borrar libro")
        print("7. Agregar Generos")
        print("8. Actualizar Generos")
        print("9. Crear Prestamo")
        print("10. Actualizar Prestamo")
        print("11. Ver todos los datos cargados")
        print("12. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            crear_usuario(nombre, apellido, dni, telefono, email)

        elif opcion == '2':
            numero_usuario = int(input("ID del usuario: "))
            telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ")
            email = input("Nuevo email (dejar en blanco para no cambiar): ")
            estado = input("Nuevo estado (1=Activo, 0=Inactivo, dejar en blanco para no cambiar): ")
            estado = int(estado) if estado else None
            actualizar_usuario(numero_usuario, telefono or None, email or None, estado)

        elif opcion == '3':
            numero_usuario = int(input("ID del usuario: "))
            borrar_usuario(numero_usuario)

        elif opcion=='4':
            nombre_libro = input("Nombre del Libro: ")
            autor = input("Autor: ")
            fecha_lanzamiento = input("Fecha de Lanzamiento (DD/MM/YYYY): ")
            fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%d/%m/%Y").strftime("%Y-%m-%d") if fecha_lanzamiento else None
            id_genero = int(input("ID del Género: "))
            agregar_libro(nombre_libro, autor, fecha_lanzamiento, id_genero)

        elif opcion=='5':
            numero_libro = int(input("ID del Libro a actualizar: "))
            nombre_libro = input("Nuevo nombre del Libro (dejar en blanco para no cambiar): ")
            autor = input("Nuevo Autor (dejar en blanco para no cambiar): ")
            fecha_lanzamiento = input("Nueva Fecha de Lanzamiento (DD/MM/YYYY, dejar en blanco para no cambiar): ")
            fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%d/%m/%Y").strftime("%Y-%m-%d") if fecha_lanzamiento else None
            id_genero = input("Nuevo ID del Género (dejar en blanco para no cambiar): ")
            id_genero = int(id_genero) if id_genero else None
            actualizar_libro(numero_libro, nombre_libro or None, autor or None, fecha_lanzamiento, id_genero)
        
        elif opcion=='6':
            numero_libro = int(input("ID del Libro a borrar: "))
            borrar_libro(numero_libro)
        
        elif opcion=='7':
            nombre_genero = input("Nombre del Género: ")
            agregar_genero(nombre_genero)
        
        elif opcion=='8':
            numero_genero = int(input("ID del Género a actualizar: "))
            nuevo_nombre = input("Nuevo nombre del Género: ")
            actualizar_genero(numero_genero, nuevo_nombre)
        
        elif opcion=='9':
            usuario_id = int(input("ID del Usuario: "))
            libro_id = int(input("ID del Libro: "))
            crear_prestamo(usuario_id, libro_id)
        
        elif opcion=='10':
            prestamo_id = int(input("ID del Préstamo: "))
            fecha_devolucion_real = input("Fecha de Devolución Real (DD/MM/YYYY): ")
            fecha_devolucion_real = datetime.strptime(fecha_devolucion_real, "%d-%m-%Y") if fecha_devolucion_real else None
            actualizar_prestamo(prestamo_id, fecha_devolucion_real)
            
        elif opcion=='11': 
            while True:
                print("1. Ver Usuarios")
                print("2. Ver Libros")
                print("3. Ver Generos")
                print("4. Ver Prestamos")
                print("5. Volver al Menu Principal")
                datos=input("elija una opcion para ver los datos cargados correspondientes: ")
                
                if datos=='1':
                    ver_usuarios()
                    
                elif datos=='2':
                    ver_libros()
                    
                elif datos=='3':
                    ver_generos()
                    
                elif datos=='4':
                    ver_prestamos()
                
                elif datos=='5':
                    menu()
                    break
        
        elif opcion == '12':
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
        
    
        
        
        
