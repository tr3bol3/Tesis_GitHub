from config.wsgi import *
from core.erp.models import Type

# Listar
query = Type.objects.all()
print(query)

# Insertar

#t = Type()
#t.name = "No Becado"
#t.save()

# Edicion

#try:
#    t = Type.objects.get(pk = 2)
#    t.name = 'Presidente'
#    t.save()
#except Exception as e:
#    print(e)

# Eliminacion

#try:
#    t = Type.objects.get(id=2)
#    t.delete()
#except Exception as e:
#    print(e)
