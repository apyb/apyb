from django.contrib import admin
from . import models


class WebContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.WebContent, WebContentAdmin)
