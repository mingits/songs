# Generated by Django 2.1.2 on 2019-03-07 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='s',
            name='t',
        ),
        migrations.RemoveField(
            model_name='t',
            name='c1',
        ),
        migrations.RemoveField(
            model_name='t',
            name='c2',
        ),
        migrations.RenameModel(
            old_name='c1',
            new_name='Category_1',
        ),
        migrations.DeleteModel(
            name='c2',
        ),
        migrations.DeleteModel(
            name='s',
        ),
        migrations.DeleteModel(
            name='t',
        ),
        migrations.AddField(
            model_name='title',
            name='c1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Category_1'),
        ),
        migrations.AddField(
            model_name='title',
            name='c2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Category_2'),
        ),
        migrations.AddField(
            model_name='song',
            name='t',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Title'),
        ),
    ]
