# Generated by Django 2.1.3 on 2019-05-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backstage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduationProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pkeywords', models.TextField()),
                ('pdescription', models.TextField()),
                ('pstu', models.TextField()),
                ('pstatus', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'GraduationProject',
            },
        ),
        migrations.CreateModel(
            name='ProjectDifficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdiname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StuChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('pno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduationManagement.GraduationProject')),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student')),
                ('tno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher')),
            ],
            options={
                'db_table': 'StuChoice',
            },
        ),
        migrations.AddField(
            model_name='projectscore',
            name='schoic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduationManagement.StuChoice'),
        ),
        migrations.AddField(
            model_name='projectdocument',
            name='schoic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduationManagement.StuChoice'),
        ),
        migrations.AddField(
            model_name='graduationproject',
            name='pdifficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduationManagement.ProjectDifficulty'),
        ),
        migrations.AddField(
            model_name='graduationproject',
            name='pdirection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduationManagement.ProjectDirection'),
        ),
        migrations.AddField(
            model_name='graduationproject',
            name='tno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='stuchoice',
            unique_together={('sno', 'tno', 'pno')},
        ),
    ]
