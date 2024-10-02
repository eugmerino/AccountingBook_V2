from django.urls import path,include
from . import views

# parametro '' se muestra en el navegador
# parametro name= se ocupa en los redirect
urlpatterns = [
    path('',views.start),
    path('login/',views.loginView, name="login"),
    path('dashboard/',views.dashboard, name="dashboard")
]