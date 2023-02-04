from django import forms
from django.conf import settings

# Create your forms here.


class FormMasc(forms.Form):
    
      
      nombre=forms.CharField(max_length=50)
      fragancia=forms.CharField(max_length=200)
      tamanio = forms.CharField(max_length=10)
      autor= forms.CharField(max_length=30)
      precio=forms.CharField(max_length=30)
      fecha=forms.DateField()
      detalles=forms.CharField(max_length=200)
    
class FormFem(forms.Form):
    
      
      nombre=forms.CharField(max_length=50)
      fragancia=forms.CharField(max_length=200)
      tamanio = forms.CharField(max_length=10)
      autor= forms.CharField(max_length=30)
      precio=forms.CharField(max_length=30)
      fecha=forms.DateField()
      detalles=forms.CharField(max_length=200)


class FormInf(forms.Form):
    
      
      nombre=forms.CharField(max_length=50)
      fragancia=forms.CharField(max_length=200)
      tamanio = forms.CharField(max_length=10)
      autor= forms.CharField(max_length=30)
      precio=forms.CharField(max_length=30)
      fecha=forms.DateField()
      detalles=forms.CharField(max_length=200)



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    
    nombre = forms.CharField(label='Nombre',)
    apellido= forms.CharField(label='Apellido',)
    dni= forms.CharField(label='D.N.I',)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    nombre = forms.CharField(label='Nombre',)
 
    class Meta:
        model = User
        fields = ['nombre', 'apellido','dni','username', 'email', 'password1', 'password2',]
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

#------------------------------EDITAR USUARIO----------------------------#
class UserEditForm(UserCreationForm):

    # Obligatorios
    nombre = forms.CharField(label='Nombre',)
    apellido= forms.CharField(label='Apellido',)
    dni= forms.CharField(label='D.N.I',)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    nombre = forms.CharField(label='Nombre',)
 
    class Meta:
        model = User
        fields = ['nombre', 'apellido','dni','username', 'email', 'password1', 'password2',]
