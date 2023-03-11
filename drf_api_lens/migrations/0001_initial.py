# Generated by Django 4.1.7 on 2023-03-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorCapture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(blank=True, max_length=256, null=True)),
                ('url_requested', models.CharField(blank=True, max_length=1024, null=True)),
                ('request_headers', models.TextField(blank=True, null=True)),
                ('request_body', models.TextField(blank=True, null=True)),
                ('query_params', models.TextField(blank=True, null=True)),
                ('request_method', models.CharField(blank=True, max_length=8, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=50, null=True)),
                ('response_body', models.TextField(blank=True, null=True)),
                ('response_status_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('execution_time', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'error_capture',
            },
        ),
    ]
