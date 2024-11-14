# Generated by Django 5.0.7 on 2024-11-13 08:18

import django.db.models.deletion
import faq_public.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('public_id', models.AutoField(primary_key=True, serialize=False)),
                ('public_name', models.CharField(max_length=20, unique=True)),
                ('public_address', models.TextField(blank=True, null=True)),
                ('public_tel', models.TextField(blank=True, null=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('opening_hours', models.TextField(blank=True, null=True)),
                ('qr_code', models.CharField(blank=True, max_length=100, null=True)),
                ('agent_id', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Public_Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('접수', '접수'), ('처리 중', '처리 중'), ('완료', '완료')], default='접수', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='faq_public.public')),
            ],
        ),
        migrations.CreateModel(
            name='Public_Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='faq_public.public')),
            ],
        ),
        migrations.CreateModel(
            name='Public_User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('marketing', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_users', to='faq_public.public_department')),
                ('public', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='public_users', to='faq_public.public')),
            ],
        ),
        migrations.CreateModel(
            name='Public_Edit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=faq_public.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_edits', to='faq_public.public_user')),
            ],
        ),
    ]
