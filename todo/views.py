from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Arbol
from .forms import ArbolForm

from .models import Tarea
from .forms import TareaForm

pila = []

def home(request):
    pila.clear()
    return redirect("homen",1)

def homen(request, arbol_nodo):
    n=arbol_nodo
    arbols=Arbol.objects.get(nodo=n)      
    context={'arbols': arbols}
    return render(request, 'todo/home.html', context)

def homsi(request, arbol_nodo):
    n=arbol_nodo*2
    return redirect("homen",n)

def homno(request, arbol_nodo):
    n=(arbol_nodo*2)+1
    return redirect("homen",n)

def respuesta(request, arbol_nodo):
    arbols=Arbol.objects.get(nodo=arbol_nodo)     
    context={'arbols': arbols}
    return render(request, 'todo/respuesta.html', context)

#respuestas ambiguas
def hompsi(request, arbol_nodo):
    opuesta=(arbol_nodo*2)+1
    pila.append(opuesta)
    n=arbol_nodo*2
    return redirect("homen",n)

def hompno(request, arbol_nodo):
    opuesta=(arbol_nodo*2)
    pila.append(opuesta)
    n=(arbol_nodo*2)+1
    return redirect("homen",n)

def homnose(request, arbol_nodo):
    if(arbol_nodo%2)==0:
        n=arbol_nodo*2
        opuesta=(arbol_nodo*2)+1
        pila.append(opuesta)
    else:
        n=(arbol_nodo*2)+1
        opuesta=(arbol_nodo*2)
        pila.append(opuesta)       
    return redirect("homen",n)

def oportunidad(request, arbol_nodo):
    if pila!=[]:
        n=pila.pop()
        return redirect("homen",n)
    else:
        n=arbol_nodo
        return redirect("agregar_nodo",n)

def agregar_nodo(request, arbol_nodo):
    arbols = Arbol.objects.get(nodo=arbol_nodo)
    if request.method=="POST":
        form = ArbolForm(request.POST)
        if form.is_valid():
            res=form.cleaned_data['respuesta'].upper()
            pre=form.cleaned_data['pregunta'].lower()
            
            nodo_si = Arbol(nodo=(arbols.nodo*2)+1,texto=arbols.texto,pregunta=False)
            nodo_no = Arbol(nodo=(arbols.nodo*2),texto=res,pregunta=False)
            nodo_si.save()
            nodo_no.save()
            
            arbols.texto=pre
            arbols.pregunta=True
            arbols.save()
            return redirect('home')
    else:
        form = ArbolForm()
    
    context={'form' : form,
             'arbols' : arbols}
    
    return render(request, 'todo/agregar.html', context)




#Ejemplos
def agregar(request):
    if request.method=="POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    
    context={'form' : form}
    
    return render(request, 'todo/agregar.html', context)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')

def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method=="POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareaForm(instance=tarea)
    
    context={"form" : form}
    return render(request, "todo/editar.html", context)
