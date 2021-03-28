from . import views
from django.urls import path
urlpatterns = [
    path('', views.home),
    path('detail/<str:id_article>/', views.detail)
]
