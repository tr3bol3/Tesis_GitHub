from config.wsgi import *
from core.erp.models import *

# LISTAR

print(Estudiante.objects.all())

for i in Estudiante.objects.filter():
    print(i.ausencia_estudiante_set.count())
