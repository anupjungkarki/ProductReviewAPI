from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer, ImageSerializer, MyTokenObtainPairSerializer
from .models import Product, Image
from rest_flex_fields import is_expanded
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    # Yo pailako Method
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Yo chai permit_list_expand without giving object id
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize', 'image']
    filterset_fields = ('category',)

    # This is Overwritten Method Which is Field Expansion on 'List' Views is used because only using expanded field in the serializer
    # can expand the single objects so we can use permit_list_expands and overriding methods to expand fields in all list of data.
    # Yesle chai List ma nai sabai data haru expand garchha tara pailako method le chai particular object ko id de paxi matra expand gartho.
    def get_queryset(self):
        queryset = Product.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'image'):
            queryset = queryset.prefetch_related('image')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_related('sites')

        if is_expanded(self.request, 'company'):
            queryset = queryset.prefetch_related('sites__company')

        if is_expanded(self.request, 'productsize'):
            queryset = queryset.prefetch_related('sites__productsize')

        return queryset


class ImageViewSet(FlexFieldsModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

