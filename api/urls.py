from django.urls import path

from .views import TodoViewSet

urlpatterns = [
    path('',TodoViewSet.as_view({'get': 'list', 'post': 'create','delete':'destroy','put':'update','patch':'partial_update'}),name='home_page'),
    path('<int:pk>/',TodoViewSet.as_view({'get': 'list', 'post': 'create','delete':'destroy','put':'update','patch':'partial_update'}),name='home_page'),
]
