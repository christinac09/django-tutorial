# Generated by Django 5.2.4 on 2025-07-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_quiz_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='uuid_id',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='uuid_id',
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='types',
            field=models.JSONField(null=True),
        ),
    ]
