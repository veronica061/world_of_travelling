$(document).ready(function() {
    // Открытие модального окна
    $('#addReviewBtn').click(function() {
        $('#reviewModal').modal('show');
    });

    // Отправка отзыва
    $('#submitReview').click(function() {
        const reviewText = $('#reviewText').val().trim();
        const csrfToken = $('[name=csrfmiddlewaretoken]').val();

        if (!reviewText) {
            alert('Пожалуйста, введите текст отзыва');
            return;
        }

        // Показываем индикатор загрузки
        $('#submitReview').prop('disabled', true).html(
            '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Отправка...'
        );

        $.ajax({
            url: '/submit_review/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'text': reviewText
            }),
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(response) {
                if (response.success) {
                    $('#reviewModal').modal('hide');
                    $('#reviewText').val('');
                    // Добавляем новый отзыв на страницу
                    addReviewToPage(response.review);
                } else {
                    alert('Ошибка: ' + (response.error || 'Неизвестная ошибка'));
                }
            },
            error: function(xhr) {
                let errorMsg = 'Ошибка соединения';
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    errorMsg = xhr.responseJSON.error;
                }
                alert(errorMsg);
            },
            complete: function() {
                // Восстанавливаем кнопку
                $('#submitReview').prop('disabled', false).text('Отправить');
            }
        });
    });

    // Функция добавления отзыва
    function addReviewToPage(review) {
        const reviewHtml = `
            <div class="review-item mb-3">
                <blockquote class="blockquote">
                    <p>${review.text}</p>
                    <footer class="blockquote-footer">
                        ${review.author} <small class="text-muted">${review.created_at}</small>
                    </footer>
                </blockquote>
            </div>
        `;
        $('#reviews').prepend(reviewHtml);
    }
});
