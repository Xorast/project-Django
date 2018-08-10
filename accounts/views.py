from django.shortcuts    import render, redirect
from django.http         import HttpResponse
from django.contrib.auth import authenticate
from django.contrib      import auth
from .forms              import UserLoginForm, UserRegistrationForm, ProfileRegistrationForm



def login(request):
    
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)
    
            if user is not None:
                auth.login(request, user)
                next = request.GET.get('next', "/")
                return redirect(next)
                
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})



def register(request):
    
    if request.method == "POST":
        user_form        = UserRegistrationForm(request.POST)
        profile_form     = ProfileRegistrationForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user            = user_form.save()
            profile         = profile_form.save(commit=False)
            profile.user    = user
            profile.save()
            
            u       = user_form.cleaned_data['username']
            p       = user_form.cleaned_data['password1']
            user    = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
                
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'profile_form': profile_form})
    


def logout(request):
    auth.logout(request)
    return redirect('/')
    
 
    
def profile(request):
    return render(request, "accounts/profile.html")