from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('crear/', views.crear_auditoria, name='crear_auditoria'),
    path('lista/', views.lista_auditorias, name='lista_auditorias'),
    path('hallazgos/', views.lista_hallazgos, name='lista_hallazgos'),
    path('<int:pk>/', views.detalle_auditoria, name='detalle_auditoria'),
    path('<int:pk>/editar/', views.editar_auditoria, name='editar_auditoria'),
    path('<int:pk>/hallazgo/', views.reportar_hallazgo, name='reportar_hallazgo'),
    path('hallazgo/<int:pk>/editar/', views.editar_hallazgo, name='editar_hallazgo'),
]
