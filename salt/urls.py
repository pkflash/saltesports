from django.urls import path
from . import views

app_name = "salt_app"
urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("content", views.content, name="content"),
    path("gallery", views.gallery, name="gallery"),
    path("members", views.members, name="members"),
    path("recent", views.recent, name="recent"),
    path("members/puresalt", views.puresalt, name="puresalt"),
    path("members/shrutik", views.shrutik, name="shrutik"),
    path("members/nessboy12", views.nessboy12, name="nessboy12"),
    path("members/latios", views.latios, name="latios"),
    path("members/dtier", views.dtier, name="dtier")

]