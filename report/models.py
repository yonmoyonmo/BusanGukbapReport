from django.db import models
from django.conf import settings
from django.utils import timezone
from django_resized import ResizedImageField


def user_path(instance, filename):
    from random import choice
    import string  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '%s.%s' % (pid, extension)


class Report(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(timezone.now(), null=True)
    author = models.CharField(max_length=100)
    content = models.TextField()

    fullshot = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )
    detailshot = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )
    menushot = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )

    youtubelink = models.TextField()

    lat = models.FloatField()
    lng = models.FloatField()

    location = models.CharField(max_length=50)

    gukmool = models.IntegerField()
    gogi = models.IntegerField()
    kimchi = models.IntegerField()
    service = models.IntegerField()
    weesaeng = models.IntegerField()

    def __str__(self):
        return self.title
