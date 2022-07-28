from django import forms
from .models import PostsXlex, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = PostsXlex
        fields = ('title', 'tags', 'author', 'category', 'content', 'img_destaque', 'meta_description', 'key_word',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            'key_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = PostsXlex
        fields = ('title', 'tags', 'content',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =  ('name', 'excerpt')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description Category'}),
        }

