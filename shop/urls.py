from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("shop/",views.index,name = "ShopHome"),
    path("about/",views.about,name = "AboutUS"),
    path("contact/",views.contact,name = "Contactus"),
    path("songview/",views.SongView,name = "Song"),
    path("search/",views.search,name ="Search"),
    path("library/",views.library,name ="Song Library"),
    path("add/<int:id>",views.add_to_lib,name ="add_to_lib"),
]