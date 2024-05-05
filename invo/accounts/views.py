from django.shortcuts import render, redirect
from accounts.models import Client, Domain
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django_tenants.utils import tenant_context
import datetime
from django.contrib import messages


from .forms import SignUpForm

def home(request):
    return render(request, 'accounts/home.html')

'''def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            user = authenticate(username=username, password = password)

            if user is not None:
                login(request, user)

                return redirect('/dashboard/')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html',{
        'form' : form
    })

'''
def signup(request): 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            tenant = Client(schema_name = name,
                    name = name,
                    user = user
                    )
            tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

            # Add one or more domains for the tenant
            domain = Domain(
                domain = str(datetime.datetime.now().year) + str(tenant.id)
            )
    
            domain.domain = domain.domain + '.localhost' # don't add your port or www here!
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('/signin/')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {
        'form':form,
        })

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            domain = user.user.all().first().get_primary_domain()
            url = f"http://rangerover.mysite.com:8000/dashboard"

            return redirect(url)
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('signin')	


    else:
        return render(request, 'accounts/signin.html', {})

'''
def signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
          form = SignUpForm(request.POST)

          if form.is_valid():
              name = form.cleaned_data.get('first_name')
              email = form.cleaned_data.get('email')
              password = form.cleaned_data.get('password1')
              form.save()

              u = User.objects.create_user(first_name = name,username = "user-" + str(email)[:5], password = password, email = email)

              tenant = Client(schema_name = name,
                    name = name,
                    user = u
                    )
              tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

    # Add one or more domains for the tenant
              domain = Domain(
                    domain = str(datetime.datetime.now().year) + str(tenant.id)
                )
    
              domain.domain = domain.domain + '.localhost' # don't add your port or www here!
              domain.tenant = tenant
              domain.is_primary = True
              domain.save()

              #with tenant_context(tenant):
                #User.objects.create_user(first_name = name,username = "user-" + str(email)[:5], password = password, email = email)

              user = authenticate(username = email, password = password)

              if user is not None:
                login(request, user)

                return redirect('/dashboard/')
              
              #return redirect('/signin/')

    else:
        return redirect('/signup/')
    
    form = SignUpForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/signup.html', context)
'''


'''
def signup(request):
    #if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #u.refresh_from_db()

            name = form.cleaned_data.get('name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            #email = form.cleaned_data.get('email')
            #password = form.cleaned_data.get('password')
            
            #u.profile.username = email
            #u.save()

            tenant = Client(schema_name = name,
                    name = name,
                    user = user
                    )
            tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

    # Add one or more domains for the tenant
            domain = Domain(
                    domain = str(datetime.datetime.now().year) + str(tenant.id)
            )
    
            domain.domain = domain.domain + '.localhost' # don't add your port or www here!
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            if user is not None:
                login(request, user)

            return redirect('accounts/signin.html') #home
        else:
            form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})
'''