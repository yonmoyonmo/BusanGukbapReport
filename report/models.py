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

    location = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    gukmool = models.IntegerField()
    gogi = models.IntegerField()
    kimchi = models.IntegerField()
    service = models.IntegerField()
    weesaeng = models.IntegerField()

    def __str__(self):
        return self.title


class Report2(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(timezone.now(), null=True)
    author = models.CharField(max_length=100)
    content = models.TextField()

    thumbnail = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )
    fullshot = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )
    fullshot_caption = models.CharField(max_length=200)
    detailshot = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )
    detailshot_caption = models.CharField(max_length=200)
    menushot = ResizedImageField(
        upload_to=user_path, quality=75, blank=True, null=True
    )
    menushot_caption = models.CharField(max_length=200)

    youtubelink = models.TextField()

    location = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    gukmool = models.IntegerField()
    gogi = models.IntegerField()
    kimchi = models.IntegerField()
    service = models.IntegerField()
    weesaeng = models.IntegerField()

    def __str__(self):
        return self.title
#-----------new version of models------------#


class Comment(models.Model):
    report = models.ForeignKey(
        'Report3',
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.text


class Report3(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(timezone.now(), null=True)
    author = models.CharField(max_length=100)
    content = models.TextField()

    open_close = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    youtubelink = models.CharField(max_length=200)

    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title


def report_dir_path(instance, filename):
    from random import choice
    import string  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    title = instance.report.title
    return '%s/%s.%s' % (title, pid, extension)


class ReportImages(models.Model):
    report = models.ForeignKey(
        'Report3',
        on_delete=models.CASCADE,
        related_name='Images')
    image = ResizedImageField(
        upload_to=report_dir_path, quality=75, blank=True, null=True)

    def __str__(self):
        return self.image.url


class Gukmool(models.Model):
    report = models.ForeignKey(
        'Report3', on_delete=models.CASCADE, related_name="gukmools")
    YUKSU_CHOICES = [
        ('bone', '뼈'),
        ('meat', '살코기'),
        ('mix', '혼합'),
    ]
    SIMPLE_OX = [
        ('yes', 'O'),
        ('no', 'X'),
    ]
    yuksu = models.CharField(
        max_length=50,
        choices=YUKSU_CHOICES,
        default='bone'
    )
    yeomdo = models.CharField(max_length=50)
    hexColor = models.CharField(max_length=50)

    saewoo = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )
    salt = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )
    blackPepper = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )
    toRyeom = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )
    yangNyeomJang = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )
    ddaroGukbap = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )
    NETgukbap = models.CharField(
        max_length=10,
        choices=SIMPLE_OX,
        default='O'
    )

    def __str__(self):
        return self.report.title


class Gogui(models.Model):
    report = models.ForeignKey(
        'Report3', on_delete=models.CASCADE, related_name="goguis")
    TEXTURE_CHOICES = [
        ('soft', '부드러움'),
        ('jol', '쫄깃함'),
        ('hard', '퍽퍽함'),
    ]
    THICKNESS_CHOICES = [
        ('thin', '얇음'),
        ('thick', '두꺼움')
    ]
    SMELL_CHOICES = [
        ('5', '상'),
        ('4', '상중'),
        ('3', '중'),
        ('2', '중하'),
        ('1', '하'),
    ]
    SIMPLE_OX = [
        ('yes', 'O'),
        ('no', 'X'),
    ]

    meatPart = models.CharField(max_length=50)
    texture = models.CharField(max_length=30, choices=TEXTURE_CHOICES)
    thickness = models.CharField(max_length=30, choices=THICKNESS_CHOICES)
    smell = models.CharField(max_length=10, choices=SMELL_CHOICES)
    dippingSource = models.CharField(max_length=10, choices=SIMPLE_OX)

    def __str__(self):
        return self.report.title


class Kimchi(models.Model):
    report = models.ForeignKey(
        'Report3', on_delete=models.CASCADE, related_name="kimchis")
    SPICY_CHOICES = [
        ('5', '상'),
        ('4', '상중'),
        ('3', '중'),
        ('2', '중하'),
        ('1', '하'),
    ]
    spicy = models.CharField(max_length=10, choices=SPICY_CHOICES)
    banchan = models.CharField(max_length=200)

    def __str__(self):
        return self.report.title


class Service(models.Model):
    report = models.ForeignKey(
        'Report3', on_delete=models.CASCADE, related_name="services")

    KINDNESS_CHOICES = [
        ('3', '상'),
        ('2', '중'),
        ('1', '하'),
    ]
    SIMPLE_OX = [
        ('yes', 'O'),
        ('no', 'X'),
    ]
    banchanTime = models.CharField(max_length=10)
    gukbaptime = models.CharField(max_length=10)
    kindness = models.CharField(max_length=10, choices=KINDNESS_CHOICES)
    banchanRefill = models.CharField(max_length=10, choices=SIMPLE_OX)
    selfServing = models.CharField(max_length=10, choices=SIMPLE_OX)
    gukmulRefill = models.CharField(max_length=10, choices=SIMPLE_OX)
    dessert = models.CharField(max_length=10, choices=SIMPLE_OX)

    def __str__(self):
        return self.report.title


class Weesaeng(models.Model):
    report = models.ForeignKey(
        'Report3', on_delete=models.CASCADE, related_name="weesaeng")
    SIMPLE_TMB_CHOICES = [
        ('3', '상'),
        ('2', '중'),
        ('1', '하'),
    ]
    floor = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)
    table = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)
    spoons = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)
    cups = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)
    kitchen = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)
    tissue = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)
    toilets = models.CharField(max_length=10, choices=SIMPLE_TMB_CHOICES)

    def __str__(self):
        return self.report.title
