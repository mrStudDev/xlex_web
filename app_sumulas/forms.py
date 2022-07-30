from django import forms
from .models import Sumulas, SumulaMateria, SumulaTribunal


choices = SumulaTribunal.objects.all().values_list('name', 'name')
choice_list_sumula_tribunal = []

for item in choices:
    choice_list_sumula_tribunal.append(item)

choices = SumulaMateria.objects.all().values_list('name', 'name')
choice_list_sumula_materia = []

for item in choices:
    choice_list_sumula_materia.append(item)


class AddSumulaForm(forms.ModelForm):
    class Meta:
        model = Sumulas
        fields = (
            'title_sumula',
            'author',
            'sumula_tribunal',
            'sumula_materia',
            'content_sumula',
            'fundamentacao_sumula',
            'tags_sumula',
            'meta_sumula',
            'key_word',
            )

        widgets = {
            'title_sumula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'sumula_tribunal': forms.Select(choices=choice_list_sumula_tribunal, attrs={'class': 'form-control'}),
            'sumula_materia': forms.Select(choices=choice_list_sumula_materia, attrs={'class': 'form-control'}),
            'content_sumula': forms.Textarea(attrs={'class': 'form-control'}),
            'fundamentacao_sumula': forms.Textarea(attrs={'class': 'form-control'}),
            'tags_sumula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'meta_sumula': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),

        }


class EditSumulaForm(forms.ModelForm):
    class Meta:
        model = Sumulas
        fields = (
            'title_sumula',
            'author',
            'sumula_tribunal',
            'sumula_materia',
            'content_sumula',
            'fundamentacao_sumula',
            'tags_sumula',
            'meta_sumula',
            'key_word',
            )

        widgets = {
            'title_sumula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'sumula_tribunal': forms.Select(choices=choice_list_sumula_tribunal, attrs={'class': 'form-control'}),
            'sumula_materia': forms.Select(choices=choice_list_sumula_materia, attrs={'class': 'form-control'}),
            'content_sumula': forms.Textarea(attrs={'class': 'form-control'}),
            'fundamentacao_sumula': forms.Textarea(attrs={'class': 'form-control'}),
            'tags_sumula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'meta_sumula': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),

        }


class AddSumulaMateriaForm(forms.ModelForm):
    class Meta:
        model = SumulaMateria
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class AddSumulaTribunalForm(forms.ModelForm):
    class Meta:
        model = SumulaTribunal
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class EditSumulaMateriaForm(forms.ModelForm):
    class Meta:
        model = SumulaMateria
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class EditSumulaTribunalForm(forms.ModelForm):
    class Meta:
        model = SumulaTribunal
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }