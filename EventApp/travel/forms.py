from django import forms
from .models import TravelModel
from tinymce.widgets import TinyMCE

class TravelForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = TravelModel
        fields = [
            'title','thumbnail_image','content',
        ]
        widgets={
            'title': forms.TextInput(attrs={'class':'w-100'}),
            'thumbnail_image': forms.FileInput(attrs={'class': 'form-control form-large  '}),
        } 

