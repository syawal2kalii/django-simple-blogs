from . import views
from django.urls import path
urlpatterns = [
    path('', views.home),
    # single parameter
    path('detail/<str:id_article>/', views.detail),
    # multi parameter
    path('detail/<str:id_article>/<int:users_id>/', views.details)
]
