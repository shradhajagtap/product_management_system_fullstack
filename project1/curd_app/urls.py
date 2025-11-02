from django.urls import path
from . import views

urlpatterns = [
    # --- React API endpoints ---
    path('api/orders/', views.api_orders, name='api_orders'),
    path('api/orders/<int:pk>/', views.api_order_detail, name='api_order_detail'),
    path('api/orders/<int:pk>/update/', views.api_order_update, name='api_order_update'),
    path('api/orders/<int:pk>/delete/', views.api_order_delete, name='api_order_delete'),
    

    # --- Django HTML endpoints ---
    path('create/', views.create_order, name='create_url'),
    path('show/', views.show_order, name='show_url'),
    path('update/<int:pk>/', views.update_order, name='update_url'),
    path('cancel/<int:pk>/', views.cancel_order, name='cancel_url'),
]
