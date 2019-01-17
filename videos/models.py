from django.db import models

class Category(models.Model):
    """ Category model."""

    name = models.CharField(verbose_name='Category name', max_length=120)
    cover = models.ImageField(verbose_name='Category cover image')

    def __str__(self) -> str:
        """
        Call as string
        :return: str
        """
        return self.name

class Video(models.Model):
    """Video model."""

    cover = models.CharField(verbose_name='Video cover', max_length=255)
    file = models.CharField(verbose_name='Video file', max_length=255)
    views = models.IntegerField(verbose_name='Video views')
    is_private = models.BooleanField(verbose_name='Video private')
