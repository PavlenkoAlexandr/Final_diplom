from django.urls import path
from shops.views import ShopView

app_name = 'shops'
urlpatterns = [
    path('shops', ShopView.as_view(), name='shops'),
]