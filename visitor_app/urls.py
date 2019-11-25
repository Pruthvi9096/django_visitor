from django.urls import path
from . import views

urlpatterns = [
    path("visit/", views.visit_index, name="visit_index"),
    path("<int:pk>/", views.visit_profile, name="visit_profile"),
   	path('create/',views.create_visit,name="create_visit"),
   	path('create/save/',views.save_visit,name="save_visit"),
   	path('visitor/',views.create_visitor,name="create_visitor"),
   	path('create_visitor/',views.create_employee,name="create_employee"),
   	path('save_visitor/',views.visitor_save,name="visitor_save"),
   	path('visitor/save/',views.save_visitor,name="save_visitor"),
   	path('take_photo/',views.open_webcam,name="open_webcam"),
   	path('visitfor_create/',views.add_employee,name="add_employee"),
   	path('visitfor_create/save/',views.save_employee,name="save_employee"),
   	path('department_create/',views.add_department,name="add_department"),
   	path('department_create/save/',views.save_department,name="save_department"),
   	path('create_department/',views.create_department,name="create_department"),
   	path('save_department/',views.save_department_dashboard,name="save_department_dashboard"),
   	path('check_in/<int:pk>/',views.check_in,name="check_in"),
   	path('check_out/<int:pk>/',views.check_out,name="check_out"),
   	path('delete/<int:pk>/',views.delete_record,name="delete_record"),
   	path('view_all_visitor/',views.all_visitor,name="all_visitor"),
   	path('view_all_department/',views.all_department,name="all_department"),
   	path('view_all_visitor/save/<int:pk>/',views.save_info,name="save_info"),
   	path('edit_visitor_info/<int:pk>/',views.edit_info,name="edit_info"),
   	path('delete_visitor_info/<int:pk>/',views.delete_info,name="delete_info"),
   	path('delete_department/<int:pk>/',views.delete_department,name="delete_department")
]
