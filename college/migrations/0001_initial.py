# Generated by Django 3.2.8 on 2022-07-27 09:17

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0017_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(max_length=255, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=255)),
                ('course_name', models.CharField(max_length=255)),
                ('course_pic', models.ImageField(upload_to='image/download/uploads/course/')),
                ('course_description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('event_place', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/download/uploads/events/')),
                ('description', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=255)),
                ('gallery_pic', models.ImageField(upload_to='image/download/uploads/gallery/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('1', 'ADMIN'), ('2', 'STAFF'), ('3', 'STUDENT')], default=1, max_length=50)),
                ('profile_pic', models.ImageField(upload_to='image/download/uploads/login/')),
                ('password', models.CharField(max_length=15)),
                ('otp', models.CharField(default='1234', max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.CharField(max_length=255)),
                ('session_end', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stf_id', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50)),
                ('salary', models.IntegerField(default=0)),
                ('paid_salary', models.IntegerField(default=0)),
                ('account_no', models.CharField(default='', max_length=50)),
                ('ifsc_code', models.CharField(default='', max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.login')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addmission_no', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('parent_mobile_no', models.CharField(max_length=50)),
                ('admission_fees', models.IntegerField(default=0)),
                ('paid_amount', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.course')),
                ('session_year_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.login')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('session_year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.session')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=255)),
                ('subject_name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Student_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('notes', models.FileField(upload_to='image/download/uploads/notes/')),
                ('status', models.IntegerField(default=0)),
                ('reply', models.TextField(default='No Reply')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.staff')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_fees_Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_no', models.CharField(max_length=100)),
                ('paid_amount', models.IntegerField()),
                ('payment_id', models.CharField(max_length=200)),
                ('remark', models.TextField(default='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Attendance_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.student_attendance')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.student')),
            ],
        ),
        migrations.AddField(
            model_name='student_attendance',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.subject'),
        ),
        migrations.CreateModel(
            name='Staff_salary_Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_no', models.CharField(max_length=100)),
                ('salary_paid', models.IntegerField()),
                ('payment_id', models.CharField(max_length=200)),
                ('remark', models.TextField(default='')),
                ('account_no', models.CharField(default='', max_length=50)),
                ('ifsc_code', models.CharField(default='', max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_marks', models.IntegerField()),
                ('external_marks', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.session')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_no', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='college.course')),
            ],
        ),
        migrations.CreateModel(
            name='CustomeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('1', 'ADMIN'), ('2', 'STAFF'), ('3', 'STUDENT')], default=1, max_length=50)),
                ('profile_pic', models.ImageField(upload_to='image/download/uploads/profile_pic/')),
                ('mobile_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('dob', models.CharField(blank=True, max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]