from django.urls import path, include
from . import views

urlpatterns = [
    #path('categories', views.CategoriesView.as_view()),
    #path('menu-items', views.MenuItemsView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/category', views.CategoriesView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemDetailView.as_view()),
    path('groups/managers/users', views.ManagersListView.as_view()),
    path('groups/managers/users/<int:pk>', views.ManagersRemoveView.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewListView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewRemoveView.as_view()),
    path('cart/menu-items', views.CartOperationsView.as_view()),
    path('orders', views.OrderOperationsView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    path('ratings', views.RatingView.as_view({'get':'list'})),
]