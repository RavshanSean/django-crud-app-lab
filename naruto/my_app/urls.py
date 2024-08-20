from django.urls import path
from . import views # Import views to connect routes to view functions


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ninjas/', views.index, name='index'),
    path('ninjas/<int:ninja_id>/', views.ninja_detail, name='ninja-detail'),
    path('ninjas/create/', views.NinjaCreate.as_view(), name='ninja-create'),
    path('ninjas/<int:pk>/update/', views.NinjaUpdate.as_view(), name='ninja-update'),
    path('ninjas/<int:pk>/delete/', views.NinjaDelete.as_view(), name='ninja-delete'),
]
