
# create urls.py file
from django.urls import path
from.import views

# relationship between views and urls (app)
urlpatterns =[
    path('', views.index,name='index')
]
