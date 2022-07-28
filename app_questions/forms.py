from django import forms
from .models import Question, MateriaQuestion, BancaQuestion


choices = BancaQuestion.objects.all().values_list('name', 'name')
choice_list_banca_question = []

for item in choices:
    choice_list_banca_question.append(item)

choices = MateriaQuestion.objects.all().values_list('name', 'name')
choice_list_materia_question = []

for item in choices:
    choice_list_materia_question.append(item)


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'title_question',
            'author',
            'banca_question',
            'materia_question',
            'question_ask',
            'alternativa_a',
            'alternativa_b',
            'alternativa_c',
            'alternativa_d',
            'alternativa_e',
            'alternativa_correta',
            'fundamentacao',
            'lei_question',
            'jurisprudencia_question',
            'tags_question',
            'meta_question',
            'key_word',
            )

        widgets = {
            'title_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(choices=choice_list_banca_question, attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'banca_question': forms.Select(choices=choice_list_materia_question, attrs={'class': 'form-control'}),
            'materia_question': forms.Select(attrs={'class': 'form-control'}),
            'question_ask': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_a': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_b': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_c': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_d': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_e': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_correta': forms.Textarea(attrs={'class': 'form-control'}),
            'fundamentacao': forms.Textarea(attrs={'class': 'form-control'}),
            'lei_question': forms.Textarea(attrs={'class': 'form-control'}),
            'jurisprudencia_question': forms.Textarea(attrs={'class': 'form-control'}),
            'tags_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'meta_question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),

        }


class EditQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'title_question',
            'author',
            'banca_question',
            'materia_question',
            'question_ask',
            'alternativa_a',
            'alternativa_b',
            'alternativa_c',
            'alternativa_d',
            'alternativa_e',
            'alternativa_correta',
            'fundamentacao',
            'lei_question',
            'jurisprudencia_question',
            'tags_question',
            'meta_question',
            'key_word',
            )

        widgets = {
            'title_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'banca_question': forms.Select(choices=choice_list_banca_question, attrs={'class': 'form-control'}),
            'materia_question': forms.Select(choices=choice_list_materia_question, attrs={'class': 'form-control'}), 
            'question_ask': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_a': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_b': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_c': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_d': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_e': forms.Textarea(attrs={'class': 'form-control'}),
            'alternativa_correta': forms.Textarea(attrs={'class': 'form-control'}),
            'fundamentacao': forms.Textarea(attrs={'class': 'form-control'}),
            'lei_question': forms.Textarea(attrs={'class': 'form-control'}),
            'jurisprudencia_question': forms.Textarea(attrs={'class': 'form-control'}),
            'tags_question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'meta_question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),

        }


class AddMateriaQuestionForm(forms.ModelForm):
    class Meta:
        model = MateriaQuestion
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class AddBancaQuestionForm(forms.ModelForm):
    class Meta:
        model = BancaQuestion
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class EditMateriaQuestionForm(forms.ModelForm):
    class Meta:
        model = MateriaQuestion
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class EditBancaQuestionForm(forms.ModelForm):
    class Meta:
        model = BancaQuestion
        fields = (
            'name',
            'excerpt',
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }