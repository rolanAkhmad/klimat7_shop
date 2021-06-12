from django.db import models
from django.shortcuts import reverse
from io import BytesIO
from django.core.files import File
from PIL import Image

from ckeditor.fields import RichTextField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_company_count(self):
        company_list = Product.objects.filter(category_id=self.id)
        return company_list.count()

class Product(models.Model):
    class Meta:
        ordering = ('-date_added', )
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Наименование", max_length=255)
    slug = models.SlugField(verbose_name="Артикул", max_length=255)
    short_description = RichTextField(verbose_name="Краткое описание",blank=True, null=True)
    description = RichTextField(verbose_name="Описание",blank=True, null=True)
    specifications = RichTextField(verbose_name="Характеристики", blank=True, null=True)
    price = models.FloatField(verbose_name="Цена")
    date_added = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
    in_stock = models.BooleanField(verbose_name="В наличии", default=True)
    manufacturer = models.CharField(verbose_name="Производитель", max_length=100, blank=True, null=True)

    def get_super_title(self):
        return self.title + ' ' + self.category.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"category_slug": self.category.slug, 'slug': self.slug})

    def get_main_image(self):
        try:
            product_galery_list = self.images.all()
            return product_galery_list[0].thumbnail.url
        except:
            return "/static/images/no_photo.jpg"

    def get_image_gallery(self):
        try:
            return self.images.all()
        except: 
            return []

class ProductGalery(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name='Изображение', upload_to='media', default="images/banner.jpg")
    thumbnail = ImageSpecField(source="image", processors=[ResizeToFill(200,200)])
    medium_image = ImageSpecField(source='image', processors=[ResizeToFill(500,500)])
    is_main = models.BooleanField(verbose_name="Главное изображение", default=False)