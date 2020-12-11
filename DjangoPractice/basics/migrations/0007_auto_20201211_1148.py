# Generated by Django 3.1.4 on 2020-12-11 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0006_auto_20201211_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='like',
            name='page_in',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basics.page'),
            preserve_default=False,
        ),
    ]
