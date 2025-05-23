from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from landing.forms import SignUpForm, LoginForm

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя в базу данных
            # Получаем email и пароль из формы
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            # Выполняем аутентификацию
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  # Входим в систему
                return redirect("http://45.11.27.183/")  # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'landing/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему!')
                return redirect("http://45.11.27.183/")
            else:
                messages.error(request, 'Неправильный email или пароль.')
        else:
            # Обработка ошибок формы
            for field, errors in form.errors.items():
                if field == '__all__':
                    for error in errors:
                        messages.error(request, error)
                else:
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = LoginForm()
    return render(request, 'landing/login.html', {'form': form})
