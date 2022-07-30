from django.contrib import admin

from .models import Sumulas, SumulaMateria, SumulaTribunal


class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["title_sumula", "content_sumula"]
    prepopulated_fields = {"slug": ("title_sumula",)}

    class Meta:
        model = Sumulas


admin.site.register(Sumulas, PostAdmin)
admin.site.register(SumulaMateria)
admin.site.register(SumulaTribunal)
