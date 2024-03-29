from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Place, User, Comment, Food, Food_Type
from .forms import LoginForm, CommentForm


# Create your views here.

def test_map(request):
    return render(request, "places2/map.html")


def home(request):
    data = Place.objects.all()
    comments = Comment.objects.all()
    context = {"places": data}
    context["cafe"] = data.filter(type = 1)
    context["restaurant"] = data.filter(type = 2)
    context["fastfood"] = data.filter(type = 3)
    context["persin"] = data.filter(type = 4)
    context["kebab"] = data.filter(type = 5)
    context["vegan"] = data.filter(type = 6)
    context["international"] = data.filter(type = 7)
    context["fried"] = data.filter(type = 8)
    context["seafood"] = data.filter(type = 9)
    context["traditional"] = data.filter(type = 10) 
    context["user_count"] = User.objects.all().count()
    context["place_count"] = data.count()
    context["comment_count"] = comments.count()
    context["food_count"] = Food.objects.count()
    context["last_comments"] = comments.order_by('-date_created')[:4]
    return render(request, "places/index.html", context)


def single_page(request, id):
    loged_in = not(request.user.is_anonymous)
    place = get_object_or_404(Place, id=id)
    foods = Food.objects.filter(restaurant=id)
    food_types = Food_Type.objects.all().values()
    menu = {}
    for food in foods:
        food_type = food.food_type
        type_title = food_types.get(title = food_type)["title_fa"]
        if type_title in menu.keys():
            menu[type_title].append(food.name)
        else:
            menu[type_title] = [food.name]
    
    comments = Comment.objects.filter(restaurant=id)
    context = {"place": place, "loged_in":loged_in, "comments": comments, "menu": menu, "active_show": '1'}
    return render(request, "places/single_page.html", context)


@login_required 
def add_comment(request, id):
    if request.method == "POST":
        body = request.POST.get("comment_body")
        score = request.POST.get("score")
        form = CommentForm()
        form.score = score
        form.body = body
        if form.is_valid:
            comment = Comment()
            comment.written_by = request.user
            place = Place.objects.get(id=id)
            comment.restaurant = place
            comment.body = body
            comment.score = score
            comment.save()
            return redirect(f"/places/{id}")
    return render(request, "places/add_comment.html", {"place_id": id})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            in_username = form.data.get("username")
            in_password = form.data.get("password")
            user = authenticate(username=in_username, password=in_password)
            if user:  
                login(request, user)          
                return HttpResponse(f"wellcome {in_username}")
            else:
                return HttpResponse("user not found")
    else:
        form = LoginForm()   
    return render(request, "places/login.html", {"form": form})
    ...
    
    
    
    
    
