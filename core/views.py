from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from core.Carrito import Carrito
from core.models import Producto


from .models import Product,HandrollReady,Kai,Selladitas,Bowl
from .forms import ProductForm,BowlForm,DesayunoForm,AlmuerzoForm,HandrollForm
from .Carrito import Carrito
from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)


def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Product.objects.all()
    bowls = Bowl.objects.all()
    hc = HandrollReady.objects.all()
    context={
        'productos':productos,
        "bowls":bowls,
        "hc":hc,
    }
    return render(request, "core/tienda.html",context)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def agregar_handclassic(request, producto_id):
    carrito = Carrito(request)
    producto = HandrollReady.objects.get(id=producto_id)
    carrito.agregar_handclassic(producto)
    return redirect("Tienda")

def agregar_bowl(request, producto_id):
    carrito = Carrito(request)
    producto = Bowl.objects.get(id=producto_id)
    carrito.agregarBowl(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")


#Crear las funciones y asignarlas a un template

#funcion index, toma una peticion, retorna cuerpo en ruta
def Index(request):
    p=Product.objects.all()
    return render(request, 'core/index.html', {"produc":p})


#Listar productos
def ListaProducto(request):
    p=Product.objects.all()
    context={
        "product":p,
    }
    return render(request, 'core/list_product.html',context)

def NuevoProducto(request):
    p=Product.objects.all()
    form=ProductForm(request.POST or None)
    if request.method == 'POST':
        

        if form.is_valid():
            a=form.save(commit=True)

            return HttpResponseRedirect("/listaproducto/")
        else:
            print('error')  
    context={
        "product":p,
        "form":form,
    }
    return render(request, 'core/new_product.html',context)

# def ModificarProducto(request,id):
#     # dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# fetch the object related to passed id
# 	obj = get_object_or_404(Product, id = id)

# 	# pass the object as instance in form
# 	form = ProductForm(request.POST or None, instance = obj)

# 	# save the data from the form and
# 	# redirect to detail_view
# 	if form.is_valid():
# 		form.save()
# 		return HttpResponseRedirect("/"+id)

# 	# add form dictionary to context
	

#     return render(request, "core/update_product.html", context)
    
def Update(request,id):
    context={

    }
    obj = get_object_or_404(Product, id = id)

    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/listaproducto/")
    else:
        print('error')

    context["form"] = form

    return render(request, 'core/update_product.html',context)
def EliminarProducto(request,id):
    # dictionary for initial data with
    # field names as keys
    
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
    context ={
        'product':obj
    }
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    
    return render(request, 'core/delete_product.html',context)

# def Carrito(request):
#     product = Product.objects.all()
#     context = {
#         "product":product,
#     }
#     return render(request, 'core/carrito.html',context)

def registros(request):
    bf= BowlForm()
    dsyn = DesayunoForm()
    almrz = AlmuerzoForm()
    hr = HandrollForm()
    hrcls = HandrollReady.objects.all()
    kai = Kai.objects.all()
    sll = Selladitas.objects.all()
    context={
        "bf":bf,
        "dsyn":dsyn,
        "almrz":almrz,
        "hr":hr,
        "hrcls":hrcls,
        "kai":kai,
        "sll":sll,
    }
    return render(request, 'core/registros.html',context)