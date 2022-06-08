from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def registerview(request):
    form = UserCreationForm()
    template_name = 'auth_app/register.html'
    context = {'form':form}
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('loginurl')
    return render(request,template_name,context)

def loginview(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == "POST":
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('bookurl')
    return render(request,template_name,context)

def logoutview(request):
    logout(request)
    return redirect ('loginurl')