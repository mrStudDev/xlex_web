from django.contrib import admin

from .models import Question, MateriaQuestion, BancaQuestion


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["title_question", "question_ask"]
    prepopulated_fields = {"slug": ("title_question",)}

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)
admin.site.register(MateriaQuestion)
admin.site.register(BancaQuestion)