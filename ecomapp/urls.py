from django.urls import path,include
from .import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('user_login',views.user_login,name='user_login'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('category1',views.category1,name='category1'),
    path('add_category',views.add_category,name='add_category'),
    path('products',views.products,name='products'),
    path('add_product',views.add_product,name='add_product'),
    path('show_product',views.show_product,name='show_product'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('reg',views.reg,name='reg'),
    path('user_home',views.user_home,name='user_home'),
    path('view_user',views.view_user,name='view_user'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
    path('show/<int:id>',views.show,name='show'),
    path('add_cart/<int:id>',views.add_cart,name='add_cart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('logout',views.logout,name='logout'),
    path('checkout',views.checkout,name='checkout'),
    path('cartincrement/<int:id>',views.cartincrement,name='cartincrement'),
    path('cartdecrement,<int:id>',views.cartdecrement,name='cartdecrement')
    # # path('pay',views.pay,name='pay')
    
    
]
