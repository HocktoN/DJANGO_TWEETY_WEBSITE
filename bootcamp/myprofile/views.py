
from django.shortcuts import redirect, render
from django.contrib.auth.models import  User
from . models import Gonderi

def benim(request):
    current_user = request.user
    gonderis = Gonderi.objects.filter(kullanici__id = current_user.id).order_by('-id')
    context = {'gonderis':gonderis}
    return render(request,"profilim.html",context)

    
def paylas(request):
    gonderi = Gonderi(icerik= request.POST['icerik'])
    image = request.FILES.get('image')
    gonderi.image = image
    kullanici = User.objects.get(id = request.POST['user_id'])
    gonderi.kullanici = kullanici
    gonderi.save()
    return redirect("index")




# Create your views here.
