from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('cm', views.cm, name='cm'),

    #Add
    path('cm1/addcm1/', views.addcm1, name='addcm1'),

    # Update Page 1
    path('cm_1_update/', views.cm_1_update, name='update'),
    path('cm_1_update/do', views.updaterecord, name='updaterecord'),


    #Add  about
    path('about_add/', views.about_add, name='about_add'),
    path('about_add/do', views.about_add_do, name='about_add_do'),


    # Update About 
    path('about_update/', views.about_update, name='abput_update'),
    path('about_update/do', views.about_update_do, name='abput_update_do'),
  



]    


