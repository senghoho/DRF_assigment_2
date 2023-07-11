from django.urls import path
from .views import *
from . import views

app_name="music"
urlpatterns = [
    path('', views.album_list_create),
    path('<int:album_id>/track', views.track_list_create),
    path('album/<int:album_id>',views.album_detail_update_delete),
    path('track/<int:track_id>',views.track_detail_update_delete),
    path('tags/<str:tag_name>', views.find_tag),
    path('tags2', views.find_tag2),
]