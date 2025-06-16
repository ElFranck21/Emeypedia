from django.db import models

class Comentarios (models.Model):
    nombre= models.TextField(default='')
    comentario= models.TextField(default='')
