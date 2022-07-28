from django import forms
from .models import CasoConcreto, MateriaCaso, DireitoCaso

choices = DireitoCaso.objects.all().values_list('name', 'name')
choice_list_direito = []

for item in choices:
    choice_list_direito.append(item)

choices = MateriaCaso.objects.all().values_list('name', 'name')
choice_list_materia = []

for item in choices:
    choice_list_materia.append(item)


class AddCasoForm(forms.ModelForm):
    class Meta:
        model = CasoConcreto
        fields = (
            'title_caso',
            'author',
            'direito_caso',
            'materia_caso',
            'content_caso',
            'lei_caso',
            'jurisprudencia_caso',
            'tags_caso',
            'img_caso',
            'meta_caso',
            'key_word',
            )

        widgets = {
            'title_caso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),            
            'direito_caso': forms.Select(choices=choice_list_direito, attrs={'class': 'form-control'}),
            'materia_caso': forms.Select(choices=choice_list_materia, attrs={'class': 'form-control'}),
            'content_caso': forms.Textarea(attrs={'class': 'form-control'}),
            'lei_caso': forms.Textarea(attrs={'class': 'form-control'}),
            'jurisprudencia_caso': forms.Textarea(attrs={'class': 'form-control'}),
            'tags_caso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'meta_caso': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),

        }

class EditCasoForm(forms.ModelForm):
    class Meta:
        model = CasoConcreto
        fields = (
            'title_caso',
            'author',
            'direito_caso',
            'materia_caso',
            'content_caso',
            'lei_caso',
            'jurisprudencia_caso',
            'tags_caso',
            'img_caso',
            'meta_caso',
            'key_word',
            )

        widgets = {
            'title_caso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'direito_caso': forms.Select(choices=choice_list_direito, attrs={'class': 'form-control'}),
            'materia_caso': forms.Select(choices=choice_list_materia, attrs={'class': 'form-control'}),
            'content_caso': forms.Textarea(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'lei_caso': forms.Textarea(attrs={'class': 'form-control'}),
            'jurisprudencia_caso': forms.Textarea(attrs={'class': 'form-control'}),
            'tags_caso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'meta_caso': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),
        }

class AddDireitoCasoForm(forms.ModelForm):
    class Meta:
        model = DireitoCaso
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }

class AddMateriaCasoForm(forms.ModelForm):
    class Meta:
        model = MateriaCaso
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }
class EditDireitoCasoForm(forms.ModelForm):
    class Meta:
        model = DireitoCaso
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }

class EditMateriaCasoForm(forms.ModelForm):
    class Meta:
        model = MateriaCaso
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }