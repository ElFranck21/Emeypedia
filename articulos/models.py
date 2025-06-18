from django.db import models

class Articulo (models.Model):
    titulo= models.CharField(max_length=30)
    CATEGORIAS = [
        ('resumen', 'Resumen'),
        ('historia', 'Historia'),
        ('gameplay', 'Gameplay'),
        ('guias', 'Guías'),
        ('galeria', 'Galería de imágenes'),
    ]
    subcategoria = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    tipo = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    contenido_texto = models.TextField(default='')
    subcategoria2 = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    contenido_texto2 = models.TextField(default='')
    subcategoria3 = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    gameplay = models.FileField(upload_to='', blank=True, null=True, default='resumen')
    subcategoria4 = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    contenido_texto4 = models.TextField(default='')
    subcategoria5 = models.CharField(max_length=20, choices=CATEGORIAS, default='resumen')
    imagenes = models.ImageField(upload_to='')


    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"