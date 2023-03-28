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
  
    #add skill
    path('skill_add/', views.skill_add, name='skill_add'),
    path('skill_add/do', views.skill_add_do, name='skill_add_do'),
    path('skill_all/', views.skill_all, name='skill_all'),
    path('skill_all/cm', views.cm, name='cm'),
    path('skill_all/skill_add/', views.skill_add, name='skill_addk'),
     path('skill_all/skill_add/do', views.skill_add_do, name='skill_addkk'),
    path('skill_all/delete/<int:id>', views.skill_delete, name='skill_delete'),    

     path('skill_add/do1', views.skill_add_do1, name='skill_add_do1'),
     path('skill_all/delete1/<int:id>', views.skill_delete1, name='skill_delete'),  

     path('skill_all/skill_add/', views.skill_add, name='skill_addk1'),
     path('skill_all/skill_add/do1', views.skill_add_do1, name='skill_addkk1'),



    #edu
    path('edu_add/', views.edu_add, name='edu_add'),
    path('edu_add/do', views.edu_add_do, name='edu_add_do'),
    path('edu_all/', views.edu_all, name='edu_all'),
    path('edu_update/<int:id>', views.edu_update, name='edu_update'),
    path('edu_update/do/<int:id>', views.edu_update_do, name='edu_update_do'),
    path('edu_delete/<int:id>', views.edu_delete, name='edu_delete'),
    path('edu_all/eud_add', views.edu_add, name='edu_add'),




]    


