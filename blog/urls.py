from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', views.list_view, name='list'),
    path('', views.PostListView.as_view(), name='list'),
    # path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.detail_view, name='detail'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('share-post/<int:pk>', views.SharePost.as_view(), name='share')
]
