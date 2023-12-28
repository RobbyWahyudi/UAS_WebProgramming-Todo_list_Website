from django.contrib import admin
from .models import Task, Kategori


class ListAdmin(admin.ModelAdmin):
    list_display = (
        "judul",
        "tanggal_jatuh_tempo",
        "status",
        "kategori",
    )


admin.site.register(Task, ListAdmin)
admin.site.register(Kategori)
