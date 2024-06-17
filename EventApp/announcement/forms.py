from django import forms
from .models import AnnouncementModel
from tinymce.widgets import TinyMCE

class AnnouncementForm(forms.ModelForm):
    content= forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta:
        model= AnnouncementModel
        fields =[
            'title', 'content'
        ]
        widgets={
            'title': forms.TextInput(attrs={'class':'w-100'}),
        }