# Generated by Django 2.2 on 2019-05-11 17:02

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Subjects', validators=[app.models.test_proper_year], verbose_name='课程编号'),
        ),
    ]
