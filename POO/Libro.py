class Libro:
    
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.antiguedad = 2026 - anio_publicacion
        
libro1 = Libro("Harry Potter", "J.K. Rowling", 1997)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

print("Título:", libro1.titulo, "| Autor:", libro1.autor, "| Año:", libro1.anio_publicacion,"|antiguedad:", libro1.antiguedad )
print("Título:", libro2.titulo, "| Autor:", libro2.autor, "| Año:", libro2.anio_publicacion,"|antiguedad:", libro2.antiguedad)
print("Título:", libro3.titulo, "| Autor:", libro3.autor, "| Año:", libro3.anio_publicacion,"|antiguedad:", libro3.antiguedad)



