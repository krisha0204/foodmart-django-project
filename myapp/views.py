from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User 
from .models import food

def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['uname']
        pw = request.POST['pwd']
        user = auth.authenticate(username=un, password=pw)

        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        print("REGISTER CALLED!")


        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        un = request.POST['uname']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        if p1 != p2:
            messages.error(request, "Passwords do not match!")
            return redirect('/register/')

        if User.objects.filter(username=un).exists():
            messages.error(request, "Username already exists!")
            return redirect('/register/')

        if User.objects.filter(email=em).exists():
            messages.error(request, "Email already exists!")
            return redirect('/register/')

        user = User.objects.create_user(
            username=un,
            password=p1,
            email=em,
            first_name=fn,
            last_name=ln,
        )
        user.save()

        messages.success(request, "User registered successfully!")
        return redirect('/login/')

    return render(request, 'register.html')


def food_view(request):
    foods = food.objects.all()   # FIXED — model name
    return render(request, "food.html", {
        "foods": foods,
        "username": request.user.username
    })


def add_food(request):
    if request.method == "POST":
        food.objects.create(
            product=request.POST["prod"],
            price=request.POST["price"],
            foodgrade=request.POST["fgrade"],
            image = request.FILES.get('image'),

        )
        return redirect("food")

    return render(request, "add.html")


from .models import food

def edit(request, id):
    fooddata = food.objects.get(id=id)

    if request.method == "POST":
        fooddata.product = request.POST.get("product")
        fooddata.price = request.POST.get("price")
        fooddata.foodgrade = request.POST.get("foodgrade")
        fooddata.save()
        return redirect("food")

    return render(request, "edit.html", {"fooddata": fooddata})


def delete(request, id):
    obj = get_object_or_404(food, id=id)
    obj.delete()
    return redirect('/food/')

