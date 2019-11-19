from django.shortcuts import render, get_object_or_404
from .models import Carnes
from .forms import CarnesForm,CustomUserCreationForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    posts = Carnes.objects.order_by('-pk')
    return render(request, 'blog/index.html', {'posts': posts})
def detalle(request, pk):
    post = get_object_or_404(Carnes, pk=pk)
    return render(request, 'blog/detalle.html', {'post': post})
def nuevo(request):
    if request.method == "POST":
        form = CarnesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detalle', pk=post.pk)
    else:
        form = CarnesForm()
    return render(request, 'blog/nuevo.html', {'form': form})
def registro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
def editar(request, pk):
    post = get_object_or_404(Carnes, pk=pk)
    if request.method == "POST":
        form = CarnesForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detalle', pk=post.pk)
    else:
        form = CarnesForm(instance=post)
    return render(request, 'blog/editar.html', {'form': form})