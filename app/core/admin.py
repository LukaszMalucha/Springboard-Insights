from django.contrib import admin

from core import models


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["title", "deadline", "start_date", "end_date", "nfq", "ote_flag", "link"]
    search_fields = ['title', ]
    class Meta:
        model = models.CourseModel


admin.site.register(models.CourseModel, CourseModelAdmin)
