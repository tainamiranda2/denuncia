
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  login_required(views.denunciaList), name="denuncia_list"),
    path('denuncia/<int:id>',  login_required(views.denunciaView), name="denuncia_view"),
    path('denuncia/add',  login_required(views.denunciaAdd), name="denuncia_add"),
    path('denuncia/edit/<int:id>',  login_required(views.denunciaEdit), name="denuncia_edit"),
    path('denuncia/delete/<int:id>', login_required(views.denunciaDelete), name="denuncia_delete"),
    path('accounts/', include('django.contrib.auth.urls')),

]

