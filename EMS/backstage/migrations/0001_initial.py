
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('people_num', models.IntegerField()),
            ],
            options={
                'db_table': 'adm_class',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='通知', max_length=150)),
                ('messages', models.TextField(max_length=150)),
                ('author', models.CharField(max_length=128)),
                ('receiver', models.CharField(choices=[('全体成员', '全体成员'), ('信息科学与技术学院', '信息科学与技术学院'), ('化学工程学院', '化学工程学院'), ('材料科学与工程学院', '材料科学与工程学院'), ('机电工程学院', '机电工程学院'), ('经济管理学院', '经济管理学院'), ('理学院', '理学院'), ('文法学院', '文法学院'), ('生命科学与技术学院', '生命科学与技术学院'), ('继续教育学院', '继续教育学院'), ('马克思主义学院', '马克思主义学院'), ('国际教育学院', '国际教育学院'), ('侯德榜工程师学院', '侯德榜工程师学院'), ('能源学院', '能源学院'), ('巴黎居里工程师学院', '巴黎居里工程师学院'), ('个人', '个人')], default='全体成员', max_length=32)),
                ('year', models.CharField(default='2016', max_length=32)),
                ('visible', models.BooleanField(default=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'announcement',
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('crno', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('crtype', models.CharField(max_length=10)),
                ('contain_num', models.IntegerField()),
            ],
            options={
                'db_table': 'class_room',
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('short_name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cno', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=128)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.College')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseForSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'course_for_select',
            },
        ),
        migrations.CreateModel(
            name='CourseScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
            options={
                'db_table': 'course_selected',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=128, unique=True)),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('in_college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.College')),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.CreateModel(
            name='MajorCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cproper', models.BooleanField(default=True)),
                ('score', models.IntegerField()),
                ('chour', models.IntegerField()),
                ('semester', models.BooleanField(default=True)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Course')),
            ],
            options={
                'db_table': 'major_courses',
            },
        ),
        migrations.CreateModel(
            name='MajorPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('cls_num', models.IntegerField()),
                ('people_num', models.IntegerField()),
                ('score_grad', models.IntegerField()),
                ('stu_years', models.IntegerField()),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Major')),
            ],
            options={
                'db_table': 'major_plan',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=32)),
                ('score_got', models.IntegerField()),
                ('in_year', models.IntegerField()),
                ('in_cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.AdmClass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128)),
                ('sex', models.BooleanField(default=True)),
                ('in_year', models.IntegerField()),
                ('edu_background', models.CharField(max_length=128, null=True)),
                ('title', models.CharField(default='讲师', max_length=128)),
                ('description', models.TextField(null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.College')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('mcno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorCourses')),
                ('tno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher')),
            ],
            options={
                'db_table': 'teaching_table',
            },
        ),
        migrations.AddField(
            model_name='majorcourses',
            name='mno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorPlan'),
        ),
        migrations.AddField(
            model_name='courseselected',
            name='mcno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorCourses'),
        ),
        migrations.AddField(
            model_name='courseselected',
            name='sno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student'),
        ),
        migrations.AddField(
            model_name='coursescore',
            name='sno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student'),
        ),
        migrations.AddField(
            model_name='admclass',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorPlan'),
        ),
        migrations.AlterUniqueTogether(
            name='teaching',
            unique_together={('tno', 'mcno')},
        ),
        migrations.AlterUniqueTogether(
            name='majorplan',
            unique_together={('year', 'major')},
        ),
        migrations.AlterUniqueTogether(
            name='majorcourses',
            unique_together={('cno', 'mno')},
        ),
    ]
