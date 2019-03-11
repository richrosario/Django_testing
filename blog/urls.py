from django.urls import path
from . import views # . is current DIR

urlpatterns = [
    path('', views.home, name = 'blog-home'), #/blog
    path('about/', views.about, name = 'blog-about'), #/blog/about
    path('test/', views.test, name = 'blog-test'), #/blog/test
]