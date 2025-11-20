from django.contrib import admin
from .models import NormaReferencia, ProcesoSoftware, PlanAuditoria, Auditoria, Hallazgo, Evidencia

@admin.register(NormaReferencia)
class NormaReferenciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo')
    search_fields = ('codigo', 'titulo')

@admin.register(ProcesoSoftware)
class ProcesoSoftwareAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'responsable')
    search_fields = ('nombre', 'responsable')

@admin.register(PlanAuditoria)
class PlanAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_inicio', 'fecha_fin')
    search_fields = ('titulo',)

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('proceso', 'plan', 'auditor_lider', 'fecha_programada', 'estado')
    list_filter = ('estado', 'fecha_programada')
    search_fields = ('auditor_lider', 'proceso__nombre')
    filter_horizontal = ('normas',)

@admin.register(Hallazgo)
class HallazgoAdmin(admin.ModelAdmin):
    list_display = ('auditoria', 'tipo', 'norma_relacionada', 'fecha_reporte')
    list_filter = ('tipo', 'fecha_reporte')
    search_fields = ('descripcion',)

@admin.register(Evidencia)
class EvidenciaAdmin(admin.ModelAdmin):
    list_display = ('hallazgo', 'descripcion')
    search_fields = ('descripcion',)
