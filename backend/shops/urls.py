from django.urls import path
from shops.views import ShopView, PartnerState

app_name = 'shops'
urlpatterns = [
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('shops', ShopView.as_view(), name='shops'),
]