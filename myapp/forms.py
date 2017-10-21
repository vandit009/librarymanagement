from django import forms
from myapp.models import Topic
from django.forms.widgets import RadioSelect, Textarea
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm
class TopicForm(forms.ModelForm):
    class Meta:
        model= Topic
        fields=['subject', 'intro_course', 'time', 'avg_age']
        widgets={'time': RadioSelect}
        labels={
                'time': 'Preferred Time',
                'avg_age': 'What is your age',
                'intro_course':'This should be an introductory level course'
                }
class InterestForm(forms.Form):
    interested= forms.ChoiceField(widget=RadioSelect, choices= ((0, 'No '),(1, 'Yes')))
    age=forms.IntegerField(initial=20)
    comments=forms.CharField(widget=Textarea,label='Additional Comments',) 

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    birthday = forms.DateField(required = False)



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birthday']


        if commit:
            user.save()

        return user
