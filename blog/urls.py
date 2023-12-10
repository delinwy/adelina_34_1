from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('current_date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('products/', views.products_view),
    path('products/create/', views.product_create),
    path('products/<int:product_id>/', views.product_detail_view),
<<<<<<< HEAD
    path('categories/', views.categories_view),
    path('categories/create/', views.category_create),
]
=======
    path('categories/', views.categories_view)
] 
>>>>>>> 619864d936e084df7ae9702f76dc5c22662c0c86

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
