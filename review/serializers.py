from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product, Category, Company, ProductSize, ProductSite, Comment, Image
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'products': ('review.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('review.CategorySerializer', {'many': True}),
            'sites': ('review.ProductSiteSerializer', {'many': True}),
            'comments': ('review.CommentSerializer', {'many': True}),
            'image': ('review.ImageSerializer', {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'review.CategorySerializer',
            'productsize': 'review.ProductSizeSerializer',
            'company': 'review.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'review.CategorySerializer',
            'user': 'review.UserSerializer'
        }


class ImageSerializer(FlexFieldsModelSerializer):
    # From The Globally Setting
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    # From Locally Register
    # image = VersatileImageFieldSerializer(
    #     sizes=[
    #         ('full_size', 'url'),
    #         ('thumbnail', 'thumbnail__100x100'),
    #         ('medium_square_crop', 'crop__400x400'),
    #         ('small_square_crop', 'crop__50x50'),
    #     ]
    # )

    class Meta:
        model = Image
        fields = ['id', 'name', 'image']

# For Add Custom Claim Payload
# Default payload includes the user_id. You can add any information you want, you just have to modify the claim.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
