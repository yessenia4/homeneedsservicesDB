# Generated by Django 3.0.5 on 2020-05-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hns', '0016_auto_20200502_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorapplications',
            name='dateapproved',
            field=models.DateField(db_column='dateApproved', default=None),
        ),
    ]
