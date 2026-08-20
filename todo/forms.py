from django import forms;
from .models import Todo;

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo;
        fields = ['title','content','priority','is_done']
        
        widgets = {
            "title":forms.TextInput(attrs={
                    "class" : "form-input",
                    "placeholder": "Enter todo title",
                }),
            
            "content":forms.Textarea(attrs={
                    "class" : "form-input",
                    "placeholder": "Enter todo description",
                    "rows":4,
                }),
            
            "priority":forms.NumberInput(attrs={
                    "class":"form-input",
                    "min":1,
                }),
            
            "is_done":forms.CheckboxInput(attrs={"class":"check-box"})
        }