from django.shortcuts import render
from django.template import loader
from perfuApp.models import*
from perfuApp.forms import*
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.



def inicio (request):
    
    return render(request, 'inicio.html')


@login_required
def Masculinas(request):

      if request.method == "POST":

            miFormulario = FormMasc(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  masc = MasculinaS(nombre=informacion['nombre'] ,fragancia=informacion["fragancia"],tamanio=informacion["tamanio"],autor=informacion["autor"],precio=informacion["precio"],fecha=informacion["fecha"],detalles=informacion["detalles"])
                  masc.save()
                  return render(request, "inicio.html")
      else:
            miFormulario = FormMasc()

            return render(request, "masculinas.html", {"miFormulario": miFormulario})

@login_required
def leerMasc(request):

      masc = MasculinaS.objects.all() #trae todos los profesores

      contexto= {"masc":masc} 

      return render(request, "lmasc.html",contexto)




def eliminarMasc(request, perfume_nombre):
 
    masc = MasculinaS.objects.get(nombre=perfume_nombre)
    masc.delete()
 
    # vuelvo al menú
    masc = MasculinaS.objects.all()  # trae todos los profesores
 
    contexto = {"masc": masc}
 
    return render(request, "lmasc.html", contexto)


def editarMasc(request, perfume_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    masc = MasculinaS.objects.get(nombre=perfume_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = FormMasc(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            masc.nombre = informacion['nombre']
            masc.fragancia = informacion['fragancia']
            masc.tamanio = informacion['tamanio']
            masc.autor = informacion['autor']
            masc.precio = informacion ['precio']
            masc.fecha = informacion ['fecha']
            masc.detalles = informacion ['detalles']

            masc.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "lmasc.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = FormMasc(initial={'nombre': masc.nombre, 'fragancia': masc.fragancia,'tamanio': masc.tamanio, 'autor': masc.autor, 'precio':masc.precio, 'fecha':masc.fecha,'detalles':masc.detalles})

    # Voy al html que me permite editar
    return render(request, "edmasc.html", {"miFormulario": miFormulario, "perfume_nombre": perfume_nombre})




@login_required
def Femeninas(request):

      if request.method == "POST":

            miFormulario = FormFem(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  fem = FemeninaS(nombre=informacion['nombre'] ,fragancia=informacion["fragancia"],tamanio=informacion["tamanio"],autor=informacion["autor"],precio=informacion["precio"],fecha=informacion["fecha"],detalles=informacion["detalles"])
                  fem.save()
                  return render(request, "inicio.html")
      else:
            miFormulario = FormFem()

            return render(request, "femeninas.html", {"miFormulario": miFormulario})

@login_required
def leerFem(request):

      fem = FemeninaS.objects.all() #trae todos los profesores

      contexto= {"fem":fem} 

      return render(request, "lfem.html",contexto)

def eliminarFem(request, perfume_nombre):

      fem=FemeninaS.objects.get(nombre=perfume_nombre)
      fem.delete()


      fem=FemeninaS.objects.all()
      contexto= {'fem':fem}

      return render(request, "lfem.html", contexto)


def editarFem(request, perfume_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    fem = FemeninaS.objects.get(nombre=perfume_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = FormFem(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            fem.nombre = informacion['nombre']
            fem.fragancia = informacion['fragancia']
            fem.tamanio = informacion['tamanio']
            fem.autor = informacion['autor']
            fem.precio = informacion ['precio']
            fem.fecha = informacion ['fecha']
            fem.detalles = informacion ['detalles']

            fem.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "lfem.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = FormMasc(initial={'nombre': fem.nombre, 'fragancia': fem.fragancia,'tamanio': fem.tamanio, 'autor': fem.autor, 'precio':fem.precio, 'fecha':fem.fecha,'detalles':fem.detalles})

    # Voy al html que me permite editar
    return render(request, "edfem.html", {"miFormulario": miFormulario, "perfume_nombre": perfume_nombre})





@login_required
def Infantiles(request):

      if request.method == "POST":

            miFormulario = FormInf(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  inf = InfantileS(nombre=informacion['nombre'] ,fragancia=informacion["fragancia"],tamanio=informacion["tamanio"],autor=informacion["autor"],precio=informacion["precio"],fecha=informacion["fecha"],detalles=informacion["detalles"])
                  inf.save()
                  return render(request, "inicio.html")
      else:
            miFormulario = FormInf()

            return render(request, "infantiles.html", {"miFormulario": miFormulario})



@login_required
def leerInf(request):

      inf = InfantileS.objects.all() #trae todos los profesores

      contexto= {"inf":inf} 

      return render(request, "linf.html",contexto)


def eliminarInf(request, perfume_nombre):

      inf=InfantileS.objects.get(nombre=perfume_nombre)
      inf.delete()

      inf= InfantileS.objects.all()
      contexto= {'inf':inf}

      return render(request, 'linf.html', contexto)



def editarInf(request, perfume_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    inf = InfantileS.objects.get(nombre=perfume_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = FormFem(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            inf.nombre = informacion['nombre']
            inf.fragancia = informacion['fragancia']
            inf.tamanio = informacion['tamanio']
            inf.autor = informacion['autor']
            inf.precio = informacion ['precio']
            inf.fecha = informacion ['fecha']
            inf.detalles = informacion ['detalles']

            inf.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "corregido_exito.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = FormMasc(initial={'nombre': inf.nombre, 'fragancia': inf.fragancia,'tamanio': inf.tamanio, 'autor': inf.autor, 'precio':inf.precio, 'fecha':inf.fecha,'detalles':inf.detalles})

    # Voy al html que me permite editar
    return render(request, "edinf.html", {"miFormulario": miFormulario, "perfume_nombre": perfume_nombre})





#--------------------LOGIN----------------------------------------------------#
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})



#VISTA DE REGISTRO

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register(request):

      if request.method == 'POST':

            # form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"registro_ok.html" , )

      else:
            # form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})





from perfuApp.forms import FormInf, FormFem, FormMasc, UserEditForm

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
           
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




def busquedamasc(request):
      return render(request, 'busqueda_masc.html')

def buscar(request):
      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            masculinas = MasculinaS.objects.filter(nombre__icontains=nombre)

            return render(request, "busqueda_masc.html", {"masculinas":masculinas, "nombre":nombre})

      else: 
             respuesta = "No enviaste datos"
                        
      return HttpResponse(respuesta)
    
def busquedafem(request):
      return render(request, 'busqueda_fem.html')

def buscarf(request):
      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            femeninas = FemeninaS.objects.filter(nombre__icontains=nombre)

            return render(request, "busqueda_fem.html", {"femeninas":femeninas, "nombre":nombre})

      else: 
             respuesta = "No enviaste datos"
                        
      return HttpResponse(respuesta)








