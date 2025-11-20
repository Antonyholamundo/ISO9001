from django.db import models
from django.utils import timezone

class NormaReferencia(models.Model):
    """
    Represents the standard clauses (e.g., ISO 9001:2015 Clause 8.3).
    """
    codigo = models.CharField(max_length=50, unique=True, help_text="e.g., '8.3'")
    titulo = models.CharField(max_length=255, help_text="e.g., 'Design and development of products and services'")
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"

class ProcesoSoftware(models.Model):
    """
    Represents a software development process to be audited.
    """
    nombre = models.CharField(max_length=100, unique=True, help_text="e.g., 'Code Review', 'Deployment'")
    responsable = models.CharField(max_length=100, help_text="Person or role responsible")
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class PlanAuditoria(models.Model):
    """
    High-level plan for an audit cycle.
    """
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    objetivo = models.TextField()
    alcance = models.TextField()

    def __str__(self):
        return self.titulo

class Auditoria(models.Model):
    """
    A specific audit instance linking a process to a plan.
    """
    ESTADOS = [
        ('PROGRAMADA', 'Programada'),
        ('EN_CURSO', 'En Curso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    plan = models.ForeignKey(PlanAuditoria, on_delete=models.CASCADE, related_name='auditorias')
    proceso = models.ForeignKey(ProcesoSoftware, on_delete=models.CASCADE)
    normas = models.ManyToManyField(NormaReferencia, related_name='auditorias')
    auditor_lider = models.CharField(max_length=100)
    fecha_programada = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PROGRAMADA')
    
    def __str__(self):
        return f"Auditoría de {self.proceso} ({self.fecha_programada})"

class Hallazgo(models.Model):
    """
    Findings discovered during the audit.
    """
    TIPOS = [
        ('NC_MAYOR', 'No Conformidad Mayor'),
        ('NC_MENOR', 'No Conformidad Menor'),
        ('OBSERVACION', 'Observación'),
        ('OPORTUNIDAD', 'Oportunidad de Mejora'),
    ]

    auditoria = models.ForeignKey(Auditoria, on_delete=models.CASCADE, related_name='hallazgos')
    norma_relacionada = models.ForeignKey(NormaReferencia, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    evidencia_objetiva = models.TextField(help_text="Description of the evidence found")
    fecha_reporte = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.auditoria}"

class Evidencia(models.Model):
    """
    Attachments or links serving as evidence for a finding.
    """
    hallazgo = models.ForeignKey(Hallazgo, on_delete=models.CASCADE, related_name='evidencias')
    archivo = models.FileField(upload_to='evidencias/', blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    url_externa = models.URLField(blank=True, null=True, help_text="Link to external system (e.g., Jira, GitHub)")

    def __str__(self):
        return self.descripcion
