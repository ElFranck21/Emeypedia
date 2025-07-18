from django.db import models


class Articulo(models.Model):
    TIPOS = [
        ('juego', 'Juego'),
        ('serie', 'Serie'),
        ('pelicula', 'Película'),
        ('anime', 'Anime'),
        ('libro', 'Libro'),
        ('musica', 'Música'),
        ('otro', 'Otro'),
    ]

    CATEGORIAS = [
        ('resumen', 'Resumen'),
        ('historia', 'Historia'),
        ('gameplay', 'Gameplay'),
        ('guias', 'Guías'),
        ('galeria', 'Galería de imágenes'),
        ('noticias', 'Noticias'),
        ('entrevistas', 'Entrevistas'),
        ('reseñas', 'Reseñas'),
        ('opiniones', 'Opiniones'),
        ('análisis', 'Análisis'),
        ('curiosidades', 'Curiosidades'),
        ('trivia', 'Trivia'),
        ('fanart', 'Fanart'),
        ('memes', 'Memes'),
        ('cosplay', 'Cosplay'),
        ('merchandising', 'Merchandising'),
        ('eventos', 'Eventos'),

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
    subcategoria6 = models.CharField(max_length=20, choices=CATEGORIAS, default='noticias')
    contenido_texto6 = models.TextField(default='', blank=True, null=True)
    subcategoria7 = models.CharField(max_length=20, choices=CATEGORIAS, default='entrevistas')
    contenido_texto7 = models.TextField(default='', blank=True, null=True)
    subcategoria8 = models.CharField(max_length=20, choices=CATEGORIAS, default='reseñas')
    contenido_texto8 = models.TextField(default='', blank=True, null=True)
    subcategoria9 = models.CharField(max_length=20, choices=CATEGORIAS, default='opiniones')
    contenido_texto9 = models.TextField(default='', blank=True, null=True)
    subcategoria10 = models.CharField(max_length=20, choices=CATEGORIAS, default='análisis')
    contenido_texto10 = models.TextField(default='', blank=True, null=True)
    subcategoria11 = models.CharField(max_length=20, choices=CATEGORIAS, default='curiosidades')
    contenido_texto11 = models.TextField(default='', blank=True, null=True)
    subcategoria12 = models.CharField(max_length=20, choices=CATEGORIAS, default='trivia')
    contenido_texto12 = models.TextField(default='', blank=True, null=True)
    subcategoria13 = models.CharField(max_length=20, choices=CATEGORIAS, default='fanart')
    imagen_fanart = models.ImageField(upload_to='articulos/fanart/', blank=True, null=True)
    subcategoria14 = models.CharField(max_length=20, choices=CATEGORIAS, default='memes')
    imagen_memes = models.ImageField(upload_to='articulos/memes/', blank=True, null=True)
    subcategoria15 = models.CharField(max_length=20, choices=CATEGORIAS, default='cosplay')
    imagen_cosplay = models.ImageField(upload_to='articulos/cosplay/', blank=True, null=True)
    subcategoria16 = models.CharField(max_length=20, choices=CATEGORIAS, default='merchandising')
    imagen_merchandising = models.ImageField(upload_to='articulos/merchandising/', blank=True, null=True)
    subcategoria17 = models.CharField(max_length=20, choices=CATEGORIAS, default='eventos')
    contenido_texto17 = models.TextField(default='', blank=True, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articulos')

    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"
