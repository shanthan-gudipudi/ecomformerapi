# Generated by Django 3.2.8 on 2021-11-06 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Yards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yardname', models.CharField(max_length=250)),
                ('yardlocation', models.CharField(max_length=500)),
                ('yarddiscription', models.TextField()),
                ('yardcontact', models.IntegerField()),
                ('yardaddress', models.CharField(max_length=500)),
                ('yardimg', models.ImageField(upload_to='')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yard_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=200)),
                ('itemdiscription', models.TextField()),
                ('itemprice', models.IntegerField()),
                ('itemimg', models.ImageField(upload_to='')),
                ('itemstatus', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('itemtype', models.CharField(choices=[('fruits', 'Fruits'), ('vegitables', 'Vegitables'), ('spices', 'Spices'), ('others', 'Others')], max_length=20)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('itemproducer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
