#  Sistema de Préstamo de Libros

# (US1) Registrar libros
# Se debe poder agregar libros con un ID, título, autor y estado de disponibilidad.

# (US2) Prestar libros sin necesidad de registro previo
# Cualquier persona debe poder tomar prestado un libro proporcionando su nombre, apellido, cédula y teléfono.

# (US3) Devolver libros
# Un usuario debe poder devolver un libro, cambiando su estado a "Disponible".

# (US4) Listar libros
# Se debe mostrar una lista de todos los libros con su estado (Disponible/No disponible).

# (US5) Listar préstamos
# Se debe poder ver qué usuario tiene qué libro prestado.
books = []  # Lista para almacenar los libros

def addBook():
    book = {
        "id": len(books) + 1,  # Genera un ID automático
        "titulo": input("Ingrese el título del libro: "),
        "autor": input("Ingrese el autor: "),
        "disponible": True  # Estado de disponibilidad
    }
    books.append(book)
    print(f" Libro '{book['titulo']}' agregado correctamente.\n")

def listarLibros():
    if not books:
        print(" No hay libros registrados.\n")
        return

    print("\n Lista de libros:")
    for book in books:
        estado = "Disponible" if book["disponible"] else "Prestado"
        print(f"ID: {book['id']} | {book['titulo']} - {book['autor']} ({estado})")
    print()

# Pruebas
addBook()
addBook()
listarLibros()

def prestarLibro():
    listarLibros()  # Muestra los libros disponibles
    libro_id = int(input("Ingrese el ID del libro que desea prestar: "))

    for book in books:
        if book["id"] == libro_id:
            if not book["disponible"]:
                print(" El libro ya está prestado.\n")
                return
            
            usuario = {
                "nombre": input("Ingrese su nombre: "),
                "apellido": input("Ingrese su apellido: "),
                "cedula": input("Ingrese su cédula: "),
                "telefono": input("Ingrese su teléfono: ")
            }

            book["disponible"] = False
            book["prestado_a"] = usuario
            print(f" Libro '{book['titulo']}' prestado a {usuario['nombre']} {usuario['apellido']}.\n")
            return

    print(" No se encontró un libro con ese ID.\n")


def devolverLibro():
    listarLibros()  # Muestra los libros actuales
    libro_id = int(input("Ingrese el ID del libro que desea devolver: "))

    for book in books:
        if book["id"] == libro_id:
            if book["disponible"]:
                print(" Este libro ya está disponible.\n")
                return

            book["disponible"] = True
            book.pop("prestado_a", None)  # Elimina la info del usuario
            print(f" Libro '{book['titulo']}' devuelto correctamente.\n")
            return

    print(" No se encontró un libro con ese ID.\n")

def consultarLibro():
    libro_id = int(input("Ingrese el ID del libro que desea consultar: "))

    for book in books:
        if book["id"] == libro_id:
            estado = "Disponible" if book["disponible"] else "Prestado"
            print(f" El libro '{book['titulo']}' está {estado}.\n")
            return

    print(" No se encontró un libro con ese ID.\n")

def listarLibros():
    if not books:
        print("📚 No hay libros registrados.\n")
        return

    print("\n📖 Lista de libros:")
    for book in books:
        estado = "Disponible" if book["disponible"] else "No disponible"
        print(f"ID: {book['id']} | {book['titulo']} - {book['autor']} ({estado})")
    print()
