# Generated by Django 4.2.3 on 2023-07-25 22:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('freight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freight',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freight',
            name='external_freight_id',
            field=models.IntegerField(),
        ),
    ]
