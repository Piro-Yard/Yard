# Generated by Django 4.0.2 on 2022-02-10 07:04

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userId', models.CharField(max_length=30, verbose_name='아이디')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('password', models.CharField(max_length=128, verbose_name='패스워드')),
                ('email', models.CharField(max_length=50, verbose_name='이메일')),
                ('nickName', models.CharField(max_length=30, verbose_name='닉네임')),
                ('gender', models.CharField(choices=[('여성', '여성'), ('남성', '남성'), ('기타', '기타')], max_length=10, verbose_name='성별')),
                ('birth', models.DateField(null=True, verbose_name='출생년도')),
                ('userImg', models.ImageField(blank=True, null=True, upload_to='userImg')),
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
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='가수')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='출생년도')),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='해쉬태그 종류')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('albumTitle', models.CharField(max_length=50, verbose_name='앨범 이름')),
                ('releasedDate', models.DateField(verbose_name='출시일')),
                ('lyric', models.TextField(verbose_name='가사')),
                ('albumImg', models.ImageField(blank=True, null=True, upload_to='albumImg')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.artist', verbose_name='artistId')),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedName', models.CharField(max_length=50, verbose_name='피드 이름')),
                ('createdDate', models.DateField(verbose_name='피드 생성일')),
                ('content', models.TextField(blank=True, null=True, verbose_name='피드 내용')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.artist', verbose_name='artist id')),
                ('musicId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.music', verbose_name='music id')),
                ('tags', models.ManyToManyField(blank=True, to='user.HashTag')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(default=datetime.date.today, verbose_name='인증 날짜')),
                ('musicId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.music', verbose_name='music id')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
        ),
    ]