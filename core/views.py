from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
# Create your views here.
from core.Carrito import Carrito
from core.models import Producto


from .models import Product,Article,Comanda,Selladitas,Desayuno,Almuerzo ,HandrollReady,Kai,Selladitas,Bowl
from .forms import ProductForm,BowlForm,DesayunoForm,AlmuerzoForm,HandrollForm
from .Carrito import Carrito
from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)
from django.db.models import Q

def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Product.objects.all()
    bowls = Bowl.objects.all()
    hc = HandrollReady.objects.all()
    al = Almuerzo.objects.all()
    des = Desayuno.objects.all()
    sell = Selladitas.objects.all()
    queryset= request.GET.get("buscar")
    if queryset:
        productos = Product.objects.filter(
            Q(id__icontains = queryset)
        ).distinct()
        bowls = Bowl.objects.filter(
            Q(id__icontains = queryset)
        ).distinct()
        hc = HandrollReady.objects.filter(
            Q(id__icontains = queryset)
        ).distinct()
        al = Almuerzo.objects.filter(
            Q(id__icontains = queryset)
        ).distinct()
        des = Desayuno.objects.filter(
            Q(id__icontains = queryset)
        ).distinct()
        sell = Selladitas.objects.filter(
            Q(id__icontains = queryset)
        ).distinct()
    context={
        'productos':productos,
        "b":bowls,
        "hc":hc,
        "al":al,
        "des":des,
        "sell":sell
    }
    return render(request, "core/tienda.html",context)

def agregar_producto(request, producto_id,typ):
    carrito = Carrito(request)
    if typ == 'hc':
        producto = HandrollReady.objects.get(id=producto_id)
    elif typ == 'al':
        producto = Almuerzo.objects.get(id=producto_id)
    elif typ == 'b':
        producto = Bowl.objects.get(id=producto_id)
    elif typ == 'des':
        producto = Desayuno.objects.get(id=producto_id)
    elif typ == 'sell':
        producto = Selladitas.objects.get(id=producto_id)
        
    else:
        producto=''
    carrito.agregar(producto)
    return redirect("Tienda")

def agregar_handclassic(request, producto_id):
    carrito = Carrito(request)
    producto = HandrollReady.objects.get(id=producto_id)
    carrito.agregar_handclassic(producto)
    return redirect("Tienda")

# def agregar_bowl(request, producto_id):
#     carrito = Carrito(request)
#     producto = Bowl.objects.get(id=producto_id)
#     carrito.agregarBowl(producto)
#     return redirect("Tienda")

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

# def restar_handclassic(request, producto_id):
#     carrito = Carrito(request)
#     producto = HandrollReady.objects.get(id=producto_id)
#     carrito.restar_hc(producto)
#     return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")


#Crear las funciones y asignarlas a un template

#funcion index, toma una peticion, retorna cuerpo en ruta
def Index(request):
    p=Product.objects.all()
    return render(request, 'core/index.html', {"produc":p})

def Confirm(request):
    return render(request, 'core/confirm.html')

def ToKitchen(request):
    comd = Comanda()
    if request.session["carrito"].items:
        for key, value in request.session["carrito"].items():
            article = Article()
            article.cod=value["nombre"]
            article.name=value["nombre"]
            article.cantidad=value["cantidad"]
            article.total=value["acumulado"]
            article.save()
            comd.save()
            comd.article.add(article)
            comd.save()
        comd.cooking=True
        comd.time_to_kitchen = timezone.now()
        comd.save()
        
        request.session["carrito"]={}
    else:
        print('no hay carirto')

    return redirect("Tienda")
      
def Kitchen(request):
    cmd = Comanda.objects.all()
    artcl = Article.objects.all()
    context={
        "cmd":cmd,
        "artcl":artcl,
    }
    return render(request, 'core/kitchen.html',context)

def KitchenAll(request):
    cmd = Comanda.objects.all()
    artcl = Article.objects.all()
    context={
        "cmd":cmd,
        "artcl":artcl,
    }
    return render(request, 'core/kitchenall.html',context)

def Ready(request,comd_id):
    cmd = Comanda.objects.get(id=comd_id)
    cmd.cooking=False
    cmd.finished=True
    cmd.time_finished= timezone.now()
    cmd.save()
    return redirect("Tienda")


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

def NewBowl(request):
    bf= BowlForm()
    context={
        "bf":bf
    }
    return render(request, 'core/newbowl.html',context)