from django.contrib import admin

from notesapi.models import Article, Contract, Employee, WorkingCenter

# Register your models here.
admin.site.register(Employee)
admin.site.register(Contract)
admin.site.register(WorkingCenter)


@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ("title", "description")
    list_display = ("title", "description")
