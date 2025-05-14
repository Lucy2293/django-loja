from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class LoginUsuarioView(LoginView):
    template_name = 'login.html'

class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy('login')

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria, Produto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages  # <-- IMPORTANTE

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria_list.html'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome']
    success_url = reverse_lazy('categoria_list')
    template_name = 'form.html'

# Mesma lógica para Produto
class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    success_url = reverse_lazy('produto_list')
    template_name = 'form.html'
   
class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome','preco', 'categoria']  # Altere conforme seu modelo
    template_name = 'form.html'
    success_url = reverse_lazy('produto_list')  # Altere para onde redirecionar após salvar


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('produto_list')

    # Este método é chamado quando o usuário confirma a exclusão
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()  # pega o produto que será deletado
        messages.success(request, f'Produto "{obj.nome}" foi excluído com sucesso.')  # adiciona a mensagem
        return super().delete(request, *args, **kwargs)  # continua com o processo normal de exclusão

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nome']
    success_url = reverse_lazy('categoria_list')
    template_name = 'form.html'  # reutilizando o mesmo template da criação

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    template_name = 'confirm_delete.html'  # você vai criar esse template

