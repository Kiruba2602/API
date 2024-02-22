from django.urls import path, include
from . import views
from .views import RegisterView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
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
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='obtain_token'),
]