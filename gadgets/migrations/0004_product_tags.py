# Generated by Django 4.0.6 on 2022-07-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='gadgets.tag', verbose_name='tags'),
        ),
    ]
