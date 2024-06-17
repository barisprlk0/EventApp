from django.contrib import admin
from .models import AnnouncementModel
from tinymce.widgets import TinyMCE
from django.db import models


class AnnouncementModelAdmin(admin.ModelAdmin):
    fields = (
            'title','author','content'
        )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

admin.site.register(AnnouncementModel, AnnouncementModelAdmin)
