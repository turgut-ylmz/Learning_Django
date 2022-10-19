from django.db import models

class Student(models.Model):
    COUNTRIES = [ # choices = COUNTRIES
        ('TR', 'Turkey'),
        ('US', 'America'),
        ('DE', 'Germany'),
        ('FR', 'France'),
    ]
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    number = models.IntegerField('Numara')
    about = models.TextField('Hakkında', blank=True, null=True)
    country = models.CharField('Ülke', max_length=2, choices=COUNTRIES, default='TR')
    avatar = models.ImageField('Resim', blank=True, null=True, upload_to='media/')
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    # https://docs.djangoproject.com/en/4.1/ref/models/options/#model-meta-options
    class Meta:
        ordering = ['number'] # DESC -> ['-number']
        verbose_name_plural = 'Öğrenciler'