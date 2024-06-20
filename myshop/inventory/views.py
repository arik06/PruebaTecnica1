from rest_framework import viewsets
from .models import Product, Console, Accessory
from .serializers import ProductSerializer, ConsoleSerializer, AccessorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        sort = self.request.query_params.get('sort', None)
        filter = self.request.query_params.get('filter', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        platform = self.request.query_params.get('platform', None)
        condition = self.request.query_params.get('condition', None)

        if filter:
            queryset = queryset.filter(name__icontains=filter)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if platform:
            queryset = queryset.filter(platform=platform)
        if condition:
            queryset = queryset.filter(condition=condition)

        if sort:
            if sort == 'price-asc':
                queryset = queryset.order_by('price')
            elif sort == 'price-desc':
                queryset = queryset.order_by('-price')
            elif sort == 'date-asc':
                queryset = queryset.order_by('created_at')
            elif sort == 'date-desc':
                queryset = queryset.order_by('-created_at')

        return queryset

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer

    def get_queryset(self):
        queryset = Console.objects.all()
        sort = self.request.query_params.get('sort', None)
        filter = self.request.query_params.get('filter', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        type = self.request.query_params.get('type', None)

        if filter:
            queryset = queryset.filter(name__icontains=filter)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if type:
            queryset = queryset.filter(type=type)

        if sort:
            if sort == 'price-asc':
                queryset = queryset.order_by('price')
            elif sort == 'price-desc':
                queryset = queryset.order_by('-price')
            elif sort == 'date-asc':
                queryset = queryset.order_by('created_at')
            elif sort == 'date-desc':
                queryset = queryset.order_by('-created_at')

        return queryset

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

    def get_queryset(self):
        queryset = Accessory.objects.all()
        sort = self.request.query_params.get('sort', None)
        filter = self.request.query_params.get('filter', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        if filter:
            queryset = queryset.filter(name__icontains=filter)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if sort:
            if sort == 'price-asc':
                queryset = queryset.order_by('price')
            elif sort == 'price-desc':
                queryset = queryset.order_by('-price')
            elif sort == 'date-asc':
                queryset = queryset.order_by('created_at')
            elif sort == 'date-desc':
                queryset = queryset.order_by('-created_at')

        return queryset
