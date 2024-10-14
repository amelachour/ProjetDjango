from django import forms
from .models import Cours

class CourseForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['title', 'description', 'file']
<<<<<<< HEAD
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Entrez le titre du cours'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Entrez une description du cours'
        })
        self.fields['file'].widget.attrs.update({
            'class': 'form-control'
        })
=======
>>>>>>> c4f4019b0ff2ad6983f6bd24f6b5f3e4a8431bde
