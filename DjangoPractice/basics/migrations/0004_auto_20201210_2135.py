# Generated by Django 3.1.4 on 2020-12-10 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basics', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='page_in',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='basics.page'),
        ),
    ]
