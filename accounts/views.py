from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Count

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/eve/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
              #  user.save();
                print('User Created')
            return redirect('login')
        else:
            messages.info(request,'passwords do not match..')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def user_stats(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    most_predicted=File.objects.filter(userNamef=username).annotate(mc=Count('prediction')).order_by('-mc')[0].mc
    num_search=File.objects.filter(userNamef=username).count()
    correct=num_search.objects.filter(isCorrect=True)
    context = {
        "most_predicted": most_predicted,
        "num_search": num_search,
        "correct": correct
    }
    return render(request, 'eve/index.html', context)