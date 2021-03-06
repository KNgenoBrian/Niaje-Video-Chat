from django.urls import path
from . import views

app_name = 'videochat'

urlpatterns = [
    path('', views.lobby, name="lobby"),
    path('room/', views.room, name="room"),
    path('get_token/', views.getToken),

    # path('create_room/', views.createRoom),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]
