from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone
import django.db.models.deletion
from django.db import migrations, models
import django.contrib.auth.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('bug_type', models.CharField(max_length=200)),
                ('report_date', models.DateTimeField(verbose_name='date published')),
                ('status', models.CharField(max_length=2, choices=[
                    ('O', 'Open'),
                    ('C', 'Closed'),
                    ('IP', 'In Progress'),
                ])),
            ],
        ),
    ]
        
    options={
                'swappable': 'AUTH_USER_MODEL',
            },
    managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        
    
    
    
    
    
    
    
   







