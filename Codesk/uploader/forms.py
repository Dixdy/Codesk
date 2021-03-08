from django import forms
from uploader.models import ImageFile


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ('image', )

class UploadFileForm(forms.Form):
    file = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))