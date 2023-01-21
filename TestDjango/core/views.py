from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def datos(request):
    contexto= {"nombre" :"Francois Cerdieu"}
    Hijo=Class_perrsona("Adams Francois","2")
    contexto= {"nombre" :"Francois Cerdieu","pariente":Hijo}
    return render(request, 'datos.html', contexto)

class Class_perrsona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
