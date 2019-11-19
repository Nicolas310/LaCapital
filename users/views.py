from django.shortcuts import render, get_object_or_404
from .models import Carnes

# Create your views here.
def index(request):
    posts = Carnes.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})
def detalle(request, pk):
    post = get_object_or_404(Carnes, pk=pk)
    return render(request, 'blog/detalle.html', {'post': post})