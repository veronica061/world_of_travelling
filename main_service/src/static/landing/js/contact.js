document.addEventListener('DOMContentLoaded', function () {

    const form = document.getElementById('registration-form');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            clearErrors();

            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();

            let isValid = true;

            // Валидация имени
            if (!validateName(name)) {
                showError('name-error', 'Имя должно содержать только буквы и одну заглавную.');
                isValid = false;
            }

            // Валидация электронной почты
            if (!validateEmail(email)) {
                showError('email-error', 'Введите корректный адрес электронной почты.');
                isValid = false;
            }

            // Если форма валидна, отправляем данные
            if (isValid) {
                alert('Форма успешно отправлена!');
            }
        });
    }

    // Функция для валидации имени
    function validateName(name) {
        const regex = /^[A-ZА-Я][a-zа-я]*$/;
        return regex.test(name);
    }

    // Функция для валидации электронной почты
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Функция для отображения ошибки
    function showError(elementId, message) {
        const errorElement = document.getElementById(elementId);
        if (errorElement) {
            errorElement.textContent = message;
        }
    }

    // Функция для очистки ошибок
    function clearErrors() {
        const errorElements = document.querySelectorAll('.text-danger');
        errorElements.forEach(function (element) {
            element.textContent = '';
        });
    }
});
