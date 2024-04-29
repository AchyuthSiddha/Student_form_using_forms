from django.shortcuts import render

# Create your views here.
from app.forms import StudentForm


def Std_info(request):
    # form=StudentForm()
    submitted=False
    name=''
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print("data is sucessfully")
            print('Rollno:',form.cleaned_data['Rollno'])
            print('name:',form.cleaned_data['name'])
            print('marks:',form.cleaned_data['marks'])
            submitted=True
            name=form.cleaned_data['name']
    form=StudentForm()
    

    
    return render(request,'result.html',{'form':form,"submitted":submitted,'name':name})