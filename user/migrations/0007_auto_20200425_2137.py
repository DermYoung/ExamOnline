# Generated by Django 3.0.3 on 2020-04-25 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200425_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='clazz',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='user.Clazz', verbose_name='班级'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='clazz',
            table=None,
        ),
    ]
