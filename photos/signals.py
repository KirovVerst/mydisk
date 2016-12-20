from django.db.models.signals import pre_delete
from django.dispatch import receiver
from photos.models import Photo
import os


@receiver(pre_delete, sender=Photo)
def delete_file(sender, **kwargs):
    photo = kwargs.get('instance')
    path = photo.get_absolute_path()
    if os.path.exists(path):
        try:
            os.remove(path)
            folder = os.path.dirname(path)
            if not os.listdir(folder):
                os.rmdir(folder)
        except OSError as e:
            print(e.strerror)
