# Generated by Django 5.0.3 on 2024-03-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_alter_traducao_target_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traducao',
            name='target_language',
            field=models.CharField(default='', max_length=2),
        ),
    ]
