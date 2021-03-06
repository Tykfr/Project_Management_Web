# Generated by Django 2.2.2 on 2019-06-22 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='description',
            field=models.TextField(default='Blank Objective'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProjectUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_name', models.CharField(max_length=100)),
                ('update', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collab.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectiveUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_name', models.CharField(max_length=100)),
                ('update', models.TextField()),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collab.Objective')),
            ],
        ),
    ]
