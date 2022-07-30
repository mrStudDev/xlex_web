from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class SumulaTribunal(models.Model):
    name = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=150, default="Description...")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('post-single', args=(str(self.id)))
        return reverse('home')


class SumulaMateria(models.Model):
    name = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=150, default="Description...")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('post-single', args=(str(self.id)))
        return reverse('home')


choices = SumulaTribunal.objects.all().values_list('name', 'name')
choice_list_sumula_tribunal = []

for item in choices:
    choice_list_sumula_tribunal.append(item)

choices = SumulaMateria.objects.all().values_list('name', 'name')
choice_list_sumula_materia = []

for objs in choices:
    choice_list_sumula_materia.append(objs)


class Sumulas(models.Model):
    title_sumula = models.CharField(max_length=120)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    sumula_tribunal = models.CharField(choices=choice_list_sumula_tribunal, max_length=100, default="XLEX")
    sumula_materia = models.CharField(choices=choice_list_sumula_materia, max_length=100, default="XLEX")
    content_sumula = RichTextUploadingField(blank=True, null=True)
    fundamentacao_sumula = RichTextUploadingField(blank=True, null=True, default="Sorry")
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags_sumula = models.CharField(max_length=200)
    key_word = models.CharField(max_length=50)
    meta_sumula = models.TextField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.title_sumula + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('post-single', args=(str(self.id)))
        return reverse('home')
