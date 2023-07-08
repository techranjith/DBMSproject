from django.urls import path,include

from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('login',views.login,name='login'),
   path('register',views.register,name='register'),
   path('logout',views.logout,name='logout'),
  
   path('cart/',views.cart,name='cart'),
   
   path('products/<int:id>',views.products,name="logout"),
   path('search',views.search,name='search'),

   path('sellerlogin',views.sellerlogin,name='sellerlogin'),
   path('sellerregister',views.sellerregister,name="sellerregister"),

   path('account/<int:userid>',views.account,name="account"),
   path('account/products/<int:id>',views.account,name="account"),

   path('selleraccount/<int:userid>',views.selleraccount,name="selleraccount"),
   path('sellerlogout',views.sellerlogout,name="sellerlogout"),

   path('addproduct',views.addproduct,name="addproduct"),
   path('add',views.add,name="add"),
   
   path('delete/<int:pid>/<int:uid>',views.delete,name="delete"),
   path('buy/<int:productid>/<int:customerid>',views.buy,name="buy"),

   path('account/edit/<int:userid>',views.edit,name='edit'),
   path('account/edit/addedit/<int:userid>',views.addedit,name='addedit'),


]