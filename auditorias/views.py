from django.shortcuts import render, redirect, get_object_or_404
from .models import Auditoria, Hallazgo
from .forms import AuditoriaForm, HallazgoForm

def dashboard(request):
    """
    Main dashboard view showing audit status and recent findings.
    """
    # Metrics
    total_auditorias = Auditoria.objects.count()
    auditorias_programadas = Auditoria.objects.filter(estado='PROGRAMADA').count()
    total_hallazgos = Hallazgo.objects.count()
    nc_mayores = Hallazgo.objects.filter(tipo='NC_MAYOR').count()

    auditorias_recientes = Auditoria.objects.all().order_by('-fecha_programada')[:5]
    hallazgos_recientes = Hallazgo.objects.all().order_by('-fecha_reporte')[:5]
    
    context = {
        'total_auditorias': total_auditorias,
        'auditorias_programadas': auditorias_programadas,
        'total_hallazgos': total_hallazgos,
        'nc_mayores': nc_mayores,
        'auditorias': auditorias_recientes,
        'hallazgos': hallazgos_recientes,
    }
    return render(request, 'auditorias/dashboard.html', context)

def lista_auditorias(request):
    auditorias = Auditoria.objects.all().order_by('-fecha_programada')
    return render(request, 'auditorias/auditoria_list.html', {'auditorias': auditorias})

def lista_hallazgos(request):
    hallazgos = Hallazgo.objects.all().order_by('-fecha_reporte')
    return render(request, 'auditorias/hallazgo_list.html', {'hallazgos': hallazgos})

def crear_auditoria(request):
    if request.method == 'POST':
        form = AuditoriaForm(request.POST)
        if form.is_valid():
            auditoria = form.save()
            return redirect('detalle_auditoria', pk=auditoria.pk)
    else:
        form = AuditoriaForm()
    return render(request, 'auditorias/auditoria_form.html', {'form': form})

def editar_auditoria(request, pk):
    auditoria = get_object_or_404(Auditoria, pk=pk)
    if request.method == 'POST':
        form = AuditoriaForm(request.POST, instance=auditoria)
        if form.is_valid():
            form.save()
            return redirect('detalle_auditoria', pk=pk)
    else:
        form = AuditoriaForm(instance=auditoria)
    return render(request, 'auditorias/auditoria_form.html', {'form': form, 'titulo': 'Editar Auditoría'})

def detalle_auditoria(request, pk):
    auditoria = get_object_or_404(Auditoria, pk=pk)
    return render(request, 'auditorias/auditoria_detail.html', {'auditoria': auditoria})

def reportar_hallazgo(request, pk):
    auditoria = get_object_or_404(Auditoria, pk=pk)
    if request.method == 'POST':
        form = HallazgoForm(request.POST)
        if form.is_valid():
            hallazgo = form.save(commit=False)
            hallazgo.auditoria = auditoria
            hallazgo.save()
            return redirect('detalle_auditoria', pk=pk)
    else:
        form = HallazgoForm()
    return render(request, 'auditorias/hallazgo_form.html', {'form': form, 'auditoria': auditoria})

def editar_hallazgo(request, pk):
    hallazgo = get_object_or_404(Hallazgo, pk=pk)
    if request.method == 'POST':
        form = HallazgoForm(request.POST, instance=hallazgo)
        if form.is_valid():
            form.save()
            return redirect('detalle_auditoria', pk=hallazgo.auditoria.pk)
    else:
        form = HallazgoForm(instance=hallazgo)
    return render(request, 'auditorias/hallazgo_form.html', {'form': form, 'auditoria': hallazgo.auditoria, 'titulo': 'Editar Hallazgo'})
