from django.urls import path
from . import views

urlpatterns = [
    path('', views.deals_list, name='deals'),
    path('download/', views.download_deals, name='download_deals'),
    path('add/', views.add_deal, name='add_deal'),
    path('edit/<int:id>/', views.edit_deal, name='edit_deal'),
    path('delete/<int:id>/', views.delete_deal, name='delete_deal'),
]
