from django.urls import path

from main_page import views

app_name = "main_page"

urlpatterns = [
    path("", views.where_to_go, name="main"),
    path("places/", views.show_places, name="show_places"),
    path("add_places/", views.add_places, name="add_places"),
    path("places/<int:id>/", views.place_detail, name="place_detail"),
]
