from django.contrib import admin

from core import models


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["title", "deadline", "start_date", "end_date", "nfq", "ote_flag", "link"]
    search_fields = ['title', ]
    class Meta:
        model = models.CourseModel

class UpdateModelAdmin(admin.ModelAdmin):
    ordering = ["status", "updated"]
    list_display = ["status", "updated"]
    search_fields = ["status", "updated"]

    class Meta:
        model = models.UpdateModel


admin.site.register(models.CourseModel, CourseModelAdmin)
admin.site.register(models.UpdateModel, UpdateModelAdmin)