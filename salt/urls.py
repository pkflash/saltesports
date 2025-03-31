from django.urls import path
from . import views

app_name = "salt_app"
urlpatterns = [
    path("salt/home", views.home, name="home"),
    path("salt/about", views.about, name="about"),
    path("salt/content", views.content, name="content"),
    path("salt/gallery", views.gallery, name="gallery"),
    path("salt/members", views.members, name="members"),
    path("salt/recent", views.recent, name="recent"),
    path("salt/members/puresalt", views.puresalt, name="puresalt"),
    path("salt/members/shrutik", views.shrutik, name="shrutik"),
    path("salt/members/shrutikmk", views.shrutikmk, name="shrutikmk"),
    path("salt/members/nessboy12", views.nessboy12, name="nessboy12"),
    path("salt/members/latios", views.latios, name="latios"),
    path("salt/members/dtier", views.dtier, name="dtier"),
    path("salt/members/rodnysalt", views.rodnysalt, name="rodnysalt"),
    path("salt/members/azrael", views.azrael, name="azrael"),
    path("salt/members/steamy", views.steamy, name="steamy"),
    path("salt/members/era", views.era, name="era"),
    path("salt/members/widara", views.widara, name="widara"),
    path("salt/members/marsbars", views.marsbars, name="marsbars"),
    path("salt/members/fletchling", views.fletchling, name="fletchling"),
    path("salt/members/lui$", views.lui, name="lui"),
    path("salt/members/lonelymatt", views.lonelymatt, name="lonelymatt"),
    path("salt/members/phi", views.phi, name="phi"),
    path("salt/members/snorlax", views.snorlax, name="snorlax"),
    path("salt/members/versedace", views.versedace, name="versedace"),
    path("salt/members/saltlord", views.saltlord, name="saltlord"),
    path("salt/members/alsoda", views.alsoda, name="alsoda"),
    path("salt/members/ikan", views.ikan, name="ikan"),
    path("salt/members/kurama", views.kurama, name="kurama"),
]