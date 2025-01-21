from django.urls import path
from . import views

app_name = "salt_app"
urlpatterns = [
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("content", views.content, name="content"),
    path("gallery", views.gallery, name="gallery"),
    path("members", views.members, name="members"),
    path("recent", views.recent, name="recent"),
    path("members/puresalt", views.puresalt, name="puresalt"),
    path("members/shrutik", views.shrutik, name="shrutik"),
    path("members/shrutikmk", views.shrutikmk, name="shrutikmk"),
    path("members/nessboy12", views.nessboy12, name="nessboy12"),
    path("members/latios", views.latios, name="latios"),
    path("members/dtier", views.dtier, name="dtier"),
    path("members/rodnysalt", views.rodnysalt, name="rodnysalt"),
    path("members/azrael", views.azrael, name="azrael"),
    path("members/steamy", views.steamy, name="steamy"),
    path("members/era", views.rileygibson, name="era"),
    path("members/widara", views.widara, name="widara"),
    path("members/marsbars", views.venuspenis, name="marsbars"),
    path("members/fletchling", views.fletchling, name="fletchling"),
    path("members/lui$", views.luis, name="lui$"),
    path("members/lonelymatt", views.matt, name="lonelymatt"),
    path("members/phi", views.phi, name="phi"),
    path("members/snorlax", views.snorlax, name="snorlax"),
    path("members/versedace", views.versed, name="versedace"),
    path("memebers/saltlord", views.saltlord, name="saltlord"),
    path("memebers/alsoda", views.alsoda, name="alsoda"),
    path("memebers/ikan", views.ikan, name="ikan"),
    path("memebers/kurama", views.kurama, name="kurama"),
]