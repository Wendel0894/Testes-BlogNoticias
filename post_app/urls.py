
from django.urls import path
from .views import (
    HomePage,
    HealthNewsPage,
    TechnologyNewsPage,
    ScienceNewsPage,
    SportsNewsPage,
    BlogManageView,
    DetailNoticeView,
    AddNoticeView,
    DeleteNoticeView,
    EditNoticeView,
    ManageCommentsView,
    CreateAdminCommentView,
    DetailCommentView,
    EditCommentView,
    DeleteCommentView,
    VisualizarNoticeView,
    ComentarNoticia

)

urlpatterns = [
    path('', HomePage.as_view(), name = 'Home'),
    path('Saude/', HealthNewsPage.as_view(), name = 'Saude'),
    path('Tecnologia/', TechnologyNewsPage.as_view(), name = 'Tecnologia'),
    path('Ciencia/', ScienceNewsPage.as_view(), name = 'Ciência'),
    path('Esportes/', SportsNewsPage.as_view(), name = 'Esportes'),
    path('Gerenciar/Noticias/', BlogManageView.as_view(), name = 'manage_notices'),
    path('Gerenciar/Noticia/<int:pk>/', DetailNoticeView.as_view(), name = 'detail_notice'),
    path('Gerenciar/Noticia/Adicionar/', AddNoticeView.as_view(), name = 'add_notice'),
    path('Gerenciar/Noticia/Remover/<int:pk>/', DeleteNoticeView.as_view(), name = 'delete_notice'),
    path('Gerenciar/Noticia/Editar/<int:pk>/', EditNoticeView.as_view(), name = 'edit_notice'),
    path('Gerenciar/Comentarios/', ManageCommentsView.as_view(), name = 'manage_comments'),
    path('Gerenciar/Comentario/Adicionar/', CreateAdminCommentView.as_view(), name = 'add_comment'),
    path('Gerenciar/Comentario/<int:pk>/', DetailCommentView.as_view(), name = 'detail_comment'),
    path('Gerenciar/Comentario/Editar/<int:pk>/', EditCommentView.as_view(), name = 'edit_comment'),
    path('Gerenciar/Comentario/Deletar/<int:pk>/', DeleteCommentView.as_view(), name = 'delete_comment'),
    path('Noticia/<int:pk>/', VisualizarNoticeView.as_view(), name = 'visualizar_noticia'),
    path('Noticia/<int:pk>/Comentar', ComentarNoticia.as_view(), name = 'comentar_noticia')
]
