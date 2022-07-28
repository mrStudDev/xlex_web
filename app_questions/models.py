from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class BancaQuestion(models.Model):
    name = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class MateriaQuestion(models.Model):
    name = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


choices = BancaQuestion.objects.all().values_list('name', 'name')
choice_list_banca_question = []

for item in choices:
    choice_list_banca_question.append(item)

choices = MateriaQuestion.objects.all().values_list('name', 'name')
choice_list_materia_question = []

for objs in choices:
    choice_list_materia_question.append(objs)



class Question(models.Model):
    title_question = models.CharField(max_length=255)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    banca_question = models.CharField(choices=choice_list_banca_question, max_length=255, default="Undefined")
    materia_question = models.CharField(choices=choice_list_materia_question, max_length=255, default="Undefined")
    question_ask = RichTextUploadingField(blank=True, null=True)
    alternativa_a = models.CharField(max_length=1000)
    alternativa_b = models.CharField(max_length=1000)
    alternativa_c = models.CharField(max_length=1000)
    alternativa_d = models.CharField(max_length=1000)
    alternativa_e = models.CharField(max_length=1000)
    alternativa_correta = models.CharField(max_length=1000)
    fundamentacao = RichTextUploadingField(blank=True, null=True)
    lei_question = RichTextUploadingField(blank=True, null=True)
    jurisprudencia_question = RichTextUploadingField(blank=True, null=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags_question = models.CharField(max_length=200)
    meta_question = models.TextField(max_length=150)
    key_word = models.CharField(max_length=50)


    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title_question + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        #return reverse("questao_singular", kwargs={"id": self.id, "slug": self.slug})