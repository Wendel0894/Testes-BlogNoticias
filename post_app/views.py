
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia, Comentario
from django.urls import reverse_lazy

# Create your views here.

class HomePage(ListView): #Pagina inicial
    model = Noticia
    template_name = 'post_app/home.html'
    context_object_name = 'notices_list'

class HealthNewsPage(ListView): #Visão com noticias sobre a area da saúde
    model = Noticia
    template_name = 'post_app/saude.html'
    context_object_name = 'notices_list'

class TechnologyNewsPage(ListView): #Visão com noticias sobre tecnologia
    model = Noticia
    template_name = 'post_app/tecnologia.html'
    context_object_name = 'notices_list'

class ScienceNewsPage(ListView): #Visão com noticias sobre ciência
    model = Noticia
    template_name = 'post_app/ciencia.html'
    context_object_name = 'notices_list'

class SportsNewsPage(ListView): #Visão com noticias sobre esportes
    model = Noticia
    template_name = 'post_app/esports.html'
    context_object_name = 'notices_list'

class BlogManageView(LoginRequiredMixin, ListView): #Visão com todas as noticias cadastradas no sistema
    model = Noticia
    template_name = 'post_app/manage_notices.html'
    context_object_name = 'notices_list'

class DetailNoticeView(LoginRequiredMixin, DetailView): #Visão com os detalhes de uma notícia especifica
    model = Noticia
    template_name = 'post_app/detail_notice.html'
    context_object_name = 'noticia'

class AddNoticeView(CreateView): #Visão para adicionar uma nova notícia
    model = Noticia
    template_name = 'post_app/add_notice.html'
    fields = ['titulo', 'assunto', 'texto', 'header_image']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

class DeleteNoticeView(LoginRequiredMixin, DeleteView): #Visão para deletar uma notícia especifica
    model = Noticia
    template_name = 'post_app/delete_notice.html'
    success_url = reverse_lazy('manage_notices')

class EditNoticeView(LoginRequiredMixin, UpdateView): #Visão para editar as informações de uma noticia !
    model = Noticia
    template_name = 'post_app/edit_notice.html'
    fields = '__all__'

class ManageCommentsView(LoginRequiredMixin, ListView): #Visão com todos os comentários que foram feitos em todas as notícias
    model = Comentario
    template_name = 'post_app/manage_comments.html'
    context_object_name = 'comentarios'

class CreateAdminCommentView(LoginRequiredMixin, CreateView): #Visão para adicionar um comentário a uma determinada notícia
    model = Comentario
    template_name = 'post_app/add_comment.html'
    fields = '__all__'


class DetailCommentView(LoginRequiredMixin, DetailView): #Visão com os detalhes de um comentário
    model = Comentario
    template_name = 'post_app/detail_comment.html'
    context_object_name = 'comentario'

class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Comentario
    template_name = 'post_app/edit_comment.html'
    fields = '__all__'

class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'post_app/delete_comment.html'
    success_url = reverse_lazy('manage_comments')

class VisualizarNoticeView(DetailView):
    template_name = 'post_app/visualizar_noticia.html'
    model = Noticia
    context_object_name = 'noticia'

class ComentarNoticia(LoginRequiredMixin, CreateView):
    model = Comentario
    template_name = 'post_app/add_comment.html'
    fields = ['opiniao']

    def form_valid(self, form):
        form.instance.cod_noticia_id = self.kwargs['pk']
        form.instance.cod_usuario = self.request.user
        return super().form_valid(form)




