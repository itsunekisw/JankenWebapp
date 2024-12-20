from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import SignupUserForm, LoginForm
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
import random

User = get_user_model()

class TopView(TemplateView):
    template_name = 'janken/top.html'


def signup_view(request):
    if request.method == 'POST':

        form = SignupUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect(to='/janken/')

    else:
        form = SignupUserForm()

    param = {
        'form': form
    }

    return render(request, 'janken/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/janken/')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'janken/login.html', param)

@login_required
def ranking_view(request):
    users = User.objects.order_by('-win_rate')

    params = {
        'users' : users
    }

    return render(request, 'janken/ranking.html', params)

@login_required
def logout_view(request):
    logout(request)

    return redirect(to='/janken/login/')

@login_required
def index_view(request):

    params = {
        'user' : request.user
    }
    return render(request, 'janken/index.html', params)
    

@login_required
def user_view(request, id=0):
    other = get_object_or_404(User, id=id)

    params = {
        'user' : request.user,
        'other' : other
    }

    return render(request, 'janken/user.html', params)

@login_required
def janken_view(request):
    if request.method == 'POST':
        com_hand = random.choice(('stone', 'scissors', 'paper'))
        player_hand = request.POST.get('hand')

        player = request.user

        result = player.play(player_hand, com_hand)
        player.save()

        params = {
            'user' : request.user,
            'result' : result,
            'player_hand' : player_hand,
            'com_hand' : com_hand
        }
        return render(request, 'janken/result.html', params)

    else:
        params = {
            'user' : request.user
        }
        return render(request, 'janken/janken.html', params)
