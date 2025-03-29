
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.denunciaList, name="denuncia_list"),
    path('denuncia/<int:id>', views.denunciaView, name="denuncia_view"),
    path('denuncia/add', views.denunciaAdd, name="denuncia_add"),
    path('denuncia/edit/<int:id>', views.denunciaEdit, name="denuncia_edit"),
    path('denuncia/delete/<int:id>', views.denunciaDelete, name="denuncia_delete"),

]

