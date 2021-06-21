from rest_framework.generics import ListAPIView
from shops.models import Shop
from shops.serializers import ShopSerializer


class ShopView(ListAPIView):
    """
    Класс для просмотра списка магазинов
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer
