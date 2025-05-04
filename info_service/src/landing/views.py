
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from landing.forms import ContactForm
from landing.models import ContactMessage
from landing.utils import send_telegram_notification


def about(request):
    return render(request, 'landing/about.html')


def services(request):
    return render(request, 'landing/services.html')


@csrf_exempt
def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            contact_message = ContactMessage.objects.create(name=name, email=email, message=message)


            send_mail(
                subject=f"Новое сообщение от {name}",
                message=message,
                from_email=email,
                recipient_list=['antonenkoveronika630@gmail.com'],
                fail_silently=False,
            )

            # Формируем сообщение для Telegram
            telegram_msg = (
                f"<b>Новое сообщение с сайта!</b>\n\n"
                f"<b>Имя:</b> {contact_message.name}\n"
                f"<b>Email:</b> {contact_message.email}\n"
                f"<b>Сообщение:</b>\n{contact_message.message}"
            )

            if send_telegram_notification(telegram_msg):
                messages.success(request, 'Ваше сообщение отправлено! Мы скоро свяжемся с вами.')
            else:
                messages.warning(request, 'Сообщение сохранено, но возникла проблема с уведомлением.')


            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('/contacts')
        else:

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = ContactForm()
    return render(request, 'landing/contacts.html', {'form': form})
