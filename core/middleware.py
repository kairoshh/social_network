from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

class LastVisitMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        user = request.user 
        if not user.is_anonymous:
            User.objects.filter(id=user.id).update(last_login=now())

        print('before')
        response = self._get_response(request)
        print('after')
        return response