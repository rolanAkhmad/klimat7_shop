from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from apps.cart.views import checkout, checkout_success, cart
from apps.core.views import frontpage
from apps.store.views import product_detail, category_detail, product_list, search
from apps.userprofiles.views import login_signup

from apps.store.api import api_add_to_cart, api_remove_from_cart, api_cart_get_total_length

from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap

from django.views.static import serve
from django.urls import include, re_path

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [
    
    # Core
    path('', frontpage, name="index"),
    path('admin/', admin.site.urls),
    path('cart/', cart, name="cart"),
    path('shop/', product_list, name="shop"),
    path('search/', search, name="search"),
    path('checkout/', checkout, name="checkout"),
    path('checkout/success', checkout_success, name="checkout_success"),
    
    #Auth
    path('signup/', login_signup, name="login-signup"),
    path('login-signup/', login_signup, name="login-signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    #Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    
    # API
    path('api/add_to_cart/', api_add_to_cart, name="api_add_to_cart"),
    path('api/remove_from_cart/', api_remove_from_cart, name="api_remove_from_cart"),
    path('api/cart_get_total_length/', api_cart_get_total_length, name="api_cart_get_total_length"),
    
    # Store
    path('<str:category_slug>/<str:slug>/', product_detail, name="product_detail"),
    path('<slug:slug>/', category_detail, name="category_detail"),

    #re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
    #re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)