from django.urls import path
from perfuApp.views import *
from django.contrib.auth.views import LogoutView


urlpatterns =[
    path('',inicio, name = 'inicio'),
    path('masculinas', Masculinas,name='masculinas'),
    path('femeninas', Femeninas,name='femeninas'),
    path('infantiles', Infantiles,name='infantiles'),
    path('lmasc', leerMasc, name='leermasc'),
    path('emasc/<perfume_nombre>/', eliminarMasc, name='eliminarmasc'),
    path('edmasc/<perfume_nombre>/', editarMasc , name='editarmasc'),
    path('lfem', leerFem, name='leerfem'),
    path('efem/<perfume_nombre>/', eliminarFem, name='eliminarfem'),
    path('edfem/<perfume_nombre>/', editarFem , name='editarfem'),
    path('linf', leerInf, name='leerinf'),
    path('einf/<perfume_nombre>/', eliminarInf, name='eliminarinf'),
    path('edinf/<perfume_nombre>/', editarInf , name='editarinf'),
    path('login', login_request, name="login"),
    path('registro', register, name='registro'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarperfil', editarPerfil, name="editarperfil"), 
    path('buscarmasc/', busquedamasc, name='buscarmasc'),
    path('buscarfem/', busquedamasc, name='buscarfem'),
    path('buscar/', buscar),
    path('buscarf/', buscar),

    





]