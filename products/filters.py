from django_filters import rest_framework as filters
from .models import Product


# We create filters for each field we want to be able to filter on
class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    sku = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.NumberFilter()
    created_at__gt = filters.NumberFilter(field_name='created_at', lookup_expr='gt')
    created_at__lt = filters.NumberFilter(field_name='created_at', lookup_expr='lt')
    creator__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'sku', 'created_at', 'created_at__gt', 'created_at__lt', 'creator__username']