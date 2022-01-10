from django.shortcuts import render
from .models import OrdemServico
from .forms import OrdemServicoForm

def ordem_servico_list(request):
    template_name = 'servico/ordem_servico_list.html'
    object_list = OrdemServico.objects.all()
    context = {
        'object_list':object_list
    }
    return render(request, template_name, context)


def ordem_servico_create(request):
    template_name = 'servico/ordem_servico_form.html'
    context = {'form': OrdemServicoForm}
    return render(request, template_name, context)


def ordem_servico_detail(request, pk):
    template_name = 'servico/ordem_servico_detail.html'
    obj = OrdemServico.objects.get(pk=pk)
    context = {
        'object': obj
    }
    return render(request, template_name, context)

def ordem_servico_update(request, pk):
    pass

def ordem_servico_delete(request, pk):
    pass

