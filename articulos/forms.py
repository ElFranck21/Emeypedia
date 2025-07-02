from django import forms
from django.core.exceptions import ValidationError
from .models import Articulo

class ArticuloAdminForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        subcategoria = cleaned_data.get('subcategoria')
        subcategoria2 = cleaned_data.get('subcategoria2')

        restricted = ['guias', 'gameplay']

        if tipo in ['pelicula', 'serie']:
            if subcategoria in restricted:
                raise ValidationError({'subcategoria': 'No puede seleccionar esta opción para películas o series.'})
            if subcategoria2 in restricted:
                raise ValidationError({'subcategoria2': 'No puede seleccionar esta opción para películas o series.'})
        return cleaned_data

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__' 
        widgets = {
            'contenido_texto': forms.Textarea(attrs={'rows': 4}),
            'contenido_texto2': forms.Textarea(attrs={'rows': 4}),
            'contenido_texto4': forms.Textarea(attrs={'rows': 4}),
        }
