# Generated by Django 5.1.2 on 2024-10-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_remove_attendance_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_number',
            field=models.PositiveIntegerField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('zoom', 'Zoom')], default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_of_meeting',
            field=models.DateField(blank=True, null=True),
        ),
    ]
