from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('journal/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('journal/new/', views.journal_new, name='journal_new'), 
    path('journal/<int:pk>/edit/', views.journal_edit, name='journal_edit'),
    path('drafts/', views.journal_draft_list, name='journal_draft_list'),
    path('journal/<pk>/publish/', views.journal_publish, name='journal_publish'),
    path('journal/<pk>/remove/', views.journal_remove, name='journal_remove'),
    path('journal/<int:pk>/comment/', views.add_comment_to_journal, name='add_comment_to_journal'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('signup/', views.signup, name='signup'),



]