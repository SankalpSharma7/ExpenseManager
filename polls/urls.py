from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('transaction/getAll', views.get_all_transactions),
    path('transaction/<int:transaction_id>', views.transaction),
    path('types/<str:type>', views.get_transaction_by_type),
    path('sum/<int:transaction_id>', views.sum_transactions)
]