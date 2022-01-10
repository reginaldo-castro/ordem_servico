from django.shortcuts import render
from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import ClienteForm
from .models import Cliente


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.all()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(
                Q(razao_social__icontains=search)
                | Q(bairro__icontains=search)
             )
        return qs