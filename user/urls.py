from django.urls import path,include
from . import views

# parametro '' se muestra en el navegador
# parametro name= se ocupa en los redirect
urlpatterns = [
    path('empleados/',views.userMainView, name="empleados")
]