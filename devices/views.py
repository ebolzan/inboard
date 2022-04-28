from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Device
from django.core.exceptions import ValidationError




from .forms import UserForm
# Create your views here.

@login_required(login_url='/admin/')
def index(request):
    latest_question_list = Device.objects.all()[:5]
    template = loader.get_template('devices/index2.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def login(request):

    print(request.method)

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            HttpResponse()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("deu")
            gest = User.objects.get(manager=user.id)
            print(gest.is_managerUs)
        else:
            print("NAOOOO")
            error_message = 'reusable should not be zero'
            field = 'username'
            form.add_error(field, error_message)
    else:
        form = UserForm()

    return render(request, 'devices/login.html', {'form': form})