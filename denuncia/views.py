from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Denuncia
from .form import DenunciaForm
from django.contrib import messages

def denunciaList(request):
    denuncia = Denuncia.objects.all().order_by('-created_at')

    return render(request, 'denuncia/list.html', {'denuncia':denuncia})

def denunciaView(request, id):
    denuncia= get_object_or_404(Denuncia, pk=id)
    return render(request, 'denuncia/denuncia.html', {'denuncia':denuncia})

def denunciaAdd(request):
    if request.method== 'POST':
        form= DenunciaForm(request.POST)
        if form.is_valid():
            denuncia= form.save(commit=False)
            denuncia.save()
            return redirect('/')
    else:
        form= DenunciaForm()
        return render(request, 'denuncia/cadastro.html', {'form': form})

def denunciaEdit(request, id):
    denuncia = get_object_or_404(Denuncia, pk=id)
    form = DenunciaForm(instance=denuncia)

    if(request.method=='POST'):
        form = DenunciaForm(request.POST, instance=denuncia)
        if(form.is_valid()):
            denuncia.save()
            return redirect('/')
        else:
            return render(request, 'denuncia/edit.html', {'form': form, 'denuncia': denuncia})

    else: 
        return render(request, 'denuncia/edit.html', {'form': form, 'denuncia': denuncia})

def denunciaDelete(request, id):
    denuncia = get_object_or_404(Denuncia, pk=id)
    denuncia.delete()
    messages.info(request, 'Deletado com sucesso.')
    return redirect('/')
