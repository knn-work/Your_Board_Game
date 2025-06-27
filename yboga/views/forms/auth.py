from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from yboga.forms.auth_form import LoginForm


def user_auth(request):
    """
    Аутентификация пользователя.
    """
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()

    # Важно: рендерим форму даже если POST не прошёл валидацию
    context = {"title": "Авторизация", "form": form}
    return render(request, "user_auth_form.html", context=context)


def user_logout(request):
    logout(request)
    return redirect("index")
