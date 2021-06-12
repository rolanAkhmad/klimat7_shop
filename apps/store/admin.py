from django.contrib import admin
from .models import Category, Product, ProductGalery

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductGalery

class MyCustomizationToFKWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        return self.model.objects.get_or_create(title = value)[0] if value else None

# class ProductGalleryWidget(ForeignKeyWidget):
#     def clean(self, value, row=None, *args, **kwargs):
#         return self.model.object

class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=MyCustomizationToFKWidget(Category, 'title'))
    # image = fields.Field(column_name='images', attribute='images', widget =)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'category', 'manufacturer', 'price', 'description', 'detail_description')
        export_order = ('id', 'title', 'slug', 'category', 'price', 'manufacturer',)


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
    inlines = [GalleryInline,]
    list_display = ('id', 'title', 'slug', 'category', 'manufacturer', 'price', 'in_stock')
    list_display_links = ('title', 'category',)
    list_filter = ('category', 'manufacturer','in_stock')
    search_fields = ('title', 'category__name', 'manufacturer')

    fieldsets = (
        ('Основное', {
            'fields': ('title','slug','category','price','in_stock','manufacturer')
        }),
        ('Описание', {
            'fields': ('short_description','description', 'specifications')
        }),
    )
    
admin.site.register(Category)
