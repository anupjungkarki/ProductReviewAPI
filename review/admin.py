from django.contrib import admin
from .models import Company, Category, Comment, Product, ProductSize, ProductSite, Image
from django.contrib.auth.models import Group


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'updated')
    list_filter = ('category',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


@admin.register(ProductSite)
class ProductSiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product', 'company', 'productsize', 'price', 'url', 'updated']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'product', 'user', 'updated']


# To unregister The Model From The Admin Panel
admin.site.unregister(Group)

# To change The title Written in the Top Left Corner In Admin Panel
admin.site.site_header = 'Product Review Admin Panel'
