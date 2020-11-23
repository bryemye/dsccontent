from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentList.as_view()),
    path('edit/<int:content_id>', views.editContent, name='edit'),
    path('new', views.newDatabaseEntry, name='newDatabaseEntry'),
    path('edit/<int:content_id>/editDatabaseEntry', views.editDatabaseEntry, name='editDatabaseEntry'),

]
