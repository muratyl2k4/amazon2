from django import forms
from .models import excelDataa

class UploadFileForm(forms.ModelForm):
    class Meta: 
        model = excelDataa
    
        fields = ('com_asin' , 'target_asin' ,)