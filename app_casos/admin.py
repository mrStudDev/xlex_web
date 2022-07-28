from django.contrib import admin

from .models import CasoConcreto, MateriaCaso, DireitoCaso


class CasoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["title_caso", "content"]
    prepopulated_fields = {"slug": ("title_caso",)}

    class Meta:
        model = CasoConcreto


admin.site.register(CasoConcreto, CasoAdmin)
admin.site.register(MateriaCaso)
admin.site.register(DireitoCaso)

