from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class DireitoCaso(models.Model):
    name = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=150, default="Sorry")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class MateriaCaso(models.Model):
    name = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=150, default="Sorry")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


choices = DireitoCaso.objects.all().values_list('name', 'name')
choice_list_direito = []

for item in choices:
    choice_list_direito.append(item)

choices = MateriaCaso.objects.all().values_list('name', 'name')
choice_list_materia = []

for item in choices:
    choice_list_materia.append(item)


class CasoConcreto(models.Model):
    title_caso = models.CharField(max_length=120)
    img_caso = models.ImageField(upload_to='images/', default=1, null=True, blank=True)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    direito_caso = models.CharField(choices=choice_list_direito, max_length=100, default="XLEX")
    materia_caso = models.CharField(choices=choice_list_materia, max_length=100, default="XLEX")
    meta_caso = models.TextField(max_length=150)
    content_caso = RichTextUploadingField(blank=True, null=True)
    lei_caso = RichTextUploadingField(blank=True, null=True)
    jurisprudencia_caso = RichTextUploadingField(blank=True, null=True)
    tags_caso = models.CharField(max_length=200)
    key_word = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title_caso + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
