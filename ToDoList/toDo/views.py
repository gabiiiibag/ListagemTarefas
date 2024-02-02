from .models import toDo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date

class toDoListView(ListView):
    model = toDo
    template_name = 'toDo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['toDo_list'] = toDo.objects.all()
        return context

class toDoCreateView(CreateView):
    model = toDo
    template_name = 'toDo_form.html'
    fields = ["titulo","entrega"]
    success_url = reverse_lazy("toDo_list")

class toDoUpdateView(UpdateView):
    model = toDo
    template_name = 'toDo_form_update.html'
    fields = ["titulo", "entrega"]
    success_url = reverse_lazy("toDo_list")

class toDoDeleteView(DeleteView):
    model = toDo
    template_name = 'toDo_confirm_delete.html'
    success_url = reverse_lazy("toDo_list")

class toDoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(toDo, pk=pk)
        todo.completed()
        return redirect("toDo_list")