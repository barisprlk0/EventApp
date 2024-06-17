from django.contrib import admin
from .models import TravelModel
from tinymce.widgets import TinyMCE
from django.db import models


class TravelModelAdmin(admin.ModelAdmin):
    fields = (
            'title','thumbnail_image','content'
        )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

admin.site.register(TravelModel, TravelModelAdmin)
