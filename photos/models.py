from django.contrib.auth.models import User
from django.db import models
from mydisk.settings import BASE_DIR, MEDIA_ROOT
import os


# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.user.id, filename)


class Photo(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now_add=True)

    def get_absolute_path(self):
        return os.path.join(BASE_DIR, MEDIA_ROOT, str(self.file))
