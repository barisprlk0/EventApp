from django import forms
from .models import TravelModel, Rating
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


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['value']
        widgets = {
            'value': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)] )
        }
