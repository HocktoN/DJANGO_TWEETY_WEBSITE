from django.shortcuts import render
from myprofile.models import Gonderi


def index(request):
    gonderis = Gonderi.objects.all().order_by('-id')
    context = {'gonderis':gonderis}
    return render(request,"index.html",context)

def search(request):
    gonderis = Gonderi.objects.filter(icerik__contains = request.GET['search'])  

    context = {
        'gonderis':gonderis, 
    } 
    return render(request,'index.html',context) 



# Create your views here.
