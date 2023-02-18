from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('list', views.list_view, name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.detail_view, name='detail'),
]
