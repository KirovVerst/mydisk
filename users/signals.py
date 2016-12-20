from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from mydisk.settings import MEDIA_ROOT

import os


@receiver(signal=post_save, sender=User)
def user_post_save_signal(sender, **kwargs):
    user = kwargs.get('instance')
    user_dir = os.path.join(MEDIA_ROOT, str(user.id))
    if not os.path.exists(user_dir):
        try:
            os.makedirs(user_dir)
        except OSError as e:
            print(e.strerror)
