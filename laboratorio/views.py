from django.shortcuts import render
from laboratorio.forms import LaboratorioForm
from .models import Laboratorio
from django.http import HttpResponseRedirect, Http404


def v_laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {
        'form': LaboratorioForm()  
    }

    return render(request, 'laboratorio_create.html', context)
    
def v_laboratorio_edit(request, laboratorio_id):
    try:
        context = {
            'labo': Laboratorio.objects.get(id = laboratorio_id), 
        }
        
    except:
        raise Http404 
    
    if request.method == 'POST': #if para actualizar datos ya creados
        form = LaboratorioForm(request.POST, instance  = context['labo']) #para actualizar datos creados
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        

    #context ya existe
    context['form'] = LaboratorioForm(instance = context['labo'])

    return render(request, 'laboratorio_edit.html', context)

def v_laboratorio_list(request):
    
    context = {'lab': Laboratorio.objects.all()}
    return render (request, 'laboratorio_list.html', context)
    
    
def v_laboratorio_delete(request, laboratorio_id):
    cont = {
        'lav': Laboratorio.objects.get(id = laboratorio_id)
    }

    if request.method == 'POST':
        cont['lav'].delete()
        return HttpResponseRedirect('/')

    return render(request, 'laboratorio_delete.html', cont)
