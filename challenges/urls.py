from django.urls import path

from . import views

# * URL config
urlpatterns = [
    #! The order of path is IMPORTANT
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='abc')
]
