from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .forms import FoodFitness,FoodFitnessForm

# Create your views here.

def index(request):  #Test Server
    return render(request,'cwApp/index.html')

def blankForm(request):   #Function to get methond
    application=FoodFitnessForm()   #Blank form
    context={
        'application':application
    }
    return render(request,'cwApp/createUser.html',context)   #goes to the template with form
def createUser(request):
    application=FoodFitnessForm(request.POST)   #has posted form
    context={
        'application':application
    }

    if request.method=="POST":
        User.objects.create_user(request.POST['username'],'',request.POST['password'])   #creates user
        return render(request,'cwApp/accountCreated.html')   #sends it to account crated page



def accountCreated(request):
    return render(request,'cwApp/accountCreated.html')  #sends to account created page