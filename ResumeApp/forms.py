from django import forms 

from .models import Candidate

GENDER_CHICES = [
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
 ('Banglore', 'Banglore')
]


class CandidateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices= JOB_CITY_CHOICE,label='Prefered Job Location',widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Candidate
        fields = '__all__'
        labels ={
            'firstname':'First Name',
            'lastname': 'Last Name',
            'date_of_birth' : 'Date of Birth',
            'profile_img':'Profile Image',
            'pin':'PIN',
        }

        widgets = {
            'date_of_birth':forms.DateInput(attrs={'id':'datepicker'}),
            }


    # def __init__(self,*args, **kwargs):
    #     super(Candidate).__init__(*args, **kwargs)
    #     # self.fields['']