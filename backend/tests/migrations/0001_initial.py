# Generated by Django 4.0.3 on 2022-03-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('visits', models.IntegerField(default=0)),
                ('birthday', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
