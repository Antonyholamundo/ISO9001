from django.core.management.base import BaseCommand
from auditorias.models import NormaReferencia, ProcesoSoftware, PlanAuditoria
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Crea datos de prueba para el sistema de auditorías'

    def handle(self, *args, **kwargs):
        # Crear Normas ISO 9001
        normas_data = [
            ('4.1', 'Comprensión de la organización y de su contexto'),
            ('4.2', 'Comprensión de las necesidades y expectativas de las partes interesadas'),
            ('5.1', 'Liderazgo y compromiso'),
            ('6.1', 'Acciones para abordar riesgos y oportunidades'),
            ('7.1', 'Recursos'),
            ('7.5', 'Información documentada'),
            ('8.1', 'Planificación y control operacional'),
            ('8.2', 'Requisitos para los productos y servicios'),
            ('8.3', 'Diseño y desarrollo de los productos y servicios'),
            ('8.4', 'Control de los procesos, productos y servicios suministrados externamente'),
            ('8.5', 'Producción y provisión del servicio'),
            ('8.6', 'Liberación de los productos y servicios'),
            ('9.1', 'Seguimiento, medición, análisis y evaluación'),
            ('9.2', 'Auditoría interna'),
            ('9.3', 'Revisión por la dirección'),
            ('10.1', 'Generalidades (Mejora)'),
            ('10.2', 'No conformidad y acción correctiva'),
        ]

        for codigo, titulo in normas_data:
            NormaReferencia.objects.get_or_create(
                codigo=codigo,
                defaults={'titulo': titulo}
            )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Creadas {len(normas_data)} normas ISO 9001'))

        # Crear Procesos de Software
        procesos_data = [
            ('Gestión de Requisitos', 'Product Owner'),
            ('Diseño y Arquitectura', 'Arquitecto de Software'),
            ('Desarrollo de Código', 'Tech Lead'),
            ('Revisión de Código (Code Review)', 'Tech Lead'),
            ('Pruebas Unitarias', 'QA Lead'),
            ('Pruebas de Integración', 'QA Lead'),
            ('Despliegue (Deployment)', 'DevOps Lead'),
            ('Gestión de Configuración', 'DevOps Lead'),
            ('Documentación Técnica', 'Tech Writer'),
            ('Control de Versiones', 'Tech Lead'),
        ]

        for nombre, responsable in procesos_data:
            ProcesoSoftware.objects.get_or_create(
                nombre=nombre,
                defaults={'responsable': responsable}
            )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Creados {len(procesos_data)} procesos de software'))

        # Crear Planes de Auditoría
        planes_data = [
            ('Plan de Auditoría Q1 2025', date(2025, 1, 1), date(2025, 3, 31), 
             'Auditoría del primer trimestre enfocada en procesos de desarrollo'),
            ('Plan de Auditoría Q2 2025', date(2025, 4, 1), date(2025, 6, 30),
             'Auditoría del segundo trimestre enfocada en calidad y testing'),
            ('Auditoría de Certificación ISO 9001', date(2025, 11, 1), date(2025, 11, 30),
             'Auditoría de certificación para renovación ISO 9001:2015'),
        ]

        for titulo, inicio, fin, objetivo in planes_data:
            PlanAuditoria.objects.get_or_create(
                titulo=titulo,
                defaults={
                    'fecha_inicio': inicio,
                    'fecha_fin': fin,
                    'objetivo': objetivo,
                    'alcance': 'Todos los procesos de desarrollo de software'
                }
            )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Creados {len(planes_data)} planes de auditoría'))
        self.stdout.write(self.style.SUCCESS('\n¡Datos de prueba creados exitosamente! 🎉'))
