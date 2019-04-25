from django import forms
from .models import Dept, Course,Exam

class FormName(forms.Form):
    dept = forms.ModelChoiceField(queryset= Dept.objects.all(), )
    course = forms.ModelChoiceField( queryset= Course.objects.all() )
    date = forms.DateField()


# from django import forms
# from .models import Dept, Course, Exam
#
# class FormName(forms.ModelForm):
#     class Meta:
#         model = Exam
#         fields = ('dept', 'course')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['course'].queryset = Course.objects.none()
