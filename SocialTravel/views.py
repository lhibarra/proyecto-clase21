from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm
# Create your views here.

def index(request):
    return render(request, "SocialTravel/index.html")

def mostra_otro_template(request):
    posts = Post.objects.all()
    return render(request, "SocialTravel/otro_template.html", { "posts":posts})

def mostrar_pos(request):
    contex = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    return render (request,"SocialTravel/admin_post.html", contex)

def agregar_post(request):
    form_post = PostForm(request.POST)
    form_post.save()#Construyo objeto tipo PosForm con los datos carfagos por el usuario
    contex = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    return render (request, "SocialTravel/admin_post.html", contex)

def buscar_post(request):
    criterio = request.GET.get("criterio")
    contex = {
        "posts": Post.objects.filter(carousel_caption_title__icontains = criterio).all(),  
        
    }
    return render(request, "SocialTravel/admin_post.html", contex)
