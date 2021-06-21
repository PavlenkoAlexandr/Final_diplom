from django.urls import path
from partner.views import PartnerOrders, PartnerUpdate, PartnerState

app_name = 'orders'
urlpatterns = [
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),

]