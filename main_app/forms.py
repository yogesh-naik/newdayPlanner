from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Task,Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','tag']
        labels = {'name': 'Task'}
        # exclude = ['user']
        
        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            
class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','tag']
        labels = {'name': 'Task'}
        
        def __init__(self, *args, **kwargs):
            super(TaskEditForm, self).__init__(*args, **kwargs)
            self.fields['name','tag'].required = False
            
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']
        labels = {'comments': 'Comments/Reminders'}