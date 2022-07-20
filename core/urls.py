
from django.contrib import admin
from django.urls import path, include
from gadgets.views import ProductList, ProductDetails, ProductDestroy, ProductUpdate, ProductCreate, CategoryListCreate, product_list_with_categories, account_register, account_activation


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', ProductList.as_view(), name='product_list'),
    path('products/create', ProductCreate.as_view(), name='product_create'),
    path('products/<pk>/delete', ProductDestroy.as_view(), name='product_Destroy'),
    path('products/<pk>/update', ProductUpdate.as_view(), name='product_update'),
    path('products/<pk>', ProductDetails.as_view(), name='product_details'),
    path('product-category', CategoryListCreate.as_view()),
    path('products', product_list_with_categories, name='product_list_with_categories'),
    path('registration', account_register, name='registration'),
    path('activate/<uidb64>/<token>', account_activation, name='account_activation')
]
