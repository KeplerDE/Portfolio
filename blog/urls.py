from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),
]


