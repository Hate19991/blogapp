from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required

def home(request):
    content = Notes.objects.all()
    return render(request , "index.html" , {"contents": content})

@login_required
def write(request):
    if request.method == 'POST':
        text = request.POST['text']
        title = request.POST['title']
        image = request.POST['image']
        addition =  Notes(title=title,text=text , image=image)
        addition.save()
        return redirect('home')
    return render(request , "note.html")

@login_required
def update_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        new_text = request.POST['text']
        note.text = new_text
        new_title = request.POST['title']
        note.title = new_title
        new_image = request.POST['image']
        note.image = new_image
        note.save()  
        return redirect('home')
    return render(request, 'update_note.html', {"contents": note})


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'index.html', {"contents": note})



def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username , email , password1)
            user.save()
            auth.login(request , user)
            return redirect('home')
        return render(request,'login.html',{'success':'Account Created Successfully,Please log in,i am begging you'})
    return render(request,'signin.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user:
            auth.login(request , user)
            return redirect('home')
        else:
            error_message = "hmmm it seems you didn't enter the right details"
            return render(request , 'login.html',{'error_message':error_message})
    return render(request , 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

def email_req(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user.exists():
            return render(request , 'email_req.html',{'success':'success alert'})
        else:
            return render(request , 'email_req.html',{'error':'error alert'})
    
