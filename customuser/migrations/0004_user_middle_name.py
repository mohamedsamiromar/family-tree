# Generated by Django 4.1 on 2022-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_alter_user_managers_remove_user_is_stuff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default=False, max_length=150, verbose_name='middle_name'),
        ),
    ]
