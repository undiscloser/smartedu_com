# Generated by Django 4.0.2 on 2022-02-26 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('courses', '0004_course_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
    ]
