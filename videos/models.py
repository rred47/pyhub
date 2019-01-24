from django.db import models


class Category(models.Model):
    """ Category model."""

    name = models.CharField(verbose_name='Category name', max_length=120)
    cover = models.ImageField(verbose_name='Category cover image')

    def __str__(self) -> str:
        """
        Call class as string
        :return: str
        """
        return self.name


class Video(models.Model):
    """Video model."""

    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='videos')
    name = models.CharField(verbose_name='Video name', max_length=60)
    cover = models.ImageField(verbose_name='Video cover image')
    file = models.FileField(verbose_name='Video file')
    views = models.IntegerField(verbose_name='Video views', default=0)
    is_private = models.BooleanField(verbose_name='Video private', default=False)

    def __str__(self) -> str:
        """
        Call class as string

        :return: Self name
        """
        return self.name
