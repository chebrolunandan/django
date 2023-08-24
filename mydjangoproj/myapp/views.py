from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.forms import StudForm
def home(request):
    student = StudForm()
    return render(request,"index.html",{'form':Student})

def contact(request):
    if request.method=="POST":
                return render(request,'contact.html')
    else:
      student=StudForm()
      return render(request,"index.html",{'form':student})