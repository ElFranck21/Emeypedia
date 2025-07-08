from django.db import models


class Articulo(models.Model):
    TIPOS = [
        ('juego', 'Juego'),
        ('serie', 'Serie'),
        ('pelicula', 'Película'),
    ]

    CATEGORIAS = [
        ('resumen', 'Resumen'),
        ('historia', 'Historia'),
        ('gameplay', 'Gameplay'),
        ('guias', 'Guías'),
        ('galeria', 'Galería de imágenes'),
    ]

    titulo = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20, choices=TIPOS, default='juego') 

    subcategoria = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    contenido_texto = models.TextField(default='')
    subcategoria2 = models.CharField(max_length=20, choices=CATEGORIAS, default='historia')
    contenido_texto2 = models.TextField(default='')
    subcategoria3 = models.CharField(max_length=20, choices=CATEGORIAS, default='gameplay')
    gameplay = models.FileField(upload_to='', blank=True, null=True)
    subcategoria4 = models.CharField(max_length=20, choices=CATEGORIAS, default='guias')
    contenido_texto4 = models.TextField(default='', blank=True, null=True)
    subcategoria5 = models.CharField(max_length=20, choices=CATEGORIAS, default='galeria')
    imagenes = models.ImageField(upload_to='articulos/', blank=True, null=True)

    def __str__(self):
      return f"{self.titulo} - {self.get_tipo_display()}"
