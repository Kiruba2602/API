from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemListView.as_view()),
    path('menu-items/category', views.CategoryView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemDetailView.as_view()),
    path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
]