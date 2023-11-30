from django.contrib import admin
from django.urls import path

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('current_date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('products/', views.products_view),
    path('categories/', views.categories_view)
]
