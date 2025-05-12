from django.urls import path
from .views import LoginUsuarioView, LogoutUsuarioView
from .views import CategoriaListView, CategoriaCreateView, ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nova/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_edit'),
    path('produtos/<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='produto_delete'),
]