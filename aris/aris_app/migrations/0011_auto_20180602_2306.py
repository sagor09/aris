# Generated by Django 2.0.5 on 2018-06-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aris_app', '0010_auto_20180602_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='tab_first_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='tab_second_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project'),
        ),
    ]
