# Generated by Django 3.0.8 on 2020-07-13 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200712_2002'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='booked_books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='books.Book'),
        ),
    ]
