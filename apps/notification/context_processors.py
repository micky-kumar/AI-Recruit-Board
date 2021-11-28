from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        return {'notification': request.user.notification.filter(is_read=False)}

    else:
        return {'notifications': []}