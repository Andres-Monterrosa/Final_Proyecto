# Generated by Django 4.0.5 on 2022-06-03 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacion', models.CharField(max_length=250)),
                ('codigo_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro')),
            ],
        ),
    ]
