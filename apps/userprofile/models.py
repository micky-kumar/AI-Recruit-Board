from django.db import models
from django.contrib.auth.models import User
from apps.job.models import Application
from multiselectfield import MultiSelectField

# Create your models here.

class Userprofile(models.Model):
    skills = (
        ('Python','Python'),
        ('AWS', 'AWS'),
        ('Azure', 'Azure'),
        ('None', 'None')
    )

    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    skill_set = MultiSelectField(choices = skills, default='none')

    def __str__(self):
        return str(self.user)



User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.created_at

    class Meta:
        ordering = ['created_at']
