from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MasculinaS)

admin.site.register(FemeninaS)

admin.site.register(InfantileS)

admin.site.register(Avatar)



admin.site.site_header = 'Mi aplicacion'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Admnistración'
# Register your models here.
