from django.shortcuts import render
from .models import Carnes

# Create your views here.
def index(request):
    posts = Carnes.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})