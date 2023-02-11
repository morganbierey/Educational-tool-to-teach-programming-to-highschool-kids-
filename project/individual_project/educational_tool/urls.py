from django.urls import path
from educational_tool import views

#manually created this file 
app_name = 'educational_tool'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
path('pycompiler/', views.pycompiler, name='pycompiler'),
path('register/', views.register, name='register'),
# path('runcode', views.runcode, name='runcode'),

]
