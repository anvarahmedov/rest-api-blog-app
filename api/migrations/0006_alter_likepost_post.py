# Generated by Django 5.1.5 on 2025-02-04 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_likecomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='api.post'),
        ),
    ]
