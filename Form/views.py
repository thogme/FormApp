from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from .forms import Formulario

def listado(request):
    lists = List.objects.order_by('numero')
    return render(request, 'Form/listado.html', {'lists':lists})

#def individuo(request, pk):
#    list = get_object_or_404(List, pk=pk)
#    return render(request, 'Form/individuo.html', {'list':list})

def entrada(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('listado')
    else:
        form = Formulario()
    return render(request, 'Form/editado.html',{'form': form})

def resultado(request):
    if request.method == "GET":
        busquedas = List.objects.exclude(numero__isnull=False)
        return render(request, 'Form/resultado.html', {'busquedas': busquedas})
