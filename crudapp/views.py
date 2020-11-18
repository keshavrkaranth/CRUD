from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def Homepage(request):
    if request.method=='POST':
        form = studentReg(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = studentReg()
        else:
            return HttpResponse("error")
    else:

        form = studentReg()
    user_details = Student.objects.all()

    return render(request,'home.html',{"form":form,
                                       'details':user_details,
                                       })



def delete(request,id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('/')


