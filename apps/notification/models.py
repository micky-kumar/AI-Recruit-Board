from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notification(models.Model):
    MESSAGE = 'message'
    APPLICATION = 'application'

    CHOICES =(
        (MESSAGE, 'Message'),
        (APPLICATION, 'Application')
    )

    to_user = models.ForeignKey(User, related_name='notification', on_delete=models.CASCADE)
    notifaction_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotification', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created_at']