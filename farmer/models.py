from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Yards(models.Model):
    class YardObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status= 'published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    yardname = models.CharField(max_length=250)
    yardlocation  = models.CharField(max_length=500)
    yarddiscription = models.TextField()
    yardcontact = models.IntegerField()
    yardaddress = models.CharField(max_length=500)
    yardimg = models.ImageField()
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='yard_posts')
    status = models.CharField(
        max_length=10,choices=options,default='published')
    objects = models.Manager()
    yardobjects= YardObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.yardname


class Items(models.Model):
    class ItemObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(itemstatus= 'published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    options1 = (
        ('fruits', 'Fruits'),
        ('vegitables', 'Vegitables'),
        ('spices', 'Spices'),
        ('others', 'Others'),
    )
    itemname = models.CharField(max_length=200)
    itemdiscription = models.TextField()
    itemprice  = models.IntegerField()
    itemimg  = models.ImageField()
    itemproducer = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='items_posts')
    itemstatus = models.CharField(
        max_length=10, choices=options, default='published')
    itemtype = models.CharField(max_length= 20 ,choices=options1,default='fruits')
    published = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    itemobjects = ItemObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.itemname