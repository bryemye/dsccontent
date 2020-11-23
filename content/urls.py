from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContentList.as_view()),
    path('edit/<int:content_id>', views.editContent, name='edit'),
    path('edit/<int:content_id>/new', views.newDatabaseEntry, name='new'),
    path('edit/<int:content_id>/editDatabaseEntry', views.editDatabaseEntry, name='editDatabaseEntry'),
    path('edit/<int:content_id>/newDatabaseEntry', views.newDatabaseEntry, name='newDatabaseEntry'),
]
