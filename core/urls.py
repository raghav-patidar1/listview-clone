from django.urls import path
from . import views


urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductList().get_response),
]