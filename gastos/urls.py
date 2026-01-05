from django.urls import path
from .views import gastos_list_create, gastos_detail, gastos_total

urlpatterns = [
    path('gastos/', gastos_list_create),
    path('gastos/<int:pk>/', gastos_detail),
    path('gastos/total/', gastos_total),
]
