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

def edit(request,id):
    if request.method =='POST':
        user = Student.objects.get(id=id)
        form = studentReg(request.POST,instance=user)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    else:
        user = Student.objects.get(id=id)
        form=studentReg(instance=user)
    return render(request,'edit.html',{'form':form})


