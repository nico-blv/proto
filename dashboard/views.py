from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from vacunos.models import Vaca, Lote

# Create your views here.

@login_required
def home(request):
    return render(request, "dashboard/home.html")
def login(request):
    return render(request, "dashboard/login.html")
@login_required
def grafico(request):
    return render(request, "dashboard/graficos.html")
@login_required
def list(request):
    vaca = Vaca.objects.all()
    return render(request, "dashboard/listado.html", {'vc':vaca})
@login_required
def lote(request):
    loteV = Lote.objects.all()
    return render(request, "dashboard/lote.html", {'lot':loteV})