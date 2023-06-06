from django.shortcuts import render,redirect

# Create your views here.
def index_pg(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    return redirect('/admin/')


def login_pg(request):
    return render(request, 'login.html')


def import_pg(request):
    return render(request, 'import.html')