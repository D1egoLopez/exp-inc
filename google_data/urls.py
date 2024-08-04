from django.urls import path
from . import views

urlpatterns = [
    path('raw-data-sheet-exp', views.exp, name='expenses data'),
    path('raw-data-sheet-inc', views.inc, name='income data'),
    path('sumas', views.summas )
]
