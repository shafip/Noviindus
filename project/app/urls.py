from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_view
urlpatterns = [
    # path('', views.home,name="home"),
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('add/product', AddDoctor.as_view(), name='add_product'),
    path('productview', ProductList.as_view(), name='product_list'),
    path('table/', ProductListTable.as_view(), name='producttable'),
    path('product/update/<int:pk>/', Updateproduct.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product-delete'),
    # path('cart', views.CartView.as_view(), name="cartview"),
    path('cart/', views.cartview, name='cartview'),
    # path('addtocart/<int:product_id>/',views.AddProductCart, name='addtocart'),
    path('add_to_cart/<int:product_id>/', views.addproductcart, name='addcart'),
    path('cart/update/<int:product_id>/<str:action>/', views.cartupdate, name='cart_update'),
    path('cart/delete/<int:pk>/', CartDelete.as_view(), name='cart-delete'),
    path('', auth_view.LogoutView.as_view(template_name='user/productview.html'), name="logout"),


]