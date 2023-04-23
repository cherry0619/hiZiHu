from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('archives/',views.archives,name="archives"),
    path('categories/',views.categories,name='categories'),
    path('tag/',views.tag,name='tag'),
]