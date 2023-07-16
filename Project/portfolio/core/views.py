from django.shortcuts import render, HttpResponse

html_base = """<h1>Bienvenidos a mi web personal</h1>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/about">Acerca de</a></li>
<li><a href="/portafolio">Portafolio</a></li>
</ul>
"""

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contacto(request):
    return render(request, "core/contacto.html")
