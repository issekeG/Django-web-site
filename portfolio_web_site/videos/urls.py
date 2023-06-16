from django.urls import path
from .views import Index, recharge_projet_notebook

app_name = 'videos'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('notebook', recharge_projet_notebook, name='recharge_notebook')
]
