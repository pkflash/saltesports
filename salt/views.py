from django.shortcuts import render

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
    return render(request, "salt/members.html")

def recent(request):
    return render(request, "salt/recent.html")

def puresalt(request):
    return render(request, "salt/members/puresalt.html")

def shrutik(request):
    return render(request, "salt/members/shrutik.html")

def nessboy12(request):
    return render(request, "salt/members/nessboy12.html")

def latios(request):
    return render(request, "salt/members/latios.html")

def dtier(request):
    return render(request, "salt/members/dtier.html")

def rodnysalt(request):
    return render(request, "salt/members/rodnysalt.html")