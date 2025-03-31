from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
def home(request):
    return render(request, "salt/saltesports.html")

def about(request):
    return render(request, "salt/about.html")

def content(request):
    return render(request, "salt/content.html")

def gallery(request):
    return render(request, "salt/gallery.html")

def members(request):
    members = Member.objects.filter(is_active=True)
    return render(request, "salt/members.html", {
        "members": members
    })

def puresalt(request):
    return render(request, "salt/members/puresalt.html")

def dtier(request):
    return render(request, "salt/members/dtier.html")

def rodnysalt(request):
    return render(request, "salt/members/rodnysalt.html")

def era(request):
    return render(request, "salt/members/era.html")

def widara(request):
    return render(request, "salt/members/widara.html")

def azrael(request):
    return render(request, "salt/members/azrael.html")

def lui(request):
    return render(request, "salt/members/lui$.html")

def phi(request):
    return render(request, "salt/members/phi.html")

def snorlax(request):
    return render(request, "salt/members/snorlax.html")

def versedace(request):
    return render(request, "salt/members/versedace.html")

def saltlord(request):
    return render(request, "salt/members/saltlord.html")

def alsoda(request):
    return render(request, "salt/members/alsoda.html")

def ikan(request):
    return render(request, "salt/members/ikan.html")

def kurama(request):
    return render(request, "salt/members/kurama.html")

def shrutikmk(request):
    return render(request, "salt/members/shrutikmk.html")

def lonelymatt(request):
    return render(request, "salt/members/lonelymatt.html")

def nessboy12(request):
    return render(request, "salt/members/nessboy12.html")

def shrutik(request):
    return render(request, "salt/members/shrutik.html")

def steamy(request):
    return render(request, "salt/members/steamy.html")

def marsbars(request):
    return render(request, "salt/members/marsbars.html")

def latios(request):
    return render(request, "salt/members/latios.html")

def fletchling(request):
    return render(request, "salt/members/fletchling.html")

def recent(request):
    return render(request, "salt/recent.html")