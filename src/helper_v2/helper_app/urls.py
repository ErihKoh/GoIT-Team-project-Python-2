from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', views.RegisterPage.as_view(), name='register'),
    path('', views.HomeView.as_view(), name='home'),
    path('contacts_list', views.ContactsView.as_view(), name='contacts_list'),
    path('contact-add/', views.AddContact.as_view(), name='contact-add'),
    path('contact-delete/<int:pk>/',
         views.DeleteContact.as_view(), name='contact-delete'),
    path('contact-update/<int:pk>/',
         views.UpdateContact.as_view(), name='contact-update'),
    path('contact/<int:pk>/', views.ContactDetailView.as_view(), name='contact'),     
    path('notes/', views.NotesListView.as_view(), name='notes'),
    path('notes/note/<int:pk>/', views.NoteDetailView.as_view(), name='note'),
    path('notes/note-create', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/note-update/<int:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/note-delete/<int:pk>/', views.NoteDeleteView .as_view(), name='note-delete'),
    path('news', views.NewsView.as_view(), name='news'),
    path('files', views.FilesView.as_view(), name='files'),
    path('aboutUs', views.AboutView.as_view(), name='aboutUs'),
]
