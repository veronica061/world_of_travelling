from django.shortcuts import redirect

class AuthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != '/login':
            return redirect('http://localhost:8001/login')
        return self.get_response(request)
