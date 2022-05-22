from django.shortcuts import render,redirect
from . forms import  LoginForm, RegisterForm
from django.contrib.auth import  login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import  User



def user_login(request):
    
    if request.method == 'POST': #eğer method post ise 
        form = LoginForm(request.POST) #loginformdan bir nesne türet ve gelen değerleri bu nesnede sakla.
        if form.is_valid(): #form geçerli ise
            username=form.cleaned_data['username'] #formdan gelen değerleri atama
            password = form.cleaned_data['password'] # """""
            user = authenticate(request, username = username, password = password) 

            if user is not None: # böyle bir kullanıcı varsa
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.info(request,'Hesap aktif değil!') #meşaz ver xD
            else:
                messages.info(request,'Kullanıcı adı veya parola hatalı!')
    else:
        form = LoginForm() #eğer get isteği atıldıysa formu boş göster

    return render(request,'login.html',{'form':form})


def user_register(request):
    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Hesap oluşturuldu. Giriş yapabilirsin!')
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request,'register.html',{'form':form})

    
def user_logout(request):
    logout(request)
    return redirect("index")







# Create your views here.
