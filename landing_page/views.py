from django.shortcuts import render
# from .models import Student
# Create your views here.
def gett(request):
    return render(request,'landing_page/all.html')