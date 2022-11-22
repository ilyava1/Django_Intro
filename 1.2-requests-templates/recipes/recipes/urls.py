from django.urls import path
from calculator.views import home_view, prepare_dish

urlpatterns = [
    path('', home_view, name='home'),
    path('<user_choise>/', prepare_dish)
]
