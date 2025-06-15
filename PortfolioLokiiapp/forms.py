from django import forms
from.models import Skill,Project,Person,Blog,ClientService




class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'email', 'address', 'number', 'skill', 'image']


#thsi for form data reterive skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency', 'image'] 
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'file', 'image_file']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'video']
        
class ClientServiceForm(forms.ModelForm):
    class Meta:
        model = ClientService
        fields = ['name', 'description', 'image'] 
        





























