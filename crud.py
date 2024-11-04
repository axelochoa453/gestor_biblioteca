from config import session
from modelos import Usuario, Libro, Genero, Prestamo
from datetime import datetime, timedelta
import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

def crear_usuario(nombre, apellido, dni, telefono, email):
    nuevo_usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        dni=dni,
        telefono=telefono,
        email=email
    )
    session.add(nuevo_usuario)
    session.commit()
    print(f"\nUsuario {nombre} {apellido} creado con éxito.")

def actualizar_usuario(numero_usuario, telefono=None, email=None, estado=None):
    usuario = session.query(Usuario).filter_by(Numero_Usuario=numero_usuario).first()
    if usuario:
        if telefono:
            usuario.telefono = telefono
        if email:
            usuario.email = email
        if estado is not None:
            usuario.estado = estado
        session.commit()
        print("""
              
              Usuario actualizado con éxito.
              
              """)
    else:
        print("""
              
              Usuario no encontrado.
              
              """)

def borrar_usuario(numero_usuario):
    actualizar_usuario(numero_usuario, estado=0)
    print("""
          
          Usuario marcado como inactivo.
          
          """)

def agregar_libro(nombre_libro, autor, fecha_lanzamiento, id_genero):
    nuevo_libro = Libro(
        nombre_libro=nombre_libro,
        autor=autor,
        fecha_lanzamiento=fecha_lanzamiento,
        id_genero=id_genero
    )
    session.add(nuevo_libro)
    session.commit()
    print("""
          
          Libro agregado correctamente.
          """)

def actualizar_libro(numero_libro, nombre_libro=None, autor=None, fecha_lanzamiento=None, id_genero=None):
    libro = session.query(Libro).filter_by(Numero_Libro=numero_libro).first()
    if not libro:
        print("""
              
              Libro no encontrado.
              
              """)
        return

    if nombre_libro:
        libro.nombre_libro = nombre_libro
    if autor:
        libro.autor = autor
    if fecha_lanzamiento:
        libro.fecha_lanzamiento = fecha_lanzamiento
    if id_genero:
        libro.id_genero = id_genero

    session.commit()
    print("""
          
          Libro actualizado correctamente.
          
          """)

def borrar_libro(numero_libro):
    libro = session.query(Libro).filter_by(Numero_Libro=numero_libro).first()
    if not libro:
        print("""
              
              Libro no encontrado.
              
              """)
        return

    libro.estado = 0
    session.commit()
    print("""
          
          Libro borrado
          
          """)
    
def agregar_genero(nombre_genero):
    nuevo_genero = Genero(genero=nombre_genero)
    session.add(nuevo_genero)
    session.commit()
    print("""
          
          Género agregado correctamente.
          
          """)

def actualizar_genero(numero_genero, nuevo_nombre):
    genero = session.query(Genero).filter_by(Numero_Genero=numero_genero).first()
    if not genero:
        print("""
              
              Género no encontrado.
              
              """)
        return

    genero.genero = nuevo_nombre
    session.commit()
    print("""
          
          Género actualizado correctamente.
          
          """)

def crear_prestamo(usuario_id, libro_id):
    usuario = session.query(Usuario).filter_by(Numero_Usuario=usuario_id, estado=1).first()
    libro = session.query(Libro).filter_by(Numero_Libro=libro_id, estado=1).first()
    
    if not usuario:
        print("""
              
              El usuario no existe o está inactivo.
              
              """)
        return
    if not libro:
        print("""
              
              El libro no existe o está inactivo.
              
              """)
        return

    fecha_prestamo = datetime.now()
    fecha_devolucion_estimada = fecha_prestamo + timedelta(days=7)
    nuevo_prestamo = Prestamo(
        usuario_id=usuario_id,
        libro_id=libro_id,
        fecha_prestamo=fecha_prestamo,
        fecha_devolucion_estimada=fecha_devolucion_estimada
    )
    session.add(nuevo_prestamo)
    session.commit()
    print("""
          
          Préstamo creado correctamente.
          
          """)

def actualizar_prestamo(prestamo_id, fecha_devolucion_real=None):
    prestamo = session.query(Prestamo).filter_by(Numero_Prestamo=prestamo_id).first()
    if not prestamo:
        print("""
              
              Préstamo no encontrado.
              
              """)
        return

    if fecha_devolucion_real:
        prestamo.fecha_devolucion_real = fecha_devolucion_real
        if prestamo.fecha_devolucion_real > prestamo.fecha_devolucion_estimada:
            usuario = session.query(Usuario).filter_by(Numero_Usuario=prestamo.usuario_id).first()
            if usuario:
                usuario.estado = 0
                print("""
                      
                      El usuario devolvió fuera de plazo y se lo marco como inactivo.
                      
                      """)
    
    session.commit()
    print("""
          
          Préstamo actualizado correctamente.
          
          """)

def ver_usuarios():
    usuarios = session.query(Usuario).all()
    print("\nLista de Usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario.Numero_Usuario}, Nombre: {usuario.nombre} {usuario.apellido}, DNI: {usuario.dni}, "
              f"Teléfono: {usuario.telefono}, Email: {usuario.email}, Estado: {'Activo' if usuario.estado == 1 else 'Inactivo'}")

def ver_libros():
    libros = session.query(Libro).all()
    print("\nLista de Libros:")
    for libro in libros:
        print(f"ID: {libro.Numero_Libro}, Título: {libro.nombre_libro}, Autor: {libro.autor}, "
              f"Fecha de Lanzamiento: {libro.fecha_lanzamiento}, Género ID: {libro.id_genero}, "
              f"Estado: {'Disponible' if libro.estado == 1 else 'No disponible'}")

def ver_generos():
    generos = session.query(Genero).all()
    print("\nLista de Géneros:")
    for genero in generos:
        print(f"ID: {genero.Numero_Genero}, Género: {genero.genero}")

def ver_prestamos():
    prestamos = session.query(Prestamo).all()
    print("\nLista de Préstamos:")
    for prestamo in prestamos:
        print(f"ID: {prestamo.Numero_Prestamo}, Usuario ID: {prestamo.usuario_id}, Libro ID: {prestamo.libro_id}, "
              f"Fecha de Préstamo: {prestamo.fecha_prestamo}, Fecha de Devolución Estimada: {prestamo.fecha_devolucion_estimada}, "
              f"Fecha de Devolución Real: {prestamo.fecha_devolucion_real or 'No devuelto aún'}")
