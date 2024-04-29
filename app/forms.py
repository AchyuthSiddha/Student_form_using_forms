from django import forms


class StudentForm(forms.Form):
    Rollno=forms.IntegerField()
    name=forms.CharField()
    marks=forms.IntegerField()


    