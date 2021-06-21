from django.urls import path
from products.views import ProductInfoView

app_name = 'products'
urlpatterns = [
    path('products', ProductInfoView.as_view(), name='products'),
]
