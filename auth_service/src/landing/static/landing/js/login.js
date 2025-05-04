document.addEventListener('DOMContentLoaded', function () {

    const form = document.getElementById('registration-form');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            clearErrors();

            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();

            let isValid = true;

            // Валидация электронной почты
            if (!validateEmail(email)) {
                showError('email-error', 'Введите корректный адрес электронной почты.');
                isValid = false;
            }

            // Валидация пароля
            if (!validatePassword(password)) {
                showError('password-error', 'Пароль должен быть от 6 до 20 символов.');
                isValid = false;
            }

            // Если форма валидна, отправляем данные
            if (isValid) {
                alert('Форма успешно отправлена!');
                window.location.href = '/';
            }
        });
    }

    // Функция для валидации электронной почты
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Функция для валидации пароля
    function validatePassword(password) {
        return password.length >= 6 && password.length <= 20;
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
