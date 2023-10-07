from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Specify any dependencies if applicable
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