from django.urls import path
from . import views

urlpatterns = [
    path("visit/", views.visit_index, name="visit_index"),
   	path('visit/create/',views.create_visit,name="create_visit"),
   	path('visit/create/save/',views.save_visit,name="save_visit")
]
