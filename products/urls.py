from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('', views.ListCreateProductApiView.as_view(), name='get_post_products'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProductAPIView.as_view(), name='get_delete_update_products')
]