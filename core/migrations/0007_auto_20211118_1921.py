# Generated by Django 3.2.9 on 2021-11-19 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(default='', max_length=64)),
                ('zipcode', models.CharField(default='', max_length=16)),
                ('syllabus_boilerplate', models.TextField(max_length=2056)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='section_id',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='Instructor_ID',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Student_ID',
        ),
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(default='', max_length=512),
        ),
        migrations.AddField(
            model_name='course',
            name='course_prereqs',
            field=models.TextField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office_loc',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='meeting_times',
            field=models.TextField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='student',
            name='student_ID',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='course_discussion_blurb',
            field=models.TextField(default='', max_length=512),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='course_discussion_link',
            field=models.URLField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='course_materials_blurb',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='course_website',
            field=models.URLField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='grading_blurb',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.instructor'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='office_hours',
            field=models.TextField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='ta_blurb',
            field=models.TextField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='file',
            name='instructor_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='file',
            name='syllabus_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instructor'),
        ),
        migrations.AlterField(
            model_name='section',
            name='meeting_location',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_id',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
        migrations.CreateModel(
            name='SyllabusList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_id', models.ManyToManyField(to='core.Syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.ManyToManyField(to='core.School')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='school_list',
            field=models.ManyToManyField(to='core.SchoolList'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='syllabus_list',
            field=models.ManyToManyField(to='core.SyllabusList'),
        ),
        migrations.AddField(
            model_name='student',
            name='school_list',
            field=models.ManyToManyField(to='core.SchoolList'),
        ),
        migrations.AddField(
            model_name='student',
            name='syllabus_list',
            field=models.ManyToManyField(to='core.SyllabusList'),
        ),
    ]
