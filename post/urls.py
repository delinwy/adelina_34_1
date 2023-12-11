from django.urls import path
from post import views


urlpatterns = [
    path('', views.main_view),
    path('current_date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('products/', views.products_view),
    path('products/create/', views.product_create),
    path('products/<int:product_id>/', views.product_detail_view),
    path('categories/', views.categories_view),
    path('categories/create/', views.category_create),
    path('categories/', views.categories_view)
]
