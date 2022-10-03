from django.shortcuts import render,redirect
from .models import Productos

# Create your views here.
def listar_productos(request):
    productos=Productos.objects.all()
    print(productos)
    return render(request,'listar_productos.html', {"productos" : productos})

def crear_producto(request):
    producto = Productos(nombre=request.POST['nombre'],contenido_neto=request.POST['contenido_neto'], precio=request.POST['precio'],descripcion=request.POST['descripcion'])
    producto.save()
    return redirect('/productos/')

def borrar_producto(request, producto_id):
    producto=Productos.objects.get(id=producto_id)
    producto.delete()
    return redirect('/productos/')

