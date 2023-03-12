from django.urls import path
from .views import home, delete_img, post_img, update_note


urlpatterns = [
    path('', view=home, name='home'),
    path('post-img/', post_img, name='post'),
    path('delete-img/<int:id>', delete_img, name='delete'),
    path('update-note/<int:id>', update_note, name='update')
]