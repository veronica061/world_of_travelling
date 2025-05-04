from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from landing.models import Review


def index(request):
    reviews = Review.objects.all().order_by('-created_at')[:10]
    return render(request, 'landing/index.html', {'reviews': reviews})


def get_reviews(request):
    last_time = request.GET.get('last_time')

    try:
        if last_time:
            last_time = timezone.datetime.fromisoformat(last_time)
            new_reviews = Review.objects.filter(created_at__gt=last_time)
        else:
            new_reviews = Review.objects.all().order_by('-created_at')[:10]

        reviews_data = [{
            'id': review.id,
            'text': review.text,
            'author': review.author,
            'created_at': review.created_at.isoformat()
        } for review in new_reviews]

        return JsonResponse({
            'reviews': reviews_data,
            'last_time': timezone.now().isoformat()
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



def submit_review(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        review = Review.objects.create(
            author=request.user,
            text=text
        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "reviews_reviews",
            {
                "type": "new_review",
                "text": review.text,
                "author": review.author.username,
                "created_at": review.created_at.strftime('%d.%m.%Y %H:%M')
            }
        )

        return JsonResponse({"status": "ok"})
