from django.urls import path
from products.views import PartnerUpdate, ProductInfoView

app_name = 'products'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('products', ProductInfoView.as_view(), name='shops'),
]
